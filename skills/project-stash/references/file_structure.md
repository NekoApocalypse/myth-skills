# File Structure

## Paths

| Resource | Path |
|---|---|
| Active Projects Board | `~/.openclaw/workspace/PROJECTS.md` |
| Daily Snapshots Vault | `~/.openclaw/workspace/vault/myth-projects-stash/daily-snapshots/` |
| Completed Projects Vault | `~/.openclaw/workspace/vault/myth-projects-stash/completed/` |
| Chinese Calendar Script | `~/.openclaw/workspace/myth-skills/project-stash/scripts/cn_calendar.py` |

## Naming Conventions

All dates use timezone `Asia/Shanghai` (CST).

- **Daily Snapshots:** `{YYYY-MM-DD}_PROJECTS.md` (e.g., `2026-02-21_PROJECTS.md`)
- **Completed Projects:** `{YYYY-MM-DD}_{Project_Name}.md` (spaces replaced with underscores)

## Directory Layout

```
~/.openclaw/workspace/
├── PROJECTS.md                                  # Active projects board
├── vault/myth-projects-stash/
│   ├── daily-snapshots/                         # Daily PROJECTS.md copies
│   │   ├── 2026-02-20_PROJECTS.md
│   │   └── ...
│   └── completed/                               # Archived finished projects
│       ├── 2026-02-19_Some_Project.md
│       └── ...
└── myth-skills/project-stash/                   # This skill
    ├── SKILL.md
    ├── scripts/cn_calendar.py
    ├── assets/
    │   └── PROJECTS_TEMPLATE.md                 # PROJECTS.md format template
    └── references/
        ├── file_structure.md                    # (this file)
        └── debrief.md                           # Debrief procedure (agent + cron)
```
