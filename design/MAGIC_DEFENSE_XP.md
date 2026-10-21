# Magicka, protective magic and defensive-use XP — accepted XP rates

**Status:** XP multipliers are accepted and consolidated in [rules/ADVANCEMENT.md](../rules/ADVANCEMENT.md). This document explores attribution, pacing and implementation questions that remain unresolved. Specifically, **2 XP per actual Magicka spent**, **4 XP per actual HP lost while armored**, and **2 XP per attacker check total for a consequential defense-mediated miss** are now selected. Existing accepted skill threshold `5 × max(1, skill)`, weapon attack/damage skill bonuses `floor(skill/5)`, and offensive skill XP `2 × actual HP removed` remain unchanged.

See [defensive AC rules](../rules/DEFENSE.md), [generalized quick-check XP](GENERALIZED_EXTENDED_XP.md), and [24-skill catalog](skills_v2.json).

## Accepted shared skill XP methods

| Source | Accepted award and receiver | Trigger / caveat |
| --- | --- | --- |
| Actual offensive HP lost to a weapon, spell or skill-produced damage | **2 XP per attributable HP** to the skill producing that damage | HP genuinely removed, no overkill or damage resisted |
| Actual Magicka spent | **2 XP per actual Magicka spent** to the spell's school | On a **real cast that spends the resource**, whether hit lands or not. Not continuously each round of an active spell |
| Actual HP suffered in worn Light/Heavy Armor | **4 XP per HP lost** to the worn armor skill | Regardless of selected Block/Dodge reaction or failure. Harm must be of a kind the armor could ordinarily address; no arbitrary cap on taking authentic risks |
| HP suffered while an appropriate active protective spell applies (Oakflesh-like) | **2 XP per HP lost** to that spell's school, **plus** the Magicka-cost award at casting | Real enemy/physical harm; buff is active and relevant to protection. An additional award to worn armor for the same injury is plausible **parallel practice**, unlike awarding the same dealt damage twice |
| Meaningful enemy attack turned aside by selected trained defense | **2 XP × attack check total** to the **selected** Block/Dodge/Heavy Armor/Light Armor skill | The attack would have hit the **legally applicable gear-only baseline**, but missed due to that skill + attribute; natural 1 isn't the defender's feat; nat20 cannot be defeated by AC |
| Enemy attack prevented specifically by AC conferred by active protective spell | **2 XP × attack check total** to the spell's school | Spell must be *decisive*, not merely present; caster spent Magicka separately when it was cast |

The attacker check **total** is the raw d20 result plus all legal attack modifiers, **not** just the natural d20 face (a 13 plus +17 = 30, awarding 60 XP on a credited avoidance). For sanity when heavy penalties produce a check below zero, XP is `2 × max(0, attack_total)`. The raw attack total still governs success/failure.

## Damage attribution and layering

If multiple skills produce the same attack's HP loss, define *each effect's genuinely attributable part* rather than awarding every contributing skill the full attack's HP. E.g. a sword deals 10 physical HP loss and an active Destruction augmentation adds 4 HP of separate magical damage: tentatively 20 XP to One-Handed and 8 XP to Destruction, plus any actual Magicka spent when the augmentation was cast. If the target has fewer than 14 HP remaining, total credited damage across these sources cannot exceed its real remaining HP. Determining source order/mitigation for mixed damage types is still a combat integration question; don't make remote Enchanting skill increase every time an item that artisan sold damages someone.

For protective layering, evaluate an incoming attack against nested AC thresholds in a fixed, recorded priority: applicable gear-only AC; selected attribute/defense training; qualifying spell-provided AC. If the attack would have hit without the trained defense but the trained defense prevents it, that trained skill earns the avoidance XP. If it would have hit even with the trained defense but is stopped only by a protective spell, the spell earns the avoidance XP. **Do not give each layer the full avoidance award for one missed attack.**

