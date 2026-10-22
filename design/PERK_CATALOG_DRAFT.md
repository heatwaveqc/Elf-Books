# Full Elder Scrolls perk catalogue — playtest draft

> **NON-OPERATIVE PROPOSAL.** This catalogue exists to test the shape of the perk system. The adopted [point economy and composite prerequisites](../rules/PERKS.md) remain authoritative. The three previously adopted combat-perk **effects** are preserved; **all proposed purchase thresholds, accepted Specialty lists and the other 77 effects need review before purchase is enabled**. In particular, entries labeled *Needs supporting subsystem* are not playable just because they have text.

## Rules of interpretation

**Purchase:** One bankable perk point per entry or separately purchased named rank is the baseline **proposal**, not a new final cost policy. Perks remain available outside the character's chosen starting Talent.

**Qualification:** Every entry supplies its own Attribute, Skill, accepted Specialty candidates, and 0–100 requirement. Add the actual **0–25 Attribute + 0–25 Skill + one actually held, accepted Specialty (max 25) + 0–25 starting Talent only when it governs that Skill**. Never add equipment dice or multiple Specialties. The listed Attribute is a purchasing prerequisite; a perk's *actual action* may use a different Attribute if expressly stated. Above 75 requires a Skill governed by the character's starting Talent **and** an applicable Specialty. The Specialty IDs below are **proposed vocabulary**; they have not been adopted as a global specialty registry. Read each set as alternatives, not a requirement to buy them all.

**Once per round:** A per-round use resets when the round's three-action budgets refresh, not once per attack or every six-second real-time interval an individual character spends talking. An extra *reaction* waives only its normal **action cost**; all physical/legal defenses, fatigue hazards, source pools and deadlines still apply. One incoming attack gets only one chosen defense, even if multiple free-response perks have been acquired.

**Technique dice and Accuracy margin:** Where a perk adds *technique dice*, **roll them as real additional Effect/Application dice**. These dice are attributed to the perk, not falsely to Attribute/Talent/Skill/Specialty or equipment for XP, character perk confirmations, or deed enchantments. **Finesse grants one additional Potence d10 for each surplus Accuracy success above static opposition**; the resulting faces are rolled and counted normally (1–6 = 0 successes, 7–9 = 1, 10 = 2). It is **not** a flat increase in successes. Its extra dice do not add to the attack's ordinary Fatigue hazard. The final Effect still faces the ordinary resource threshold. Costs and natural recovery remain unchanged.

**Conditional mechanics:** Describing a desired end state is not authorization to invent unsolved summoning, stagger, crafting, poison, enchanting, tracking, economics or random loot rules. Such perks are labeled *Needs supporting subsystem* with the exact dependency.

**Source provenance:** This is a mechanical adaptation of the repository's [75 inspiration entries](tes_perk_seeds.json), not copied official rulebook text. Ten unclear/placeholder labels are replaced by purposeful draft names. Survival and Lore receive original proposed perks because the Skyrim-inspired survey supplied no actual tree. An additional **Spell Synthesis** perk names the already-adopted permission to *design* multi-effect spells; it is **distinct** from Enchanting's **Extra Effect** (two item enchantments), which waits for enchanting.

## High-priority demonstrations

### Finesse — surplus Accuracy grants real Potence dice

After a legal One-Handed Accuracy roll successfully meets the opponent's static Avoidance, calculate **surplus Accuracy successes** as `max(0, rolled Accuracy successes − actual static Avoidance)`. **Add that many new d10 to the normal damage Potence pool, roll them, and count their actual successes.** These are perk-sourced dice, not guaranteed successes.

**Example:** One-Handed Accuracy rolls **8 successes** against static Dodge **3**, for **five surplus successes**. Finesse therefore grants **5d10** to the damage Potence roll, not +5 automatic Potence successes. Suppose the ordinary Potence dice generate **4 successes** and the five Finesse dice show **2, 7, 10, 4, 8**, contributing **0 + 1 + 2 + 0 + 1 = 4** additional successes. **Final damage Potence is 8**, determined by the actual dice. Those same five dice could contribute anything from **0 through 10** successes; with this d10 system their average is **2.5**. At equal Accuracy and Avoidance there are no bonus dice, and a failed Application does not create an Effect.

Bonus Finesse dice are not ordinary Attribute/Talent/Skill/Specialty dice for learning XP or double-10 perk points; they are not weapon equipment dice for deed enchantments either. **They do not raise the self-Fatigue hazard** or create extra attack actions. High Accuracy margins still add many real dice, making this worth a focused balance test against undefended targets. The exact number of Finesse dice should be recorded with the Potence roll for replay.

### Free defense family

**Light Footed** (Dodge), **Shield Reflex** (Block), **Flowing Parry** (One-Handed Parry) each allow **one legally available reaction of that exact method per round without paying an action**. The reaction still consumes its ordinary **Fatigue hazard**: Dodge `2× worn armor Encumbrance`, Block/Parry `max(0, defending item's Damage, defending item's Defense)`. They do **not** turn static defenses into actual defense rolls. A character with all three perks could obtain one free reaction from each on **different incoming attacks**, but cannot stack several defenses onto the same attack. These special responses can be used after all three standard actions have been committed, provided the character remains conscious/aware and the defense is genuinely feasible.

### Power Bash and Dual Flurry

Power Bash adds up to **Strength DICE** to bash damage with **+2d Fatigue hazard per added damage die**, in addition to the weapon mode's normal hazard and charged even on a miss. For Strength 20, adding 4d costs **8d additional hazard**; a base Damage 2/hazard 2 bash now has +6 weapon-plus-technique Damage and a **10d total Fatigue hazard**.

