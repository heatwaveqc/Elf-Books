# Geard Lif core snapshot for Elf-Books

This directory is a **local, reviewed snapshot** of four player-audience Geard Lif rules, imported from [heatwaveqc/geard-lif](https://github.com/heatwaveqc/geard-lif) at pinned commit `237448aa78d0305070b503ab85af612a0b381a93`. The upstream repository is private; the copied pages were deliberately marked **player-facing** upstream. Nothing in the source repository's GM or AI-only layers is imported.

Elf-Books follows Geard Lif (internally documented as Raven's Heart) as its **base rules engine**, not D&D/d20. The canonical upstream engine remains Geard Lif. The checked-in snapshot is the version actually available to public Elf-Books readers and GM runtimes: upstream changes do **not** silently change a pinned campaign.

## Read order

1. [Project Framework](source/Project_Framework.tid): universal consequential action in combat, crafting, travel, research and social play; Complexity, Recalcitrance, Scope, Time
2. [Resource Tracks](source/Resource_Tracks.tid): Mind/Body/Soul, six graded resources, marks, promotion, recovery and Costs
3. [Tentative d10 Resolution](source/Tentative_D10_Resolution.tid): pool 7–9 = one success, 10 = two; not finalized
4. [Tentative Tier Scaling](source/Tentative_Tier_Scaling.tid): provisional 10× per Tier, individual quantities have Tiers
5. [Status and missing fundamentals](SYSTEM_STATUS.md)
6. [Elder Scrolls implementation boundaries](../../rules/RULES_INDEX.md)
7. [Migration and critical path](../../MIGRATION_BACKLOG.md)

For executable **pure arithmetic exercises**, see [`scripts/geard_core.py`](../../scripts/geard_core.py). This script can compute d10 successes, Tier conversion, resource severity/mark/recovery and track project progress. It cannot run a complete encounter: upstream success ties, precise Effect-vs-Recalcitrance mechanics, skills, damage/equipment and advancement are still unresolved.

## Updating the snapshot

- Inspect [UPSTREAM.json](UPSTREAM.json) for the source commit and paths.
- Fetch the four *public-player-marked* upstream tiddlers at a specific newer commit.
- Compare their diffs to this snapshot; separately re-evaluate the status notes and any Elf-Books overlays.
- Run repository tests and migrate ongoing private campaign rules only with explicit consent.
- Never copy upstream `ai/`, `geard-audience: gm`, or unpublished material into the public snapshot without a specific review.
- Do not automatically copy or sublicense Geard Lif material beyond the owner's authorized Elf-Books adaptation; no general license is implied by this import.

The preserved prior d20 system is on [`archive/d20-pre-geard-lif`](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif); **it is historical**, not an alternate active engine.
