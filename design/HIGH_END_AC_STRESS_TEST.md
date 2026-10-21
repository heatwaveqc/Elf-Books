# High-end AC stress test — base 10, gear stacking, and unarmored parity

**Status: HISTORICAL STRESS TEST ONLY.** The user subsequently accepted [DEFENSE.md](../rules/DEFENSE.md): fifth-edition equipment contributions, full +1-per-5 defensive skill, and **no base 10**, including lethal unarmored parity. The former 3.5 +5 stacked item case here is not current equipment policy. This remains a useful record of earlier alternatives.

**Original test status: numerical investigation and alternatives.** This revisits [CONSOLIDATED_SKILLS_DEFENSE.md](CONSOLIDATED_SKILLS_DEFENSE.md), where `AC = 10 + attribute + armor + shield + selected defensive skill` was originally proposed. Do **not** silently interpret this document as an adopted rule.

## Player's proposed revision

```text
AC = Attribute Mod + Armor Mod + Shield Mod + Selected Defensive Contribution
```

No automatic +10 base. Heavy Armor uses CON; Light Armor and Dodge use DEX; Block uses STR; only one skill contributes training (+1 per 5 points, maximum +20). Armor/Block/Dodge equipment and any legal natural armor bonuses remain. Block and Dodge consume a reaction until a low-level perk removes that requirement. **Armor learns from actual HP damage suffered, regardless of selected defensive method; this carries real danger and is not inherently an exploit.** There is no arbitrary XP cap on actual injury in this proposal. A separate qualified avoidance event can teach the selected skill, and perk-critical treatment remains undecided.

### High-end attack scenario

Assume all relevant abilities 25 → +7. A skill-100 attacker with a +5 enchanted weapon has `attack_bonus = +20 +7 +5 = +32`.

Defender has Heavy Armor 100 (+20), CON 25 (+7), +5 full plate (mundane armor 8 + enhancement 5 =13), +5 heavy shield (mundane shield 2 + enhancement 5 =7), and *illustrative* natural armor +5.

```text
With base 10: AC = 10 + 7 + 20 + 13 + 7 + 5 = 62
Without 10: AC =      7 + 20 + 13 + 7 + 5 = 52
Attack roll = d20 +32; max ordinary total 52.
```

Under 3.x natural 1/20 automatic miss/hit, the attacker **only hits on a natural 20 (5%) in BOTH cases**. Removing 10 by itself does not fix this fully stacked situation. Without natural armor, no-base-10 AC =47, requiring a 15–20 (30%); adding +10 baseline changes that to nat20-only.

### The reverse extreme: no armor

For equally skilled **unarmored** opponents with no magical weapon/armor, relevant modifiers +7 and skill bonuses +20 on either side: attacker `d20 +27` vs defender skill + attribute = `AC 27` without 10. The attack hits on *every die face except natural 1*: **95%**. Restoring base 10 yields AC37 and a **55%** hit chance (needed roll 10–20).

The phenomenon occurs at *any* equal attack/defense modifier without gear, because removing 10 eliminates the passive d20 midpoint. Dropping 10 helps stacked armor but causes unarmored/parity combat to be near automatic hits. This is a structural effect, not a matter of high-level balance only.

## Numerical comparison

| Equal-capability attacker | Defender, no-base-10 AC | Ordinary hit threshold (needed natural roll) | Hit probability without +10 | With +10 |
| --- | ---: | ---: | ---: | ---: |
| Full plate +5, heavy shield +5, natural +5; defense skill 100 | 52 | 20 | **5%** | **5%** |
| Same, without natural armor | 47 | 15 | 30% | 5% |
| Full gear + natural, but defensive training max +10 rather than +20 | 42 | 10 | **55%** | 5% |
| Full gear + natural, plate's mundane +8 moves to damage reduction, defense +20 | 44 | 12 | **45%** | 5% |
| Full gear + natural, combined equipment AC bonuses capped at 15 | 42 | 10 | **55%** | 5% |
| Identical unarmored skill/attribute, no enchants | 27 | 0 | **95%** | 55% |

These are **stress-test variants only**: moving mundane plate armor to DR, halving defense mastery, or capping gear are each different rules changes. Do not combine them or set one as the new default without review.

## Design decision

- **Keep full +20 armor skill and full stacking gear, remove 10:** top-tier specialist tanks can be hit only on natural 20 by equally skilled attackers. This might be an intentional specialization advantage, but requires separate counterplay (touch attacks, armor penetration, spell effects, grapples, maneuvering).
- **Lower defensive training to +10 at skill 100:** top-end armored peer is hittable again, but unarmored characters become extremely vulnerable unless they receive a different baseline defensive mechanism.
- **Give armor substantial damage reduction instead of its entire mundane armor AC bonus:** retains +20 trained defense and gives the actual-hits-for-armor-XP model a natural function; gear enchantment and natural armor still need explicit stacking rules.
- **Cap/suppress some equipment AC stacking:** possible but adds a less intuitive threshold and potentially reduces the value of highly magical gear.
- **Use a base 10 only for certain defense modes:** can restore parity for unarmored Dodge but creates method-dependent discontinuities; must be tested thoroughly.

**Recommended next step:** choose desired *attack hit rates* for three peer-to-peer cases—unarmored duelists, normal shield fighters, and fully enchanted plate tanks—**before** changing the formula. A TES-flavored system may prefer armor to reduce harm on hits, while Dodge and Block chiefly prevent hits. In any case, getting wounded should legitimately train worn armor if that is the chosen rule.

## Tests

See `scripts/ac_stress.py` and `tests/test_ac_stress.py`. Those verify exact roll probabilities including natural 1/20 auto behavior. The existing `scripts/defense_math.py` is preserved as the *previous proposal* and is not implicitly updated.

Reference values: https://www.d20srd.org/srd/equipment/armor.htm and https://www.d20srd.org/srd/combat/combatStatistics.htm ; magical armor enhancement stacking https://www.d20srd.org/srd/magicItems/magicArmor.htm . Calculations are original.
