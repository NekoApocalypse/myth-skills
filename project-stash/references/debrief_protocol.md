# Debrief Protocol

The daily debrief prompt injected by cron. This is the verbatim text used to generate debriefs.

---

## Prompt Text (Injectable)

```
[Project Stash Debrief]
Answer as Myth. Read `PROJECTS.md` and `COMPLETED_LOG.md` (workspace root; may not exist yet if no projects have been completed). Write a debrief following this order:

1. **Calendar:** Run `python3 /home/node/.openclaw/workspace/myth-skills/project-stash/scripts/cn_calendar.py`. Output current CST date/time/weekday and day status. Report `next_workday` (if resting), `next_holiday_block`, and `upcoming_buban`. Add a brief greeting.

2. **Projects:** List active projects with 1-line progress each.

3. **Momentum Check:** Compare current `PROJECTS.md` with the 3 newest snapshots in `vault/myth-projects-stash/daily-snapshots/`. For each project that appeared in a snapshot but is missing from current `PROJECTS.md`, cross-reference `COMPLETED_LOG.md`:
   - If found in `COMPLETED_LOG.md` → mark as "completed ✅" (intentional closure)
   - If absent from `COMPLETED_LOG.md` → mark as "dropped ⚠️" (may need follow-up)
   Analyze overall velocity, focus vs. scatter, and execution rhythm.

4. **Pep Talk:** Deliver a brief pep talk.

5. **Ask for Updates:** Ask the operator for updates on active projects.

6. **Backup:** If the CST time is 20:00 or later, run the snapshot script:
   `bash /home/node/.openclaw/workspace/myth-skills/project-stash/scripts/snapshot.sh`
   and confirm the output path it reports.

**Your reply IS the debrief.** Output the full debrief text as plain text. Do not summarize. Do not output a file path. The full text of your reply will be delivered directly to the channel.
```

---

## Notes

- `COMPLETED_LOG.md` may not exist if no projects have been completed yet — handle gracefully (treat all disappearances as dropped)
- The snapshot script (`scripts/snapshot.sh`) prints the saved path on success; confirm that path in the debrief output
