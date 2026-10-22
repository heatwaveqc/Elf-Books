# Combat and defenses — Geard Lif adapter (OPEN)

**Base engine:** [local Geard Lif Project framework](../engine/geard-lif/source/Project_Framework.tid) and [graded resources](../engine/geard-lif/source/Resource_Tracks.tid). Old D20 AC formulas, automatic hits/misses, 5e armor bonuses and HP damage **do not apply**.

Locked upstream separation:

- Attacking **Accuracy** is applied against normally static **Avoidance**.
- Successful application leads to **Potence** against **Resilience**; the applicable Body resilience is **Health**, and the wound resource is **Injury**.
- Natural body defenses, heavy/light armor, shields, parries, Dodge, cover, skills and spells must be represented as legally applicable changes to these quantities, not stacked D20 AC scores.
- Repeated small blows accumulate graded marks; a large Effect can inflict severe marks immediately. **Armor, Oakflesh-like magic and other protection may raise the effective threshold for how severe the Injury is**, but **Health (Resilience), not armor, sets the number of mark slots at Minor/Middling/Major/Fatal**. The exact amount each protective method changes threshold remains to be designed. See the imported unified [[Resource Tracks]]/Project rules.

**Static Dodge (working):** select the applicable Agility, Talent (if it governs Dodge), Dodge Skill and one relevant Specialty. Convert 0–25 source ratings to dice using floor(rating/5), then **halve the combined dice and round down once** for static Avoidance. A one-die pool has static defense 0, a two- or three-die pool has 1. When legitimately targeted and actively choosing that defense, each participating trait receives **ceil(rating/10) XP at Tier 0**, or **rating/10 ×5^Tier XP at Tier 1+**, tracked in the existing XP ledger. Other defenses and real Fatigue/Mana Cost resistance use the same *source-based passive practice* principle, with their actual contributors (not automatic Dodge). See [Advancement](ADVANCEMENT.md).

**Open:** attack/effect roll resolution, tie policy, defense reactions, range/position, movement/initiative, armor and shield contribution, magical wards and flesh spells, weapon reach/speed, multiattack, injury prevention, combat practice and passive critical/perk opportunities.

**Oakflesh prototype adopted:** For a successfully established Oakflesh effect, the **rolled Potence successes add directly to the recipient's effective Injury severity/Resistance threshold**, as a **flat equipment-equivalent protective bonus**. Health's dice-equivalent Resilience and marks per grade are unchanged. This is *not* an added number of static Avoidance dice or extra slots, and is not a general buff to Health's non-Injury uses. Example: Health 2 and Oakflesh Potence 4 make the incoming-Injury grade threshold **6** but leave **two slots per grade**. Interactions/stacking with ordinary armor and other protection remain OPEN. Willing accessible subjects need no separate Accuracy check; hostile application uses legal magical defenses, but Potence and Cost are still rolled on an Accuracy miss. [Magic](../design/MAGIC.md).

**Priority:** test a swordsman versus bandit and an Oakflesh-style protective spell using the *same Project engine* and track actual graded Injury, rather than resurrecting a separate D20 subsystem.

See [MIGRATION_BACKLOG.md](../MIGRATION_BACKLOG.md).

**Countermagic:** an available counterspell can instead select **Wits + Mysticism** (with applicable Talent/Specialty), floored as one combined static defense, not stacked onto Dodge or an already-chosen ward. A school spell's **self-Cost** uses **Will + governed Talent + the spell's own School Skill + relevant declared Spell Specialty + eligible gear** static resistance. Mind/Will sets Mana capacity independently of these extra threshold contributions. See [Magic](../design/MAGIC.md). Reaction cost/action legality are still open.

**Mode-specific defenses:** See [Attack Modes](ATTACK_MODES.md). A contested effect declares its attack mode and allowed defensive Attribute + Skill pools. Cold weather and a direct freezing Malediction both use **Health + Survival**; ice spears/arrows allow Dodge or shield Block, not normal Parry. Four social attack modes specify social/factual defenses. Add governed-Skill Talent, relevant Specialty, and only eligible external bonuses; equipment/enchantments/ensorcellments/temporary magic together may add at most the unmodified personal dice pool.

**Soul defense clarity:** resisting an *attempt* to manipulate, frighten or shame uses eligible method-specific **Insight/Temperance + Skill**, not Conviction + Speechcraft. **Conviction** determines the target's Soul resource mark capacity and base severity threshold after an effect lands. Ordinary social attacks directly mark **Attention only**; direct Plasticity attacks are supernatural. Strength + Speechcraft is a legal offensive intimidation pool.

**Exhausted fast track:** an otherwise valid fast-targeted hostile Effect redirects into the paired slow track once fast was exhausted *before* this incident. This is a resource-routing step **after** Application defense, not a license for new attack modes: a normal social attempt still uses Attention-targeting rules, even when its harm ultimately reaches Plasticity. Reevaluate severity using the appropriate slow resistance, without adding injury on the hit that just exhausts fast.

**Deflect Arrows (perk-only arrow Parry):** If already granted this effect, a character with a ready weapon legitimately capable of Parry may use the usual Dexterity + weapon Skill Parry against an **arrow**, instead of the ordinary default Dodge/Block-only menu. It spends **one** defensive reaction action and pays the normal parrying item's rolled Fatigue Cost. It is neither a universally available Parry nor a free defense; see [perk pilot](../design/COMBAT_PERK_PILOTS.md). The perk's attribute/specialty purchase gates are still open.
