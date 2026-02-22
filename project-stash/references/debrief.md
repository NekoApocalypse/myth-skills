# Debrief Procedure

Answer as Myth. Read `PROJECTS.md` and produce a debrief with the following sections in order.

## 1. Calendar

Run `python3 ~/.openclaw/workspace/myth-skills/project-stash/scripts/cn_calendar.py`.

Output from the JSON result:
- Current CST date, time, and weekday
- Day status (`work_normal`, `work_buban`, `rest_normal`, `rest_holiday`)
- `next_workday` (only on rest days)
- `next_holiday_block` (name, start, end)
- `upcoming_buban` (list of upcoming compensatory workdays)

Add a brief greeting appropriate to the day.

## 2. Projects

List each active project from `PROJECTS.md` with a 1-line progress summary.

## 3. Momentum Check

Compare current `PROJECTS.md` with the **3 newest snapshots** in `~/.openclaw/workspace/vault/myth-projects-stash/daily-snapshots/`. Also check recent entries in `~/.openclaw/workspace/vault/myth-projects-stash/completed/` for recently finished work.

Analyze:
- **Velocity** -- are projects moving forward? Any recently completed?
- **Focus vs. scatter** -- concentrated effort or spread thin?
- **Execution rhythm** -- consistent daily progress or bursts and stalls?

## 4. Pep Talk

Deliver a brief pep talk.

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
- The reply will be delivered directly to the channel.
