# Weapon skill contributes to damage; 2.5× effective XP cost — design candidate

**Status: core formulas approved by player (not a complete playable game).** The user explicitly approved the five-times-current-skill XP requirement and two XP per point of actual offensive damage, and previously endorsed adding floor(skill/5) to flat weapon damage. The pacing examples, separate source attribution, exact reactions/perks and off-hand/extra-attack interaction remain calibration topics. Read [GENERALIZED_EXTENDED_XP.md](GENERALIZED_EXTENDED_XP.md) for the newest generalized quick/extended noncombat advancement model; [CRAFTING_DC_XP.md](CRAFTING_DC_XP.md) is a prior comparison.

**Previous status: preferred numerical experiment.** This follows [actual-damage K=5 experiment](ACTUAL_DAMAGE_XP.md), but adds offensive mastery to damage and replaces the high effective XP cost with an algebraically equivalent integer scheme. The skill and AC architecture is described in [DEFENSE.md](../rules/DEFENSE.md).

## Proposed core

Let `S` be the applicable rated weapon skill, from 0 to 100. For an ordinary weapon hit:

```text
Skill Bonus              = floor(S / 5)
Attack                   = d20 + attribute modifier + Skill Bonus + other attack bonuses
Rolled Weapon Damage     = weapon dice + attribute damage modifier + Skill Bonus + other damage bonuses
Effective Damage         = target's HP actually removed by the attack after defenses/mitigation
Weapon Skill XP Gained   = 2 × Effective Damage
XP to gain next skill    = 5 × max(1, S)
```

**Why 2 XP/HP and 5× cost?** The user's suggested rank cost `2.5 × current skill` and 1 XP/HP introduces half-XP thresholds at odd ranks. Doubling both terms yields **identical advancement** using integers, exactly, with no rounding. Treat these as one paired choice; applying 5× cost but awarding 1 XP/HP would be the slower previous experiment.

If desired, compare the equivalent expression as `XP_next = 2.5 × max(1,S)` in conceptual units, but store **5× rank and 2× experience from each base learning unit** in the game.

Both attack and damage use the same `floor(S/5)` modifier; bonus applies once per **legal weapon attack** (including any legal extra attack). It is a **flat modifier**, not another damage die. On a D&D 5e critical hit, roll qualifying damage dice twice but add flat modifiers once. The natural 20 may additionally qualify for an applicable perk breakthrough, using that separate rule.

**Actual damage:** assign the attack only the enemy HP removed after resistance/reduction, capped by HP available when the hit lands; no XP for uninjured invulnerable targets or overkill. A 20-HP target yields at most 40 weapon XP in this 2× unit system if there is no healing during the encounter, regardless of the weapon's attack cadence. Fast weapons and multiattack can earn XP more quickly *per turn*, but not more from the **same finite HP pool**. Credited sources for enchantment riders, poison, summons and spell side effects still need an attribution rule.

## Example pacing, before misses, critical hits and overkill

| Skill transition | XP to next ranks, 5× scheme | Illustrative average applied damage per landed hit | Successful hits for +5 ranks |
| --- | ---: | ---: | ---: |
| 20→25 | 550 | 1d8 (4.5) +3 STR +4 skill = 11.5 | 23.9 |
| 50→55 | 1,300 | 1d8 (4.5) +5 STR +10 skill = 19.5 | 33.3 |
| 95→100 | 2,425 | 1d8 (4.5) +7 STR +19 skill +3 enchant = 33.5 | 36.2 |

The skill bonus does not change *within* each five-rank example interval, so these arithmetic ratios are valid before resource/circumstance effects. The novice 20→25 interval previously required ~47.8 successful hits at **K=5 with damage excluding skill bonus and 1 XP/HP** (1d8+3 = 7.5). Adding skill damage alone gives ~47.8 hits at 11.5 dmg and 1 XP/HP; doubling awards to 2 XP/HP gives ~23.9 hits.

### Critical hits

For a single d8, each natural-20 attack (under standard 5e weapon critical rules) adds another expected 4.5 damage **before HP caps and mitigation**. Natural 20s occur on 5% of **attack attempts**, not necessarily 5% of successful hits. At illustrative 60% total hit probability (including crits), expected weapon XP per attempt is `(0.60 × 11.5 + 0.05 × 4.5) × 2 = 14.25`, implying **~38.6 attempts** to earn 550 XP. That's ~23.2 successful hits on average. This isn't exactly 24 attempts because misses do not yield weapon damage XP.

These expected ratios are approximations: once a target is near 0 HP, overkill reduces awarded HP damage, and probabilistic XP-to-rank crossing needs a simulation to get an exact expected stopping time.

## Combat balancing implications

1. A 1d8+3 character at skill 20 now deals **7–15 actual rolled damage on an ordinary hit**, average 11.5. Starting HP from the category-ECL formula might be low enough for one-hit incapacitations. Verify survivability separately; the user intentionally accepts dangerous unarmored combat but has not automatically approved every starting HP value.
2. High skill adds up to **+20 flat damage per attack** and +20 to hit; this boosts offense significantly in fights with multiple attacks per turn. An off-hand or extra attack receiving the skill bonus again may be especially strong. Test dual-wielding and multiple attacks, particularly whether the skill bonus applies to off-hand damage.
3. Small, fast weapons aren't punished by only training on base damage: all correctly attributed HP loss teaches the skill. However a flat bonus **per hit** makes high attack-count styles more damaging per turn; decide if that's intended.
4. Weapon XP from finite HP lost is mostly independent of overkill because it is capped by enemy remaining HP. Training on risky, legitimate enemies is allowed. Other sources (DoT/healing, damage to objects, protection magic) need appropriate attribution rules.
5. If the **universal** rank cost is adjusted, apply the same normalized unit conversion to armor, Block/Dodge, magic and noncombat activities. At K=5, 2 XP per actual HP **taken** while armored is the natural counterpart to 2 XP per HP **dealt**, preserving the previously agreed risk-based armor learning. Exact equal pacing is not guaranteed: attacks and wounds occur at different rates.
6. Do not assume the prior magic-cost divisor 4 or social 5/15/30/60 tiers are already calibrated. Their effective award scale under a universal 2.5× cost needs to be reviewed.

## Pending decisions

- Confirm skill bonus to damage, applied once per qualifying successful attack, including critical-hit handling.
- Confirm effective rate (K=5 / 2 XP per actual HP) versus other multipliers; test novice survivability and higher-level damage first.
- Formalize whether off-hand/multiattack strikes each receive full skill damage and how they interact with perks.
- Determine which skill earns XP from weapon enchantments, poison, magical riders, summons and damage over time.
- Review HP, Magicka, armor, Block/Dodge, crafting and noncombat XP using the new common scale.

D20 critical rule reference: https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game . All above mathematics original.
