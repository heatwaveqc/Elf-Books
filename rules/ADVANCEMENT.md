# Skill Advancement — accepted numeric rules

**Status: accepted XP framework, not yet a playable game.** The 24-skill catalog, perk acquisition, spell catalog, combat details and persistence are still being developed. This page supersedes older proposed XP multipliers.

## Core

- Skill ratings range from 0 to 100.
- XP required to raise rating S to S+1: **5 × max(1, S)**. Keep surplus XP.
- Weapon skill adds **floor(S/5)** to attack rolls and flat weapon damage.
- Store XP in integer **tenths** for exact fractional awards.

## XP awards

| Meaningful activity | Award |
| --- | --- |
| Actual outgoing HP damage attributable to that skill | **2 XP per HP removed** |
| Actual Magicka spent casting | **2 XP per Magicka spent** |
| Actual HP lost while wearing relevant armor | **4 XP per HP lost** to armor skill |
| Genuine incoming attack stopped by the chosen defensive method | **2 XP × full enemy attack result** |
| Actual HP lost under relevant protective magic | **2 XP per HP lost** to its school |
| Genuine incoming attack stopped specifically by protective magic | **2 XP × full enemy attack result** to its school |
| Successful meaningful quick check | **2 XP × DC** |
| Failed meaningful quick check | **0.5 XP × DC** |
| Successful extended work interval | **0.1 XP × credited progress** |

Outgoing damage counts **actual target HP removed**, after mitigation and capped by remaining HP. Source attribution for multi-part effects must not double count the same outgoing HP.

Magicka XP is awarded **once when actual Magicka is spent**, including utility spell practice without a damaging outcome. It may be added to genuine damage or protective results.

Worn armor learns from actual HP loss even if an attempted Block/Dodge failed; actual intentional risk is legitimate practice. Protective magic can independently learn from an injury while relevant: a 10-HP injury may therefore award 40 Armor XP and 20 Alteration XP, plus earlier XP from Magicka expended.

Defensive avoidance awards require a qualifying attack that **would hit without the applicable defense** but misses with it. The attacking enemy's natural 1 is an automatic miss that teaches no defense XP; natural 20 auto-hits. Attribute XP to the **decisive defense or magical protection** rather than paying several avoidance awards for the same missed attack. For defensive magic use the same counterfactual AC test.

In opposed quick checks, **effective DC is opponent's check total**. Ties are resolved before awarding XP. A genuine attempt may teach on failure, but gratuitous rerolls against an unchanged task are not separate objectives.

For substantial projects, predeclare DC, work interval, progress goal, and genuine project resources. A successful interval yields **Check Result × DC** raw progress; credit only up to the remaining progress goal. Each ten credited progress points earn one XP. A failed interval makes no progress and earns no progress-based XP. Completing the same project using more check rolls cannot increase its total XP. A chat response can summarize many real work intervals while still advancing the fictional calendar and resolving costs and consequences.

### Examples

- Destruction: spend 8 Magicka, remove 12 actual enemy HP ⇒ **16 + 24 = 40 XP**.
- Block: enemy roll 13 + 10 = 23 against gear AC 18 and Block AC 27 ⇒ **46 Block XP**.
- Project: DC25, goal 1,000, result 30 ⇒ 750 progress and 75 XP; next interval can credit only the remaining 250, awarding 25 XP.
- A successful DC25 quick check ⇒ 50 XP; a meaningful failed DC25 check ⇒ 12.5 XP.

## Next development phase

**Perks**: skill gates, active critical discoveries, passive defensive opportunities, instructor teaching and whether earned discoveries can be banked. Critical successes **do not** directly increase skill ranks.

Details still needed for specific spell effects, unconventional damage mitigation, teamwork, defensive reactions and GM save integration. Numeric XP progression is settled; **Elf-Books is not yet playable**.

References: [Defense](DEFENSE.md), [Generalized extended checks](../design/GENERALIZED_EXTENDED_XP.md), [Magic and defense XP study](../design/MAGIC_DEFENSE_XP.md).
