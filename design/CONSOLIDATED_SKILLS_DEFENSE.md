# Consolidated skills and defensive resolution — v2 design

**Status: proposed, not authoritative or playable.** This is the preferred *discussion draft*. The older [52-skill roster](../rules/skills.json) remains in the repository solely for historical comparison; [24-skill structured candidate](skills_v2.json) has not yet replaced it as executable character-sheet data. No existing game is migrated.

## Why consolidate

The old catalog included nine language ratings, overlapping Long Blade / One-Handed / Axe / Blunt specialties, separate Running / Swimming / Climbing / Jumping, and overlapping Lockpicking / Security and Speechcraft / Mercantile / Etiquette / Streetwise skills. These multiply resource ECL, bookkeeping, and roll eligibility without much distinct gameplay.

**Proposed new roster: 24 skills, evenly distributed** to keep the original Warrior→Health, Mage→Magicka, Rogue→half of each resource formula meaningful. Categories are gameplay classifications, not claims about each TES title's formal skill grouping.

| Warrior (8) | Mage (8) | Rogue (8) |
| --- | --- | --- |
| One-Handed | Alteration | Light Armor |
| Two-Handed | Conjuration | Dodge |
| Archery | Destruction | Sneak |
| Block | Illusion | Security |
| Heavy Armor | Mysticism | Legerdemain |
| Unarmed | Restoration | Speechcraft |
| Athletics | Alchemy | Survival |
| Smithing | Enchanting | Lore |

### Historical coverage without fake extra ranks

- Long Blade / Short Blade / Axe / Blunt Weapon / Spear → One-Handed or Two-Handed **depending on actual grip**, *not* an independent skill bonus. Critical Strike becomes an eligible weapon perk, Backstabbing a Sneak-linked perk.
- Block remains distinct from armor; weapon parries and shields use it.
- Medium Armor → Light or Heavy Armor **based on the suit's fixed classification**; never both. Unarmored/Acrobatics/Dodging → Dodge, with an unarmored perk branch.
- Running, Swimming, Jumping and Climbing → Athletics. Armorer → Smithing. Medical → Survival (mundane treatment); magical recovery remains Restoration.
- Pickpocket → Legerdemain, locks/traps → Security, commerce/streetwise/etiquette/persuasion → Speechcraft.
- Thaumaturgy → Alteration or Mysticism according to the **effect**, not two simultaneous skills.
- Nine Daggerfall language skills → distinct **learned languages/specializations**, not nine independent skills adding to ECL. Lore covers languages as *fields of study*, not automatic fluency. A character who understands one language does not thereby understand all languages.

Future perks can preserve finer distinctions (Long Blade expertise, mace breaker, archery sniping, battlefield medic) without restoring overlapping base skills. The first 48 perk hooks are candidate ideas only, not purchased/awarded actions.

## Defensive AC: one applied skill, not three stacking bonuses

**Recommended draft:**

```text
attack_total = d20 + attacker_attribute + floor(offensive_skill / 5) + other_attack_mods
AC = 10 + universal_AC_modifiers + selected_defense_method_contribution

method contribution = method_gear_AC + floor(selected_defense_skill / 5)
```

The **universal** components include bonuses still present when that method is stripped out (size, miscellaneous magic, eligible attributes, *other* worn gear). Attribute AC bonuses must be applied **once**, and Dexterity caps from armor still matter. For Dodge, the allowed Dexterity bonus is considered part of the Dodge method contribution for defense-XP attribution rather than counted twice.

Before the enemy attack roll (or before an automatic default is applied), the defender selects exactly one of:

- **Armor**: Heavy Armor or Light Armor, depending on worn equipment, plus that suit's armor bonus. Passive and available even when a defender cannot react, unless an attack type bypasses armor.
- **Block**: Block skill plus shield contribution (or weapon-parry configuration). Requires an available shield/parry weapon and ability to react; no default skill bonus just from carrying a shield while surprised. The worn armor's *equipment bonus* remains in universal AC but its armor **skill bonus doesn't stack**.
- **Dodge**: Dodge skill plus eligible Dexterity contribution. Requires awareness and ability to move/react, as appropriate; can be used with armor but obeys its movement and Dexterity restrictions. Worn armor/shield *equipment bonuses* that normally apply remain universal; their **training bonuses don't stack**.

A defender may select a less-trained method on purpose. Otherwise the GM may use the best legal method **before rolling**, recorded consistently; do not choose retroactively after seeing the enemy roll. Any one method yields **at most +20 AC from training** at skill 100, not +60. At low skill, gear still helps. A skill of 0 does not make plate worthless or make a novice incapable of blocking.

Armor-based AC can be *bypassed* for touch-style attacks under a 3.x-inspired ruleset; Dodge may remain applicable, while Block requires an explicit ward/energy-block perk to protect against touch, spells or insubstantial attacks. These exceptions are still design questions. Do not take the chosen skill bonus against an attack if the method cannot affect that attack.

