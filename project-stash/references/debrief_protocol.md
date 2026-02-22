# Debrief Protocol

The daily debrief prompt injected by cron. This is the verbatim text used to generate debriefs.

---

## Prompt Text (Injectable)

```
[Project Stash Debrief]
Answer as Myth. Read `PROJECTS.md`. Write a debrief following this order:

1. **Calendar:** Run `python3 /home/node/.openclaw/workspace/myth-skills/project-stash/scripts/cn_calendar.py`. Output current CST date/time/weekday and day status. Report `next_workday` (if resting), `next_holiday_block`, and `upcoming_buban`. Add a brief greeting.

2. **Projects:** List projects with 1-line progress.

3. **Momentum Check:** Compare current PROJECTS.md with the 3 newest snapshots in `vault/myth-projects-stash/daily-snapshots/`. For each project that appeared in snapshots but is missing from current PROJECTS.md, check `COMPLETED_LOG.md`:
   - If present in COMPLETED_LOG.md → mark as "completed ✅"
   - If absent from COMPLETED_LOG.md → mark as "dropped ⚠️"
   Analyze velocity, focus vs. scatter, and execution rhythm. Distinguish completions from drops.

4. **Pep Talk:** Deliver a brief pep talk.

5. **Ask for Updates:** Ask the operator for updates on active projects.

6. **Backup:** If the CST time is 20:00 or later, execute this command to take a daily snapshot:
   `cp PROJECTS.md vault/myth-projects-stash/daily-snapshots/$(TZ='Asia/Shanghai' date +%Y-%m-%d)_PROJECTS.md`
   and confirm it was saved.

**Your reply IS the debrief.** Output the full debrief text above as plain text. Do not summarize. Do not output a file path. The full text of your reply will be delivered directly to the channel.
```

---

## Key Change from Previous Version

The momentum check now uses `COMPLETED_LOG.md` to distinguish between:
- **Completed projects** (logged, archived) — intentional closure
- **Dropped projects** (not logged, no archive) — may need follow-up

This resolves the ambiguity when a project disappears from the active board.
