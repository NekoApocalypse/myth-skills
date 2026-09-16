---
name: convict-conditioning
description: "Convict Conditioning coach for New Blood status, progression, training logs, and daily reminders. Use when the user mentions convict conditioning, cc coach, or asks for convict conditioning status, convict conditioning updates, cc status, or cc updates."
---

# Convict Conditioning

Coach the Operator's Convict Conditioning program. The active program is whatever the live status file records (New Blood at init).

## Files

Live files are authoritative. Read them on every status, log, progression, or reminder turn.

- Status: `/home/node/.openclaw/workspace/convict-conditioning/02_current_status.md`
- Log: `/home/node/.openclaw/workspace/convict-conditioning/03_training_log.md`

Skill assets are bootstrap and reference only:

- `assets/01_new_blood_reference.md` — schedule, ladders, progression rules
- `assets/02_current_status.md` — initial snapshot
- `assets/03_training_log.md` — log template

Copy assets into the live paths only when those live files are missing. Leave existing live files alone.

## Daily reminder

Standard week is 2 sessions. Appointed days: Monday (Pushups + Leg Raises) and Friday (Pullups + Squats). A missed appointed day can be made up later the same CST week (Mon–Sun).

When running the daily reminder, read the live log for this CST week and report:

- Weekday in CST
- Current week progress as `N/2` (logged sessions this CST week)
- Remaining chains not yet trained this week
- Schedule: today's appointed session, a makeup if an appointed day was missed, or rest

Keep it short. No tables.

## Status and progression

On status or next-step questions, read live status plus the matching ladder in the New Blood reference. Report the current step, exercise, target, ready flag, and the next-step goalpost (exercise + target). If the chain is at the last tabulated step, say so.

On an explicit request to progress a named chain:

1. Advance that chain one step in the live status file
2. Set exercise and target from the ladder
3. Reset ready-to-progress
4. Append a progression-history row
5. Mention the new goalpost

Advance a step only on that explicit request, or when the reference rule says the next scheduled session should move up after a ready-to-progress mark. Feeling easy is not enough.

## Session log

Append a new dated entry. Do not rewrite old entries. Compare each chain's work sets to its current target with the evaluation rule in the New Blood reference. Update ready-to-progress in live status. Record the assessment in the log.

## Cron

A daily isolated job should fire this reminder into #myth-coach. Keep the cron prompt skill-driven: `Run the convict-conditioning skill daily reminder.`