Dual Flurry retains **one action for two independent actual attacks**, each with its own accuracy/effect and a separate attempted-attack Fatigue Cost. Three committed attack actions can produce six strikes. The next strike sees the previous strike's Fatigue/injury penalties and possible Fatigue→Injury overflow.

### Two different "Extra Effect" concepts

**Spell Synthesis** (Mysticism, Intelligence, proposed 75) authorizes *design* of multi-component spell formulas. Each component retains its own Potence, defense and Mana Cost, with the existing +1 surcharge for each component beyond the first; ordinary casters may still learn and cast a finished formula.

**Extra Effect** (Enchanting, Intelligence, proposed 100) authorizes two item enchantments on one item. It remains **unimplemented** until enchanting itself exists. They are intentionally not the same perk.

## Perks by Skill

### One-Handed (6)

#### Critical Charge

- **Proposed requirement:** **50/100**, **Strength + One-Handed**, with one of: Swords, Axes, Maces. **Cost:** 1 bankable perk point (draft).
- **Effect:** After spending a movement action to enter melee with a previously out-of-reach target, your first One-Handed hit this turn gets +2 technique Damage dice. The attack's normal melee Fatigue hazard increases by 2d even if it misses; the movement still costs its own action.
- **Readiness:** Draft effect; candidate mechanics.

#### Dual Flurry

- **Proposed requirement:** **30/100**, **Dexterity + One-Handed**, with one of: Dual Wielding, Swords, Axes, Daggers. **Cost:** 1 bankable perk point (draft).
- **Effect:** With two ready melee weapons, one attack action makes two full separate strikes, one with each weapon. Resolve each Accuracy, Potence, and normal Fatigue Cost separately; accumulated fatigue affects later strikes.
- **Readiness:** Adopted effect; proposed purchase gate. Effects match the existing adopted combat pilot; this draft adds only proposed purchase gates.

#### Hack and Slash

- **Proposed requirement:** **30/100**, **Strength + One-Handed**, with one of: Axes, Hatchets. **Cost:** 1 bankable perk point (draft).
- **Effect:** An Injury-causing axe hit may leave a bleeding wound. At the injured subject's subsequent turns a bleeding incident inflicts a Minor Injury unless a successful wound-care action staunches it; no stacking multiple bleeds on the same wound.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Bleeding timing, wound-care complexity and which injuries can bleed.

#### Armsman

- **Proposed requirement:** **0/100**, **Strength + One-Handed**, with one of: Swords, Axes, Maces, Daggers. **Cost:** 1 bankable perk point (draft).
- **Effect:** For a successful muscle-powered One-Handed attack, add 1 perk-technique die to Potence. The attack's Fatigue hazard rises by 1d, whether it hits or misses; this is not an increase to the weapon's permanent Damage rating.
- **Readiness:** Draft effect; candidate mechanics.

#### Finesse

- **Proposed requirement:** **70/100**, **Dexterity + One-Handed**, with one of: Swords, Daggers, Precise Striking. **Cost:** 1 bankable perk point (draft).
- **Effect:** On a successfully applied muscle-powered One-Handed Injury/Fatigue attack, each rolled Accuracy success ABOVE the target's actual static Avoidance provides ONE ADDITIONAL d10 to the attack's damage Potence roll. Roll those dice normally (1–6 gives 0 successes, 7–9 gives 1, 10 gives 2) and combine their actual successes with the regular Potence roll before grading harm. The added dice are perk-derived, not Attribute/Talent/Skill/Specialty or equipment dice for XP, character perk confirmations, or future gear deeds. They do not increase the attack's self-Fatigue hazard. Equal Accuracy versus Avoidance gives no extra dice, and a miss has no Potence effect.
- **Readiness:** New proposal.

#### Flowing Parry

- **Proposed requirement:** **60/100**, **Dexterity + One-Handed**, with one of: Swords, Daggers, Weapon Parries. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per six-second round, make ONE otherwise legal One-Handed weapon Parry reaction without spending an ordinary action. It still requires a parry-capable ready weapon and pays the normal weapon Parry Fatigue hazard; arrows still require Deflect Arrows.
- **Readiness:** New proposal.

### Two-Handed (3)

#### Sweep

- **Proposed requirement:** **70/100**, **Strength + Two-Handed**, with one of: Greatswords, Battleaxes, Warhammers, Polearms. **Cost:** 1 bankable perk point (draft).
- **Effect:** When two enemies are within the same plausible sweep arc, spend one attack action to attempt a separate Two-Handed Accuracy and Potence against each. Roll and pay a separate normal Fatigue hazard per attempted strike; movement or positioning must actually permit the arc.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Adjacent-target geometry and multi-target attack timing.

#### Great Critical Charge

- **Proposed requirement:** **50/100**, **Strength + Two-Handed**, with one of: Greatswords, Battleaxes, Warhammers. **Cost:** 1 bankable perk point (draft).
- **Effect:** After spending a movement action to enter melee with a previously out-of-reach enemy, your next Two-Handed strike this turn adds 3 technique Damage dice. It also adds 3d to its normal attempted-attack Fatigue hazard.
- **Readiness:** Draft effect; candidate mechanics.

#### Barbarian

- **Proposed requirement:** **0/100**, **Strength + Two-Handed**, with one of: Greatswords, Battleaxes, Warhammers, Polearms. **Cost:** 1 bankable perk point (draft).
- **Effect:** Add 1 perk-technique Damage die to each muscle-powered Two-Handed attack. Add 1d to that attack's ordinary Fatigue hazard, including on a miss.
- **Readiness:** Draft effect; candidate mechanics.

