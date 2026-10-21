# Rules index — authority and implementation status

**Overall status: FOUNDATION, NOT PLAYABLE.** This index is the authority for what is resolved versus still under design; never infer complete rules merely because files exist.

## Resolution foundation
- **Intended source:** SRD 5.2.1 under CC BY 4.0 (see [LEGAL.md](../LEGAL.md)). Reference material is linked, not mirrored.
- **Accepted direction:** d20-style checks, recognizable combat vocabulary, classless and level-free default, archetypes as optional starting packages, player-selectable campaign advancement policy, independent GM campaign saves.
- **NOT automatically adopted from the SRD:** class progression, character levels, proficiency-bonus-by-level, hit-dice-by-level, spell slots, encounter CR, class-exclusive abilities and level-based spells. Explicit replacements required.
- **Current defense balance concern:** [High-end AC stress test](../design/HIGH_END_AC_STRESS_TEST.md) demonstrates that deleting +10 alone does not make fully enchanted tanks hittable, but causes equal-skill unarmored attacks to hit 95%. Armor XP from actual HP loss regardless of defense is affirmed as player-preferred direction. **No final base-AC adjustment is approved.**
- **Current consolidation candidate:** [24 consolidated skills and single-method defensive AC](../design/CONSOLIDATED_SKILLS_DEFENSE.md), with original perk seeds and a full crosswalk of 52 former names. Existing `rules/skills.json` and its older mathematical exercises remain **archived candidates**, not the chosen operative skill roster.
- **Prototyped, not approved:** skill 0–100, check bonus `floor(skill/5)` (3.x-style +20 at skill 100), category ECL for Health/Magicka. **Use-based XP is now the preferred advancement direction; the nat-20 skill-jump and successful-learning-check ladder are superseded proposals, not live rules.**
- **Unresolved:** final ability-to-skill check formula, learning DC, exact degree of 3.x combat adaptation and AC/defense scaling, proficiency replacement; HP and damage scaling; armor/saves; action economy divergences; spellcasting and Magicka; enchanting/alchemy; skill XP/progress; threats and pacing.
- **Do not start actual play** until the replacements are implemented, tested, and approved.

## Design documents (proposals, not rules)
- **[Preferred consolidation and defensive AC proposal](../design/CONSOLIDATED_SKILLS_DEFENSE.md)** — 24 skills in 8/8/8 categories; one applicable defense method adds `floor(skill/5)` to AC; enemy natural 1 is not defender's crit
- [Candidate structured 24-skill roster](../design/skills_v2.json) — original 48 perk seeds and complete 52-skill historical crosswalk
- [Earlier 52 rated skills, historic crosswalk and draft perks](SKILLS.md) — archived candidate, not the preferred roster
- [Earlier structured skills and perks](skills.json) — 52 skills / 104 perk hooks, preserved for comparative tests
- [Current use-based advancement proposal](../design/USE_BASED_ADVANCEMENT.md) — deterministic skill XP from consequential use; natural-20 perk discovery with passive-defense alternatives, not yet approved
- [Superseded learning-check comparison and still-proposed ECL formulas](../design/ADVANCEMENT_MATH.md) — archival attribute-based learning experiment; 0–100 and resource math remain open

- [Foundation adaptation points](FOUNDATION.md)
- [Skill advancement alternatives](../design/PROGRESSION.md)
- [Magic requirements](../design/MAGIC.md)

## Play operation (procedural authority)
- [Character creation](../game/CHARACTER_CREATION.md)
- [Pre-session preparation](../game/PRE_SESSION_PREP.md)
- [GM protocol](../game/GM_PROTOCOL.md)
- [Persistence](../game/PERSISTENCE.md)
- [Test plan](../game/TEST_PLAN.md)

## Lore
- [Provenance and disputed accounts](../lore/LORE_POLICY.md)
- [Timeline/era index](../lore/ERAS.md)

Each approved mechanic needs: an explicit rule, examples, numeric checks, and a versioned change note. An individual campaign pins the rule revision and must explicitly accept migrations.
