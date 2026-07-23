---
name: health-tracker
description: Updates and summarizes the Operator's Garmin health data (sleep and activities).
---

# Health Tracker

This skill manages the Operator's Garmin health data (sleep and activities).

## Directories
- `health_stats/`: Markdown files tracking weekly stats (`YYYY-Wxx.md`).
- `health_stats/raw/`: Raw Garmin JSON responses.

## Scripts
- `scripts/update_health.py`: Fetches latest data (today/yesterday) and updates the current ISO week's markdown file.

## Guidelines
- If new sleep data does not appear after a sync (especially in the morning), it could be because the Operator has not woken up yet or the watch hasn't synced. In that case, do not assume data is missing permanently; just ask the Operator about their previous night's sleep.
