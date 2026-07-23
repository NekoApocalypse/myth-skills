#!/usr/bin/env python3
"""Fetch and update Garmin Connect health data (sleep and activities)."""

import os
import json
import re
from datetime import datetime, date, timedelta
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

try:
    from garminconnect import Garmin
except ModuleNotFoundError:
    import sys
    venv_python = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".venv", "bin", "python"))
    if os.path.exists(venv_python) and os.path.abspath(sys.executable) != venv_python:
        os.execv(venv_python, [venv_python, *sys.argv])
    raise

import logging
logging.getLogger("garminconnect.client").setLevel(logging.ERROR)

DEFAULT_TIMEZONE = "Asia/Shanghai"
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
HEALTH_DIR = os.path.join(WORKSPACE_DIR, "health_stats")
RAW_DIR = os.path.join(HEALTH_DIR, "raw")

def required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value

def iso_week_filename(d: date) -> str:
    iso = d.isocalendar()
    return f"{iso.year}-W{iso.week:02d}.md"

def display_timezone() -> ZoneInfo:
    timezone_name = os.environ.get("GARMIN_TIMEZONE", DEFAULT_TIMEZONE)
    try:
        return ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as exc:
        raise SystemExit(f"Invalid GARMIN_TIMEZONE: {timezone_name}") from exc

def get_nested(data: dict[str, Any], *path: str) -> Any:
    current: Any = data
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current

def format_duration(seconds: int | float | None) -> str:
    if seconds is None:
        return "n/a"
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes = remainder // 60
    return f"{hours}h {minutes:02d}m"

def stage_seconds(sleep: dict[str, Any], key: str) -> int | None:
    value = sleep.get(key)
    return int(value) if isinstance(value, (int, float)) else None

def format_timestamp(value: Any, tz: ZoneInfo, encoded_local: bool = False) -> str:
    from datetime import timezone
    if isinstance(value, (int, float)):
        timestamp = float(value)
        if timestamp > 1_000_000_000_000:
            timestamp /= 1000
        if encoded_local:
            return datetime.fromtimestamp(timestamp, timezone.utc).strftime(f"%Y-%m-%d %H:%M {tz.key}")
        return datetime.fromtimestamp(timestamp, tz).strftime("%Y-%m-%d %H:%M %Z")
    if isinstance(value, str):
        normalized = value.strip()
        if not normalized:
            return "n/a"
        try:
            return format_timestamp(float(normalized), tz, encoded_local=encoded_local)
        except ValueError:
            pass
        try:
            parsed = datetime.fromisoformat(normalized.replace("Z", "+00:00"))
        except ValueError:
            return normalized
        if parsed.tzinfo is not None:
            parsed = parsed.astimezone(tz)
        return parsed.strftime("%Y-%m-%d %H:%M %Z")
    return "n/a"

