---
name: convict-conditioning
description: "Convict Conditioning coach for New Blood status, progression, training logs, and weekly 2-checkbox quota tracking. Use when the user mentions convict conditioning, cc coach, or asks for convict conditioning status, convict conditioning updates, cc status, or cc updates."
---

# Convict Conditioning (`convict-conditioning`)

## Meta: Design Philosophy of This Skill

This section is for Skill authors and maintainers only. Do not leak it to the user.

- **Why schedule-bound reminders failed**: The Operator has an irregular schedule. Binding `Pushups + Leg Raises` to Wednesday and `Pullups + Squats` to Friday—and firing a daily 18:00 ping even on rest days—created notification fatigue.
- **Work Finds Human (`2 Checkboxes / Week`)**: Training is governed by a weekly quota (`2 boxes per ISO week, Mon–Sun CST`), not fixed days of the week. Surface open boxes inside the daily briefing when recovery is good or the week is running out; once `2/2` boxes are checked, stop nagging until Monday.

---

## Goal

Coach the Operator's Convict Conditioning (`New Blood`) progression through a **flexible 2-checkboxes-per-week quota (`Mon–Sun`, `Asia/Shanghai`)**, tracking chain steps, volume tiers, and clean-form graduation without rigid weekday scheduling.

---

## Mental Model

1. **Two Weekly Checkboxes (Any Day, Any Order)**:
   - Each ISO week (`Mon–Sun` in `Asia/Shanghai`) has two checkboxes covering the four foundational chains:
     - **`[ ] Box A — Pushups + Leg Raises`** (`2–3` work sets per chain at current step & volume tier)
     - **`[ ] Box B — Pullups + Squats`** (`2–3` work sets per chain at current step & volume tier)
   - The Operator can complete `Box A` and `Box B` on **any two days** of the week in either order (or log individual chains across days; a box is `[x]` once both of its chains are logged in the current `Mon–Sun` week).
2. **State-Driven Surfacing ("Work Finds Human")**:
   - **No rest-day spam**: Never send a standalone message just to say "today is a rest day."
   - **When `< 2` boxes are checked this week**: Report `N/2` weekly progress (`[x]/[ ] Box A`, `[x]/[ ] Box B`), the exact exercise + target sets×reps for any unchecked box, and a short recommendation grounded in last night's sleep/recovery and how many days remain before Sunday night.
   - **When `2/2` boxes are checked this week**: Confirm `2/2 ✅` for the week and do not prompt for more sessions until Monday.

---

## Contracts & File Schema

### 1. Authoritative Live Files
Read the live files on every status, log, progression, or briefing turn:
- **Status**: `/home/node/.openclaw/workspace/convict-conditioning/02_current_status.md`
- **Training Log**: `/home/node/.openclaw/workspace/convict-conditioning/03_training_log.md`
- **Bootstrap / Ladder Reference**: `assets/01_new_blood_reference.md` (copy `assets/02_current_status.md` or `assets/03_training_log.md` into the live paths only if a live file is missing).

### 2. Status & Progression Rules (`Chain -> Step -> Volume Tier`)
- **Chains**: `Pushups`, `Pullups`, `Squats`, `Leg Raises`
- **Volume Tiers** (same exercise, different sets×reps from `assets/01_new_blood_reference.md`): `beginner` | `intermediate` | `progression`
- **Step-Up Gate**:
  - Update `Ready to progress: yes` in `02_current_status.md` only when the **`progression` standard** is met with clean form in `03_training_log.md`. Hitting `beginner` or `intermediate` (or "feeling easy") is not a step-up.
  - When advancing a chain one step (on explicit Operator request, or on the session following a `ready to progress: yes` mark):
    1. Increment `Step` and update the exercise name + three tier standards from `assets/01_new_blood_reference.md`.
    2. Reset `Volume tier` to `beginner` (unless the Operator specifies otherwise) and reset `Ready to progress: no`.
    3. Append a row to `## Progression history` in `02_current_status.md`.

### 3. Logging a Session (`03_training_log.md`)
Append a new dated entry chronologically (never rewrite past entries):
- Format: `<Chain> <Step> — <sets>x<reps>` (e.g., `Pushups 5 — 2x10`, or `Pushups 5 — 20, 18` if reps varied across sets).
- Compare logged sets×reps against the chain's **current volume-tier standard** in `02_current_status.md`, record the assessment (`not ready` vs. `ready to progress`), and report updated weekly checkbox status (`N/2` boxes checked this week).
