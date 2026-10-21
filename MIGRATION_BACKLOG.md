# Geard Lif migration backlog — Elf-Books return-to-parity audit

**Scope:** Move Elf-Books from the archived D20 prototype to a local, pinned snapshot of Geard Lif / Raven's Heart core. **This checklist is the authoritative gap list.** It distinguishes genuine Geard Lif upstream gaps from Elder Scrolls-specific conversion and the existing solo GM infrastructure. No check below is implied completed merely by the import.

**Old D20 baseline:** [archive/d20-pre-geard-lif](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif) at `f5b31ccbed44ba4767d86f7098e3ddfdb7ee5956`. The historical calculations and 24-skill/perk design drafts remain accessible there. **Upstream snapshot:** [engine/geard-lif](engine/geard-lif/README.md).

## Already migrated / preserved

- [x] **Old D20 version recoverable:** separate immutable-by-policy archive branch, no fork or history rewrite.
- [x] **Local Geard Lif core:** four source player-audience rule tiddlers, pinned upstream SHA, import/provenance policy and locked/provisional status summary.
- [x] **Core arithmetic reference:** tentative d10 success counting and Tier conversion, *meet-to-beat* Accuracy, shared graded severity/promotion/recovery, Project Scope-as-marks completion and adjustable injury thresholds. No obsolete D20-like progress pool.
- [x] **Elder Scrolls scope/lore:** era, region, canon divergence, provenance, and per-campaign private world facts preserved.
- [x] **Independent solo campaign concept:** GM preflight, antagonists/clocks, private saves and event logs retained as requirements, but character/runtime mapping requires implementation.
- [x] **24 skill names and 75 TES perk inspirations:** preserve as *content* and provenance without treating obsolete 0–100 gates as Geard Lif mechanics.

## P0 — before even a reliable four-scene vertical slice

- [x] **A. Meet-it-to-beat-it resolution (UPSTREAM):** Accuracy successes **>=** Complexity/Avoidance hit/apply. Only then roll independent Potence. On positive Potence, inflict Minor below effective threshold R, Middling at R, Major at 2R, Final at 3R, and multiple Final marks at successive multiples. Zero successes yield no mark. Excess Accuracy does not amplify Potence without an explicit bridge.
- [x] **A2. Universal essence-ping progress (UPSTREAM + ADAPTER):** **four grades of marks for everyone and everything**. Project **Scope** is slots per grade and **Recalcitrance** controls the grade threshold; final exhaustion completes the Project. Personal **Resilience** is slots per grade and baseline grade threshold; armor/wards can adjust the injury threshold but **not slot count**. Promotion follows the resource-mark engine, not a separate numeric Scope point pool.
- [ ] **A3. Edge/adjudication integration:** define zero Recalcitrance behavior; exact protective-equipment injury threshold formula; project setbacks/repair, partial group work and how interim graded project progress changes a real situation. These are not unresolved core resolution mechanics.
- [x] **B1. Trait architecture (UPSTREAM + ADAPTER):** **12 independent attributes** (four roles each in Body/Mind/Soul), one named Talent governing **exactly five** chosen skills with its own separate progression tree, a 24-skill TES roster, and narrower per-skill Specialties. One Talent provides bonus dice only to governed skills; every other skill is usable/trainable. Includes 12 preset Talent samples, freely named five-skill custom packages, local d10 pool validator/tests.
- [ ] **B2. Trait economics and derivations (UPSTREAM + ADAPTER):** starting attributes, Skill/Specialty/Talent rating allocations; confirm provisional 0–5 cap, equipment and teammate additions, cost/XP advancement of traits, static Avoidance from Avoidance attributes, method choice for Accuracy versus Potence, real Talent-tree nodes/branch rules, and how custom-tree equivalence works. **No implicit class lock**.
- [ ] **C. First-tier survivability (UPSTREAM):** validate Injury, Fatigue, Attention and Mana tracks, recovery cadence, Costs, peer-level threat odds and solo PC survival; choose starting Resilience capacity and initial gear. No numeric HP/MP pool assumed.
- [ ] **D. Combat adapter (ADAPTER):** one attack as a Project; static Avoidance, armor and shield effects, Block/Dodge legal action cost and reactive options, natural defenses, damage-to-mark handling and applied attack resolution. Decide where spells/armor intervene, including magical wards and Oakflesh.
- [ ] **E. Magic bridge (UPSTREAM + ADAPTER):** implement a minimal cast procedure with school, target, Accuracy/Potence, Cost rating/Mana marks, duration/concentration, summoning limitations, and protection on Injury. Do not use the D20 spell-slot/DC system.
- [ ] **F. Advancement redesign (ADAPTER, with upstream hooks):** retain **use-based skills** and **bankable perk points** in spirit. Select a new experience unit for Project progress, effect magnitudes/graded injuries, overcoming Avoidance and self-targeted Mana Costs. Old 5×skill, 2×HP, 4×HP and 2×Magicka are **archived numerical rules**; they do not apply to rating 0–5 or graded marks.
- [ ] **G. Criticals/perk points (UPSTREAM + ADAPTER):** agree the critical and botch probability distribution for a d10 pool, passive combat breakthrough eligibility, one bankable perk per qualifying event, skill/trait gates, trainer restriction, artifact exception. Never use "any 10" as a replacement for natural 20 without statistical calibration.
- [ ] **H. Four-scene acceptance test:** resolve complete *bandit fight*, *high-pressure theft*, *Oakflesh/protective ward*, and *month-long smithing Project* including rolls, time, resource changes, rewards and event logs. No active game until these can be played coherently.

