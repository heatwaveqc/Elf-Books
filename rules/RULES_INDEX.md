# Rules index — authority and implementation status

**Overall status: FOUNDATION, NOT PLAYABLE.** This index is the authority for what is resolved versus still under design; never infer complete rules merely because files exist.

## Resolution foundation
- **Intended source:** SRD 5.2.1 under CC BY 4.0 (see [LEGAL.md](../LEGAL.md)). Reference material is linked, not mirrored.
- **Accepted direction:** d20-style checks, recognizable combat vocabulary, classless and level-free default, archetypes as optional starting packages, player-selectable campaign advancement policy, independent GM campaign saves.
- **NOT automatically adopted from the SRD:** class progression, character levels, proficiency-bonus-by-level, hit-dice-by-level, spell slots, encounter CR, class-exclusive abilities and level-based spells. Explicit replacements required.
- **Agreed defense core:** [DEFENSE.md](DEFENSE.md): AC = legal gear/magic bonuses + chosen defense's attribute modifier + floor(defense skill/5), **without innate +10**; heavy armor CON, light armor/dodge DEX, block STR; Block/Dodge cost reaction until suitable early perk; actual HP lost while armored teaches that armor skill even after failed other defenses. Unarmored equal-skill 95% hits deliberately accepted. **Detailed equipment stack, reactions/perks and combat still incomplete.** [Older stress test](../design/HIGH_END_AC_STRESS_TEST.md) is historical.
- **Current consolidation candidate:** [24 consolidated skills and single-method defensive AC](../design/CONSOLIDATED_SKILLS_DEFENSE.md), with original perk seeds and a full crosswalk of 52 former names. Existing `rules/skills.json` and its older mathematical exercises remain **archived candidates**, not the chosen operative skill roster.
- **Accepted XP core:** `XP_next=5×max(1,current_skill)` for all skill ratings; attributable **offensive skill** activity earns `2×actual HP damage` (after mitigation and overkill caps). Weapon skills add `floor(skill/5)` to both hit rolls and flat attack damage, with 5e-style critical dice doubled but flat modifiers not doubled. See [WEAPON_SKILL_DAMAGE_XP.md](../design/WEAPON_SKILL_DAMAGE_XP.md). Spell-damage attribution, off-hand/multiattack and detailed combat are still open.
- **Earlier damage-only XP test (comparison only):** [ACTUAL_DAMAGE_XP.md](../design/ACTUAL_DAMAGE_XP.md): `next_rank_xp = 5 × max(1, current skill)`; offensive weapon XP = enemy HP **actually removed** by that weapon attack (not base damage or overkill); tests expose the early-game slowdown and the need to recalibrate armor, magic and noncombat. The [earlier K=1, base-damage experiment](../design/XP_CALIBRATION.md) remains for comparison.
- **Prototyped, not approved:** skill 0–100, check bonus `floor(skill/5)` (3.x-style +20 at skill 100), category ECL for Health/Magicka. **Use-based XP is now the preferred advancement direction; the nat-20 skill-jump and successful-learning-check ladder are superseded proposals, not live rules.**
- **Unresolved:** final ability-to-skill check formula, learning DC, exact degree of 3.x combat adaptation and AC/defense scaling, proficiency replacement; HP and damage scaling; armor/saves; action economy divergences; spellcasting and Magicka; enchanting/alchemy; skill XP/progress; threats and pacing.
- **Do not start actual play** until the replacements are implemented, tested, and approved.

## Design documents (proposals, not rules)
- **[Accepted core defensive AC and reactions](DEFENSE.md)** — no base +10; spell/equipment stacking and perk details pending
- **[Latest weapon-damage-and-XP candidate](../design/WEAPON_SKILL_DAMAGE_XP.md)** — skill adds to flat damage; 2 XP/HP with K=5 rank cost, still unapproved
- [Earlier actual damage / K=5, 1 XP/HP experiment](../design/ACTUAL_DAMAGE_XP.md) — comparison
- [Earlier base-damage / K=1 XP comparison](../design/XP_CALIBRATION.md) — archival benchmark
- **[Archived consolidation and earlier defensive AC proposal](../design/CONSOLIDATED_SKILLS_DEFENSE.md)** — 24 skills in 8/8/8 categories; one applicable defense method adds `floor(skill/5)` to AC; enemy natural 1 is not defender's crit
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