**Concrete example, no other bonuses:**
- Worn armor contributes +6, shield contributes +2, Dexterity contributes +2, Heavy Armor rating 50 → trained +10.
- Choosing Armor yields AC `10 + 2 Dex + 2 shield + (6 armor + 10 mastery) = 30`.
- Choosing Block rating 40 → +8 produces AC `10 + 2 Dex + 6 armor + (2 shield + 8 mastery) = 28`.
- Choosing Dodge rating 25 → +5 produces AC `10 + 6 armor + 2 shield + (2 Dex + 5 mastery) = 25`.
- **Never stack** +10 Armor, +8 Block and +5 Dodge into a single AC.

**Balance caveat:** AC 30 against an attacker at +5 is nearly automatic protection (natural 20 still hits). A peer specialist with +20 skill, +4 ability and magic equipment has a fair chance. We must test 3.x-scaled threats; simply attaching +20 AC skills to untouched 5e monsters will break balance.

## XP: credit the actual defense, not merely being attacked

Define `AC_without_method` (universal AC) and `AC_with_method` (universal plus selected method's equipment and training). On an ordinary attack roll:

- If `attack_total < AC_without_method`: a miss that didn't need the selected method. No defense XP for this attack.
- If `AC_without_method <= attack_total < AC_with_method`: the selected method prevented a credible hit. Award its training XP, scaled to credible threatened harm and capped against farming.
- If `attack_total >= AC_with_method`: hit; no AC-mediated defense XP. If later using damage reduction, measure credited reduction separately.
- Enemy **natural 1**: automatic miss, but no defensive XP or perk roll just because the foe fumbled.
- Enemy **natural 20**: automatic hit, regardless of effective AC; no AC-mediated defensive XP or perk roll.

This counts both **armor equipment** and **armor training** as contributing to protective successes, so beginners can advance. It doesn't give full progress merely for being targeted, surviving a helpless enemy or farming a non-threatening opponent. Armor, Block and Dodge are not all credited for the same attack. Other consequences, such as an attacker missing because of terrain, are not credited to an unselected defense skill.

## Critical perks when you are defending

The enemy's natural 1 is **not a defensive critical**: it has an automatic miss independent of defender training. Counting it would let a character farm perk rolls merely by standing among many harmless enemies.

**Recommended draft:** on a consequential attack that your **chosen defense method actually prevents**, and if you meet a perk threshold and have an available unearned perk, roll an **independent defense discovery d20**. A natural 20 gives the defender a qualified perk breakthrough opportunity for **that defense skill**, not a full skill level. This roll does not change the original hit/miss result.

Use the same logic for passive armor, Dodge and Block. A non-attack spell where **only the victim rolls a save** needs a similarly independent *caster* mastery roll on a meaningful effect, not an arbitrary conversion of the enemy's natural 1 into caster genius.

Why not use attacker-miss margin? A “miss by 10+ caused exclusively by +5 mastery” condition is mathematically impossible at low mastery, even when the defender makes a perfect read. This would gate early armor perks for accidental mathematical reasons.

**Perk rate caveat:** 5% of *qualifying* defensive saves is not 5% of all attacks directed at the PC, whereas offense can roll natural 20 on many attempted attacks. If defense gains perks too slowly, compare criticals per typical play session or grant milestone technique opportunities; don't fake randomness or quietly boost odds.

## Specializations and growth

- Rated skills remain 0–100 and the +1 per five ranks is a proposal.
- Weapon specialties, armor materials and languages may be learned as **tags/competencies/perks** rather than a second base rating. A specialized perk must not mechanically become an unbounded stacking second skill bonus.
- The older per-category ECL equation remains under consideration: `min(sum_skill/20, highest_skill/5)` and half-Rogue to Health and Magicka. Reducing 52 skills to 24 changes ECL growth speed; calibrate characters again before treating Health/Magicka as final.
- Continue **deterministic meaningful-use skill XP** and **perks through critical breakthroughs**; no separate successful-learning-check ladder.
- Do not award skill XP to two defensive disciplines on a single attack, or to two weapon skills on one strike.

## Testing before approval

1. Attack bonuses +5/+10/+20 vs defensive skill 0/25/50/100 and armor/shield/no armor.
2. Equal-level PCs with differing offense/defense investment and real opponents, including enemy minions that only hit on natural 20.
3. Flat-footed, grappled, restrained, surprise, ranged, touch/spell, and shieldless cases.
4. XP attribution: gear-only save at skill 0, trained defense save, inconsequential miss, nat 1, nat 20.
5. Defense perks per session vs weapon/spell use; no free perks from fumbles, trivial attackers or multiple simultaneous defenses.
6. 8/8/8 ECL vs old 19/9/24 ECL at equivalent starting budgets. Race, ability scores, and equipment should be controlled.

Relevant mechanical background: https://www.d20srd.org/srd/combat/combatStatistics.htm (3.5 SRD attack/AC, automatic 1 and 20). This document uses original explanations and does not redistribute the SRD.
