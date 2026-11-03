---
name: project-stash
description: >
  Manage the Operator's personal active projects board (PROJECTS.md), low-stakes side stash (SIDE_PROJECTS.md),
  completed vault archive, and daily personal briefings (Morning Debrief & Nightly Wind-Down).
  Use when the Operator asks about their projects or status, adds/updates/completes a personal project,
  or runs the morning/evening personal debrief.
---

# Project Stash & Personal Alignment (`project-stash`)

## Meta: Design Philosophy of This Skill

This section is for Skill authors and maintainers only. Do not leak it to the user.

- **Responsibility Split (`Myth` vs. `matterman`)**:
  - `matterman` (the workstation Command Center) owns all day-to-day company engineering, quant research pipelines, MR tracking, and weekday company debriefs.
  - `Myth` (`PROJECTS.md` & `SIDE_PROJECTS.md`) owns the Operator's **personal well-being, personal creations/interests, trader craft (`[O3]`), and high-altitude career alignment (`[O1–O3]` North Stars)**—with zero company task sub-tickets or trade secrets.
- **Work Finds Human (Full Board View + Curated Recommendations)**:
  - Because `PROJECTS.md` is now personal-only and concise, the Morning Debrief shows the **full Objectives & Active Projects board** alongside **Body/Sleep + 2/week Convict Conditioning checkboxes** and a **Today's Recommended Feed** (2–3 concrete recommendations for the day).
  - The Nightly Wind-Down (`22:30`) focuses on recovery, activities, CC checkboxes, and a calm reflection without dumping the full board a second time.

---

## Goal

Maintain a clean, high-signal personal project spine (`PROJECTS.md` $\rightarrow$ `vault/myth-projects-stash/completed/`) and deliver daily briefings that align the Operator's **body/recovery**, **personal projects**, **trader craft**, and **career north stars**.

---

## Mental Model & Scope Boundaries

1. **What Lives on `PROJECTS.md` (Personal & Alignment Scope Only)**:
   - **`Active Objectives ([O1]–[O3])`**: High-altitude career and life north stars (max 3). O1/O2 stay on the board as north-star context, while day-to-day company execution lives on `matterman` (never add granular company sub-tickets or trade secrets to `PROJECTS.md`).
   - **`Active Projects`**: Personal tools/creations, trader-craft studies (`[O3]`), writing/essays, and personal admin/errands. Items are flat by default; only use `1.1 / 1.2` sub-tasks when a personal project genuinely needs multi-step tracking.
   - **`Wait List ⏳` & `Reviews (Scheduled Ticklers)`**: Personal external dependencies (`Blocker + Deliverable + Follow-up trigger`) and 1-line scheduled review reminders.
2. **One Completion Rule Everywhere (`Archive to completed/ -> Delete from Board`)**:
   - Whenever a project or sub-task is finished:
     1. Write a concise completion file to `~/.openclaw/workspace/vault/myth-projects-stash/completed/{YYYY-MM-DD}_{Task_or_Project_Name}.md` (`Asia/Shanghai` date, spaces $\rightarrow$ underscores).
     2. **Delete the completed entry from `PROJECTS.md` entirely.** Never keep a `## Completed` section or `[DONE]` items lingering on `PROJECTS.md`.
3. **`SIDE_PROJECTS.md` (Low-Stakes Incubator)**:
   - Holds reading lists, wishlists, and someday/maybe ideas that do not belong on the active board. Surface at most one candidate from here when the Operator has open weekend/rest bandwidth.

---

## Contracts & Operations

### 1. Add, Update, or Report Status on `PROJECTS.md`
- **Add / Update**: Edit `~/.openclaw/workspace/PROJECTS.md` directly (see [`assets/PROJECTS_TEMPLATE.md`](assets/PROJECTS_TEMPLATE.md)), keeping sequential numbering (`1, 2, 3...`) and `[O{n}]` objective tie-ins where relevant.
- **Report Status (Ad-Hoc)**: Read `PROJECTS.md` and summarize cleanly (read-only; no snapshots).

### 2. Daily Briefings (`Morning Debrief` & `Nightly Wind-Down`)
- Follow [`references/debrief.md`](references/debrief.md) for:
  - **Morning Debrief (`08:30 CST`)**: Calendar $\rightarrow$ Body/Sleep & Weekly CC Checkboxes (`N/2`) $\rightarrow$ Full Objectives & Active Projects Board $\rightarrow$ Today's Recommended Feed (`2–3` picks + Pep Talk).
  - **Nightly Wind-Down (`22:30 CST`)**: Garmin activity sync + Weekly CC Checkboxes (`N/2`) + 1 thing handled today + calm power-down note + daily snapshot.

### 3. File Paths & Calendar Helper
- See [`references/file_structure.md`](references/file_structure.md) for canonical paths.
- Run the Chinese calendar classifier via:
  ```bash
  python3 ~/.openclaw/workspace/myth-skills/skills/project-stash/scripts/cn_calendar.py [YYYY-MM-DD]
  ```
