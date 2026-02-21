# Project Stash Skill

This skill manages the Operator's Project Stash (GTD/buffer system) and daily debriefs.

## File Locations
- **Active Projects Board:** `/home/node/.openclaw/workspace/PROJECTS.md`
- **Daily Snapshots Vault:** `/home/node/.openclaw/workspace/vault/myth-projects-stash/daily-snapshots/`
- **Completed Projects Vault:** `/home/node/.openclaw/workspace/vault/myth-projects-stash/completed/`
- **Chinese Calendar Script:** `/home/node/.openclaw/workspace/myth-skills/project-stash/cn_calendar.py`

## Conventions & Rules

1. **Daily Snapshots:** 
   - Naming convention: `{YYYY-MM-DD}_PROJECTS.md` (e.g., `2026-02-21_PROJECTS.md`).
   - Timezone for dates must always be `Asia/Shanghai` (CST).

2. **Completed Projects:**
   - When a project is marked as done, it MUST be removed from `PROJECTS.md`.
   - It MUST be archived into the Completed Projects Vault.
   - Naming convention: `{YYYY-MM-DD}_{Project_Name}.md` (spaces replaced with underscores).
   - The archived file should contain a brief summary of the completed work.

## Prompts & Scripts
- `debrief_prompt.md`: The exact prompt used by the daily cron jobs to generate the debrief.
- `cn_calendar.py`: The script used to fetch Chinese holiday/workday data.