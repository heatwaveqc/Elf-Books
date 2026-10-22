# Perks — Elder Scrolls breakthrough and qualification rules

**Status:** The **bankable perk point**, **double-10 and double-1 confirmations**, **0–100 composite qualification**, and **no starting-Talent perk tree** rules below are ADOPTED. The [75 TES perk inspirations](../design/tes_perk_seeds.json) remain *content seeds*, not a completed list of purchasable Geard Lif perks. Their individual effects, costs, extra prerequisites, action timing and specific allowed Specialties still need conversion and tests.

## Perk-point economy

- **One shared bank of character perk points.** Points earned from genuine offensive/active breakthroughs and genuine hostile defense breakthroughs may be saved and spent on any eligible skill perk; **no per-Skill or initial-Talent bank**. One point buys one ordinary perk or one explicitly priced perk rank by default, pending individually authored prerequisites and rank/cost exceptions.
- **No maximum points per roll**: a remarkable roll can earn multiple bankable points. Rapid advancement is intentional.
- Normal Skill/Attribute/Talent/Specialty practice XP and perk points remain **separate ledgers**, with no conversion assumed. Trainers teach traits; they do not normally grant points or perks. Explicit artifact, revelation, or story rewards may grant exceptional points/perks.
- A perk belongs to its relevant **Skill**, independently of which five Skills the character's initial Talent governs. Anybody meeting the actual purchase prerequisites may buy it.

## Starting Talent is not a perk tree

A character's **single starting five-skill Talent** contributes its rating to dice pools and relevant perk prerequisites and advances as an ordinary rated trait. **It has no ordinary Talent perk tree or personal nodes.** The 12 sample Talents and any custom five-skill Talent are still legitimate; there is no need to design a unique set of perks for each.

**Vampirism, lycanthropy and potentially other acquired supernatural Talents** are separate future systems with **their own optional perk trees** and specific requirements. They do not consume or replace the character's starting five-skill Talent merely by being acquired. Their particular dice bonuses, interaction with the single applicable Talent on ordinary rolls, progression and condition-specific perk effects remain **OPEN**; do not silently allow two Talent bonuses on one Skill roll.

## Skyrim-style 0–100 perk qualifications

Every ordinary Skill perk definition specifies a **required Attribute**, **required Skill**, **acceptable Specialty or group of Specialties**, and **minimum combined rating** from 0 to 100. Use the character's *actual 0–25 ratings*, **not** dice-equivalent values, skill-game rank, or equipment contributions:

`qualification = named Attribute rating + starting Talent rating (only if it governs this Skill) + Skill rating + one eligible Specialty rating`

- Choose **at most one** Specialty accepted by this perk. If none is eligible, the Specialty contribution is 0. When multiple listed Specialties qualify, use the best single rating, **never their sum**. A perk can specify an empty allowed-Specialty group if appropriate.
- The Talent is 0 for any Skill **outside** the starting five, regardless of how high the Talent is. Its bonus is never universal to all Skills. **Equipment, temporary magic and other external bonus dice cannot satisfy a perk rating prerequisite.**
- The perk's **named Attribute is mandatory**; do not substitute whichever Attribute happens to govern the last action. The eligible Specialty set must be recorded in that perk's definition, and can include several weapon types, schools or practices where thematically sensible.
- **Maximum Attribute + Skill without either Talent or Specialty = 50.** To reach **51–75**, Talent *or* a qualifying Specialty is necessary; above **75**, **both** are mandatory. **100** requires all four relevant ratings at 25. Not being in a Skill's starting-Talent package does not bar its perks below or at 75.
- The combined threshold is a **purchase prerequisite**, not a substitute for any additional explicit predecessor perk, special ability, story or tool prerequisite an individual perk may have. The catalog conversion will define those separately. Multi-effect spell creation's perk is already a required **design permission**, but its attribute, accepted Specialties and minimum rating still need their individual definition.
- Above Tier 0, do not sum Trait ratings from *different Tiers* into a fictitious 100+ rating. Which higher-Tier qualification to evaluate is left to the individual later-Tier perk definition; initial 0–100 thresholds use the relevant character's Tier-0 ratings.

## Confirmed natural 10 — acting character

For **each original natural 10 on a character's actually rolled, eligible personal Attribute, Talent, Skill or Specialty d10** in a consequential action:

1. Record the die's original face and personal source.
2. **Reroll it once** as a *confirmation die*, separately from the original action.
3. Each confirmation face that is **also 10** awards the **acting character one bankable perk point**.
4. No cap per roll; a 10 followed by anything else awards no perk point.

Confirmation dice **do not** count toward Accuracy, Potence, Costs, ordinary use XP, natural-10 learning bootstrap, or a new confirmation. The original 10 still has its normal two successes and XP. Do not reroll a reroll.

## Confirmed natural 1 — attacked character

For **each original natural 1 in the attacker's actually rolled, eligible personal Attribute, Talent, Skill or Specialty d10** in a genuine consequential hostile action directed at a defender:

1. Identify the **genuinely targeted defender** for that attack event; this does **not** require fabricating a defender's normal static Avoidance roll. A legal target can still gain the opportunity if the attacker misses.
2. For each eligible **attacker personal die showing 1**, **the defender rolls a separate d10 confirmation**.
3. **Every resulting confirmation 1** gives **that defender one bankable perk point**, including multiple confirmations in a single attack.
4. This roll does **not** change the attack's actual success, its harm or its defending reactions, and gives no separate XP or chain of confirmations.

