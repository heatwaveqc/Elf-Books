# Roadmap and acceptance tests

## Current scaffold checks
- `python3 scripts/validate_scaffold.py` validates links/file layout, template structure, and the absence of real public campaign files.
- `python3 -m unittest discover -s tests` exercises validator happy/failure paths.
- GitHub Actions runs those checks for pushes and PRs.

These are **structural** tests; passing them does **not** declare the game playable.

## Skill model structural prototype
- [Skill and draft perk catalog](../rules/SKILLS.md) has 52 rated skills and 104 candidate unlock hooks; aliases and historical umbrella names don't receive their own advancement.
- [Prototype calculator](../scripts/skill_math.py) and tests cover 0–100 conversion, category ECL caps, half-Rogue contribution, empty-category behavior and learning natural 20s. These tests verify specified formulas, **not gameplay balance or approval**.

## Use-based design calibration
- [Proposed action-output XP and critical-perk discovery](../design/USE_BASED_ADVANCEMENT.md) supersedes success-based learning checks, but quantitative XP conversion and passive armor/magic perk opportunities remain undecided.
- Test armor attribution: enemy total below unarmored AC → no XP, between unarmored and armored AC → armor XP, between armored and shield AC → Block XP, above full AC → no prevented-hit XP. Honor automatic hit/miss natural rolls.
- Test that burst damage, overkill, no-cost spells, self-harm, invulnerable targets and repeatable trivial transactions cannot produce infinite progression.

## 24-skill and defense candidate checks
- [Consolidated 24-skill proposal](../design/CONSOLIDATED_SKILLS_DEFENSE.md) maps all 52 old skills to 8 Warrior, 8 Mage and 8 Rogue skills; preserve prior catalog only for crosswalk/history, not as additive ratings.
- [Defense prototype](../scripts/defense_math.py) asserts one chosen defense skill against each attack, natural 1/20 attack behavior, XP credit only for defense-mediated credible miss, gear-only novice defense, and separately rolled defense perk breakthrough. It is a testing artifact, not live mechanics.
- Test peer and mismatch attack-versus-AC curves before treating a +20 defense bonus as operative, and retest ECL pooling after cutting category sizes.

## AC stress tests
- [Full-endgame and unarmored parity comparison](../design/HIGH_END_AC_STRESS_TEST.md) and [calculator](../scripts/ac_stress.py) confirm 5% hit against full +5 plate/+5 shield/+5 natural at 100 skills regardless of base10; 95% hit in matched unarmored duels if base10 is removed.
- Reassess defensive scale, gear stacking and damage absorption. This is a design issue, **not** a failing test: unit tests validate the arithmetic and make unacceptable extremes visible.
- Allow actual, risky HP damage to train worn armor regardless of defensive method. Avoidance XP remains separate. Do not automatically mark deliberate risk as abuse.

## Accepted defense core and XP calibration
- [Core defensive formula](../rules/DEFENSE.md) replaces innate +10 with skill/5, retains fifth-edition equipment *contributions*, distinguishes Heavy-CON / Light-DEX / Block-STR / Dodge-DEX, and requires reactions for active Block/Dodge until perks.
- [XP benchmarking](../design/XP_CALIBRATION.md) tests 20→25, 50→55, 95→100 and 20→100 with d8 expected nominal damage, actual HP lost to armor, and candidate magic/noncombat scales. XP magnitudes are **not approved**.
- [Core defense smoke tests](../tests/test_xp_calibration.py) check without-10 AC, +3 plate/shield endgame matchup, reaction consumption/perk bypass, and armor gaining XP from actual HP loss despite a failed Block.

## Actual-damage XP and fivefold rank-cost candidate
- [New XP experiment](../design/ACTUAL_DAMAGE_XP.md) tests K=5 versus K=1 and base d8 versus applied real HP loss. [Pure calculator](../scripts/actual_damage_xp.py) tests that overkill is not extra learning, mitigated damage earns less, and a 20-HP enemy awards no more than 20 damage XP regardless of hit count.
- Test that skill 20→25 can become ~3 times slower than the previous base-damage model with only 1d8+3 actual HP per hit; high-end 1d8+7+3 damage is below the 22.5 XP/hit break-even.
- Recalibrate armor, Block/Dodge, schools of magic, crafting and social rewards whenever the rank-cost scale changes. No new XP numbers are operative without approval.