### Archery (4)

#### Hunter's Discipline

- **Proposed requirement:** **50/100**, **Perception + Archery**, with one of: Bows, Crossbows, Field Archery. **Cost:** 1 bankable perk point (draft).
- **Effect:** After combat, recover twice as many of the arrows that were actually fired and remain physically retrievable, subject to the actual number of recoverable arrows. Does not create missing or destroyed ammunition.
- **Readiness:** Draft effect; candidate mechanics.

#### Ranger

- **Proposed requirement:** **60/100**, **Agility + Archery**, with one of: Bows, Mounted Archery. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may take one ordinary movement action without losing a previously prepared bow shot or interrupting an already established aim. Movement and attack still require their normal separate actions, and range still matters.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Ready and Aim state model.

#### Power Shot

- **Proposed requirement:** **50/100**, **Strength + Archery**, with one of: Bows, Heavy Bows. **Cost:** 1 bankable perk point (draft).
- **Effect:** When an arrow inflicts a Major-or-worse Injury mark, its impact may stagger the target, costing one available action before its next turn. An exhausted target cannot lose extra actions; only one stagger from this perk per target per round.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Stagger timing and action loss.

#### Steady Hand

- **Proposed requirement:** **40/100**, **Perception + Archery**, with one of: Bows, Crossbows, Long Range Shooting. **Cost:** 1 bankable perk point (draft).
- **Effect:** Spend one action to aim at a visible target; the next Archery Accuracy roll before your next turn gets +2 perk-technique dice. Aim is lost on loss of target awareness or changing to a different target.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Aim action baseline and awareness interruption.

### Block (5)

#### Power Bash

- **Proposed requirement:** **30/100**, **Strength + Block**, with one of: Shields, Shield Bashing. **Cost:** 1 bankable perk point (draft).
- **Effect:** On a muscle-powered shield or weapon bash, choose 0 through your Strength dice as extra Damage dice. Each added Damage die adds TWO dice to the attack's normal Fatigue hazard; pay the hazard even if the attack misses.
- **Readiness:** Adopted effect; proposed purchase gate. Effects match the existing adopted combat pilot; this draft adds only proposed purchase gates.

#### Deflect Arrows

- **Proposed requirement:** **30/100**, **Dexterity + Block**, with one of: Shields, Weapon Parries, Projectile Defense. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may use a genuine weapon Parry against an incoming arrow; it remains a one-action defensive reaction with that weapon's ordinary Parry Fatigue Cost. It requires awareness and a parry-capable weapon; it does not cover bullets or magical spears.
- **Readiness:** Adopted effect; proposed purchase gate. Effects match the existing adopted combat pilot; this draft adds only proposed purchase gates.

#### Block Runner

- **Proposed requirement:** **70/100**, **Agility + Block**, with one of: Shields, Mobile Blocking. **Cost:** 1 bankable perk point (draft).
- **Effect:** During a movement action you may retain a prepared shield Block reaction against one incoming attack until your next turn. The actual Block still consumes its normal available reaction action and Fatigue hazard; no second Block is created.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Prepared defense and movement interruption.

#### Elemental Protection

- **Proposed requirement:** **50/100**, **Will + Block**, with one of: Shields, Elemental Guarding. **Cost:** 1 bankable perk point (draft).
- **Effect:** When you declare and pay an eligible shield Block against a traveling elemental projectile but its Accuracy still meets your Avoidance, add +2 to your effective Injury severity threshold against THAT attack's elemental Potence only. Does not apply to nontraveling Maledictions or ordinary weapon blows.
- **Readiness:** Draft effect; candidate mechanics.

#### Shield Reflex

- **Proposed requirement:** **60/100**, **Dexterity + Block**, with one of: Shields, Shield Guard, Projectile Defense. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per six-second round, make ONE otherwise legal Block reaction without spending an ordinary action. It still requires a suitable guarding implement and costs its usual Block Fatigue hazard; no free Block against modes that prohibit Block.
- **Readiness:** New proposal.

### Heavy Armor (4)

#### Conditioning

- **Proposed requirement:** **70/100**, **Health + Heavy Armor**, with one of: Plate, Mail, Armor Fit. **Cost:** 1 bankable perk point (draft).
- **Effect:** While wearing armor for which you have the matching Specialty, ignore its positive Encumbrance when calculating final Dodge and ordinary movement distance. Its Armor Rating and the item's underlying Encumbrance statistic do not change.
- **Readiness:** Draft effect; candidate mechanics.

#### Cushioned

- **Proposed requirement:** **50/100**, **Health + Heavy Armor**, with one of: Plate, Mail, Fall Protection. **Cost:** 1 bankable perk point (draft).
- **Effect:** While properly wearing heavy armor, halve the incoming falling-impact Effect magnitude, rounding down, before grading Injury. This does not help against drowning, crushing pressure, or falls the armor does not actually cushion.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Falling Effect magnitude rules.

#### Tower of Strength

- **Proposed requirement:** **50/100**, **Health + Heavy Armor**, with one of: Plate, Mail, Bracing. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per round while braced in heavy armor, ignore one action-loss/stagger condition caused by a hit or shove. You still take its graded resource harm and Fatigue Costs normally.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Stagger and bracing definition.

#### Juggernaut

