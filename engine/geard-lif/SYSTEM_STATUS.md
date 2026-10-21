# Geard Lif compatibility status — snapshot review

This is a **snapshot summary** of upstream [Raven's Heart Core Design](https://github.com/heatwaveqc/geard-lif/blob/4ba2934cbb34cf8f43584016fadd2e339fad23fe/ai/design/RAVENS_HEART_CORE_DESIGN.md). That design document is private AI/development material **and is not copied into public Elf-Books**. The four public player-audience tiddlers are the executable reference sources. Do not portray provisional mechanics as locked simply because they appear in local files.

## Locked upstream concepts

- Projects universally describe meaningful action, **including combat**: Complexity, Recalcitrance, Scope, Time.
- Accuracy governs application versus static Avoidance/Complexity; Potence governs resulting Effect versus static Resilience/Recalcitrance. High Accuracy alone does **not** automatically amplify Effect.
- **Twelve independently rated attributes**, four per aspect: Body Strength/Dexterity/Agility/Health; Mind Intelligence/Perception/Wits/Will; Soul Charisma/Insight/Temperance/Conviction. Resilience is an independent fourth attribute per aspect.
- **One chosen Talent per character**, governing exactly five distinct skills; preset or custom. It contributes dice only on those skills and has a separate progression tree. No class restrictions on the other skills.
- Mind/Body/Soul each have a Resilience (Will/Health/Conviction) and slow/fast resource tracks: **Spirit/Mana (Mind/Will), Injury/Fatigue (Body/Health), Plasticity/Attention (Soul/Conviction)**.
- Four mark grades: Minor (0 penalty), Middling (-1), Major (-2), Final (-4), with promotion, cascading and recovery. Slow resources generally recover one step/day, fast resources one step/action.
- Resource Costs are self-targeted Effect rolls without Application, not fixed-point subtractions; no reduction of Cost rating by armor or external defenses.

## Unified Project and resource-mark resolution (confirmed)

- **Meet it to beat it:** Accuracy successes **>=** Complexity/Avoidance succeeds (equality hits). Then roll Potence independently.
- Potence **zero** successes gives no mark; any positive below effective threshold R gives **Minor**; exactly R **Middling**; 2R **Major**; 3R **Final**; higher full multiples give extra Final marks.
- Every person and Project carries four mark grades, with promotion/exhaustion. **Projects:** Recalcitrance controls severity threshold; **Scope** = slots at *each grade*, not a separate point total. Filling Final slots completes it. **People:** relevant Resilience controls mark slots at each grade and unmodified threshold; armor/wards may increase the *effective injury threshold* without increasing mark capacity.
- These grades are **not** cross-scale Tiers. The prior strict-greater Project gate and imaginary progress-tier-to-Scope conversion are retired.

## Provisional upstream formulas

- d10 pool: 7,8,9 = 1 success; 10 = 2, with other faces = 0.
- **Working trait ratings 0–25**, one d10 per five rating levels, five dice per source (up to 20 personal, provisional 40 with gear). **XP per contributed success:** Attribute 2, Talent 1, Skill 5, Specialty 10; 10×current rating cost (minimum 10). Each natural 10 may separately bootstrap an under-5 used Skill **and** an under-5 declared Specialty. The entire pace remains subject to balance testing.
- Tier belongs to each quantity, not the character's level; provisional conversion 10-fold between Tiers, flooring upward and multiplying downward.
- Combat uses the project framework, but equipment, hit locations, reactions, magic effects and opposed-action details are incomplete.

## Open upstream, therefore open here

- Which *specific* methods select each of the 12 attributes, how static Avoidance is derived, and **total starting budgets, selection of passive defense/Cost contributors and Talent-tree node rules**. Active source-die XP is now a working calibrated formula.
- Exact d10 critical success/failure and special cases, including zero Recalcitrance; ordinary Project **equality succeeds**, and static target comparison is known. Do not port natural 20 or natural 1 perk triggers unchanged.
- Exact armor/ward severity-threshold adjustment, how projects suffer setbacks or repair/undo marks, and any policy for zero Recalcitrance. The universal Scope-as-mark-capacity rule is already settled.
- Tier anchor calibration; high-Tier equipment Control Tier versus Effect Tier.
- Mana/Fatigue/Attention expense versus regeneration, injury dynamics and survivability.
- A new practice XP metric and perk breakthrough frequency/effect conversion for the d10 engine.
- Character sheets, NPCs/monsters, enchanting/alchemy and solo-campaign save semantics.

This document is descriptive, not a patch or silent rule change to upstream Geard Lif.

## Working trait Tier and passive XP rules

Every trait begins at Tier 0, and buying the next Tier requires rating 25 at the preceding Tier. Cost and earned XP scale by `10^Tier`. A same-Tier Skill needs at least one die from its governing Attribute and a Specialty needs at least one die from its Skill; their *ratings* may be higher than the parent rating. Talent is not a prerequisite. Maxed-trait **raw XP** is either banked for up-tier advancement or cascaded Talent→Attribute→Skill→Specialty without reapplying the receiving trait's XP multiplier. Static defense is **floor(half the combined relevant dice pool)**, and each actually used defensive/resisting trait earns **ceil(rating/10) XP at Tier 0** or exact **rating/10 ×10^Tier XP at Tier 1+**. See [the imported canonical player rule](source/Trait_Tiers_and_Experience_Cascade.tid).

**Cost threshold versus capacity:** the generic Cost magnitude still rolls unmodified; settings may define static resistance Attribute/Skill and equipment additions which change its *severity threshold*, never the target resource's Resilience-sized mark capacity. Elf-Books defines Will + applicable Talent + casting school + declared Spell Specialty for static Mana Cost resistance, while **Will** remains Mana capacity (Mind), and Conviction instead governs Plasticity/Attention (Soul) (see [Magic](../../design/MAGIC.md)).
