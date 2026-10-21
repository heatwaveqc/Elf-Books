# Perks — content principles and Geard Lif breakthrough migration

**Status: preserved player preferences, OPEN Geard mechanic.** Original Elder Scrolls perk names and thematic effects are retained in [the 75-entry catalog](../design/tes_perk_seeds.json); none are currently mechanically purchasable.

## Intended perk economy

- Preserve the preference for **bankable, character-wide perk points**, spendable at the player's discretion on eligible unowned perks.
- Ordinary skill trainers improve skill/competence, **not** perks or perk points.
- Rare artifacts, supernatural revelations and exceptional story rewards **may** grant a point or a particular perk when explicitly defined.
- Preserve actual skill/trait prerequisites for powerful techniques, but **retire** old 0–100 rank gates.

## Personal Talent progression trees

Each character now also has exactly one **five-skill Talent**, offering extra applicable dice and its own progression tree. This **does not remove any ordinary skill's perk options**, including those outside the Talent. The Talent tree is separate, and it is **not yet decided** whether advancing that tree consumes general bankable perk points, distinct Talent advancement, or earned breakthroughs. See [Talents](TALENTS.md) for examples and open design.

## Critical triggers are unresolved

Old D20 rules awarded a point from a meaningful successful natural 20, or a defender point when an attacking opponent rolled natural 1. Geard's **provisional d10 pools** have very different distributions: 10s appear on multiple dice regularly, and static defense typically does not roll a die. **Do not apply old triggers verbatim**.

Define a calibrated d10 critical/botch predicate, an opportunity for passive armor/defenders, meaningful-work eligibility and duplicate-event prevention. Separate critical perk points from earned practice proficiency. Test with realistic 5-, 10-, 20- and 40-die pools.

## Porting familiar Elder Scrolls perks

Original names and effects like Quiet Casting, Arcane Blacksmith, Extra Effect, Green Thumb, Wax Key, and Poisoned are natural candidates. Convert them to Geard Project/Mana/Fatigue/Effect rules *without using their old D20 action economy or numeric gates*. Skills removed from Skyrim may be mapped from Oblivion or developed separately.

Geard Lif **does have a Fatigue resource**, so prior "no Stamina" rejections are now **reopened for conversion review**. Percent-damage effects may belong in Potence, Resilience, or a tiered effect bridge; their old D20-reject labels are not authoritative.

The [legacy D20 perks](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif) are archived. Full Geard cost, timing, effect and eligibility definitions are P1 work in [the migration backlog](../MIGRATION_BACKLOG.md).
