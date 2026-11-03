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
- `assets/02_current_status.md` — status schema snapshot
- `assets/03_training_log.md` — log template

Copy assets into the live paths only when those live files are missing. Leave existing live files alone.

## Status schema

Live status tracks **Chain → Step → Volume tier**.

- Chain: Pushups, Pullups, Squats, Leg Raises
- Step: step number + exercise name
- Volume tier: `beginner` | `intermediate` | `progression` on that step (sets/reps only; same exercise)

Each chain section stores: step, volume tier, the three standards, ready-to-progress (step), and a note.

## Daily reminder

The reminder cron fires **every day**, including rest days. Do not skip a rest-day ping.

Standard week is 2 sessions. Appointed days: Wednesday (Pushups + Leg Raises) and Friday (Pullups + Squats). A missed appointed day can be made up later the same CST week (Mon–Sun).

When running the daily reminder, read the live log for this CST week and report:

- Weekday in CST
- Current week progress as `N/2` (logged sessions this CST week)
- Remaining chains not yet trained this week
- Schedule: today's appointed session, a makeup if an appointed day was missed, or rest

On a rest day, say it is rest and still report weekly progress. Keep it short. No tables.

## Status and progression

On status or next-step questions, read live status plus the matching ladder in the New Blood reference. Report chain, step, volume tier, the three standards, the current-tier target, ready flag, and the next-step goalpost. If the chain is at the last tabulated step, say so.

On an explicit request to set a volume tier: update that field only. Do not change the step.

On an explicit request to progress a named chain (step-up):

1. Advance that chain one step in the live status file
2. Set exercise and the three standards from the ladder
3. Reset volume tier to beginner unless the operator specifies a tier
4. Reset ready-to-progress
5. Append a progression-history row
6. Mention the new step and volume-tier goalpost

Advance a step only on that explicit request, or when the reference rule says the next scheduled session should move up after a ready-to-progress mark. Feeling easy is not enough. Hitting beginner or intermediate is not a step-up.

## Session log

Append a new dated entry. Do not rewrite old entries. Compare each chain's work sets to the **current volume-tier** standard. Update ready-to-progress only when the **progression** standard is met with clean form. Record the assessment in the log.

## Cron

A daily isolated job fires this reminder into #myth-coach every day at 18:00 CST, including rest days. Keep the cron prompt skill-driven: `Run the convict-conditioning skill daily reminder.`