Armor's **damage-suffered XP** is a separate category from avoidance and remains available after a failed Block/Dodge (provided the character survived or genuinely lost HP). Likewise Oakflesh-like magic may learn from actual damage suffered while its protective effect is relevant, *even if that strike penetrated it*. E.g. 10 HP lost while both plate and a relevant Oakflesh spell are active can teach both Armor (40 XP) and Alteration (20 XP), plus the original Magicka-expense XP from casting. This simultaneous **defensive training** is allowed by the accepted XP framework, subject to a real and relevant protective effect.

If a protective ward **reduces** 12 damage to 7 suffered, the proposed HP-suffered rules credit 7, not 12, unless separate prevented-damage practice is later added. This can penalize *more effective protection* in raw XP/hit; Magicka spent and AC-mediated avoidance help compensate, but check shield/DR spells in balance tests before finalizing.

## Pacing numbers with the accepted 2 XP per Magicka

At ranks **20→25 (550 XP)**, **50→55 (1300 XP)**, **95→100 (2425 XP)**:

| Example action | Low skill | Intermediate | High skill |
| --- | --- | --- | --- |
| Armor: 10 actual HP lost/hit → 40 XP | **14 hits** to gain +5 | **33 hits** | **61 hits** |
| Avoided attack: total 20/30/45 → 40/60/90 XP | **14 avoided attacks** | **22 avoided attacks** | **27 avoided attacks** |
| Destruction: applied 10/22/35 HP damage and spend 8/15/25 MP, 2 XP/MP | **16 casts** (36 XP/cast) | **18** (74 XP) | **21** (120 XP) |
| Utility magic, 8/15/25 MP per cast, 2 XP/MP | **35 casts** | **44 casts** | **49 casts** |

These are deterministic ceilings (rounding XP needed divided by the example award), *not* simulation outputs; cast success, damage after overkill, interruptions, hit frequency, cooldowns, replenishing Magicka, combat actions and actual incurred danger will change them. The spell rows deliberately use the same direct damage and Magicka numbers independently of skill bonus to test reward magnitudes; adding a spell-school flat damage bonus is a separate rules decision.

The **2 XP/MP** rate is now accepted. The 1 XP/MP case was a slower comparison, no longer the baseline. The utility-school comparison shows why expenditure XP matters for non-damaging spells; resource recovery, spell price tables and burst power still need encounter-level calibration.

## Avoidance qualification (important)

With a defender choosing Block (skill 30, STR +3), wearing armor/shield contributing AC 18:
```text
gear-only baseline = 18
trained Block AC = 18 + 3 + floor(30/5) = 27
enemy natural roll = 13; legal attack bonus = +10; total = 23
18 <= 23 < 27, so Block prevented a credible hit → 2 × 23 = 46 XP
```
If the natural face was **1**, the attack is an automatic miss regardless of defense, and awards zero avoidance XP. If the natural face was **20**, it hits regardless of AC and awards no avoided-attack XP; armor can still earn wound XP for actual HP lost. Reference: [D&D 2024 basic rules](https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game).

For direct magic buffs that increase AC, use the **same attack total** and counterfactual comparison; the responsible magic school earns XP for the attack it actually prevented. Keep weapon/magic/armor training events in independent ledgers while avoiding duplicate attribution within each event category.

## Remaining decisions

1. Implement the **accepted 2× actual Magicka spent** award in the GM's skill ledger, ensuring it is awarded once per real expenditure.
2. Implement approved parallel real-injury learning for worn armor and relevant protective magic; check which effects are genuinely active/relevant.
3. Should a ward that **absorbs damage to zero** receive XP for *prevented HP* rather than none, in addition to its Magicka-spend reward? Oakflesh-like AC and damage-reduction spells need consistent treatment.
4. Confirm avoidance attribution to only the defense or magic layer that truly stopped the attack, and whether that method has a legal reaction available.
5. Set spell-source rules for weapon magical riders, poison, damage over time, summons, environmental hazards, area spells, HP/life-drain and healing.
6. Compare schools that deal damage vs schools that only cost Magicka and affect the world; ensure utility Alteration, Mysticism and Illusion can advance.
7. Use the same threshold and skill XP ledger as generalized quick/extended work, with exact integer tenths if fractional progress XP is used.

No spell effect catalog, spell resource economy or finalized combat rules are introduced by this design document.