def generate_day_markdown(target_date: date, tz: ZoneInfo, sleep_data: dict, activities: list) -> str:
    date_str = target_date.isoformat()
    now_str = datetime.now(tz).strftime("%Y-%m-%d %H:%M %Z")
    
    lines = [
        f"<!-- health:{date_str}:start -->",
        f"## {date_str} {target_date.strftime('%A')}",
        "",
        f"Updated: {now_str}",
        "",
        "Sleep:"
    ]
    
    sleep = sleep_data.get("dailySleepDTO") or {}
    if not sleep:
        lines.append("- pending Garmin sync as of " + now_str)
    else:
        score = get_nested(sleep_data, "sleepScores", "overall", "value") or sleep.get("sleepScore")
        score_qual = get_nested(sleep_data, "sleepScores", "overall", "qualifierKey")
        lines.append(f"- Score: {score if score is not None else 'n/a'} ({score_qual or ''})")
        lines.append(f"- Duration: {format_duration(stage_seconds(sleep, 'sleepTimeSeconds'))}")
        
        start = sleep.get("sleepStartTimestampLocal")
        end = sleep.get("sleepEndTimestampLocal")
        encoded_local = start is not None or end is not None
        if start is None: start = sleep.get("sleepStartTimestampGMT") or sleep.get("sleepStartTimestamp")
        if end is None: end = sleep.get("sleepEndTimestampGMT") or sleep.get("sleepEndTimestamp")
        
        if start or end:
            lines.append(f"- Window: {format_timestamp(start, tz, encoded_local=encoded_local)} -> {format_timestamp(end, tz, encoded_local=encoded_local)}")
            
        lines.append(f"- Deep: {format_duration(stage_seconds(sleep, 'deepSleepSeconds'))}")
        lines.append(f"- Light: {format_duration(stage_seconds(sleep, 'lightSleepSeconds'))}")
        lines.append(f"- REM: {format_duration(stage_seconds(sleep, 'remSleepSeconds'))}")
        lines.append(f"- Awake: {format_duration(stage_seconds(sleep, 'awakeSleepSeconds'))}")

    lines.append("")
    lines.append("Activities:")
    day_acts = []
    for a in activities:
        start_time_local = a.get("startTimeLocal") or ""
        if start_time_local.startswith(date_str):
            day_acts.append(a)
            
    if not day_acts:
        lines.append("- No activities recorded.")
    else:
        for a in day_acts:
            dist = a.get("distance", 0) / 1000.0 if isinstance(a.get("distance"), (int, float)) else 0
            dur = a.get("duration", 0) / 60.0 if isinstance(a.get("duration"), (int, float)) else 0
            typ = a.get("activityType", {}).get("typeKey", "unknown")
            act_id = a.get("activityId", "unknown")
            lines.append(f"- {typ.capitalize()} | {dist:.2f} km | {dur:.1f} min | {a.get('startTimeLocal', 'n/a')} | id: {act_id}")
            
    lines.append(f"<!-- health:{date_str}:end -->")
    return "\n".join(lines)

def update_markdown_file(file_path: str, date_str: str, new_content: str, week_title: str):
    if not os.path.exists(file_path):
        content = f"# Health Stats - {week_title}\n\n{new_content}\n"
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        pattern = re.compile(rf"<!-- health:{date_str}:start -->.*?<!-- health:{date_str}:end -->", re.DOTALL)
        if pattern.search(content):
            content = pattern.sub(new_content, content)
        else:
            # append
            content = content.rstrip() + "\n\n" + new_content + "\n"
            
        # sort days
        days = re.findall(r"(<!-- health:\d{4}-\d{2}-\d{2}:start -->.*?<!-- health:\d{4}-\d{2}-\d{2}:end -->)", content, re.DOTALL)
        days.sort()
        header = re.split(r"<!-- health:\d{4}-\d{2}-\d{2}:start -->", content)[0].rstrip()
        content = header + "\n\n" + "\n\n".join(days) + "\n"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    email = required_env("GARMIN_EMAIL")
    password = required_env("GARMIN_PASSWORD")
    tz = display_timezone()
    
    os.makedirs(RAW_DIR, exist_ok=True)

    client = Garmin(email, password)
    client.login()
    
    today = datetime.now(tz).date()
    yesterday = today - timedelta(days=1)
    dates_to_fetch = [today - timedelta(days=3), today - timedelta(days=2), yesterday, today]
    
    activities = client.get_activities(0, 20) or []
    
    for d in dates_to_fetch:
        d_str = d.isoformat()
        raw_file = os.path.join(RAW_DIR, f"garmin-{d_str}.json")
        sleep_data = client.get_sleep_data(d_str)
        
        with open(raw_file, "w", encoding="utf-8") as f:
            json.dump({"sleep": sleep_data}, f, indent=2)
            
        md_content = generate_day_markdown(d, tz, sleep_data, activities)
        
        week_filename = iso_week_filename(d)
        week_filepath = os.path.join(HEALTH_DIR, week_filename)
        week_title = week_filename.replace(".md", "")
        
        update_markdown_file(week_filepath, d_str, md_content, week_title)

if __name__ == "__main__":
    main()
