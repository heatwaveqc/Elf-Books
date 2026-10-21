# Skill advancement v2 — consequential-use XP and critical perk discovery

**Status: working proposal, NOT operative rules.** A newer [24-skill consolidation and defense draft](CONSOLIDATED_SKILLS_DEFENSE.md) supersedes the earlier AC-attribution examples below for **single-method defense**; the general concept of use-based XP remains current. This supersedes the *learning-check advancement recommendation* in [ADVANCEMENT_MATH.md](ADVANCEMENT_MATH.md), but not the still-proposed 0–100 skill scale, +1 skill bonus per 5 ranks, or Warrior/Mage/Rogue ECL formulas. Do not migrate characters or begin play until the quantitative details are approved.

## Why replace successful learning checks?

Previous draft required `skill` successful attribute-based learning rolls per +1 rank, and natural 20 instead gave an immediate rank. Going from rank 95 to 100 requires `95+96+97+98+99 = 485` successful rolls without critical jumps. At +3 vs DC 15, ordinary learning success chance is 45%; expected meaningful rolls = `485/0.45 ≈ 1,078`. At 3–5 qualifying attacks per enemy, that's about **216–359 enemies** for ONE weapon skill. If all rolls succeed it's still **97–162** enemies.

D&D 3.5 typical equal-party-level encounter benchmark: roughly 13 1/3 encounters per character level for a four-PC party, around **253 encounters from levels 1 through 20**. Do not equate these directly: enemies are shared between PCs and 95→100 only changes our hit modifier +19→+20, whereas levels 1→20 add many capabilities. Official SRD XP threshold for level 20 is 190,000: https://www.d20srd.org/srd/xp.htm ; equivalent encounter-rate discussion: https://rpg.stackexchange.com/questions/75940/experience-point-calculation-for-encounters .

A 5% jump per critical solves high-rank slowdown but dominates ordinary practice early, near rank ~20–25 depending on learning DC. **Critical rolls are better candidates for discovering perks**, with XP-driven continuous improvement as the default.

## Proposed mechanics

1. Every canonical skill has an integer **rating 0–100** and separate **skill XP progress**, preserved on the character sheet and in event history. Existing bonus `floor(rating / 5)` is retained as a proposed D20 adapter.
2. A consequential application adds **deterministic practice XP** derived from the action's *meaningful output or challenge*, with a skill-specific unit and no separate chance-to-learn check.
3. XP required for the next rank increases with the rank. Candidate baseline: `XP_next(s) = max(1, s) × K`, where **K is unselected**. Do not choose K until typical input amounts and career simulations exist. Carry overflow into following ranks; never advance above 100.
4. Neither attacking the same trivial/invulnerable target indefinitely nor manufacturing self-damage should grant unlimited XP. Define meaningful targets, recoverable-threat budgets, daily/time constraints for practice, and honest trainers/research.
5. **Perk discovery:** once a skill has met a perk's rank prerequisite, a *natural 20 in a consequential use* could allow selection of one currently unlocked, unowned perk. A critical event must be recorded and not automatically duplicate a perk. Whether earlier criticals bank an insight, and whether training can teach perks, remain open.
6. **Passive skills:** armor and shield protection must get equally meaningful opportunities for both skill XP and perk discovery despite lacking their own attack rolls; candidate procedures below.
7. The primary advancement story is what a character actually *achieves and endures*, not repetitions of a learning DC. Failed attacks might award modest practice only for a genuinely difficult new technique; not every miss earns the same output XP as a hit.

## What counts as meaningful output?

| Skill family | Candidate XP basis | Important limitation |
| --- | --- | --- |
| One-/Two-Handed, blades, axe, blunt, spear, archery, hand-to-hand | Effective damage delivered **or** base weapon damage on a valid consequential hit | Actual damage encourages overkill and gear/perk feedback loops; base weapon damage (Skyrim-like) is easier to calibrate. Choose before implementation. |
| Block | Damage that shield/weapon prevented, including attacks defeated solely by shield AC | Avoid awarding both Block and armor full XP for the *same* prevented attack. |
| Heavy/Medium/Light Armor | Incoming damage armor prevented, either by AC (no hit) or by actual reduction | In conventional d20 armor primarily adds AC, so prevented HP damage isn't directly recorded without attribution. Do not reward deliberately taking unnecessary harm. |
| Unarmored, Dodging, Acrobatics | Consequential attack avoided or dangerous fall/obstacle overcome | No reward for trivially missed attacks. |
| Destruction | Effective spell damage **or** nominal/base Magicka cost of meaningful spell | If spell efficiency reduces actual MP spent, it should not punish learning; base cost needs a normalizing divisor or large spells skyrocket advancement. |
| Restoration | Meaningful HP restored, wounds stabilized, real harmful conditions removed | Zero XP for topping off at full HP or creating artificial injury loops. |
| Alteration, Illusion, Conjuration, Mysticism, Thaumaturgy | Base cost of spell that meaningfully affects a valid target/situation, adjusted for scale and duration | Casting an expensive spell into an empty room isn't automatically practice. Effects independent of combat require useful criteria. |
| Smithing, Armorer, Enchanting, Alchemy | Challenge/complexity/quality and resources of completed work | Prevent material-duping/trivial mass production from dominating skill XP. |
| Sneak, lock/security, pickpocket, speech, mercantile, etiquette, streetwise, languages | Successful or failed **consequential challenges**, stakes, difficulty, scope | Social and investigative skills need growth without one-roll-per-sentence or enormous attack-volume disadvantages. |
| Athletics, Running, Swimming, Climbing, Jumping | Difficult route/physical feat/distance completed under nontrivial conditions | No “run around the room for thousands of XP” exploit. |

