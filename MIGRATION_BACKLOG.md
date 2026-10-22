# Geard Lif migration backlog — Elf-Books return-to-parity audit

**Scope:** Move Elf-Books from the archived D20 prototype to a local, pinned snapshot of Geard Lif / Raven's Heart core. **This checklist is the authoritative gap list.** It distinguishes genuine Geard Lif upstream gaps from Elder Scrolls-specific conversion and the existing solo GM infrastructure. No check below is implied completed merely by the import.

**Old D20 baseline:** [archive/d20-pre-geard-lif](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif) at `f5b31ccbed44ba4767d86f7098e3ddfdb7ee5956`. The historical calculations and 24-skill/perk design drafts remain accessible there. **Upstream snapshot:** [engine/geard-lif](engine/geard-lif/README.md).

## Already migrated / preserved

- [x] **Old D20 version recoverable:** separate immutable-by-policy archive branch, no fork or history rewrite.
- [x] **Local Geard Lif core:** eight source player-audience rule tiddlers, pinned upstream SHA, import/provenance policy and locked/provisional status summary.
- [x] **Core arithmetic reference:** tentative d10 success counting and Tier conversion, *meet-to-beat* Accuracy, shared graded severity/promotion/recovery, Project Scope-as-marks completion and adjustable injury thresholds. No obsolete D20-like progress pool.
- [x] **Elder Scrolls scope/lore:** era, region, canon divergence, provenance, and per-campaign private world facts preserved.
- [x] **Independent solo campaign concept:** GM preflight, antagonists/clocks, private saves and event logs retained as requirements, but character/runtime mapping requires implementation.
- [x] **24 skill names and 75 TES perk inspirations:** preserve as *content* and provenance without treating obsolete 0–100 gates as Geard Lif mechanics.

## P0 — before even a reliable four-scene vertical slice

- [x] **A. Meet-it-to-beat-it resolution (UPSTREAM):** Accuracy successes **>=** Complexity/Avoidance hit/apply. Only then roll independent Potence. On positive Potence, inflict Minor below effective threshold R, Middling at R, Major at 2R, Final at 3R, and multiple Final marks at successive multiples. Zero successes yield no mark. Excess Accuracy does not amplify Potence without an explicit bridge.
- [x] **A2. Universal essence-ping progress (UPSTREAM + ADAPTER):** **four grades of marks for everyone and everything**. Project **Scope** is slots per grade and **Recalcitrance** controls the grade threshold; final exhaustion completes the Project. Personal **Resilience** is slots per grade and baseline grade threshold; armor/wards can adjust the injury threshold but **not slot count**. Promotion follows the resource-mark engine, not a separate numeric Scope point pool.
- [ ] **A3. Edge/adjudication integration:** define zero Recalcitrance behavior; exact protective-equipment injury threshold formula; project setbacks/repair, partial group work and how interim graded project progress changes a real situation. These are not unresolved core resolution mechanics.
- [x] **B1. Trait architecture (UPSTREAM + ADAPTER):** **12 independent attributes** (four roles each in Body/Mind/Soul), one named Talent governing **exactly five** chosen skills with its own separate progression tree, a 24-skill TES roster, and narrower per-skill Specialties. One Talent provides bonus dice only to governed skills; every other skill is usable/trainable. Includes 12 preset Talent samples, freely named five-skill custom packages, local d10 pool validator/tests.
- [x] **B2a. Rating/starting minimums (UPSTREAM + ADAPTER):** working **0–25** integer ratings, one die per five levels, all twelve starting Attributes >=5; exactly five Talent-governed starting Skills each >=5, other Skills and Specialties may start at zero.
- [x] **B2b. Tier prerequisites and cascade:** tier-by-tier 0–25 ratings, next Tier requires previous at 25; Attribute≥1 same-Tier die to use Skill, Skill≥1 same-Tier die to use Specialty, *without rating caps*, Talent exempt. XP costs/awards ×5^Tier. Maxed source raw XP banks for up-tier or cascades Talent→Attribute→Skill→Specialty without re-multiplication.
- [ ] **B2c. Remaining trait economics:** **total creation budget**, Talent starting rating, equipment/teamwork dice, rounding fractional static Avoidance, legal Cost/defensive trait contributors, applicable-Attribute selection, Talent-tree nodes/branch rules and equivalent custom trees.
- [ ] **C. First-tier survivability (UPSTREAM):** validate Injury, Fatigue, Attention and Mana tracks, recovery cadence, Costs, peer-level threat odds and solo PC survival; choose starting Resilience capacity and initial gear. No numeric HP/MP pool assumed.
- [ ] **D. Combat adapter (ADAPTER):** one attack as a Project; static Avoidance, armor and shield effects, Block/Dodge legal action cost and reactive options, natural defenses, damage-to-mark handling and applied attack resolution. Decide where spells/armor intervene, including magical wards and Oakflesh.
- [ ] **E. Magic bridge (UPSTREAM + ADAPTER):** **casting school/Attribute mapping and static Cost resistance now specified**; implement the adopted shared-Potence/Cost procedure and calibrated fixed parameter surcharges; duration/concentration, summoning limitations, and protection on Injury remain open. Do not use the D20 spell-slot/DC system.
- [x] **F1. Active XP math (UPSTREAM + ADAPTER):** next one-point rating costs **10×max(1,current rating)** XP. Each source die earns per-success XP: Attribute **2**, Talent **1**, Skill **5**, Specialty **10**. A natural 10 additionally bootstraps both a used Skill and declared Specialty if each is under rating 5, each receiving one source-multiplied surrogate learning success. Keep source-tagged rolls and overflow; tested.
- [x] **F2a. Passive XP formula:** for a credible selected defense or real resource-Cost resistance, award each *actually participating trait* **ceil(rating/10) whole XP at Tier 0**, and exactly rating/10 ×5^Tier for Tier 1+; static Avoidance is floored after halving total dice. Test Health on Fatigue, Will/Talent/School/Specialty on Mana, and Conviction on Soul/Attention or Plasticity resistance.
- [x] **F2b. Defensive rounding:** static opposition = **floor(total qualifying source dice / 2)**. Passive XP = **ceil(rating/10)** for each Tier-0 contributor; Tier 1+ remains exact rating/10 ×5^Tier, retaining half-XP fractions in the ledger.
- [x] **F2c. Common Magicka self-Cost package (ADAPTER):** final spell Cost magnitude is the shared Potence successes plus fixed spell surcharges (no independent spell Cost roll); static resistance uses **Will + applicable Talent + the spell's School Skill + declared Spell Specialty + eligible cost-reducing gear**; **Will determines Mana/Spirit mark capacity on Mind**, while Conviction sets Soul/Plasticity/Attention capacities. Default counterspell chooses **Wits + Mysticism** as alternative Avoidance. Exact gear values, reaction availability and Cost ratings still open.
- [ ] **F2d. Other passive integrations:** determine armor/ward/Block/parry trait packages, exact reaction economy and how extended real Project intervals are represented. Bankable perk points and Talent-tree rewards remain separate.
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

