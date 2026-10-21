# Superseded learning-check advancement and ECL — archival prototype

**The learning-check progression in this file has been superseded as the preferred design by [USE_BASED_ADVANCEMENT.md](USE_BASED_ADVANCEMENT.md).** The skill-to-d20 modifier and category ECL formulas remain open for approval. The old `learn()` code remains only for comparing designs.

This earlier proposal implemented the classless direction in [scripts/skill_math.py](../scripts/skill_math.py). The prototype supports deterministic calculations and externally supplied d20 learning rolls. **No runnable campaigns** until the choices below are approved, and until combat, spellcasting, perks and independent private saves are developed.

## 1. Rated skill and check modifier

Each canonical skill has a whole-number rating `0..100`.

```text
skill_roll_bonus = floor(skill / 5)
action check = d20 + relevant attribute modifier + skill_roll_bonus + situational modifiers
```

Examples: skill 0→+0; 5→+1; 25→+5; 50→+10; 100→+20. This adopts **D&D 3.x-style attack growth**, *not* D&D 5e bounded accuracy or an additional class/proficiency bonus. Class-based BAB, level-dependent proficiency and class-gated attack progression are NOT added. A native 20 on an **attack** does not confer a skill advancement unless a **separate** qualified learning check succeeds; do not confuse attack rolls and advancement rolls.

**Open:** defensive AC / difficulty scale must be adjusted; +20 attacks overwhelm many 5e armor values. Who uses STR vs DEX in mixed weapon techniques is part of skill definition, not a player exploit.

## 2. Progression event (candidate, exact proposal implemented)

A meaningful skill use permits **one** learning check for the relevant canonical skill. Distinct scene/encounter importance is determined by the GM and logged, not every sword swing or repeated trivial practice. Use current skill `s`, saved `progress`, governing attribute modifier `m`, learning DC `d`, and a fresh actual d20 roll:

- On natural 20, increase skill by **+1 immediately** (maximum 100), reset progress to zero. This is a learning critical, independent of whether the original use succeeded.
- Otherwise, if `d20 + m >= d`, increase `progress` by one. At `progress >= max(1,s)`, increase the skill by **+1** and reset progress.
- Other rolls grant no progress. Every eligible use, roll, progress change and advance must be saved.
- A `s=0` skill needs **one** ordinary success for the first point. This is a prototype default avoiding a zero-success automatic advancement.
- Learning DC **has not been selected**. It is passed explicitly to the calculator, not hidden in code. Nat 20 and threshold behavior can be tested without deciding a DC.

**Important pacing consequence:** a 5% chance to jump a full rank means the waiting time for an advance is never more than **20 qualifying uses on average**, regardless of skill! With attribute +3 and an illustrative learning DC 15, the model needs ~9 qualifying uses at skill 5, ~14 at skill 10, and almost 20 at skill 25+. Hence natural-20 jumps dominate progression *far before* skill 100. Training will need to compete with this; it should be compared to real advancement traces before finalizing.

## 3. Category effective levels and derived pools

There are three skill categories, each computed separately:

```text
W = min(sum(Warrior skill ratings) / 20, max(Warrior skill rating) / 5)
M = min(sum(Mage skill ratings)    / 20, max(Mage skill rating)    / 5)
R = min(sum(Rogue skill ratings)   / 20, max(Rogue skill rating)   / 5)

Health_ECL  = W + R/2
Magicka_ECL = M + R/2

Health  = floor((5 + Constitution modifier) * Health_ECL)
Magicka = floor((5 + Wisdom modifier) * Magicka_ECL)
```

Empty categories have `sum=max=0`, thus ECL 0. Fractional ECL is retained until resource pool rounding, using rational arithmetic to avoid accumulated float errors. This interpretation puts the cap on **each source category before** adding half the Rogue contribution, consistent with “Rogue skills contribute half to both.”

**Edge cases to decide:** At zero all skills, both pools are zero; newly generated PCs should have nonzero trained skills, but this still needs an explicit **starting minimum**. Also, a character who maxes Warrior and Rogue can reach `Health_ECL=30`, rather than 20. Maxing Mage and Rogue similarly yields `Magicka_ECL=30`. If 20 should be a hard total cap, add a **post-mixing** cap, but that changes the proposed rule. Existing draft preserves the unclamped 30 maximum and calls it out.

### Example (not a character template)
Warrior skill scores 40+30+20 → `W=4.5`; Mage 40+20 → `M=3`; Rogue 20+20 → `R=2`.

With CON +2, WIS +3:
```text
Health_ECL = 4.5 + 2/2 = 5.5 → Health = floor(7×5.5) = 38
Magicka_ECL = 3 + 2/2   = 4   → Magicka = floor(8×4)   = 32
```

## Pending approvals

1. Is the `+1 for every 5 skill points` reading correct?
2. Do we use an attribute **only** for learning checks, or also in resolving skill attempts?
3. What is the learning DC, and does difficulty alter it or the number of learning chances?
4. Are zero-skill training, starting HP/Magicka minima and rounding defined here as desired?
5. Should each pool cap at total effective 20 or accept 30 when Rogue+Warrior/Mage are both mastered?
6. Is natural-20 growth meant to dominate already at skill 15–25, or should it become more prominent only late in progression?
7. How are perk picks earned? Unlocking at a skill threshold is not necessarily free acquisition.
8. Which weapon skill naming profile is used to avoid overlap? Do language skills each count independently toward Rogue ECL?

No class system, character level, Stamina pool or D&D XP is required by these prototypes.
