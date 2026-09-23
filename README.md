# CapWell Rewards Simulator

A single-file browser tool for modeling annual pebbles and reward earnings in a healthcare wellness program. No install, no server, no dependencies — open `index.html` in any browser.

## What it does

Simulates how a member accumulates pebbles across four earn types, then maps those pebbles to dollar rewards:

| Earn type | How pebbles accrue |
|---|---|
| **Habits** | Daily check-ins + weekly goals, plus 4/8/12-week consistency bonuses |
| **Challenges** | Per-checkpoint pebbles + a completion bonus |
| **Learning tracks** | Daily completion pebbles over a 10-day track + a completion bonus |
| **Step-It-Up** | Daily step tier pebbles x 30 days per month — the highest tier reached, tiers do not stack |
| **Healthy actions** | One-time actions (screenings, exams) |

Reward thresholds pay out independently as they're crossed, so total reward is the sum of every threshold reached.

## Using it

**Simulate** tabs drive the member-side inputs — months active, activities per month, average completion rate. The summary bar at the top updates live and breaks earnings down by color. Use the ◀ ▶ arrows in the legend to reorder segments.

**Global config** holds the program-wide rules: habit and challenge pebble values, consistency bonus multipliers, learning track values, and per-month limits.

**Client config** holds the per-client settings that vary between employers: the healthy actions list and reward thresholds.

### Gatekeeper logic

Healthy actions can be marked *gatekeeper* or *gatekept*. Gatekept actions stay locked until every gatekeeper action is complete — this models programs that require a health survey before other activities unlock. Toggle **No gatekeepers** to make all actions independent.

## Saving and sharing configurations

Saved configs live in your browser's local storage, so they don't travel between machines or people. To share a setup with a colleague, use **Export current** to download it as JSON and have them use **Import JSON** on their end.

## Editing

## Saving configurations

Configs are saved against a client name on the **Saved configs** tab, and the list groups scenarios by client.

Storage depends on where the page is running:

- **Opened as a local file** — configs go to `localStorage`, so they stay in that one browser. Use Export / Import JSON to move them between machines or share them.
- **Published as a Claude Artifact** — configs go to the artifact's shared document store (the `db` capability), so everyone with access to the page sees the same list, and edits show up live. A status line under the save box says which mode is active. If shared storage can't be reached, saves fall back to `localStorage` and the status line says so.

When both apply, an "Upload N configs saved in this browser" button appears so local-only saves can be pushed to shared storage on purpose, rather than silently syncing.

`build-artifact.py` generates the Artifact body from `index.html` — it strips the document skeleton the Artifact runtime supplies itself, so `index.html` stays the single source of truth:

```
./build-artifact.py            # -> dist/artifact.html
```

Everything is in one file — HTML, CSS, and JavaScript. Open it in any text editor to change defaults. The starting values for activities, thresholds, and pebble rules are declared as plain JavaScript objects near the top of the `<script>` block.
