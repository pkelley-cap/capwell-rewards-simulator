# CapWell Rewards Simulator

A single-file browser tool for modeling annual points and reward earnings in a healthcare wellness program. No install, no server, no dependencies — open `index.html` in any browser.

## What it does

Simulates how a member accumulates points across four earn types, then maps those points to dollar rewards:

| Earn type | How points accrue |
|---|---|
| **Habits** | Daily check-ins + weekly goals, plus 4/8/12-week consistency bonuses |
| **Challenges** | Per-checkpoint points + a completion bonus |
| **Learning tracks** | Daily completion points over a 10-day track + a completion bonus |
| **Healthy actions** | One-time actions (screenings, exams) + monthly gym and step goals |

Reward thresholds pay out independently as they're crossed, so total reward is the sum of every threshold reached.

## Using it

**Simulate** tabs drive the member-side inputs — months active, activities per month, average completion rate. The summary bar at the top updates live and breaks earnings down by color. Use the ◀ ▶ arrows in the legend to reorder segments.

**Global config** holds the program-wide rules: habit and challenge point values, consistency bonus multipliers, learning track values, and per-month limits.

**Client config** holds the per-client settings that vary between employers: monthly goal values, the healthy actions list, and reward thresholds.

### Gatekeeper logic

Healthy actions can be marked *gatekeeper* or *gatekept*. Gatekept actions stay locked until every gatekeeper action is complete — this models programs that require a health survey before other activities unlock. Toggle **No gatekeepers** to make all actions independent.

## Saving and sharing configurations

Saved configs live in your browser's local storage, so they don't travel between machines or people. To share a setup with a colleague, use **Export current** to download it as JSON and have them use **Import JSON** on their end.

## Editing

Everything is in one file — HTML, CSS, and JavaScript. Open it in any text editor to change defaults. The starting values for activities, thresholds, and point rules are declared as plain JavaScript objects near the top of the `<script>` block.
