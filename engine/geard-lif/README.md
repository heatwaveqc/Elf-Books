# Geard Lif core snapshot for Elf-Books

This directory is a **local, reviewed snapshot** of eight player-audience Geard Lif rules, imported from [heatwaveqc/geard-lif](https://github.com/heatwaveqc/geard-lif) at pinned commit `8bf0801a9ac6731455cf70e77337ff9ebbec84d2`. The upstream repository is private; the copied pages were deliberately marked **player-facing** upstream. Nothing in the source repository's GM or AI-only layers is imported.

Elf-Books follows Geard Lif (internally documented as Raven's Heart) for its **shared Project, resources, and Tier engine**, not D&D/d20. **Progression is an explicit Elf-Books exception:** its 0–25 traits and XP-from-use stay in force even though current base Geard Lif uses 0–5 traits and Drive Marks. The historical imported use-XP pages remain part of this *pinned Elf-Books adapter*, not current upstream law. The canonical upstream engine remains Geard Lif. The checked-in snapshot is the version actually available to public Elf-Books readers and GM runtimes: upstream changes do **not** silently change a pinned campaign.

## Read order

1. [Project Framework](source/Project_Framework.tid): universal consequential action in combat, crafting, travel, research and social play; Complexity, Recalcitrance, Scope, Time
2. [Attributes and Talents](source/Attributes_and_Talents.tid): twelve independent attributes, one selected five-skill Talent, applicable skill/specialty dice
3. [Use-Based Trait Advancement](source/Use_Based_Trait_Advancement.tid): 0–25 ratings, source-tagged XP and natural-ten Skill/Specialty bootstrap
4. [Trait Tiers and Experience Cascade](source/Trait_Tiers_and_Experience_Cascade.tid): governing-die gates, Tier purchases, raw XP cascade, passive resistance XP
5. [Resource Tracks](source/Resource_Tracks.tid): Mind/Body/Soul, six graded resources, marks, promotion, recovery and Costs
6. [Tentative d10 Resolution](source/Tentative_D10_Resolution.tid): pool 7–9 = one success, 10 = two; not finalized
7. [Tentative Tier Scaling](source/Tentative_Tier_Scaling.tid): adopted ×5 per Tier, individual quantities have Tiers
8. [Status and missing fundamentals](SYSTEM_STATUS.md)
9. [Elder Scrolls implementation boundaries](../../rules/RULES_INDEX.md)
10. [Migration and critical path](../../MIGRATION_BACKLOG.md)

For executable **pure arithmetic exercises**, see [`scripts/geard_core.py`](../../scripts/geard_core.py). This script can compute d10 successes, Tier conversion, resource severity/mark/recovery and track project progress. It evaluates **meet-to-beat application**, Potence-to-four-grade marks, **Scope-sized Project mark capacity**, promotion/exhaustion, and optional protection-adjusted personal thresholds. It also includes a tested provisional four-source trait pool calculator. It can now calculate the working rating/XP curve and per-source roll XP; full character budgets, equipment values, legal reaction timing, spell-effect catalogs and Talent-tree/perk systems still need work.

## Targeted later core rule adoption

The eight imported tiddlers retain the documented historical base pin `8bf0801a9ac6731455cf70e77337ff9ebbec84d2`. A **reviewed, player-facing universal supernatural restoration** section from upstream Geard Lif commit `9a1817d14fef0d4b01c3cadcf3384cc20cff220b` is now selectively incorporated into the local [Resource Tracks](source/Resource_Tracks.tid). This gives all six personal tracks the universal **infliction-equivalence healing** rule: one grade-g restorative mark reverses `(Resilience+1)^g` Minor-mark equivalents of inflicted marks.

Only that later section was imported. **The remaining pinned text stays at its historical snapshot version**, including Elf Books' retained fast-recovery cadence; the newer Geard Lif *once-per-own-turn* cadence was not silently adopted here. The Elf Books 0–25/use-XP advancement variant also remains separate. See [UPSTREAM.json](UPSTREAM.json) for the explicit selective-import provenance and [magic](../../design/MAGIC.md) for the TES Restoration adapter.

## Updating the snapshot

- Inspect [UPSTREAM.json](UPSTREAM.json) for the source commit and paths.
- Fetch only reviewed *public-player-marked* upstream tiddlers at a specific newer commit. **Do not overwrite Elf-Books 0–25/use-XP adapter rules with the new 0–5/Drive-Mark core; port shared mechanics separately and update local adapter tests.**
- Compare their diffs to this snapshot; separately re-evaluate the status notes and any Elf-Books overlays.
- Run repository tests and migrate ongoing private campaign rules only with explicit consent.
- Never copy upstream `ai/`, `geard-audience: gm`, or unpublished material into the public snapshot without a specific review.
- Do not automatically copy or sublicense Geard Lif material beyond the owner's authorized Elf-Books adaptation; no general license is implied by this import.

The preserved prior d20 system is on [`archive/d20-pre-geard-lif`](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif); **it is historical**, not an alternate active engine.

**Current aspect ownership:** Mind/Will holds Spirit and Mana; Soul/Conviction holds Plasticity and Attention; Body/Health holds Injury and Fatigue. See [resource tracks](source/Resource_Tracks.tid) and [Elf-Books' four-source Cost rule](../../design/MAGIC.md).

Eighth imported public-player rule: [Named Action Pools and Defense Modes](source/Named_Action_Pools_and_Defense_Modes.tid). Shorthand is Attribute + Skill, with applicable governed-Skill Talent, Specialty and external bonuses. Every contested effect declares legitimate defensive pairs. All gear/enchantment/ensorcellment/temporary-buff dice share a combined cap equal to the unmodified applicable personal dice. [TES attack modes](../../rules/ATTACK_MODES.md).

**Latest fivefold upgrade:** Tier scale, trait-tier XP costs and source XP rewards now share the **×5 per Tier** rule; higher-tier passive XP can be fractional (tenths ledger). Ordinary social attacks directly mark only Attention; Plasticity requires supernatural attack. Conviction is Soul soak/capacity, not an ordinary defense against application. See [attack-mode defaults](../../rules/ATTACK_MODES.md).

**Exhausted fast → slow:** [Resource Tracks](source/Resource_Tracks.tid) now redirects further fast-targeted effects, including Costs, to the paired slow resource: Fatigue→Injury, Mana→Spirit, Attention→Plasticity. The initial exhausting incident remains wholly fast; mundane social Attacks can overflow into Plasticity without supernatural direct targeting.
