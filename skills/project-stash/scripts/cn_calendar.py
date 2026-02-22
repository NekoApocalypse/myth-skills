#!/usr/bin/env python3
"""
cn_calendar.py - Chinese calendar day classifier.

Usage:
    python3 cn_calendar.py [YYYY-MM-DD]   # defaults to today (CST/UTC+8)

Output (JSON):
    {
        "date": "2026-02-21",
        "weekday": "Saturday",
        "status": "rest_normal",           # work_normal | work_buban | rest_normal | rest_holiday
        "label": "Saturday",
        "next_workday": "2026-02-24",      # only present on rest days
        "next_holiday_block": {
            "start": "2026-04-06",
            "end": "2026-04-06",
            "name": "Tomb-sweeping Day"
        },
        "upcoming_buban": [
            { "date": "2026-02-28", "note": "补班" }
        ]
    }

Status definitions:
    work_normal  - regular weekday
    work_buban   - compensatory workday falling on a weekend (补班)
    rest_normal  - regular weekend
    rest_holiday - public holiday (weekday overridden, or holiday weekend)

Dependencies:
    pip install chinesecalendar --user --break-system-packages
    (Update yearly: pip install -U chinesecalendar --user --break-system-packages)
"""

import sys
import json
import datetime
from dataclasses import dataclass

try:
    import chinese_calendar as cc
except ImportError:
    print(json.dumps({"error": "chinesecalendar not installed. Run: pip install chinesecalendar --user --break-system-packages"}))
    sys.exit(1)

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
SCOUT_MAX_DAYS = 180
BUBAN_WINDOW_DAYS = 30


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class DayInfo:
    date: datetime.date
    status: str          # work_normal | work_buban | rest_normal | rest_holiday
    weekday_name: str    # Monday, Tuesday, etc.
    current_holiday_name: str | None  # None unless today is part of a named holiday block


# ---------------------------------------------------------------------------
# Classifier — single source of truth
# ---------------------------------------------------------------------------

def get_day_info(d: datetime.date) -> DayInfo:
    """
    Classify a date using the chinesecalendar library.

    Classification rules:
        is_workday + weekend              → work_buban   (补班)
        is_workday + weekday              → work_normal
        not workday + holiday_name        → rest_holiday (part of named holiday block)
        not workday + no holiday_name     → rest_normal  (regular weekend)

    Note: get_holiday_detail returns (is_holiday, holiday_name) where
    holiday_name is set for ALL days in a holiday period (including
    compensatory rest days), not just the core named day.
    """
    is_workday = cc.is_workday(d)
    is_weekend = d.weekday() >= 5
    _, holiday_name = cc.get_holiday_detail(d)

    weekday_name = WEEKDAYS[d.weekday()]

    if is_workday and is_weekend:
        status, current_holiday = "work_buban", None
    elif is_workday:
        status, current_holiday = "work_normal", None
    elif holiday_name:
        status, current_holiday = "rest_holiday", holiday_name
    else:
        status, current_holiday = "rest_normal", None

    return DayInfo(date=d, status=status, weekday_name=weekday_name,
                   current_holiday_name=current_holiday)


# ---------------------------------------------------------------------------
# Scout functions
# ---------------------------------------------------------------------------

def next_workday(start: DayInfo) -> str | None:
    """Return ISO date of the next work_normal or work_buban day after start."""
    d = start.date + datetime.timedelta(days=1)
    for _ in range(SCOUT_MAX_DAYS):
        if get_day_info(d).status in ("work_normal", "work_buban"):
            return d.isoformat()
        d += datetime.timedelta(days=1)
    return None


def next_holiday_block(start: DayInfo) -> dict | None:
    """
    Return the next contiguous holiday block after start.

    A "holiday block" is a contiguous period where holiday_name is not None.
    The library returns the holiday name for ALL days in the period (including
    compensatory rest days), so we simply scan for consecutive days with a name.

    If start is already in a holiday block (current_holiday_name is not None),
    skip past it first — scan begins from the day after the next workday.
    """
    # Determine where to start scanning
    if start.current_holiday_name:
        # Currently in a holiday block, skip to after next workday
        nw = next_workday(start)
        if nw is None:
            return None
        d = datetime.date.fromisoformat(nw) + datetime.timedelta(days=1)
    else:
        d = start.date + datetime.timedelta(days=1)

    block_start = None
    block_name = None

    for _ in range(SCOUT_MAX_DAYS):
        info = get_day_info(d)

        # Check if this day has a holiday name (part of a named holiday block)
        if info.current_holiday_name:
            if block_start is None:
                block_start = d
                block_name = info.current_holiday_name
        else:
            # End of holiday block
            if block_start is not None:
                return {
                    "start": block_start.isoformat(),
                    "end": (d - datetime.timedelta(days=1)).isoformat(),
                    "name": block_name,
                }
            # Reset and continue scanning
            block_start = None

        d += datetime.timedelta(days=1)

    return None


def upcoming_buban(start: DayInfo) -> list[dict]:
    """Return all work_buban dates within the next BUBAN_WINDOW_DAYS days."""
    result = []
    for i in range(1, BUBAN_WINDOW_DAYS + 1):
        d = start.date + datetime.timedelta(days=i)
        if get_day_info(d).status == "work_buban":
            result.append({"date": d.isoformat(), "note": "补班"})
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_cst = now_utc + datetime.timedelta(hours=8)

    if len(sys.argv) > 1:
        try:
            target = datetime.date.fromisoformat(sys.argv[1])
        except ValueError:
            print(json.dumps({"error": f"Invalid date: {sys.argv[1]}. Use YYYY-MM-DD."}))
            sys.exit(1)
    else:
        target = now_cst.date()

    today = get_day_info(target)

    result = {
        "time_utc": now_utc.strftime("%Y-%m-%d %H:%M UTC"),
        "time_cst": now_cst.strftime("%Y-%m-%d %H:%M CST"),
        "date": today.date.isoformat(),
        "weekday": today.weekday_name,
        "status": today.status,
        "current_holiday_name": today.current_holiday_name,
    }

    if today.status.startswith("rest_"):
        result["next_workday"] = next_workday(today)

    result["next_holiday_block"] = next_holiday_block(today)
    result["upcoming_buban"] = upcoming_buban(today)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
