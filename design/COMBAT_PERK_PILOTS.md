# First three converted combat perk effects

**Status: EFFECT RULES ADOPTED; perk purchase gates still OPEN.** These are the first mechanical conversions from the [75 Elder Scrolls perk inspirations](tes_perk_seeds.json), using the current Geard Lif [weapon/exertion contract](https://github.com/heatwaveqc/geard-lif/blob/main/tiddlers/Content/Rules/Combat_Equipment.tid) and [three-action round](https://github.com/heatwaveqc/geard-lif/blob/main/tiddlers/Content/Rules/Combat_Round_and_Actions.tid). The historical Elf Books Geard snapshot does **not** automatically incorporate all of these newer upstream combat edits; these are reviewed forward-looking adaptations. Their pure effect-plan helpers are in [combat_perks.py](../scripts/combat_perks.py).

## Power Bash (Block / shield and melee weapon bash)

**Declare the number of extra Damage dice, `k`, before the attempt.** Apply those extra dice to the chosen **muscle-powered weapon/shield bash's normal Potence Damage pool**. The chosen number cannot exceed the user's **Strength dice at the relevant Tier** (`floor(Strength rating/5)` under Elf Books' 0–25 ratings), not the raw 0–25 rating itself. The ordinary personal roll, weapon Damage bonus and all applicable modifiers remain in force. The perk may add up to that many dice, including choosing zero; it does not grant additional attack actions or alter Accuracy.

**Fatigue tradeoff:** The attack's **additional Fatigue Cost hazard dice = `2×k`**. One `k` reflects the increased Damage rating/hazard and the second `k` is its exertion premium. Add these on top of the weapon mode's **usual declared exertion hazard**; roll the resulting Fatigue Cost as one Cost incident for the attempted attack, **even if Accuracy misses**. Use the usual self-Cost resistance and fast→slow overflow rules; a missed attack does **not** refund the extra Fatigue hazard.

Example: Strength 20 supplies **4 Strength dice**. A weapon bash with normal Damage +2 and ordinary Fatigue hazard 2d, boosted by **+4 Damage dice**, has effective Damage bonus +6 and incurs **2 + 2×4 = 10d Fatigue hazard**, an **increase of 8d**. The extra Potence dice come from a **perk technique** and are recorded as `perk_skill`. **They count as Skill dice for Skill XP and for character double-10/defender double-1 perk-point confirmations**, but are not equipment dice and cannot generate prospective item deed enchantments. Weapon equipment ratings themselves are unchanged; the added bonus belongs to this attack only.

**Open detail:** Final named Attribute, permitted Specialty scope and minimum 0–100 perk threshold. Do not assign these silently; a perk effect being operational does not mean every character may purchase it yet. The muscle-powered/exertion-bearing restriction is deliberate; this is **not** an upgrade to the standalone powered-gun Damage pool.

## Deflect Arrows (Block / advanced Parry)

A character owning **Deflect Arrows** may choose an ordinary **weapon Parry** as their single active response against an incoming **arrow**, provided they are aware of the attack and holding an actual parry-capable weapon. This is an explicit exception to the default **arrow projectile permits Dodge or Block, but not Parry** rule.

The defensive pool remains the ordinary **Dexterity + wielded weapon Skill** (e.g. One-Handed or Two-Handed), with the applicable governed Talent, declared Specialty and weapon's Defense bonus. Derive the same static Avoidance as any other Parry. **Pay one available reaction action and the weapon's normal Parry Fatigue Cost**: `max(0, parrying weapon Damage, parrying weapon Defense)`. The defense's incoming-attack timing, action limit and Cost mitigation remain unchanged; this is a new *legal defensive choice*, not a free or universally automatic defense.

**Only arrows are authorized in this first pass.** Thrown weapons, crossbow bolts, bullets, traveling ice spears and direct nonmissile Maledictions are **not automatically** covered. Further specializations/perks may explicitly broaden the interceptable projectile list later.

**Open detail:** Final purchase Attribute, approved Specialties and 0–100 combined prerequisite threshold. This perk is sourced from the Block skill's TES inspiration, but its actual reaction uses the genuine weapon Parry pool, not an arbitrary replacement Block roll.

## Dual Flurry (One-Handed / dual-wield attack)

When wielding **two separate ready usable melee weapons**, one **attack action** can deliver **two full-strength, independently resolved strikes**: one with each weapon's legal attack mode. Each strike requires its **own Accuracy roll**, then its **own Potence roll when applied**, and its **own normal weapon-mode Fatigue Cost** for the attempt, even when that strike misses. Resolve the strikes sequentially: any Fatigue or Injury marks/penalties caused by the first Cost affect the next strike under the usual rules. If the first Cost exhausts Fatigue, the next strike's Cost redirects into Injury in the ordinary fast→slow manner.

Two strikes still use **only one attack action**; the perk does not add a fourth action to the round, waive or duplicate defensive reactions, grant free movement, or remove normal range/weapon requirements. **Three attack actions may therefore produce up to six actual strikes**, with up to six independent Fatigue Cost incidents and distinct eligible source-tagged attack rolls for experience and perk confirmations. These are genuine rolls, not copies of a previous attack's die faces.

**Open detail:** Final prerequisite Attribute, acceptable weapon Specialties, minimum 0–100 combined rating, and interactions with later dual-wielding techniques. Ordinary dual-wield baseline restrictions beyond having two ready usable melee weapons remain governed by the broader combat/equipment rules.

## Other sample perk status

- **Quiet Casting** — next straightforward spellcasting/stealth technique conversion; it must work with actual magical detection, sound and awareness once those are finalized.
- **Extra Effect** — already required to *design* compound spell formulae; purchased rank/gate and wording still need definition. Owning a finished multi-effect spell does not require the perk just to cast it.
- **Green Thumb** — gatherer/project-yield improvement that should integrate with ordinary resource/crafting Projects after yield calibration.
- **Arcane Blacksmith** — **DEFER until the enchanting system is designed.** No enchanted equipment modification rules should be invented just to complete this perk.
- **Deed enchantments from confirmed equipment 10s** — deliberately separate future idea, not part of these combat perk effects.

None of the three combat perks has a complete **purchase gate record** yet. They are adjudicable as *effects when granted by explicit GM/test setup*; the ordinary player perk-purchase interface must reject/unavailable them until Attribute/Specialties/minimum rating are filled in. Ordinary starting Talents have no perk trees. See [Perks](../rules/PERKS.md).
