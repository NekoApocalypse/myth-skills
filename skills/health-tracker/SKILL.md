---
name: health-tracker
description: "Syncs and summarizes the Operator's Garmin health data (sleep stages, sleep scores, and aerobic/running activities) for daily briefings and weekly reviews."
---

# Health Tracker (`health-tracker`)

## Goal

Maintain an up-to-date weekly ledger (`health_stats/YYYY-Wxx.md`) of the Operator's Garmin sleep and physical activity data, feeding the Morning Debrief, Nightly Wind-Down, and Weekly Review without standalone notification clutter.

---

## Contracts & Paths

1. **Sync Script (Self-Healing Venv & Credentials)**:
   ```bash
   python3 ~/.openclaw/workspace/myth-skills/skills/health-tracker/scripts/update_health.py
   ```
   - Automatically locates `~/.openclaw/workspace/.venv/bin/python` and falls back to reading `GARMIN_EMAIL` and `GARMIN_PASSWORD` from `~/.openclaw/workspace/local_secrets.md` if environment variables are not pre-exported.
2. **Output Files**:
   - **Weekly Markdown Ledger**: `~/.openclaw/workspace/health_stats/YYYY-Wxx.md` (ISO week, e.g., `2026-W45.md`).
   - **Raw Garmin JSON Cache**: `~/.openclaw/workspace/health_stats/raw/garmin-YYYY-MM-DD.json`.

---

## Principles & Usage in Daily Briefings

- **Morning Check-In (Sleep & Recovery Readiness)**:
  - Run `update_health.py` once before reading `health_stats/YYYY-Wxx.md`.
  - If today's sleep block still shows `pending Garmin sync` (because the watch hasn't synced yet), say so in one short line without inventing numbers or scolding.
  - Use last night's sleep duration/score and recent running/aerobic load to inform whether today is a good window for an open **Convict Conditioning (`CC`)** weekly checkbox or an aerobic run.
- **Nightly Wind-Down (Activity & Sleep Prep)**:
  - Sync `update_health.py` once in the evening to capture any daytime runs or workouts before summarizing the day.