- **Proposed requirement:** **0/100**, **Health + Heavy Armor**, with one of: Plate, Mail, Armor Fit. **Cost:** 1 bankable perk point (draft).
- **Effect:** While properly using a trained suit of heavy armor, add +1 to your effective Injury severity threshold against ordinary physical contact attacks, after applicable Armor Rating. Does not add mark slots or change the armor item's own rating.
- **Readiness:** Draft effect; candidate mechanics.

### Unarmed (2)

#### Ghost Strike

- **Proposed requirement:** **50/100**, **Will + Unarmed**, with one of: Spirit Striking, Unarmed Striking. **Cost:** 1 bankable perk point (draft).
- **Effect:** Your ordinary unarmed strikes may interact with an insubstantial or ghostly target you can perceive and physically reach, using normal attack and Injury rules. The perk does not itself grant supernatural perception or remove cross-Tier penalties.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Insubstantiality and supernatural targeting.

#### Disarming Strike

- **Proposed requirement:** **50/100**, **Dexterity + Unarmed**, with one of: Grappling, Unarmed Striking. **Cost:** 1 bankable perk point (draft).
- **Effect:** After successful unarmed Application, you may resolve the Effect as a disarming Project against the target's grip rather than inflicting Injury. Damage is forfeited for that strike; item security and remaining grip determine the Project's Recalcitrance and Scope.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Disarm Projects and resisting grip.

### Athletics (2)

#### Second Wind

- **Proposed requirement:** **100/100**, **Health + Athletics**, with one of: Sprinting, Endurance Running. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per round after you spend at least two movement actions sprinting, immediately take one extra ordinary Fatigue recovery step. This does not accelerate Injury or bypass pre-existing Fatigue-to-Injury overflow from earlier Cost incidents.
- **Readiness:** Draft effect; candidate mechanics.

#### Leaping Strike

- **Proposed requirement:** **25/100**, **Agility + Athletics**, with one of: Jumping, Acrobatics. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may make an ordinary attack while airborne during a jump without automatic positional penalty solely for being in the air. The jump or movement and the attack still consume their usual actions; landing and distance remain consequential.
- **Readiness:** Draft effect; candidate mechanics.

### Smithing (3)

#### Arcane Blacksmith

- **Proposed requirement:** **60/100**, **Intelligence + Smithing**, with one of: Tempering, Enchanted Items. **Cost:** 1 bankable perk point (draft).
- **Effect:** Permit tempering or repairing an enchanted weapon or suit of armor without automatically destroying or suppressing its enchantment. The crafting Project still requires appropriate tools, materials, Skill, and safe treatment of each magical layer.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Enchanting rules, modification Projects and enchantment stability.

#### Dwarven Smithing

- **Proposed requirement:** **30/100**, **Intelligence + Smithing**, with one of: Dwarven Metallurgy, Forging. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may undertake Smithing Projects to reproduce and repair documented Dwemer-metal equipment when suitable materials, drawings and tools exist. This grants recipe access, not free Dwarven ingots or automatic success.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Dwemer craft recipes and construction Projects.

#### Daedric Smithing

- **Proposed requirement:** **90/100**, **Intelligence + Smithing**, with one of: Daedric Metallurgy, Forging. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may undertake Daedric equipment Smithing Projects using the actual rare inputs and rituals required by the recipe. The perk allows this category of work; it does not conjure artifacts or ignore the Project's Tier.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Daedric materials, artifact constraints and recipes.

### Alteration (3)

#### Stability

- **Proposed requirement:** **70/100**, **Will + Alteration**, with one of: Flesh Magic, Alteration Duration, Wards. **Cost:** 1 bankable perk point (draft).
- **Effect:** When designing an Alteration formula with a duration, you may extend its maximum duration by ONE listed duration band without the additional +1 fixed Mana surcharge. All other parameters, Potence and Costs remain normal.
- **Readiness:** Draft effect; candidate mechanics.

#### Mage Armor

- **Proposed requirement:** **30/100**, **Health + Alteration**, with one of: Flesh Magic, Wards. **Cost:** 1 bankable perk point (draft).
- **Effect:** While not wearing protective armor, add +2 to the effective Injury resistance threshold granted by an already-active Flesh/Oakflesh spell. This does not increase Health or wound slots; the bonus disappears when wearing protective armor.
- **Readiness:** Draft effect; candidate mechanics.

#### Atronach

- **Proposed requirement:** **100/100**, **Will + Alteration**, with one of: Absorption, Wards, Alteration Defense. **Cost:** 1 bankable perk point (draft).
- **Effect:** When you successfully counter or absorb a hostile spell with a legal Alteration ward, you can redirect one restorative Minor mark to your Mana track rather than merely negating the spell. Each incoming spell can trigger at most one absorption.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Ward absorption and spell-energy transfer.

### Conjuration (5)

#### Summoner

- **Proposed requirement:** **30/100**, **Perception + Conjuration**, with one of: Summons, Daedra Summoning. **Cost:** 1 bankable perk point (draft).
- **Effect:** When designing a true creature-summoning formula, move its allowed casting range up one range band without adding the usual range surcharge. The summoned creature remains subject to its existing command, location, and lifetime restrictions.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Creature summoning Project/slot rules.

#### Atromancy

- **Proposed requirement:** **40/100**, **Intelligence + Conjuration**, with one of: Atronachs, Summons. **Cost:** 1 bankable perk point (draft).
- **Effect:** When designing an atronach-summoning formula, extend its maximum duration by one listed duration band without additional fixed Mana surcharge. Does not increase summon count or independently improve its stats.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Summon legality, duration and commands.

#### Soul Stealer

