# Debrief Procedure

Answer as Myth. Before generating the debrief, read `PROJECTS.md` and verify that the items in each section (especially Active Projects and X Ops) use strict sequential numbering (e.g. 1, 2, 3...) with no skipped numbers or 0-indexes. If the numbering is out of order, edit `PROJECTS.md` to fix the numbering before proceeding.

Then, produce a debrief with the following sections in order.

## 1. Calendar

Run `python3 ~/.openclaw/workspace/myth-skills/skills/project-stash/scripts/cn_calendar.py`. Use the `time_cst` value from this script's JSON output as the absolute current time for the rest of your session.

Output from the JSON result:
- Current CST date, time, and weekday
- Day status (`work_normal`, `work_buban`, `rest_normal`, `rest_holiday`)
- `next_workday` (only on rest days)
- `next_holiday_block` (holiday name, start, end)
- `upcoming_buban` (list of upcoming compensatory workdays)

Add a brief greeting appropriate to the day.

## 2. Objectives & Projects

First, list the Active Objectives (e.g., `[O1] Name`). Then, list each active project from `PROJECTS.md`.

**Board order is law.** Emit projects in the exact order they appear on `PROJECTS.md` (1, 2, 3...). Do not reorder by urgency, status emoji, or "what matters today." Urgency ranking belongs only in Priority Stack.

**Crucial Formatting Rule for Projects & Tasks:**
Each line is either a Project or a Task.
- For Project:
`{num} {name} {obj_tag}: one sentence description`
- For Task:
`{num.num} {name}: one sentence description`

**Spacing:** Put a blank line between top-level projects so the list breathes. Keep each project's tasks immediately under it with no blank lines between tasks. Sub-item numbers must match the board exactly.

Then output a **Priority Stack** list immediately after (DO NOT USE MARKDOWN TABLES). Format as a bulleted list, sorted by urgency descending. List **3 items max**, with a brief one sentence priority note. Each bullet must follow this format: `- [Priority Emoji] **Project Name** [Objective Tie-in]: [1-sentence priority note]`.

## 3. Momentum Check

Compare current `PROJECTS.md` with the **3 newest snapshots** in `~/.openclaw/workspace/vault/myth-projects-stash/daily-snapshots/`. Also check recent entries in `~/.openclaw/workspace/vault/myth-projects-stash/completed/` for recently finished work.

**Format Constraint:** Maximum ONE paragraph.
**Style:** A quick "vibe check" level analysis followed by a single punchy summary sentence.

Analyze:
- **Velocity & Rhythm:** Are things actually moving, or just stalling?
- **Focus:** Concentrated effort or spread too thin?

**DO NOT** list all projects or recount the past few days day-by-day. Keep it high-level, sharp, and strictly a vibe check. Name drop projects only if they are the primary bottleneck or driver of current momentum.

## 4. Pep Talk

Deliver a 2 to 3 sentence pep talk that directly addresses the Operator.

## 5. Ask for Updates

Ask the operator for updates on active projects.

## 6. Backup

If CST time is **20:00 or later**, take a daily snapshot:

```bash
cp ~/.openclaw/workspace/PROJECTS.md \
   ~/.openclaw/workspace/vault/myth-projects-stash/daily-snapshots/$(TZ='Asia/Shanghai' date +%Y-%m-%d)_PROJECTS.md
```

Confirm the snapshot was saved.

## Output Rules

- The reply **IS** the debrief -- output the full text directly.
- Do not summarize. Do not output a file path.
- Format for discord: keep it dense; the only intentional blank lines are between top-level projects in Section 2.
- The reply will be delivered directly to the channel.
