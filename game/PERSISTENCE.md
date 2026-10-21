# Private campaign persistence specification (v0 design)

**Public Elf-Books is for framework and shareable original reference material only.** Use one separately controlled **private** repository or authorized private store for campaign instances. Directory separation in a shared repo is organizational, NOT an access boundary; collaborators can read secrets and commit history.

Suggested private layout:

```text
campaigns/<opaque-id>/
  campaign.json              # public setup, era, rules SHA, status
  characters/<id>.json       # skill ratings, progress, attributes, resources
  world.json                 # player-discovered local facts, era-specific changes
  threads.json               # player-known leads/promises
  state.json                 # current scene/time/location, last sequence
  events.jsonl               # append-only player-safe material outcomes and rolls
  journal.md                 # player-safe recap
  gm/secrets.json            # never expose to player
  gm/private_events.jsonl   # secret rolls, motives, hidden clock changes
```

The `templates/` in this repo provide reference schemas only; actual game files, especially `gm/secrets.json`, are **not** committed to this public repository.

## Contract
- All updates apply to **one identified campaign** and pin the 40-character rules commit used to interpret the sheet. The GM never searches others' campaigns for ideas or saves.
- A game transitions `character_creation` → `preparing` → `active` → `paused` or `complete`. `active` requires fully resolved mechanics, player-approved session zero, and the pre-session readiness gate.
- Skill progress is canonical **only** in the character file. HP/Magicka/items live in that file, world facts in world, scene in state, secret actor clocks in GM secrets, and public leads in threads. Logs describe changes but do not duplicate current fields.
- Every consequential save advances `state.event_seq` and adds matching numbered public event(s); a private event uses its own sequence and may reference the public event. Save a coherent set of files atomically, ideally a single commit.
- Compare previous branch revision and event sequence before saving; never overwrite concurrent progress. Validate and read back committed files. Report commit/revision only after confirmation.
- Do not inject secret lore into player-facing files. A player-facing model that can directly read the GM repo is **not securely isolated**; separate access or GM-only tool context is necessary for genuine secrecy.

## Failure and migration
If the store or dice are unavailable, declare a temporary unsaved state and log pending changes for later authorized reconciliation. Do not silently save in chat memory. Changing advancement policy or upgrading rules needs a documented player-approved character migration, with old/new values visible.