- **Proposed requirement:** **30/100**, **Will + Conjuration**, with one of: Bound Weapons, Soul Trapping. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may design a bound-weapon spell whose strike also carries a distinct Soul Trap component, paying its separate Potence and Mana Cost as any other compound effect. This ability does not capture souls without a valid receptacle and target.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Soul capture and compound spell design privilege.

#### Oblivion Binding

- **Proposed requirement:** **50/100**, **Will + Conjuration**, with one of: Banishment, Bound Weapons. **Cost:** 1 bankable perk point (draft).
- **Effect:** A successful bound-weapon contact can be resolved as a banishment/turning Project against a summoned or reanimated being instead of regular Injury. Its origin, actual Tier and binding set Recalcitrance and Scope; no automatic instant banishment.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Summon and banishment Projects.

#### Twin Souls

- **Proposed requirement:** **100/100**, **Will + Conjuration**, with one of: Summons, Necromancy, Atronachs. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may maintain two independently created permanent or timed summon bindings concurrently instead of the ordinary single controlled-summon allowance. Each summon is cast, paid for, controlled, and dispelled separately.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Baseline summon limits and control economy.

### Destruction (3)

#### Rune Master

- **Proposed requirement:** **40/100**, **Perception + Destruction**, with one of: Runes, Fire Runes, Frost Runes. **Cost:** 1 bankable perk point (draft).
- **Effect:** When placing a Destruction rune, choose the next greater published range band without paying its extra fixed range surcharge. The rune remains anchored and uses its originally designed area, duration and trigger.
- **Readiness:** Draft effect; candidate mechanics.

#### Impact

- **Proposed requirement:** **40/100**, **Strength + Destruction**, with one of: Force Magic, Shock Magic, Destruction Impact. **Cost:** 1 bankable perk point (draft).
- **Effect:** When a Destruction effect deals a Major-or-worse Injury mark through an actual traveling magical impact, the hit staggers its victim once per round, imposing loss of one available action. No free stagger from a direct nonimpact curse.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Stagger action timing and spell impact classes.

#### Intense Flames

- **Proposed requirement:** **50/100**, **Charisma + Destruction**, with one of: Fire Magic, Terror Flames. **Cost:** 1 bankable perk point (draft).
- **Effect:** When a fire spell actually inflicts Major-or-worse Injury, you may also threaten the target's Attention with a separate fear effect, using its own real Potence/Cost incident and legitimate Soul defense. No automatic supernatural Plasticity damage.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Fear attack mode and dual-effect access.

### Illusion (3)

#### Quiet Casting

- **Proposed requirement:** **50/100**, **Wits + Illusion**, with one of: Silent Spellcasting, Misdirection, Sound Magic. **Cost:** 1 bankable perk point (draft).
- **Effect:** Spells you cast produce no voluntary spoken invocation, vocalization, or ordinary audible casting cues from their casting process. The actual spell effect can still make noise, glow, burn, or reveal magical signatures; this does not grant invisibility.
- **Readiness:** Draft effect; candidate mechanics.

#### Master of the Mind

- **Proposed requirement:** **90/100**, **Insight + Illusion**, with one of: Mind Magic, Undead Illusion, Construct Illusion. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may attempt Illusion effects against undead, Daedra, or constructs with some cognition even when their type would normally exclude ordinary mind effects. Mindless targets remain mindless; resistance, immunity and actual Tier still apply.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Target cognition and mind-affecting immunities.

#### Animage

- **Proposed requirement:** **20/100**, **Insight + Illusion**, with one of: Animal Influence, Mind Magic, Beast Behavior. **Cost:** 1 bankable perk point (draft).
- **Effect:** When using Illusion to influence a genuine animal with a mind, add +2 perk-technique dice to Potence. Those bonus dice affect the spell's usual Potence-derived Mana Cost but are not personal trait dice for perk confirmations.
- **Readiness:** Draft effect; candidate mechanics.

### Mysticism (3)

#### Spell Analysis

- **Proposed requirement:** **25/100**, **Intelligence + Mysticism**, with one of: Spell Analysis, Arcane Lore, Detection. **Cost:** 1 bankable perk point (draft).
- **Effect:** After examining an ongoing spell or written formula with a legitimate Mysticism research attempt, you can identify its School and any observable range, duration, or area parameters on a successful Project. Secret designer details still require sufficient access/evidence.
- **Readiness:** Draft effect; candidate mechanics.

#### Aegis of Wards

- **Proposed requirement:** **60/100**, **Wits + Mysticism**, with one of: Counterspelling, Wards, Spell Absorption. **Cost:** 1 bankable perk point (draft).
- **Effect:** When making a real Wits + Mysticism counterspell defense, add +2 perk-technique dice before converting the pool to static Avoidance. This supplies no free reaction action, no automatic spell absorption, and no extra Mana slots.
- **Readiness:** Draft effect; candidate mechanics.

#### Spell Synthesis

- **Proposed requirement:** **75/100**, **Intelligence + Mysticism**, with one of: Formula Design, Spellcraft, Arcane Theory. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may DESIGN a compound spell formula containing two or more distinct effects. Each effect keeps its own separate Potence roll, lawful target resistance and Mana Cost incident, with +1 fixed surcharge on each additional component; other casters may learn and cast the finished formula without buying this design perk.
- **Readiness:** New proposal.

### Restoration (4)

#### Ward Absorb

- **Proposed requirement:** **60/100**, **Will + Restoration**, with one of: Wards, Spell Absorption. **Cost:** 1 bankable perk point (draft).
- **Effect:** If you successfully cancel a hostile spell with a legally available Restoration ward, restore one Minor Mana mark after the incident. The incoming spell's Damage and any cost to maintain the ward still resolve normally until canceled; never heal Spirit overflow automatically.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Restoration ward cancellation and resource ordering.

