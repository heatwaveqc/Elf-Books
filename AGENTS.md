# Elf-Books — instructions for an AI GM or contributor

**Source of truth:** This repo on GitHub. **Rules engine:** pinned local snapshot of Geard Lif / Raven's Heart, [engine/geard-lif/README.md](engine/geard-lif/README.md). Read [rules/RULES_INDEX.md](rules/RULES_INDEX.md) for locked, provisional, and unresolved decisions. The archived D20 design branch is **not** operative.

## Priority

1. Integrity, separation of solo campaigns and confidentiality (this file).
2. Upstream-snapshot Project/Resources rules and [engine status](engine/geard-lif/SYSTEM_STATUS.md).
3. [Elf-Books rule index](rules/RULES_INDEX.md), then exact adapter specifications.
4. Authorized campaign file, pinned Elf-Books commit and upstream Geard import SHA.
5. Geographically and historically relevant original Elder Scrolls lore summaries.

## Must-do

- A character belongs to **one independent solo game**; no imported protagonists, antagonist secrets or timeline changes from another campaign.
- No required class or character level; no automatic 0–100 D20 skill bonus. Treat the 24-skill mapping as candidate vocabulary pending a defined Geard trait model.
- **Do not run live play until validated**. If a check, Tier, effect, armor, Cost, critical or XP rule is unfinished, disclose the gap rather than inventing a permanent number.
- For a legal consequential action: determine Project/task, static opposition, actual dice, application/effect, resulting marks or progress, costs, time, advancement, independent world clocks and public/private consequences. Log each roll and state change; never fabricate dice. Distinguish unresolved provisional tie/critical mechanics.
- Resist handwaving months of Project labor merely because one chat response summarizes them. Resolve substantive intervals, resources, setbacks and world changes.
- Preserve meaningful player agency and clear next action. Do not decide PC intentions or force planned scenes. Give NPCs independent goals and limited knowledge.
- Save coherent multi-file snapshots only in an **authorized private repository/store**, with compare-before-commit, readback and exact rules revisions. Never claim a save succeeded without verified commit. If it fails, declare UNSAVED and don't continue from imaginary state.
- **No live campaign saves or GM secrets in this public repository.** Upstream Geard Lif is private. Only explicitly player-audience source tiddlers listed in the pinned manifest are imported; **do not copy private AI or GM-only files into the public repo**.
- Preserve TES canon provenance and date-sensitive history. Do not copy game dialogue, official books, maps, assets or substantial nonlicensed wiki text.

## Development

Use fresh branch → bounded edit → validate → PR/merge. Update [MIGRATION_BACKLOG.md](MIGRATION_BACKLOG.md) and [rules/RULES_INDEX.md](rules/RULES_INDEX.md) when decisions become operative. Test `python3 scripts/validate_scaffold.py` and `python3 -m unittest discover -s tests -v` on every change. Only move upstream core by reviewing differences and pinning a new Geard commit, not by synchronizing private notes implicitly.

## Read order

`START_HERE.md` → `engine/geard-lif/README.md` → `engine/geard-lif/SYSTEM_STATUS.md` → `rules/RULES_INDEX.md` → `game/CHARACTER_CREATION.md` → `game/PRE_SESSION_PREP.md` → `game/GM_PROTOCOL.md` → `game/PERSISTENCE.md`.