**XP should generally follow credible application, not body count**: pacifists, crafters, merchants, scholars and thieves can grow without combat.

## D20 armor attribution (important!)

In an **AC-as-avoidance** system, armor often prevents a hit rather than numerically reducing damage. For an attack (not a natural 1/20 auto-miss/hit), compare the hit total against these thresholds:

- `bare_AC`: target AC without armor or shield, but with other ordinary bonuses
- `armor_AC`: same target with armor, no shield
- `full_AC`: with armor AND shield

If the total would hit `bare_AC` but misses `armor_AC`, credit the armor skill. If it would hit `armor_AC` but misses `full_AC`, credit Block/shield. Below bare AC: neither; at or above full AC: neither prevented that hit, unless the rules add actual damage reduction. Natural 1 automatically misses and cannot be credited as saved by armor; natural 20 automatically hits and cannot be credited as an armor AC save.

**Numeric example:** bare AC 10, armored AC 16, shield AC 18. An enemy total of 14 is turned aside by armor, and a 17 is turned aside by the shield. A total 8 was a simple miss; 19 hits despite protection.

A shieldless wearer has no Block credit; someone wearing armor without allowing it to play any part of defense doesn't learn from that attack. For armor that **absorbs actual HP damage** instead of giving AC, award XP based on the prevented amount, avoiding double counts. If a later skill's perks change AC thresholds, define whether an upgraded armor technique itself earns the attribution.

### How can passive armor skills get perk-critical successes?

Candidate options to evaluate, not simultaneous rules:
- **Defense discovery roll:** once for each consequential armor-mediated prevention, roll an independent d20 for a technique breakthrough. Natural 20 can discover a rank-unlocked perk. This is mathematically parallel to attackers rolling a natural 20, but adds a roll and should be logged.
- **Milestone discovery roll:** after a fixed amount of armor XP, roll a d20 to discover a perk. Works even if no active defense roll exists, but differs in cadence from weapon perks.
- **Active technique check:** let the wearer declare a special armor/block maneuver that includes an actual check; a natural 20 can teach a perk. Avoid rewriting every passive AC interaction as an opposed roll just to make armor improve.

Similarly, spells resolved solely by enemy saves need a fair way for the **caster**, rather than the target, to earn perk-critical successes. Don't interpret an enemy's natural 1 as the caster's critical success without an explicit rule.

## Calibration targets and pitfalls

- **Baseline illustrative calculation, not adopted:** `K=1` and a qualifying attack worth 10 skill XP gives **485/10 ≈ 49** attacks (about **10–17** enemies at 3–5 attacks/foe) from 95→100. This is only meaningful after weapon output and threat scaling are calibrated; magical costs of 100+ must not produce many skill levels per cast without a deliberate rule.
- Higher ranks should cost more but actions against credible higher-threat opposition typically have larger meaningful impact. Decide whether growth should *actually* slow with rank once output scaling is included.
- Rate-limit exploits without penalizing ordinary practice: cap by target HP/effective threat, tie credited mitigation to real damage risk, discount repetitive zero-stakes tasks, account for purchased training and study.
- **D&D 3.x alignment:** +20 skill attack bonus requires 3.x-appropriate AC/DC scaling; neither hit rates nor skill gains should accidentally add 5e proficiency or a class BAB.
- Distinct skill ratings and perk unlocking must not count the same sword action toward multiple overlapping historical skills (e.g. One-Handed and Long Blade) by default.
- ECL pools derive from **earned skill ranks**, not XP or bought perks. A passive armor skill can be powerful for Health growth; keep any changes to the resource formula independently reviewed.

## Next decisions
1. Choose damage basis: raw dealt, capped effective HP removed, base weapon damage (Skyrim-like), or a hybrid.
2. Pick XP units / divisor for weapon, spell, defense, social, crafting and travel categories. Calibrate a low, mid and high skill character before fixing `K`.
3. Define eligible crits: every meaningful action vs one per encounter; automatic perk on qualified crit vs “insight” to purchase.
4. Choose passive-armor/spell-without-attack critical treatment.
5. Decide thresholds and exact perks independently of the critical discovery mechanics.

References for inspiration (not copied mechanics): UESP Skyrim skills https://en.uesp.net/wiki/Skyrim:Skills ; 3.5 SRD https://www.d20srd.org/srd/xp.htm .
