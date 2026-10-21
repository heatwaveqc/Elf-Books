# Elf-Books rules authority — Geard Lif migration

**Overall status: FOUNDATION / NOT PLAYABLE.** Do not use archived D20 mechanics. **Geard Lif / Raven's Heart is the base engine**, vendored at [engine/geard-lif](../engine/geard-lif/README.md) from upstream commit `6332383e3dbf68d0f0c7184ab704758125055f83`.

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

- d10 successes (7–9=1, 10=2); **working trait ratings 0–25** with one d10 per five rating points (max 20 personal dice/40 including gear). **Source-die XP**: Attribute 2, Talent 1, Skill 5, Specialty 10 per success; a 10 can additionally bootstrap each used under-5 Skill and under-5 declared Specialty.
- **[Trait Tiers and XP cascade](ADVANCEMENT.md):** Tier N ratings require Tier N−1 at 25 to purchase. Skill dice need ≥1 governing Attribute die at the same Tier; Specialty needs ≥1 same-Tier Skill die. There is **no upper rating cap** imposed by the parent; Talent is exempt. Earned XP and point costs scale 10× per Tier. At max rating, choose up-tier bank or *raw* XP cascade Talent→Attribute→Skill→Specialty.
- Approximate 10× Tier difference converts rolled outcome magnitude versus differently scaled opposition, without a second XP multiplication.
- Full combat/equipment formulas, critical-event frequency, setbacks and repair, zero-threshold case, precise trait-to-action choices, static Avoidance, Talent tree, and creation budgets remain incomplete. Ordinary Project equality **succeeds**.

## Elf-Books material preserved but awaiting conversion

- **[Twelve attributes and five-skill Talent packages](TALENTS.md)** are adopted, with [structured attributes](attributes.json), [12 sample Talents and custom option](talents.json), and a separate as-yet-undefined Talent progression tree. **All twelve starting Attributes** and **all five Talent-governed starting Skills** have minimum rating **5**.
- [24 skill names](SKILLS.md) and [structured vocabulary](skills.json); all skills may advance regardless of Talent.
- [Perk design](PERKS.md) and [75 TES game inspirations](../design/tes_perk_seeds.json), with no final Geard gate/effect.
- **[Active use-based XP and natural-ten bootstrap](ADVANCEMENT.md)** are now working rules with tests; passive defensive/Resilience XP now has the **rating/10** per-contributing-trait working rate, scaled by action Tier (remaining work is legal defensive/Cost packages and equipment). Old HP/MP/D20 XP formulas remain archived.
- [Armor/combat adaptation](DEFENSE.md); old D20 AC is **not** active.
- [Spell/Mana design](../design/MAGIC.md); costs follow rolled resource Effects, not old MP totals.
- [Solo GM protocol](../game/GM_PROTOCOL.md), independent private campaign architecture, historical Elder Scrolls lore and GM pre-session design.

**Next development:** See [MIGRATION_BACKLOG.md](../MIGRATION_BACKLOG.md), especially remaining P0 armor/zero-threshold edge decisions, traits, survivability, combat, magic, use-based advancement, d10 perk breakthroughs and four-scene test. Implement, test, seek explicit design approval, then permit any actual game to start. CI validation confirms structure, **not playability**.