#### Necromage

- **Proposed requirement:** **70/100**, **Intelligence + Restoration**, with one of: Anti Undead, Restoration Healing, Holy Wards. **Cost:** 1 bankable perk point (draft).
- **Effect:** Against a genuinely undead subject, add +2 perk-technique dice to eligible Restoration Potence for healing, warding or turning effects when their target rules permit it. Added Potence modifies ordinary spell Mana Cost; do not assume all undead can be healed.
- **Readiness:** Draft effect; candidate mechanics.

#### Avoid Death

- **Proposed requirement:** **90/100**, **Will + Restoration**, with one of: Emergency Healing, Restoration Healing. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per day, automatically interrupt one Injury incident that would fill your final Fatal slot and kill you, immediately applying a Final-grade restorative mark to Injury before the incident becomes irrevocably lethal. It does not resurrect a person already dead and cannot trigger twice per day.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Pre-death interrupt/response timing and interaction with one-hit multiple Final marks.

#### Respite

- **Proposed requirement:** **40/100**, **Health + Restoration**, with one of: Fatigue Restoration, Restoration Healing. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may design a Restoration formula that restores Injury and Fatigue together, resolving each component with its own Potence, resistance, and Mana Cost under the existing compound-spell rules. Casting a separately learned single-resource spell still heals only its stated track.
- **Readiness:** Needs supporting subsystem. **Blocked by:** How this perk interacts with Spell Synthesis design requirement.

### Alchemy (4)

#### Green Thumb

- **Proposed requirement:** **70/100**, **Perception + Alchemy**, with one of: Herbalism, Foraging, Plant Harvesting. **Cost:** 1 bankable perk point (draft).
- **Effect:** For a successful actual plant-foraging or harvesting Project, collect twice the quantity of physically available usable plant ingredients that a normal harvest would produce. It does not fabricate plants, double nonplant loot, or bypass resource scarcity.
- **Readiness:** Draft effect; candidate mechanics.

#### Concentrated Poison

- **Proposed requirement:** **60/100**, **Intelligence + Alchemy**, with one of: Poisons, Weapon Toxins. **Cost:** 1 bankable perk point (draft).
- **Effect:** One ordinary weapon poison application can deliver its normal poison effect on twice as many successful contacts before the coating is spent. Each poison delivery still follows its original defenses, dose limits and depletion rule.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Poison coating contact count and dose model.

#### Experimenter

- **Proposed requirement:** **50/100**, **Perception + Alchemy**, with one of: Ingredient Lore, Experimental Alchemy. **Cost:** 1 bankable perk point (draft).
- **Effect:** When tasting a real alchemical ingredient during a legitimate identification attempt, one successful Alchemy Project reveals one additional concealed effect beyond normal identification. Eating still exposes you to the ingredient's real risks.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Ingredient effect-identification baseline.

#### Purity

- **Proposed requirement:** **100/100**, **Intelligence + Alchemy**, with one of: Potions, Poisons, Distillation. **Cost:** 1 bankable perk point (draft).
- **Effect:** When brewing a researched formula you may exclude known unwanted harmful effects from a potion, or known beneficial effects from a poison, while retaining one chosen main effect. Each removed component still requires actual alchemical knowledge and materials; no discovery of unknown effects.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Alchemy formula component/purity rules.

### Enchanting (3)

#### Extra Effect

- **Proposed requirement:** **100/100**, **Intelligence + Enchanting**, with one of: Weapon Enchanting, Armor Enchanting, Dual Enchanting. **Cost:** 1 bankable perk point (draft).
- **Effect:** A single crafted item may carry TWO separately designed item enchantments where the eventual item-ownership and enchantment-slot rules normally permit only one. Both effects retain separate components, costs, compatibility limits and their actual Tier.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Item enchantment system and stacking; DISTINCT from Spell Synthesis.

#### Soul Squeezer

- **Proposed requirement:** **20/100**, **Intelligence + Enchanting**, with one of: Soul Gems, Weapon Recharging. **Cost:** 1 bankable perk point (draft).
- **Effect:** When using a soul gem for item recharging, increase the usable recharging work it contributes by 50 percent, rounding down only after the actual recharge accounting is defined. It does not duplicate soul gems.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Soul-gem energy units and item recharge Projects.

#### Soul Siphon

- **Proposed requirement:** **40/100**, **Will + Enchanting**, with one of: Soul Gems, Weapon Enchanting. **Cost:** 1 bankable perk point (draft).
- **Effect:** When a wielded enchanted weapon lawfully captures usable residual soul energy from a defeated eligible creature, apply it to that item's recharge Project rather than the character's Mana. No soul is generated from an ineligible or empty target.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Soul eligibility, capture and recharge accounting.

### Light Armor (3)

#### Unhindered

- **Proposed requirement:** **50/100**, **Agility + Light Armor**, with one of: Leather Armor, Armor Fit, Skirmishing. **Cost:** 1 bankable perk point (draft).
- **Effect:** While wearing light armor for which you have the relevant Specialty, ignore its positive Encumbrance when calculating your final Dodge and ordinary movement distance. Do not alter its Armor Rating or Fatigue costs that expressly depend on item Encumbrance.
- **Readiness:** Draft effect; candidate mechanics.

#### Deft Movement