## Resource-aspect migration checkpoint

- [x] **Geard Lif / Elf-Books resource assignment:** Mind/Will → Spirit (slow), Mana (fast); Body/Health → Injury (slow), Fatigue (fast); Soul/Conviction → Plasticity (slow), Attention (fast). Both player rules and new-character schema agree.
- [x] **School-Talent-Specialty Cost mitigation:** static resistance now uses all applicable personal sources and legal gear, rounded down once; Cost dice unchanged. Tests include robe threshold and distinct Will capacity.
- [ ] **Historical private-save migration:** if any character from the former resource arrangement exists, move each track's marks with its name to the destination aspect and explicitly revalidate Resilience capacity. No automatic live save mutation.

## Named pools, defense modes and single gear cap

- [x] **Generic Geard Lif rule:** name Attribute + Skill; automatically add governing five-skill Talent and one applicable Specialty. Every contestable effect specifies attack mode and permitted named defensive pools.
- [x] **Elf-Books modes:** melee, arrows, ice spears, environmental cold, direct freezing Malediction, persuasion, deception, intimidation and reputation. Cold exposure and direct freezing curses both permit Health + Survival; projectiles permit Dodge/Block but not ordinary Parry. Four social defaults have explicit alternative pools.
- [x] **Aggregate external dice cap:** equipment, enchantments, ensorcellments and temporary magic buffs collectively grant no more dice than the unmodified personal dice pool at chosen Tier; tested for defenses and spell Cost/casting.
- [ ] **Detailed combat/social integration:** reaction timing, shield/weapon requirements, area/multitarget mechanics, reputation/crowd Projects and balancing exact bonus values.

## Fivefold Tier alignment and social restraint

- [x] Align Geard Lif **×5 Tier magnitude** with Elf-Books' **×5 Tier XP cost and award** calculators, cross-Tier success converter, source snapshots and tests. Base rank cost stays **10 × current rating**; only Tier exponent changes. Tier 1+ passive awards can be fractional halves, preserved in tenths.
- [x] Mundane social modes directly affect **Attention only** and must not name Plasticity as a direct or long-term mark track. Add supernatural identity Malediction as the legal direct Plasticity example. **Conviction is Soul soak/capacity, not social Avoidance.** Physical intimidation may use **Strength + Speechcraft** against composure/discernment defenses.
- [ ] Finalize special attack consent, social consequences, and the full supernatural identity spell's balancing and resistance conditions.

## Universal fast-resource exhaustion overflow

