# Elf-Books rules authority — Geard Lif migration

**Overall status: FOUNDATION / NOT PLAYABLE.** Do not use archived D20 mechanics. **Geard Lif / Raven's Heart is the base engine**, vendored at [engine/geard-lif](../engine/geard-lif/README.md) from upstream commit `237448aa78d0305070b503ab85af612a0b381a93`.

## Authority order

1. [Local source snapshot](../engine/geard-lif/README.md) for locked Geard rules; [status notes](../engine/geard-lif/SYSTEM_STATUS.md) distinguish provisional/open pieces.
2. [Elf-Books foundation](FOUNDATION.md) for Elder Scrolls adapter intent.
3. Specific Elf-Books mechanics **only when explicitly designated approved**.
4. [Return-to-parity checklist](../MIGRATION_BACKLOG.md) for open design and implementation tasks.
5. [Archive branch](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif) is historical comparison only, never active authority.

## Locked upstream, inherited by Elf-Books

- Consequential action as a **Project**: Complexity, Recalcitrance, Scope, Time; applies to combat and downtime.
- Two axes: Accuracy versus Complexity/Avoidance, Potence versus Recalcitrance/Resilience; static target opposition; excess Accuracy does not boost effect by default.
- Six graded resource tracks under Mind (Will), Body (Health) and Soul (Conviction); tracked severity marks and per-action/per-day recovery.
- Costs are rolled self-targeted Effects; not deducted from a numerical Magicka pool.

## Provisional upstream, not approved for actual campaigns

- d10 successes (7–9=1, 10=2); trait pools from Attribute/Talent/Skill/Specialty; 5 cap per category, up to 20 personal dice and 40 including gear.
- Approximate 10× Tier difference, converted rolled magnitude, static opposition stays at its own Tier.
- Combat mappings, critical event frequency, ties, effects versus Recalcitrance, and exact character traits remain incomplete.

## Elf-Books material preserved but awaiting conversion

- [24 candidate skill names](SKILLS.md) and [structured vocabulary](skills.json), with existing historical TES skill grouping used as metadata only.
- [Perk design](PERKS.md) and [75 TES game inspirations](../design/tes_perk_seeds.json), with no final Geard gate/effect.
- [Use-based advancement intent](ADVANCEMENT.md); old 5×skill, XP per HP, XP per Magicka etc. are **retired numeric formulas**.
- [Armor/combat adaptation](DEFENSE.md); old D20 AC is **not** active.
- [Spell/Mana design](../design/MAGIC.md); costs follow rolled resource Effects, not old MP totals.
- [Solo GM protocol](../game/GM_PROTOCOL.md), independent private campaign architecture, historical Elder Scrolls lore and GM pre-session design.

**Next development:** See [MIGRATION_BACKLOG.md](../MIGRATION_BACKLOG.md), especially P0 resolution, traits, survivability, combat, magic, use-based advancement, d10 perk breakthroughs and four-scene test. Implement, test, seek explicit design approval, then permit any actual game to start. CI validation confirms structure, **not playability**.
