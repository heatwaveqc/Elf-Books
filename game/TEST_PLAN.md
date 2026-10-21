# Validation and return-to-parity test plan — Geard Lif

**Passing CI does not mean the game is playable.** The former D20 calculators/tests are retained solely in [archive/d20-pre-geard-lif](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif).

## Current structural and arithmetic tests

- `python3 scripts/validate_scaffold.py`: required Geard snapshot/manifest, reader docs, 24 skills, public-only import, private-campaign boundary and template sanity.
- `python3 -m unittest discover -s tests -v`: provisional d10 7–9/10 counting, upward/downward Tier conversion, graded resource severity/promotion/recovery/exhaustion, Project progress clip and template/validator tests.
- GitHub Actions runs both on pushes/PRs.
- Strict Accuracy > Complexity/Avoidance and Potence > Recalcitrance/Resilience gates, plus one progress-tier upgrade per full multiple, are now **specified and tested**. How each tier credits actual Scope, the below-Resilience resource-mark rule, advancement and criticals still need further design.

## Clarified Project gate tests

- **Equality fails** for ordinary Project application and progress: Accuracy 3 vs Complexity 3 does not roll Potence; successful Accuracy 4 vs 3 followed by Potence 4 vs Recalcitrance 4 makes no ordinary Project progress.
- With R=4 and application succeeded, Potence 5/8/12 successes yield **1/2/3 progress-tier upgrades**. These do **not** automatically equal 1/2/3 Scope points until an upstream rule specifies their magnitudes.
- Personal Injury against Health 4 retains existing Minor for Effect 1–3 and Middling for Effect 4; document/reconcile the threshold difference without silently discarding the resource chart.

## Four-scene acceptance vertical slice

1. **Swordsman/bandit:** compare Accuracy to static Avoidance; Potence to Health; apply real Injury marks; demonstrate armor/shield/block/dodge intervention, genuine risk, recording and legal actions.
2. **Thief/lock under time pressure:** one Project with meaningful Complexity, Recalcitrance, Scope and Time, interference and resource strain; show solo compression cannot erase clock changes.
3. **Mage/Oakflesh:** cast, roll a **Cost** against Mana, apply protective Effect to legal defense, then resolve a hit through resource marks. Explain what practice XP applies.
4. **Smith/month of work:** declare genuine Project Scope and Time; roll enough real work intervals, account for progress/setbacks/materials and NPC clocks, update skill practice and save state.

## Other explicit tests

- Peer vs overwhelming Tier and armor equipment; low/high dice pools and resource survival.
- Physical, mental and spiritual injuries and fatigue, Mana and Attention recovery for solo PCs.
- Bankable perk breakthrough probability for different d10 pool sizes and passive defense; no natural-20 import.
- Distinct character skill learning including Destruction vs Alteration, passive Armor and noncombat Projects.
- Original TES perk imports: first Quiet Casting, Green Thumb, Arcane Blacksmith, then difficult Sweeping attacks/dual summons.
- Unique campaign save isolation, stale revision rejection, secret leak tests and authorizing a real store.

[Full prioritized checklist](../MIGRATION_BACKLOG.md) is the current readiness ledger.