- [x] **Geard Lif:** an effect targeting an **already-exhausted** fast track reroutes wholly to the paired slow track, including Costs, environmental effects, attacks and social influence: **Fatigue→Injury, Mana→Spirit, Attention→Plasticity**. The incident which first exhausts fast does not split or add free slow marks; slow grade uses its own resistance threshold. Fast recovery reopens normal routing. Nonpersonal Projects unaffected.
- [x] **Elf-Books:** tested generic aspect-resource resolver, attack-mode effect adapter and spell Cost bridge preserving *both* Mana and Spirit track histories. Mundane social attacks still directly target Attention but can inflict Plasticity by exhaustion **overflow**, without claiming supernatural direct targeting.
- [ ] **Campaign save migration:** wire `requested_resource`, `applied_resource`, and redirect flags through actual persistent event records; no existing private play saves are automatically modified by this rules update.

## Spell construction and research (2026-10-21)

- [x] **Spell as Specialty:** One-hour Intelligence + School Skill study/invention with research Complexity 5; genuine rolls generate source XP and Specialty natural-ten bootstrap. Buying spell Specialty 1 unlocks casting, and known spells can be studied further. No design Scope or separate completion track.
- [x] **Shared Potence and Cost:** One Potence roll even after missed Accuracy; Cost = rolled successes + fixed parameter surcharges. Voluntary withholding of Potence dice is legal; no duplicate active XP. Standard static Mana resistance and overflow apply.
- [x] **Fixed spell design:** range, area, duration, multiple targets and multi-effects add cost-success equivalents, with efficiencies of scale; record in the learned formula, not chosen ad hoc at casting.
- [ ] **Calibrate spell parameters:** determine actual surcharge numbers/bands, sustained upkeep, combined effects, non-damage Potence translations and exceptional cross-school designs.

## Continuing damage and multi-effect updates (2026-10-21)

- [x] Remove **weight** from the spell parameter surcharge schedule. Lifting heavy masses uses Potence as work against a movement Project with its own Complexity/Recalcitrance/Scope/Time; spell research still has no Scope track.
- [x] Timed damaging spells may **apply recorded Potence each turn**. Damaging areas are **stationary** and avoidable by leaving; physical one-target afflictions (fire) specify a real removal action/condition; supernatural single-target curses require active resistance **before every damaging instance**. **First success destroys that curse permanently and prevents the current damage**; failure inflicts original Potence damage, and the curse persists until success, expiry, dispelling or death. Do not invent new caster Potence/XP/Mana rolls per tick.
- [x] **Multi-effect design perk** required to invent combined formulae. Each distinct component rolls Potence and resolves resistance **separately**, pays its own Potence-plus-fixed-surcharge Mana Cost **individually**, and trains its genuinely participating traits. Component sequencing can redirect later Cost to Spirit within the same spell; not a single shared Potence pool or combined Cost incident.
- [ ] Price and test [provisional parameter schedule](design/SPELL_PARAMETERS.md), especially very long recurring curses; determine tick timing, removal action standards, named defensive pools on repeat curses, and cross-School compound ownership. Perk identity/tree placement is not finalized.

## Explicit progression adapter split (2026-10-21)

- [x] **Core-versus-adapter intent recorded:** current base Geard Lif uses **0–5 ratings, one die per point, and Drive Marks**. Elf-Books deliberately retains its **0–25 ratings, floor(rating/5) dice, source-tagged XP-per-use, natural-ten bootstrapping, passive XP, XP cascade and Tier×5 XP scaling**, inspired by Elder Scrolls practice-based advancement.
- [x] **Pinned historical snapshot retained:** keep the existing reviewed, player-facing source import SHA unchanged; do **not** pass off its historic 0–25 source pages as current upstream Geard rules or auto-reimport updated base progression in a future sync.
- [ ] **Future selective core sync:** review current Geard shared rules (especially six-second three-action combat, turn-start fast recovery, and construction) separately, preserving the Elf-Books progression adapter and its tests. This is not a silent numeric migration.

## Conditional Application and restorative/protective effects (2026-10-21)

- [x] **Conditional spell Application:** No third universal casting roll. Willing accessible Healing/Oakflesh can omit Perception + School Accuracy; opposed recipients use normal magical Application against an explicitly legal named defense. Cast Potence and Mana Cost still occur, including on a missed Application.
- [x] **Healing as inverse Injury:** classify Restoration healing Potence by patient **base Health Resilience/Recalcitrance**, with ordinary Minor/Middling/Major/Final grade thresholds. High-Health subjects require more Potence for the same grade. Treat a successfully applied result as restorative work, not injury. Pure classifier tested.
- [ ] **Healing mark inversion:** define exactly which Injury marks are removed/de-promoted for each healing grade, how mixed-grade wounds are handled, how other resources are restored and whether fully exhausted Injury can be recovered; no actual Injury-state mutation coded before this is agreed.
- [x] **Oakflesh:** rolled Potence is a **flat equipment-equivalent bonus to effective Injury Resistance threshold**, keeping Health-derived slots/capacity unchanged; simple arithmetic and applied-severity tests added.
- [ ] **Armor/protection stacking:** determine interactions between armor, multiple flesh spells, equipment-derived flat threshold bonuses, external-dice caps, and Tier; leave current simple single-Oakflesh example as the only implemented threshold adapter.
- [ ] **Summoning and autonomous effects**: defer complexity to later spell-effect work.
