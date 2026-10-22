# Elf-Books rules authority — Geard Lif migration

**Overall status: FOUNDATION / NOT PLAYABLE.** Do not use archived D20 mechanics. **Geard Lif / Raven's Heart is the base engine**, vendored at [engine/geard-lif](../engine/geard-lif/README.md) from upstream commit `4ba2934cbb34cf8f43584016fadd2e339fad23fe`.

## Authority order

1. [Local source snapshot](../engine/geard-lif/README.md) for locked Geard rules; [status notes](../engine/geard-lif/SYSTEM_STATUS.md) distinguish provisional/open pieces.
2. [Elf-Books foundation](FOUNDATION.md) for Elder Scrolls adapter intent.
3. Specific Elf-Books mechanics **only when explicitly designated approved**.
4. [Return-to-parity checklist](../MIGRATION_BACKLOG.md) for open design and implementation tasks.
5. [Archive branch](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif) is historical comparison only, never active authority.

## Locked upstream, inherited by Elf-Books

- Consequential action as a **Project**: Complexity, Recalcitrance, Scope, Time; applies to combat and downtime.
- Two axes: Accuracy successes **>=** Complexity/Avoidance apply; independent Potence **zero** gives nothing, any positive result yields at least a Minor mark; exactly R yields Middling, 2R Major, 3R Final. Static target opposition; excess Accuracy does not boost Potence by default.
- **All Projects and personal resources use four mark grades**, with promotion and Final exhaustion. Personal Resilience determines **slots per grade**; Project Scope determines **slots per grade** independently of Project Recalcitrance (its severity threshold). Worn armor and equivalent protective effects change an injured person's **effective severity threshold**, not slots. **Mind/Will: Spirit (slow), Mana (fast)**; **Body/Health: Injury (slow), Fatigue (fast)**; **Soul/Conviction: Plasticity (slow), Attention (fast)**. Track recovery speeds are unchanged.
- Costs are rolled self-targeted Effects; not deducted from a numerical Magicka pool.

## Provisional upstream, not approved for actual campaigns

- d10 successes (7–9=1, 10=2); **working trait ratings 0–25** with one d10 per five rating points (max 20 personal dice/40 including gear). **Source-die XP**: Attribute 2, Talent 1, Skill 5, Specialty 10 per success; a 10 can additionally bootstrap each used under-5 Skill and under-5 declared Specialty.
- **[Trait Tiers and XP cascade](ADVANCEMENT.md):** Tier N ratings require Tier N−1 at 25 to purchase. Skill dice need ≥1 governing Attribute die at the same Tier; Specialty needs ≥1 same-Tier Skill die. There is **no upper rating cap** imposed by the parent; Talent is exempt. Earned XP and point costs scale 5× per Tier. At max rating, choose up-tier bank or *raw* XP cascade Talent→Attribute→Skill→Specialty.
- Adopted 5× Tier difference converts rolled outcome magnitude versus differently scaled opposition, without a second XP multiplication.
- Full combat/equipment formulas, critical-event frequency, setbacks and repair, zero-threshold case, precise trait-to-action choices, static Avoidance, Talent tree, and creation budgets remain incomplete. Ordinary Project equality **succeeds**.

## Elf-Books material preserved but awaiting conversion

- **[Twelve attributes and five-skill Talent packages](TALENTS.md)** are adopted, with [structured attributes](attributes.json), [12 sample Talents and custom option](talents.json), and a separate as-yet-undefined Talent progression tree. **All twelve starting Attributes** and **all five Talent-governed starting Skills** have minimum rating **5**.
- [24 skill names](SKILLS.md) and [structured vocabulary](skills.json); all skills may advance regardless of Talent.
- [Perk design](PERKS.md) and [75 TES game inspirations](../design/tes_perk_seeds.json), with no final Geard gate/effect.
- **[Active use-based XP and natural-ten bootstrap](ADVANCEMENT.md)** are now working rules with tests; passive defensive/Resilience XP **rounds rating/10 UP per trait at Tier 0**; above Tier 0 use exact rating/10 ×5^Tier. Static defense is now floor(sum of eligible dice/2). The common magic self-Cost package is **Will + applicable Talent + casting School Skill + declared Spell Specialty**, plus eligible Cost-reduction gear. **Will also determines Mind's Mana/Spirit mark capacity**, which other trait dice and gear do not increase. Old HP/MP/D20 XP formulas remain archived.
- [Armor/combat adaptation](DEFENSE.md); old D20 AC is **not** active.
- [Spell/Mana design](../design/MAGIC.md); costs follow rolled resource Effects, not old MP totals.
- [Solo GM protocol](../game/GM_PROTOCOL.md), independent private campaign architecture, historical Elder Scrolls lore and GM pre-session design.

