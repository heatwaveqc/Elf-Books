# Defensive combat core — agreed formula, remaining rules still in development

**Status:** The **core formula, defense attributes, training progression, and armor-learning principle** have been accepted in design discussions. This is **not a certification that the full game is playable**: equipment stacking edge cases, natural armor, reaction-refresh timing, perk details and combat balance are still being developed.

## AC (no innate +10)

```text
AC = applicable armor equipment bonus + shield equipment bonus
   + other legally stacking AC bonuses
   + attribute modifier for selected defense
   + floor(selected defensive skill / 5)
```

Use **5e-style equipment *contributions***, not the equipment's published AC as if it were a bonus. For instance: base full plate 18 represents **+8** over conventional AC 10, mundane shield adds **+2**, studded leather 12 represents **+2**. A +3 armor enchantment adds +3 to that armor contribution when legal. Do not append a second base 10. Natural armor and other magical AC sources require an explicit compatible stacking/alternative-formula adjudication; they are not all freely additive.

| Selected defense | Governing attribute | Required condition | Reaction use |
| --- | --- | --- | --- |
| Heavy Armor | CON | Heavy armor worn | Passive |
| Light Armor | DEX | Light armor worn | Passive |
| Block | STR | Legal shield or weapon block, awareness | Uses reaction until low-level perk |
| Dodge | DEX | Ability to evade / awareness | Uses reaction until low-level perk |
| Untrained fallback | DEX | Applicable when other defenses unavailable | No trained skill bonus |

**One and only one defensive skill bonus** applies per incoming attack. All other legal equipment still protects the defender, but those skills do not stack. A block/dodge attempt must be declared or preselected **before** seeing the attack result. Using the appropriate early perk permits that method without spending the reaction; its exact skill requirement and wording remain to be designed. Until then the same reaction cannot defend against unlimited attacks.

At equal attack and defense skill, bonuses of `floor(skill/5)` cancel. A genuinely unarmored fighter without AC from other sources can be hit on up to **95%** of equal-skill attacks (3.x-style natural 1 always misses), **intentionally accepted** as lethal real-world-like exposure. This is not a reason to reinsert +10 or halve defensive skill progression.

## High-end calibration

With 5e equipment contributions, attack skill 100 (+20), relevant attribute 25 (+7), and +3 weapon (+3): **attack +30**. Heavy Armor skill 100 (+20), CON 25 (+7), +3 plate (+11), +3 shield (+5): **AC 43**, producing a **40%** chance to hit (needed d20 13–20).

This excludes independent, potentially nonstacking natural-armor effects. Do **not** use the +5 equipment stacking and full natural-armor example from the legacy 3.5 stress test as though it were the adopted 5e equipment model.

## Defensive skill XP

- **Worn Heavy or Light Armor:** gain experience from **actual HP lost to credible harmful events while wearing that armor**, even when the selected defense was Block or Dodge and failed. The risk is real, and intentionally accepting harm to learn is valid Elder Scrolls play. There is no automatic cap or blanket penalty merely because the player could have avoided the risk. The numerical rate per HP is an open design question.
- **Block and Dodge:** gain experience when the chosen maneuver prevents a genuinely threatening hit: the total attack roll, excluding automatic 1/20 rules, would have hit the defender's **non-skill/non-attribute gear-only baseline**, but misses with the selected defense included. Equipment and applicable magic belong in that baseline; credit one chosen defense only.
- Enemy **natural 1**: automatic miss, but not a Block/Dodge defensive feat. Enemy **natural 20**: automatic hit; armor may still earn XP if real HP is lost.
- Defensive perk breakthroughs are **separate qualifying critical experiences**, not automatically granted by an opponent rolling natural 1. How armor receives these breakthroughs from real damage, and exactly when a breakthrough yields a perk, remain for perk system design.

**Latest proposed amounts**: armor learns at 4 XP per actual HP lost; the selected applicable trained defense learns 2 XP per full attack check result when it actually turns a threatening hit into a miss (except natural 1 automatic miss). These are **proposals, not locked rates**. Protective spell layering and spell-school XP are discussed in [MAGIC_DEFENSE_XP.md](../design/MAGIC_DEFENSE_XP.md). Earlier benchmarks: [XP_CALIBRATION.md](../design/XP_CALIBRATION.md).

Legacy [CONSOLIDATED_SKILLS_DEFENSE.md](../design/CONSOLIDATED_SKILLS_DEFENSE.md) and [HIGH_END_AC_STRESS_TEST.md](../design/HIGH_END_AC_STRESS_TEST.md) contain earlier comparative proposals, **not current AC authority**.
