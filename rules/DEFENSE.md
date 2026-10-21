# Combat and defenses — Geard Lif adapter (OPEN)

**Base engine:** [local Geard Lif Project framework](../engine/geard-lif/source/Project_Framework.tid) and [graded resources](../engine/geard-lif/source/Resource_Tracks.tid). Old D20 AC formulas, automatic hits/misses, 5e armor bonuses and HP damage **do not apply**.

Locked upstream separation:

- Attacking **Accuracy** is applied against normally static **Avoidance**.
- Successful application leads to **Potence** against **Resilience**; the applicable Body resilience is **Health**, and the wound resource is **Injury**.
- Natural body defenses, heavy/light armor, shields, parries, Dodge, cover, skills and spells must be represented as legally applicable changes to these quantities, not stacked D20 AC scores.
- Repeated small blows accumulate graded marks; a large Effect can inflict severe marks immediately. **Armor, Oakflesh-like magic and other protection may raise the effective threshold for how severe the Injury is**, but **Health (Resilience), not armor, sets the number of mark slots at Minor/Middling/Major/Fatal**. The exact amount each protective method changes threshold remains to be designed. See the imported unified [[Resource Tracks]]/Project rules.

**Static Dodge (working):** select the applicable Agility, Talent (if it governs Dodge), Dodge Skill and one relevant Specialty. Convert 0–25 source ratings to dice using floor(rating/5), then **halve the combined dice and round down once** for static Avoidance. A one-die pool has static defense 0, a two- or three-die pool has 1. When legitimately targeted and actively choosing that defense, each participating trait receives **ceil(rating/10) XP at Tier 0**, or **rating/10 ×10^Tier XP at Tier 1+**, tracked in the existing XP ledger. Other defenses and real Fatigue/Mana Cost resistance use the same *source-based passive practice* principle, with their actual contributors (not automatic Dodge). See [Advancement](ADVANCEMENT.md).

**Open:** attack/effect roll resolution, tie policy, defense reactions, range/position, movement/initiative, armor and shield contribution, magical wards and flesh spells, weapon reach/speed, multiattack, injury prevention, combat practice and passive critical/perk opportunities.

**Priority:** test a swordsman versus bandit and an Oakflesh-style protective spell using the *same Project engine* and track actual graded Injury, rather than resurrecting a separate D20 subsystem.

See [MIGRATION_BACKLOG.md](../MIGRATION_BACKLOG.md).

**Countermagic:** an available counterspell can instead select **Wits + Mysticism** (with applicable Talent/Specialty), floored as one combined static defense, not stacked onto Dodge or an already-chosen ward. A school spell's **self-Cost** uses **Will + the spell's own School Skill** static resistance. See [Magic](../design/MAGIC.md). Reaction cost/action legality are still open.
