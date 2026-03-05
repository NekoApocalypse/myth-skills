# Project Stash Skill — Upgrade Brief (APPROVED FOR IMPLEMENTATION)

## Context
You are working inside the repo at: `/home/node/.openclaw/workspace/myth-skills`
Current branch: `myth-project-stash-upgrade`
Skill location: `project-stash/`

## Current State
The skill has:
- `SKILL.md` — minimal: file locations + naming conventions only. No operational instructions.
- `debrief_prompt.md` — the exact text injected into a daily cron job
- `cn_calendar.py` — Chinese calendar day classifier (Python, works correctly)

Active data files (outside skill dir, in workspace root):
- `/home/node/.openclaw/workspace/PROJECTS.md` — active project board
- `/home/node/.openclaw/workspace/vault/myth-projects-stash/daily-snapshots/` — dated PROJECTS.md snapshots
- `/home/node/.openclaw/workspace/vault/myth-projects-stash/completed/` — archived completed project files

## Known Design Flaw — FIXED IN THIS VERSION
**Logical conflict: completion archiving vs. debrief momentum check**

When a project completes and is removed from PROJECTS.md, the debrief's momentum check (comparing PROJECTS.md to last 3 snapshots) can't tell if it was completed or just dropped.

**Approved fix:** Create `COMPLETED_LOG.md` in the workspace root (next to PROJECTS.md). It is an append-only ledger with format:
```
date,project_name,archive_path
2026-02-22,Mem0 Trial,vault/myth-projects-stash/completed/2026-02-22_Mem0_Trial.md
```
When debrief sees a project disappear from PROJECTS.md compared to snapshots, it checks COMPLETED_LOG.md — present = completed ✅, absent = dropped ⚠️.

## Approved Structure

```
project-stash/
├── SKILL.md                          # YAML frontmatter + core operations (lean)
├── scripts/
│   ├── cn_calendar.py               # moved from root — Chinese calendar classifier
│   └── snapshot.sh                  # NEW: takes daily snapshot (wraps cp command)
└── references/
    ├── operations.md                # Detailed: how to add/update/complete a project
    ├── debrief_protocol.md          # Updated debrief prompt (completion-aware)
    └── data_model.md                # File formats, COMPLETED_LOG.md schema, conventions
```

## Implementation Instructions

### 1. Restructure the skill directory
- Move `cn_calendar.py` → `scripts/cn_calendar.py`
- Delete old `debrief_prompt.md` (content migrates to `references/debrief_protocol.md`)
- Create `scripts/`, `references/` subdirectories

### 2. Create `scripts/snapshot.sh`
A simple script that:
- Takes a snapshot of PROJECTS.md to the daily-snapshots vault
- Uses CST (Asia/Shanghai) for the date
- Path: `/home/node/.openclaw/workspace/vault/myth-projects-stash/daily-snapshots/$(TZ='Asia/Shanghai' date +%Y-%m-%d)_PROJECTS.md`
- Source: `/home/node/.openclaw/workspace/PROJECTS.md`

### 3. Rewrite `SKILL.md`
YAML frontmatter only: `name` and `description`. Description must be comprehensive (it's the trigger mechanism).

Body: lean, imperative. Cover:
- File locations (PROJECTS.md, COMPLETED_LOG.md, vault paths)
- Core operations summary (detail in references/operations.md)
- When to read which reference file
- Script locations

### 4. Create `references/operations.md`
Detailed procedures for:
- **Stash a project**: add to PROJECTS.md with standard fields (Status, Phase, Context, Progress, Next)
- **Update a project**: edit the relevant entry in PROJECTS.md
- **Complete a project**: 
  1. Write summary to `vault/myth-projects-stash/completed/{YYYY-MM-DD}_{Project_Name}.md`
  2. Append line to COMPLETED_LOG.md (workspace root)
  3. Remove from PROJECTS.md active section
- **Drop a project**: remove from PROJECTS.md (no log entry — intentionally distinguishable from completion)
- **Small-talk redirect**: if user mentions a project idea in small-talk channel, advise them to record it to the project stash in a dedicated channel

### 5. Create `references/debrief_protocol.md`
Updated version of the old `debrief_prompt.md`. Key changes:
- Momentum check now reads COMPLETED_LOG.md to explain disappearances from snapshots
- Distinguish completed vs. dropped in the momentum analysis
- Keep all existing sections: Calendar, Projects, Momentum Check, Pep Talk, Ask for Updates, Backup

The full debrief prompt text should be here (verbatim injectable format, same style as current debrief_prompt.md).

### 6. Create `references/data_model.md`
Document:
- PROJECTS.md format (fields: Status, Phase, Context, Progress, Next)
- COMPLETED_LOG.md format (CSV: date, project_name, archive_path)
- Snapshot naming: `{YYYY-MM-DD}_PROJECTS.md`  
- Completed archive naming: `{YYYY-MM-DD}_{Project_Name}.md` (spaces → underscores)
- All paths are relative to workspace root: `/home/node/.openclaw/workspace/`

## Constraints
- Do NOT modify PROJECTS.md or any vault files
- Do NOT create COMPLETED_LOG.md (that's a data file, agent creates it on first use)
- Only work within `myth-skills/project-stash/` directory
- No README, CHANGELOG, or auxiliary docs
- Test cn_calendar.py still works after move (run it, verify JSON output)
- Test snapshot.sh is executable and correct