The eligible first roll is **the attacker's**, never phantom dice from the defender's static defense. Apply only to actually rolled attack-related dice: Accuracy when it is rolled, and Potence when the attack's rules legitimately roll Potence. Self-targeted spell Mana Costs, the attacker's private non-hostile practice rolls, and made-up extra rolls do not give other characters defensive points. An event must not be replayed to farm points. Multi-target/area allocation cannot replicate the *same* original 1 once for every bystander; the exact shared-roll allocation method is **OPEN** until attack modes specify it.

## Personal dice only — equipment deed enchantments later

**Only actual dice originating from the four character-trait sources can generate *character perk points* with double 10 or double 1.** Equipment, magical items and other external bonus dice may still legitimately affect the action; their original faces are recorded and resolved normally, but **their 10s/1s are excluded from both perk-confirmation pools**.

In particular, original equipment 10s **may someday generate deed enchantments or other equipment achievements**, using a separate item-focused system. **IDEA ONLY — NOT YET IMPLEMENTED:** a gear 10 confirmed by another 10 could unlock a deed enchantment on that item. It does **not** currently create either a character perk point or a functioning item ability. Equipment 10s may still count toward **existing natural-10 Skill/Specialty bootstrap XP** under [Advancement](ADVANCEMENT.md); excluding equipment from *perk points* does **not** silently change that separate learning rule.

## Event integrity and probabilities

- The **same consequential action**, original source-tagged faces, one-shot confirmation faces, acting recipient, threatened defender (when applicable), awarded points and event ID must be recorded, so reprocessing cannot award a second time. Use one fixed pre-roll ratings snapshot. Confirmations never become source-tagged training rolls themselves.
- Each **eligible personal original d10** has probability `(1/10) × (1/10) = 1%` of generating an actor point through **10 then 10**. For a genuinely threatened target, the same original die has a separate **1%** chance of giving the defender a point through **1 then 1**. One die cannot be both an original 10 and an original 1; checks are otherwise independent across dice.
- For `n` actually rolled eligible personal dice, **expected perk points to one recipient = 0.01n**, and the chance of at least one confirmation is `1-(0.99)^n`. Approximate probabilities: 5d **4.90%**, 10d **9.56%**, 20d **18.21%**, 40d **33.10%**. Quick progression is an accepted feature, not a reason to impose a hidden per-roll cap.
- Genuine stakes still matter: no counterfeit attacks, collaborative farming loops, manufactured research rolls or infinitely repeating inconsequential checks. A defender's **passive XP from chosen defenses** remains governed by [Advancement](ADVANCEMENT.md), separate from a successful double-1 confirmation.

**Executable reference:** [scripts/perks.py](../scripts/perks.py) and [tests/test_perks.py](../tests/test_perks.py), including strict one-reroll-per-eligible-face count validation. The caller is responsible for eligibility, correct event/target identity, action sequencing and persistent point banking.

## Porting the Elder Scrolls perk catalog

The [75-entry source survey](../design/tes_perk_seeds.json) preserves lore and thematic names like Quiet Casting, Arcane Blacksmith, Extra Effect, Green Thumb, Wax Key, and Poisoned. **The original game's numeric skill gate can be translated into a minimum combined 0–100 requirement**, after choosing the correct Attribute and acceptable Specialties; it is **not** a gate on Skill alone. Author the actual Geard Lif effect, action/time, resource Cost, prerequisite choices, rank prices and tests before marking that perk purchasable. Geard's Fatigue is available for TES Stamina-inspired effects.

Archived D20 critical rules, direct HP/MP bonuses and old fixed perk gate implementations remain historical material only.

## First implemented combat-perk effects

**Effect-ready, purchase-gate-pending:** [Power Bash, Deflect Arrows and Dual Flurry](../design/COMBAT_PERK_PILOTS.md) now have explicit Geard Lif attack/defense/Cost behavior and executable [effect-plan helpers](../scripts/combat_perks.py). These three are **not freely purchasable yet**, because each still requires an authored named prerequisite Attribute, accepted Specialty group and minimum 0–100 threshold. Effects are available for explicit GM-adjudicated tests without inventing those purchase gates.

- **Power Bash:** choose up to **Strength dice** of extra muscle-powered weapon/shield bash Damage Potence, with **two extra Fatigue hazard dice per additional Damage die**, charged on the attempted attack even if it misses. Strength means the current-Tier die-equivalent rating (`floor(rating/5)` under Elf Books), **not** the raw 0–25 rating. The extra technique dice are separately tagged as perk-derived, never as gear or an Attribute/Skill source for breakthrough perks.
- **Deflect Arrows:** owning the perk lets a character **Parry an arrow** with a suitable real weapon Parry mode, paying the **ordinary 1 defensive action** and **normal weapon Parry Fatigue Cost**. This changes response legality, not the baseline default for other projectiles or direct attacks.
- **Dual Flurry:** when wielding **two ready usable melee weapons**, a single attack action delivers **two independently rolled actual strikes**, each with its normal Fatigue hazard incident, even on a miss. Three committed attack actions can therefore make **six strikes**, with accumulating fatigue and ordinary fast→slow overflow.

**Arcane Blacksmith remains deferred until enchanting mechanics exist.** Quiet Casting, Extra Effect and Green Thumb are ready for separate focused effect drafting, not presumed silently implemented by this pilot.

## Complete proposed perk catalogue

A [non-operative, 80-entry design draft](../design/PERK_CATALOG_DRAFT.md) covers all 75 source inspirations plus Finesse, Light Footed, Shield Reflex, Flowing Parry, and Spell Synthesis. The [structured draft](../design/PERK_CATALOG_DRAFT.json) specifies proposed Attribute, Skill, acceptable Specialties, combined rating requirement, effect, and supporting-system blockers for each entry. These proposals are for review and do not authorize purchase or use. The previously adopted effects for Power Bash, Deflect Arrows, and Dual Flurry remain unchanged.