**Next development:** See [MIGRATION_BACKLOG.md](../MIGRATION_BACKLOG.md), especially remaining P0 armor/zero-threshold edge decisions, traits, survivability, combat, magic, use-based advancement, d10 perk breakthroughs and four-scene test. Implement, test, seek explicit design approval, then permit any actual game to start. CI validation confirms structure, **not playability**.

**Adopted spell construction:** Each designed spell is a School Specialty; rating **1+** is needed to cast. Meaningful one-hour **Intelligence + School** study, default **Complexity 5**, awards source/bootstrapped spell XP without a Scope Project. Known spells may be studied further. A cast's **one Potence roll per distinct effect** supplies that effect's strength and independently resisted Mana Cost even when Accuracy misses. Designed range, area, target-count, duration, speed and multi-effect parameters add **fixed Cost-success surcharges**; **no mass/weight surcharge** (heavy movement uses magical work against Projects). Longer damaging durations **pulse damage each turn**, with area fixed in place; physical burning has a feasible removal action, while supernatural single-target curses require active resistance before every damaging instance: **first success ends the curse permanently**, preventing that tick's damage; failure inflicts damage and it continues until success, expiry, dispelling or death. **A perk is required to design multi-effect formulas**; components each get independent Potence, defender resistance, and Mana Cost incidents/XP, permitting in-cast Mana→Spirit overflow. Casters may voluntarily reduce Potence dice, not fixed costs. The [working pricing schedule](../design/SPELL_PARAMETERS.md) is preliminary, and non-damage conversions remain open. See [magic](../design/MAGIC.md).

**Restoration and flesh protection:** A spell has an **Application roll only when needed**; willing accessible targets of Healing/Oakflesh bypass Perception + School Accuracy, **not** Potence/Cost. Unwilling recipients use normal Malediction-like Application against an eligible named defense. Healing uses **Intelligence + Restoration** Potence as a restorative inverse Injury Effect, grading its strength against the **patient's base Health Resilience (healing Recalcitrance)**; Health is not a default Avoidance roll, and tougher patients require greater Potence for the same healing grade. **The precise inverse of mixed Injury marks/de-promotion remains OPEN.** Oakflesh adds its **actual Potence directly to effective Injury Resistance threshold** as equipment-equivalent protection while active, without changing Health rating, wound-slot capacity, or Dodge; exact armor/buff stacking remains OPEN. Summoning remains deferred. [Full rules](../design/MAGIC.md).

**Magic prototype:** [Perception/Intelligence active Destruction casting; Will + governed Talent + Destruction Skill + declared spell Specialty static Mana-Cost resistance](../design/MAGIC.md). Spell Mana Cost is **Potence successes + recorded surcharge** (no independent roll); **Will sets Mind/Mana mark capacity**, and cost-reducing robes add only to static Cost resistance dice (not mark slots). Mysticism is the default reactive counterspell Skill via Wits; full reaction mechanics remain open.

**Named-roll and defense contract:** [Upstream](../engine/geard-lif/source/Named_Action_Pools_and_Defense_Modes.tid), [Elf-Books attack-mode catalog](ATTACK_MODES.md). Rules specify **Attribute + Skill**; Talent applies if it governs that **Skill**, plus one relevant Specialty and legal external gear/magic. A hostile mode lists explicit valid defensive pools; a direct cold Malediction and exposure use Health + Survival, whereas missiles allow Dodge/Block but not default Parry. Social modes define method-specific defenses. **Combined** external equipment/enchantment/ensorcellment/temporary buffs are capped at the unmodified personal dice for that pool at chosen Tier.

**Soul combat restriction:** ordinary social attacks can directly affect **Attention only**; only **supernatural attacks** directly affect **Plasticity**. **Conviction** supplies Soul mark capacity and severity soak, not an ordinary static Avoidance pool. The [attack modes](ATTACK_MODES.md) use **Strength + Speechcraft** for physically imposing Intimidation application, with Insight/Temperance-based responses.

**Fast → slow exhaustion overflow:** a new Effect or Cost that targets an **already-exhausted fast resource** instead affects its paired slow resource. **Fatigue→Injury; Mana→Spirit; Attention→Plasticity.** The effect that first exhausts fast stays there; only subsequent incidents redirect. Mundane social attacks still directly target Attention but can reach Plasticity **via overflow**. Regrade the unchanged effect against its actual slow-target threshold; do not double-apply it. See [resource rules](../engine/geard-lif/source/Resource_Tracks.tid).
