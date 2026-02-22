---
name: project-stash
description: Manage the Operator's Project Stash (GTD/buffer system) and daily debriefs. Trigger when the user mentions project management, PROJECTS.md, daily debriefs, momentum checks, completing or dropping projects, or when they need to record a project idea that was mentioned in small-talk.
---

# Project Stash Skill

## File Locations (Workspace Root: `/home/node/.openclaw/workspace/`)

| File | Path | Notes |
|------|------|-------|
| Active Projects Board | `PROJECTS.md` | Always exists |
| Completion Ledger | `COMPLETED_LOG.md` | Created on first project completion |
| Daily Snapshots Vault | `vault/myth-projects-stash/daily-snapshots/` | |
| Completed Projects Vault | `vault/myth-projects-stash/completed/` | |

## Core Operations

| Operation | Action |
|-----------|--------|
| **Stash** | Add project to `PROJECTS.md` with standard fields |
| **Update** | Edit project entry in `PROJECTS.md` |
| **Complete** | Archive to vault → append to `COMPLETED_LOG.md` → remove from `PROJECTS.md` |
| **Drop** | Remove from `PROJECTS.md` only (no log entry — intentionally distinguishable) |

## Scripts

| Script | Purpose |
|--------|---------|
| [`scripts/cn_calendar.py`](scripts/cn_calendar.py) | Chinese calendar classifier — outputs JSON |
| [`scripts/snapshot.sh`](scripts/snapshot.sh) | Takes dated snapshot of `PROJECTS.md` to vault |

## When to Read Reference Files

- **Adding/updating/completing/dropping a project** → [`references/operations.md`](references/operations.md)
- **Running or debugging a debrief** → [`references/debrief_protocol.md`](references/debrief_protocol.md)
- **File format / schema questions** → [`references/data_model.md`](references/data_model.md)
