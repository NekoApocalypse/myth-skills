---
name: project-stash
description: >
  Manage the operator's active project board, daily debriefs, and backups.
  Use when the operator: asks about their projects or project status; wants to stash, add,
  or record a new project idea; wants to update project status or progress; marks a project
  as completed or wants to drop/abandon a project; requests a status report, momentum check,
  or daily debrief; mentions PROJECTS.md or the project stash.
---

# Project Stash

Manage the operator's active projects board, take daily snapshots, archive completed work, and run debriefs.

## Common Operations

### Complete a Task or Project

1. Create an archive file in the completed vault with a brief summary of the work done.
2. File naming: `{YYYY-MM-DD}_{Task_Name}.md` (spaces → underscores, date in CST).
3. **DELETE the entry from `PROJECTS.md` entirely.** Do not list completed items on the board. On project / task completion, record them to archive and then completely remove them from the board.
**Note on 2-Level Structure:** The project stash is exactly 2 levels deep (Project and Tasks). Each Task gets treated as its own item. Finishing a Task should be archived individually as above. Finishing a Project archives the whole thing as one file.

### Add / Update a Project

Edit `PROJECTS.md` directly. Follow the format in [assets/PROJECTS_TEMPLATE.md](assets/PROJECTS_TEMPLATE.md). Every project must carry an `Objective Tie-in` tag linking it to an Active Objective.

### Objective Management

Objectives map the high-level intent of the operator's current sprint.
1. **Max 3 Items:** No more than 3 active objectives at any given time.
2. **Immutable Begin Time:** Start dates/times cannot be changed once logged.
3. **Archive on Finish:** Completed items must be permanently archived to the vault.
4. **Mutable Content & Title:** Details and naming can evolve, but the core objective slot remains.
5. **Objective Tie-in:** Projects must tie-in to one or multiple objectives in the format of `[O{n}]`. When an objective is moved off the board, related tie-ins must be removed from the active projects.

### Reviews (Ticklers)

Code reviews, PRDs, and minor check-ins go into a dedicated `## Reviews (Scheduled Ticklers)` section on `PROJECTS.md`.
**Rule:** Review items stay EXACTLY one line per item, with a scheduled time (e.g., "[Tomorrow morning] Trading Bot PRD Review"). Do not let them clutter the main active projects. They should be handled in batches so they do not break the main flow.

### The Wait List (Managerial Workflow)

Tracks tasks, decisions, and deliverables currently blocked by or delegated to external collaborators.
1. **Purpose:** Maintain strict accountability without cluttering active project execution. 
2. **Mandatory Format:** Every item MUST explicitly state the **Blocker (Who)**, the **Deliverable (What)**, and an optional **Tickler/Follow-up trigger (When to remind)**.
3. **Board Placement:** The `## Wait List ⏳` section sits directly below `## Active Projects` in `PROJECTS.md`.
4. **Lifecycle:** During daily/weekly reviews, these items are scanned. If overdue, prompt the Operator to send a ping. Once unblocked, the item is either completed, moved back to Active Projects, or discarded.

### Report Status

Read `PROJECTS.md` and summarize active projects. No snapshots, no backups -- read-only.

## Debrief

Full 6-step debrief procedure (calendar, projects, momentum, pep talk, ask, backup): see [references/debrief.md](references/debrief.md)

## File Structure

Paths, naming conventions, and directory layout: see [references/file_structure.md](references/file_structure.md).

## Scripts

**`scripts/cn_calendar.py`** -- Chinese calendar day classifier. Returns JSON with date, weekday, work/rest status, next workday, next holiday block, and upcoming 补班 days.

```bash
python3 scripts/cn_calendar.py [YYYY-MM-DD]   # defaults to today (CST)
```

### Side Projects / Someday-Maybe

Edit or read `SIDE_PROJECTS.md`. Use this when the operator mentions "side projects", "reading list", or "shopping wishlist". These are low-stakes passion ideas and wishes that only require a weekly review, unlike the main `PROJECTS.md`.