- **Proposed requirement:** **100/100**, **Agility + Light Armor**, with one of: Evasion, Skirmishing, Leather Armor. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per round after a real attack lands despite your Light-Armor-assisted Dodge, downgrade ONE resulting Injury mark by one severity grade (Final to Major, Major to Middling, Middling to Minor). Damage is still inflicted and further marks remain unchanged.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Post-effect prevention timing, multiple Final marks and demotion handling.

#### Wind Walker

- **Proposed requirement:** **60/100**, **Health + Light Armor**, with one of: Endurance, Skirmishing, Leather Armor. **Cost:** 1 bankable perk point (draft).
- **Effect:** At the start of your own turn, while wearing light armor and after having spent a movement action in the prior round, take ONE extra ordinary Fatigue recovery step after your normal single turn-start step. Never heal Injury or other resource tracks by this rule.
- **Readiness:** Draft effect; candidate mechanics.

### Dodge (3)

#### Aerial Evasion

- **Proposed requirement:** **25/100**, **Agility + Dodge**, with one of: Acrobatics, Jumping. **Cost:** 1 bankable perk point (draft).
- **Effect:** Your legal Dodge can be used while leaping or falling whenever you remain aware and have physical room to alter your path. Pay its usual action and worn-armor Fatigue hazard; this does not give an extra action.
- **Readiness:** Draft effect; candidate mechanics.

#### Rolling Dodge

- **Proposed requirement:** **50/100**, **Agility + Dodge**, with one of: Tumbling, Evasive Footwork. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per round when you spend an actual Dodge reaction action, you may immediately shift a short distance (up to one-quarter of your ordinary move-action distance) without a separate movement action. You must have space and cannot pass through solid cover or obstacles.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Partial tactical movement and reactions.

#### Light Footed

- **Proposed requirement:** **60/100**, **Agility + Dodge**, with one of: Evasive Footwork, Tumbling, Acrobatics. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per six-second round, make ONE otherwise legal Dodge reaction without spending an action from the ordinary three-action budget, even if none remain. Choose before the hostile Accuracy roll; still pay the usual Dodge Fatigue Cost, apply armor Encumbrance, and require awareness and room.
- **Readiness:** New proposal.

### Sneak (4)

#### Light Foot

- **Proposed requirement:** **40/100**, **Agility + Sneak**, with one of: Trap Avoidance, Silent Movement. **Cost:** 1 bankable perk point (draft).
- **Effect:** When making deliberate careful movement, you do not trigger mundane pressure plates merely by your weight if the trigger could reasonably be avoided by foot placement. This does not bypass magical sensors, unavoidable full-floor triggers, or traps you do not have a chance to detect.
- **Readiness:** Draft effect; candidate mechanics.

#### Silence

- **Proposed requirement:** **70/100**, **Agility + Sneak**, with one of: Silent Movement, Combat Stealth. **Cost:** 1 bankable perk point (draft).
- **Effect:** At an ordinary walking or running movement pace, treat your movement-related noise as if moving cautiously for Sneak attempts. Armor clang, speech and other external noise sources still apply; this is not supernatural sound suppression.
- **Readiness:** Draft effect; candidate mechanics.

#### Shadow Warrior

- **Proposed requirement:** **100/100**, **Wits + Sneak**, with one of: Combat Stealth, Misdirection. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per round when there is actual concealment or a diversion, you may attempt an immediate Sneak disengagement during an ongoing encounter. Success breaks a target's visual tracking until it reacquires you; no instant invisibility while observed in the open.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Line of sight and reacquisition Project rules.

#### Backstab

- **Proposed requirement:** **30/100**, **Dexterity + Sneak**, with one of: Ambush, Daggers, Precision Striking. **Cost:** 1 bankable perk point (draft).
- **Effect:** When you make a melee attack against someone genuinely unaware of you at the time of Accuracy resolution, add +3 perk-technique Damage dice to its Potence. No bonus against targets already aware of you; the extra dice do not generate perk confirmations.
- **Readiness:** Draft effect; candidate mechanics.

### Security (4)

#### Quick Hands

- **Proposed requirement:** **40/100**, **Dexterity + Security**, with one of: Lockpicking, Covert Tools. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may attempt a normal Security lock Project while concealing that you are working on the lock; observers need a genuine successful perception/opposition attempt to notice your hands. This does not waive the lock Project or remove the time/tool requirement.
- **Readiness:** Draft effect; candidate mechanics.

#### Wax Key

- **Proposed requirement:** **50/100**, **Intelligence + Security**, with one of: Locksmithing, Lockpicking. **Cost:** 1 bankable perk point (draft).
- **Effect:** After legitimately opening an ordinary keyed lock, you can make a wax impression suitable for a later key-copying Smithing/Security Project when you have actual wax and access to the keyway. The impression is not automatically a functioning duplicate key.
- **Readiness:** Draft effect; candidate mechanics.

#### Unbreakable

- **Proposed requirement:** **100/100**, **Dexterity + Security**, with one of: Lockpicking, Precision Tools. **Cost:** 1 bankable perk point (draft).
- **Effect:** Ordinary lockpicks you use in routine lockpicking Projects do not break solely because an ordinary picking roll fails. Deliberate sabotage, unsuitable tools and exceptional trap mechanisms can still destroy them.
- **Readiness:** Draft effect; candidate mechanics.

#### Treasure Hunter

- **Proposed requirement:** **70/100**, **Perception + Security**, with one of: Lockpicking, Loot Appraisal. **Cost:** 1 bankable perk point (draft).
- **Effect:** When successfully opening a genuinely unexplored loot-bearing container, apply one extra random treasure-quality check and use the more valuable legal result, but only if the campaign's treasure generator uses randomized quality. Never rewrite already-established contents.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Loot generation quality tables and campaign persistence.

