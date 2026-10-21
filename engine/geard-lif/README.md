# Geard Lif core snapshot for Elf-Books

This directory is a **local, reviewed snapshot** of five player-audience Geard Lif rules, imported from [heatwaveqc/geard-lif](https://github.com/heatwaveqc/geard-lif) at pinned commit `ac172d47bcb0f0d6b5db42df98f67cc3abd54c3d`. The upstream repository is private; the copied pages were deliberately marked **player-facing** upstream. Nothing in the source repository's GM or AI-only layers is imported.

Elf-Books follows Geard Lif (internally documented as Raven's Heart) as its **base rules engine**, not D&D/d20. The canonical upstream engine remains Geard Lif. The checked-in snapshot is the version actually available to public Elf-Books readers and GM runtimes: upstream changes do **not** silently change a pinned campaign.

## Read order

1. [Project Framework](source/Project_Framework.tid): universal consequential action in combat, crafting, travel, research and social play; Complexity, Recalcitrance, Scope, Time
2. [Attributes and Talents](source/Attributes_and_Talents.tid): twelve independent attributes, one selected five-skill Talent, applicable skill/specialty dice
3. [Resource Tracks](source/Resource_Tracks.tid): Mind/Body/Soul, six graded resources, marks, promotion, recovery and Costs
4. [Tentative d10 Resolution](source/Tentative_D10_Resolution.tid): pool 7–9 = one success, 10 = two; not finalized
5. [Tentative Tier Scaling](source/Tentative_Tier_Scaling.tid): provisional 10× per Tier, individual quantities have Tiers
6. [Status and missing fundamentals](SYSTEM_STATUS.md)
7. [Elder Scrolls implementation boundaries](../../rules/RULES_INDEX.md)
8. [Migration and critical path](../../MIGRATION_BACKLOG.md)

For executable **pure arithmetic exercises**, see [`scripts/geard_core.py`](../../scripts/geard_core.py). This script can compute d10 successes, Tier conversion, resource severity/mark/recovery and track project progress. It evaluates **meet-to-beat application**, Potence-to-four-grade marks, **Scope-sized Project mark capacity**, promotion/exhaustion, and optional protection-adjusted personal thresholds. It also includes a tested provisional four-source trait pool calculator. It cannot run a complete encounter: final budgets/caps, equipment formulas, defense timing, magic and advancement still need work.

## Updating the snapshot

- Inspect [UPSTREAM.json](UPSTREAM.json) for the source commit and paths.
- Fetch the five *public-player-marked* upstream tiddlers at a specific newer commit.
- Compare their diffs to this snapshot; separately re-evaluate the status notes and any Elf-Books overlays.
- Run repository tests and migrate ongoing private campaign rules only with explicit consent.
- Never copy upstream `ai/`, `geard-audience: gm`, or unpublished material into the public snapshot without a specific review.
- Do not automatically copy or sublicense Geard Lif material beyond the owner's authorized Elf-Books adaptation; no general license is implied by this import.

The preserved prior d20 system is on [`archive/d20-pre-geard-lif`](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif); **it is historical**, not an alternate active engine.