## P1 — match the breadth of previous D20 design

- [ ] **I. Elder Scrolls character creation:** race/ancestry/culture, attributes, Will/Health/Conviction, starting trait dice and Tiers, free choice of classless skills and optional archetype without gatekeeping.
- [ ] **J. Offensive skill/magic specializations:** flat damage has no direct equivalent; define competence improvements to Accuracy, Potence or a bridge-perk, and decide how specific skills teach without double counting contribution to the same Effect.
- [ ] **K. Armor/avoidance practice:** preserve both **worn-armor experience from credible injury** and defensive practice from dangerous near-misses under static Avoidance. A hostile zero-success pool does not automatically equate to a natural 1 on d20.
- [ ] **L. Projects/crafting:** choose Scope, Time, Complexity and Recalcitrance for smithing, alchemy, enchanting, scholarship, lockpicking and social change; actual credited progress (not GM-added bookkeeping attempts) drives practice.
- [ ] **M. Resource-driven schools:** Destruction, Restoration, Alteration, Conjuration, Illusion, Mysticism, Alchemy, Enchanting; how wards, real healing, Soul Trap, summons, poison, area spells and non-damage utility teach. Treat Magicka → Mana **Cost Effect**, not a numeric rename.
- [ ] **N. TES combat equipment and enemies:** weapon reach/speed; shields/armor/encumbrance; Daedric and Dwarven gear; bandits/undead/dragons/Daedra; encounter metrics for Injury/marks and Tier, not CR/HP/AC.
- [ ] **O. Perk source ports:** evaluate 75 original-game inspirations against Geard action/tier/resources; restore Stamina-like effects as possible **Fatigue** perks where apt, rather than automatically rejecting them; rank thresholds 25/50/75/100 from D20 are historical.
- [ ] **P. Tier calibration:** ordinary NPC through heroic and mythic figures; spells, artifacts, soul gems, Daedric entities and Elder Scrolls reality-altering phenomena; tool Control Tier versus Effect Tier.
- [ ] **Q. Social/investigative checks and opposing projects:** persuasion, perception, intimidation, stealth, research and faction clocks. Static opposition rather than automatically rolling both sides; stage-by-stage Project progress and setbacks.
- [ ] **R. Solo pacing:** preserve the research distinction between one combat round/chat exchange and one completed downtime Project/chat exchange; skipped fictional weeks entail legitimate Costs, world clocks and consequences.

## P2 — production readiness and maintenance

- [ ] **S. Campaign-schema migration:** replace d20 character sheet and per-skill XP ledger with Geard tracks, rated traits, project progress, active effects, Tiers and perk inventory; pin **both Elf-Books rules SHA and imported Geard upstream SHA**. Old d20 saves require explicit opt-in conversion and may otherwise remain on old archive rules.
- [ ] **T. GM engine integration:** deterministic record of real d10 faces, Accuracy and Effect rolls, static opposition, rolled Cost and resource marks, project credit, real game time, private clocks and atomic saves. Explain unresolved/missing features instead of inventing rulings.
- [ ] **U. Security/publication:** Geard upstream repo is private; only deliberately player-facing tiddlers are copied here. Audit for leaking GM-only/AI-only material. GM secrets of an individual solo campaign live in a separate controlled store, never public Elf-Books.
- [ ] **V. Legal/provenance:** document Geard Lif source/ownership (no blanket license or redistribution implied), update D20 SRD attribution as historical only, and continue complying with TES fan-work boundaries.
- [ ] **W. Regression and playtesting:** automated unit tests for bounded pools/Tier/graded mark promotion/recovery, skill/AP/perk updates, solo 4-scene sample runs; evaluate peer vs overwhelming enemies and low/high resource Cost cases.
- [ ] **X. Upstream sync policy:** Geard Lif stays mechanically authoritative, Elf-Books carries a **versioned local snapshot**. Follow upstream updates through reviewed PRs, never live pull changes mid-session or create divergent undocumented engine forks.

## Carry-over inventory (what does *not* directly port)

| Earlier D20 work | New status |
| --- | --- |
| 5× current 0–100 rank XP, and 2/4× HP/MP conversion | **Archive** as formulas; retain learning-by-doing intent |
| d20 + skill/5 to attack and flat damage | **Archive**; reconsider as Accuracy vs Potence trait investments |
| AC = gear + one defense skill and attributes, no +10 | **Archive**; redesign static Avoidance and equipment effects |
| 3.5 check total × DC crafting progress | **Archive**; Geard universal Projects take Complexity/Recalcitrance/Scope/Time instead |
| Natural 20 / enemy natural 1 grants shared perk point | **Archive triggers**; keep bankable one-point breakthroughs, trainer exclusion and unique-artifact exceptions as goals |
| TES skills, perk names/themes, era lore, GM secrets model | **Keep as content**; re-author their mechanics |
| Skyrim potion, enchanting, smithing and quest references | **Keep conceptually**, subject to actual supplied lore/source |
| D20 reference math scripts and tests | **Archive branch only**; new engine test suite takes over |

## Definition of parity

We're back at approximately the previous design milestone when **all P0 entries** are decided and executable as design/test play, and the P1 skill/perk source maps are as complete as the archived 24-skill/75-perk surveys. That does **not** mean the complete game is yet ready for actual persistent solo campaigns: P2 activation gates still apply.
