# Combat and defenses — Geard Lif adapter (OPEN)

**Base engine:** [local Geard Lif Project framework](../engine/geard-lif/source/Project_Framework.tid) and [graded resources](../engine/geard-lif/source/Resource_Tracks.tid). Old D20 AC formulas, automatic hits/misses, 5e armor bonuses and HP damage **do not apply**.

Locked upstream separation:

- Attacking **Accuracy** is applied against normally static **Avoidance**.
- Successful application leads to **Potence** against **Resilience**; the applicable Body resilience is **Health**, and the wound resource is **Injury**.
- Natural body defenses, heavy/light armor, shields, parries, Dodge, cover, skills and spells must be represented as legally applicable changes to these quantities, not stacked D20 AC scores.
- Repeated small blows accumulate graded marks; a large Effect can inflict severe marks immediately. Consult the imported resource-track rules for exact mechanics.

**Open:** attack/effect roll resolution, tie policy, defense reactions, range/position, movement/initiative, armor and shield contribution, magical wards and flesh spells, weapon reach/speed, multiattack, injury prevention, combat practice and passive critical/perk opportunities.

**Priority:** test a swordsman versus bandit and an Oakflesh-style protective spell using the *same Project engine* and track actual graded Injury, rather than resurrecting a separate D20 subsystem.

See [MIGRATION_BACKLOG.md](../MIGRATION_BACKLOG.md).