## Skill bonus to weapon damage / fractional-to-integer XP equivalence
- [Latest proposed weapon formula](../design/WEAPON_SKILL_DAMAGE_XP.md) and [arithmetic tests](../tests/test_weapon_skill_xp.py) verify flat +floor(skill/5) weapon damage and 5×rank / 2 XP per actual HP equivalence to 2.5×rank / 1 XP per damage.
- Model a skill-20 novice, 50 journeyman, 95 master; natural-20 crits double damage dice **not** flat bonuses. Distinguish attack attempts from successful hits and cap XP by applied actual HP.
- Stress-test dual-wield and multiattack, early HP versus high skill-based damage, and armor/spell/noncombat relative XP under the new shared XP units.

## Crafting and task DC XP calibration
- [Candidate DC-based crafting award](../design/CRAFTING_DC_XP.md) and [calculator/tests](../tests/test_crafting_xp.py) compare candidate `2 × declared intrinsic DC` XP per actual finished work unit at 20/50/95 skill with the now-agreed universal 5× rank cost.
- A batch of five real products earns five units; five gratuitous dice rolls for one product earn only one unit. Low-DC mass production remains valid real practice if materials/time are spent.
- Check skill 100 vs extended DC 35–45 mastery items; normal 5e 5–30 difficulties assume much smaller proficiency bonuses.
- Decide failed substantial-work XP, master-project milestone sizing, economics vs complexity, and social/research skill applicability before adopting numerical crafting awards.

## Generalized quick / opposed / extended XP prototype
- [New progress-and-XP model](../design/GENERALIZED_EXTENDED_XP.md) and [targeted tests](../tests/test_generalized_skill_xp.py) cover project DC/interval/progress-goal, successful check-result × DC progress, fractional XP represented as integer tenths, failure margin, no double credit for overproduction, and opponent-result DC with 3.5 tie behavior.
- Verify externally that shorter arbitrary intervals cannot increase project XP from the same fixed goal; fix project units and interval up front and prohibit treating administrative subdivisions as fresh checks.
- Confirm proposed scalar 1 XP/10 credited progress and quick 2×DC success / 0.5×DC failure separately; learn from substantial failure without granting free reroll-based farming.
- Determine Perception/observation opposed skill mapping within the consolidated 24-skill catalog.

## Solo pacing model and calibration
- [Reproducible seeded comparison](../scripts/pacing_comparisons.py) and [test suite](../tests/test_pacing_comparisons.py) compare skill 20/50/95 across 1d8 60%-to-hit combats, static DC-based meaningful quick checks, and weekly extended projects, with HP-capped damage and natural 20s.
- [Methodology/report](../design/SOLO_PACING_COMPARISON.md) separates one-chat-project summaries from the actual week-by-week simulation; compare goal 1000/2500/6000 against constant 1000 goals.
- Do not attempt to equalize XP per *chat turn* with an artificial reward cap. World clocks, expenses and fiction elapsed are real costs for downtime.

## Before first real campaign
- Decide advancement formula and skill/check mapping; simulate novice/specialist/generalist/mage career paths and bounded-accuracy outcomes.
- Decide HP, damage, initiative, armor and saves without character levels.
- Build Magicka, schools, basic spell creation, spell learning, alchemy/enchanting starter rules.
- Populate source-linked era snapshot for a playable region and date.
- Create real private-store saver/loader with atomic event/checkpoint behavior; test simulated save conflicts and tool outage.
- Validate pre-session private spine and three independent clue paths; audit GM discretion and spoiler leaks.
- Run two character-creation tests and a 5-scene campaign, including a departure from the expected plot. Check that skill gain is fair and persisted.

## Quality bar
No generated outcomes based on fabricated rolls; no class-gated learning; no accidental level-based modifiers; no undated anachronisms; no leaking public campaign secrets; no broken continuation after restart. The user approves progression and combat balance before any release is called playable.
