# Convict Conditioning — New Blood Reference

## Weekly schedule

| Day | Training | Volume |
|---|---|---|
| Monday | Pushups + Leg Raises | 2–3 work sets per chain |
| Tuesday | Rest | — |
| Wednesday | Rest | — |
| Thursday | Rest | — |
| Friday | Pullups + Squats | 2–3 work sets per chain |
| Saturday | Rest | — |
| Sunday | Rest | — |

New Blood uses only the four basic chains. Bridges and handstand pushups are held back until later.

## Progression ladders

Notation: `3x50` means 3 work sets of 50 clean repetitions each.

Each step has three volume tiers on the same exercise:

- beginner
- intermediate
- progression (graduation to the next step)

### Pushups

| Step | Exercise | Beginner | Intermediate | Progression |
|---:|---|---:|---:|---:|
| 1 | Wall Pushups | 1x10 | 2x25 | 3x50 |
| 2 | Incline Pushups | 1x10 | 2x20 | 3x40 |
| 3 | Kneeling Pushups | 1x10 | 2x15 | 3x30 |
| 4 | Half Pushups | 1x8 | 2x12 | 2x25 |
| 5 | Full Pushups | 1x5 | 2x10 | 2x20 |
| 6 | Close Pushups | 1x5 | 2x10 | 2x20 |

### Pullups

| Step | Exercise | Beginner | Intermediate | Progression |
|---:|---|---:|---:|---:|
| 1 | Vertical Pulls | 1x10 | 2x20 | 3x40 |
| 2 | Horizontal Pulls | 1x10 | 2x20 | 3x30 |
| 3 | Jackknife Pulls | 1x10 | 2x15 | 3x20 |
| 4 | Half Pullups | 1x8 | 2x11 | 2x15 |
| 5 | Full Pullups | 1x5 | 2x8 | 2x10 |
| 6 | Close Pullups | 1x5 | 2x8 | 2x10 |

### Squats

| Step | Exercise | Beginner | Intermediate | Progression |
|---:|---|---:|---:|---:|
| 1 | Shoulderstand Squats | 1x10 | 2x25 | 3x50 |
| 2 | Jackknife Squats | 1x10 | 2x20 | 3x40 |
| 3 | Supported Squats | 1x10 | 2x15 | 3x30 |
| 4 | Half Squats | 1x8 | 2x35 | 2x50 |
| 5 | Full Squats | 1x5 | 2x10 | 2x30 |
| 6 | Close Squats | 1x5 | 2x10 | 2x20 |

### Leg Raises

| Step | Exercise | Beginner | Intermediate | Progression |
|---:|---|---:|---:|---:|
| 1 | Knee Tucks | 1x10 | 2x25 | 3x40 |
| 2 | Flat Knee Raises | 1x10 | 2x20 | 3x35 |
| 3 | Flat Bent-Leg Raises | 1x10 | 2x15 | 3x30 |
| 4 | Flat Frog Raises | 1x8 | 2x15 | 3x25 |
| 5 | Flat Straight-Leg Raises | 1x5 | 2x10 | 2x20 |
| 6 | Hanging Knee Raises | 1x5 | 2x10 | 2x15 |

## Progression rules

1. Train the chain at its current step and current volume tier.
2. Use 2–3 work sets. If the current-tier target requires 3 sets, perform 3 work sets when testing that gate.
3. Record the actual repetitions completed in every work set.
4. Count only controlled repetitions performed with the intended range of motion and acceptable form.
5. Do not count repetitions completed through obvious form breakdown. Pain is a stop signal, not a progression signal.
6. Volume tiers only change sets/reps. Hitting beginner or intermediate is not a step-up.
7. A chain is **ready to progress** (next step) when all required work sets reach the **progression** standard in the same session with clean form.
8. On the next scheduled session for that chain, move to the next step. Start at beginner on the new step unless the operator specifies a tier.
9. If the new step cannot be performed with controlled form, return to the prior step and continue building capacity.
10. Judge each chain independently. One chain can remain at Step 2 beginner while another reaches Step 6 progression.
11. The original New Blood template is normally retained until the trainee has moved past roughly Step 6 in all four chains; only then is the next program necessary.

## Agent evaluation rule

After each logged workout:

- Read the current step and volume tier from `02_current_status.md`.
- Compare the logged work sets with that volume-tier standard.
- If every required set meets or exceeds the **progression** standard with clean form, mark the chain `ready_to_progress: yes`.
- Otherwise mark it `ready_to_progress: no`.
- Do not change the current step or volume tier merely because the user says the exercise felt easy.
- When a step actually advances, update `02_current_status.md`, reset volume tier to beginner unless specified, and add a dated entry to its progression history.
- When the operator sets a volume tier, update that field only.

## Sources

- Original New Blood schedule and transition guidance: https://github.com/xwzliang/physical_conditioning/blob/master/convict_conditioning/routines.md
- Progression tables: https://virtusapp.ai/blog/convict-conditioning-program-guide/
- Pullup progression cross-check: https://farran.abwe.org/uploads/9/7/1/2/97128822/convict_conditioning_overview.pdf