### Legerdemain (3)

#### Poisoned

- **Proposed requirement:** **40/100**, **Dexterity + Legerdemain**, with one of: Pickpocketing, Poison Placement. **Cost:** 1 bankable perk point (draft).
- **Effect:** Against a genuinely unaware subject within reach, you may covertly place one actual dose of poison on or into an accessible carried item. Make the ordinary Legerdemain application; poison works only by its own legal delivery and resistance rules.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Poison delivery triggers and covert-object placement.

#### Misdirection

- **Proposed requirement:** **70/100**, **Dexterity + Legerdemain**, with one of: Pickpocketing, Weapon Theft. **Cost:** 1 bankable perk point (draft).
- **Effect:** Against someone genuinely unaware and within reach, you may attempt to lift a carried or readied handheld weapon via a Legerdemain theft Project. On success the actual item transfers; no automatic disarm against alert combatants.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Possession/disarm opposing Project difficulty.

#### Perfect Touch

- **Proposed requirement:** **100/100**, **Dexterity + Legerdemain**, with one of: Pickpocketing, Gear Theft. **Cost:** 1 bankable perk point (draft).
- **Effect:** Against someone genuinely unaware and within reach, you may attempt an exceptionally difficult Legerdemain Project to remove a worn usable item without alerting its owner. Fastened armor and secured items require credible time/access; success is not teleportation.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Time/scope and secured-gear theft rules.

### Speechcraft (4)

#### Merchant

- **Proposed requirement:** **50/100**, **Charisma + Speechcraft**, with one of: Negotiation, Trade. **Cost:** 1 bankable perk point (draft).
- **Effect:** You may open legitimate trading negotiations for categories of goods a merchant normally does not stock, provided the merchant could plausibly obtain or use them. It permits the attempt; it never compels the merchant to accept an unwanted deal.
- **Readiness:** Draft effect; candidate mechanics.

#### Bribery

- **Proposed requirement:** **30/100**, **Insight + Speechcraft**, with one of: Bribery, Guard Negotiation. **Cost:** 1 bankable perk point (draft).
- **Effect:** You can openly propose a discreet bribe to an official or guard without the offer alone automatically spoiling an otherwise legal social approach. Resolve their actual interests, duties and reactions through a Social Project; no automatic forgiveness.
- **Readiness:** Draft effect; candidate mechanics.

#### Investor

- **Proposed requirement:** **70/100**, **Charisma + Speechcraft**, with one of: Merchant Finance, Trade. **Cost:** 1 bankable perk point (draft).
- **Effect:** You can sponsor a willing merchant's real trading venture as a persistent economic Project, increasing their actual available stock and capital only as the Project's recorded progress and risks warrant. No automatic global wealth bonus.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Persistent merchants, capital and trading Projects.

#### Master Trader

- **Proposed requirement:** **100/100**, **Insight + Speechcraft**, with one of: Merchant Finance, Negotiation, Trade. **Cost:** 1 bankable perk point (draft).
- **Effect:** Once per settlement, arrange an extraordinary but plausible procurement or exchange network for a specific rare good by completing a real social/trade Project. It expands access to people who can actually supply it; does not conjure gold or merchandise.
- **Readiness:** Needs supporting subsystem. **Blocked by:** Supplier search Projects and economic world persistence.

### Survival (1)

#### Trailwise

- **Proposed requirement:** **50/100**, **Perception + Survival**, with one of: Foraging, Weathercraft, Sheltercraft. **Cost:** 1 bankable perk point (draft).
- **Effect:** After you complete a suitable genuine Survival Project to establish a safe shelter, reduce the next environmental exposure hazard magnitude for sheltered companions by 1 success before grading Fatigue (minimum zero). This does not protect against hazards the shelter cannot physically address.
- **Readiness:** Draft effect; candidate mechanics.

### Lore (1)

#### Field Scholar

- **Proposed requirement:** **50/100**, **Intelligence + Lore**, with one of: Monster Lore, Ancient History, Field Research. **Cost:** 1 bankable perk point (draft).
- **Effect:** On a successful research Project concerning a specific observed creature, artifact or ruin, learn one concrete relevant vulnerability, provenance or operational fact that available sources could establish. The GM must disclose a real fact, not invent one solely to reward the perk.
- **Readiness:** Draft effect; candidate mechanics.

## Review gates and implementation boundary

**What is settled already:** Elf Books' confirmed 10s/defender confirmed attacker 1s, banked personal-only perk points, composite 0–100 qualifications, absence of ordinary starting-Talent perk trees, and the effect text for **Power Bash, Deflect Arrows and Dual Flurry**. This draft **does not revise** any of those rules.

**Still to decide before purchasing:** Whether the proposed numeric gates and listed Specialty vocabulary are accepted; which perks have multiple ranks; whether the additional rolled Finesse damage dice are too strong at very high Accuracy margins or toward helpless targets; whether free reactions can be banked between turns (this draft says **no**, only one of each each round); and which supporting subsystems need completion. The once-per-round free-reaction perks **do not waive Fatigue Cost** by default.

**Adjudication rule:** A draft effect is **not** acquired automatically when its qualifier is met. It must appear in an adopted purchasable perk record and be paid for with a banked point. Until that happens, all examples below are voluntary GM or test-run setups.

[Machine-readable candidate catalogue](PERK_CATALOG_DRAFT.json) · [Previously adopted combat effect pilots](COMBAT_PERK_PILOTS.md) · [Existing banked perk rules](../rules/PERKS.md).
