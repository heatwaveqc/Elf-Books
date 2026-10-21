# Elf-Books rules authority — Geard Lif migration

**Overall status: FOUNDATION / NOT PLAYABLE.** Do not use archived D20 mechanics. **Geard Lif / Raven's Heart is the base engine**, vendored at [engine/geard-lif](../engine/geard-lif/README.md) from upstream commit `37699bf629cae33743f609354cff14871d9a4e79`.

## Authority order

1. [Local source snapshot](../engine/geard-lif/README.md) for locked Geard rules; [status notes](../engine/geard-lif/SYSTEM_STATUS.md) distinguish provisional/open pieces.
2. [Elf-Books foundation](FOUNDATION.md) for Elder Scrolls adapter intent.
3. Specific Elf-Books mechanics **only when explicitly designated approved**.
4. [Return-to-parity checklist](../MIGRATION_BACKLOG.md) for open design and implementation tasks.
5. [Archive branch](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif) is historical comparison only, never active authority.

## Locked upstream, inherited by Elf-Books

- Consequential action as a **Project**: Complexity, Recalcitrance, Scope, Time; applies to combat and downtime.
- Two axes: Accuracy successes **>=** Complexity/Avoidance apply; independent Potence **zero** gives nothing, any positive result yields at least a Minor mark; exactly R yields Middling, 2R Major, 3R Final. Static target opposition; excess Accuracy does not boost Potence by default.
- **All Projects and personal resources use four mark grades**, with promotion and Final exhaustion. Personal Resilience determines **slots per grade**; Project Scope determines **slots per grade** independently of Project Recalcitrance (its severity threshold). Worn armor and equivalent protective effects change an injured person's **effective severity threshold**, not slots. Six resource tracks under Mind (Will), Body (Health), Soul (Conviction) retain their appropriate recovery.
- Costs are rolled self-targeted Effects; not deducted from a numerical Magicka pool.

## Provisional upstream, not approved for actual campaigns

- d10 successes (7–9=1, 10=2); trait pools from Attribute/Talent/Skill/Specialty; 5 cap per category, up to 20 personal dice and 40 including gear.
- Approximate 10× Tier difference, converted rolled magnitude, static opposition stays at its own Tier.
- Full combat/equipment formulas, critical-event frequency, setbacks and repair, zero-threshold case, and exact character traits remain incomplete. Ordinary Project equality **succeeds**.

## Elf-Books material preserved but awaiting conversion

- [24 candidate skill names](SKILLS.md) and [structured vocabulary](skills.json), with existing historical TES skill grouping used as metadata only.
- [Perk design](PERKS.md) and [75 TES game inspirations](../design/tes_perk_seeds.json), with no final Geard gate/effect.
- [Use-based advancement intent](ADVANCEMENT.md); old 5×skill, XP per HP, XP per Magicka etc. are **retired numeric formulas**.
- [Armor/combat adaptation](DEFENSE.md); old D20 AC is **not** active.
- [Spell/Mana design](../design/MAGIC.md); costs follow rolled resource Effects, not old MP totals.
- [Solo GM protocol](../game/GM_PROTOCOL.md), independent private campaign architecture, historical Elder Scrolls lore and GM pre-session design.

**Next development:** See [MIGRATION_BACKLOG.md](../MIGRATION_BACKLOG.md), especially remaining P0 armor/zero-threshold edge decisions, traits, survivability, combat, magic, use-based advancement, d10 perk breakthroughs and four-scene test. Implement, test, seek explicit design approval, then permit any actual game to start. CI validation confirms structure, **not playability**.
