[Project Stash Debrief] 
Answer as Myth. Read `PROJECTS.md`. Write a debrief and format following order: 
1. **Calendar:** Run `python3 /home/node/.openclaw/workspace/myth-skills/project-stash/cn_calendar.py`. Output current CST date/time/weekday and day status. Report `next_workday` (if resting), `next_holiday_block`, and `upcoming_buban`. Add a brief greeting. 
2. **Projects:** List projects with 1-line progress. 
3. **Momentum Check:** Compare current PROJECTS.md with the 3 newest snapshots in `vault/myth-projects-stash/daily-snapshots/`. Analyze velocity, focus vs. scatter, and execution rhythm. 
4. **Pep Talk:** Delivera a brief pep talk. 
5. **Ask for Updates:** Ask the operator for updates on active projects. 
6. **Backup:** If the CST time is 20:00 or later, execute this command to take a daily snapshot: `cp PROJECTS.md vault/myth-projects-stash/daily-snapshots/$(TZ='Asia/Shanghai' date +%Y-%m-%d)_PROJECTS.md` and confirm it was saved.