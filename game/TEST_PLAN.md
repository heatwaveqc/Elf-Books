# Validation and return-to-parity test plan — Geard Lif

**Passing CI does not mean the game is playable.** The former D20 calculators/tests are retained solely in [archive/d20-pre-geard-lif](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif).

## Current structural and arithmetic tests

- `python3 scripts/validate_scaffold.py`: required Geard snapshot/manifest, reader docs, 24 skills, public-only import, private-campaign boundary and template sanity.
- `python3 -m unittest discover -s tests -v`: provisional d10 7–9/10 counting, Tier conversion, meet-to-beat application, four-grade Project and resource marks, severity threshold/capacity independence, promotion/exhaustion, and validator tests.
- GitHub Actions runs both on pushes/PRs.
- **Meet-to-beat Accuracy** and **graded Effect marks** are specified and tested for both people and Projects. Project Scope sets mark slots per grade, Recalcitrance sets threshold; armor adjusts threshold without altering personal Resilience capacity. Advancement and d10 criticals still need design.

## Clarified Project gate tests

- **Equality succeeds**: Accuracy 3 against Complexity 3 applies; Accuracy 2 fails without a Potence roll.
- With R=4, Potence 0 gives no mark; 1–3 gives Minor; 4–7 Middling; 8–11 Major; 12–15 Final; 16 gives two Final marks. These are not cross-scale Tiers.
- A Project of Scope 2 has two slots at **each grade**, and finishes after two Final marks; low-grade marks promote when their grade's slots overflow.
- A person with Health 4 has four Injury slots at each grade. An armor-raised threshold of 6 makes Potence 5 a Minor injury instead of Middling, but keeps four slots per grade. This threshold 6 is a **test fixture**, not a finalized armor value.

## Attributes and five-skill Talent test cases

- Verify the exact twelve attributes grouped by Body/Mind/Soul and by Potence/Accuracy/Avoidance/Resilience.
- Verify all twelve supplied preset five-skill Talents and any player-created custom Talent use only five *distinct* canonical Skill IDs.
- A Spellsword's Talent **10** (2d), Dexterity **15** (3d), One-Handed **20** (4d), Longswords **5** (1d) contributes **10d10 Accuracy**; Strength **20** (4d) produces **11d10 Potence**. Smithing **15** (3d) + Strength **20** (4d) gives **7d10** outside Spellsword.
- Test one Talent selected per character, multiple Specialties not stacking, correctly chosen active function Attributes, rating caps currently provisional, and no deriving resource capacities from other attributes.
- Confirm **0–25 ratings**, one d10 per five levels, minimum rating 5 in all starting Attributes and all five Talent-governed Skills; simulate XP pace for novice/expert and equivalent custom progression trees. Creation budget, passive XP, and Talent-tree nodes still require decisions.

## XP award regression tests

- At rating 20, a trait generates **4 personal dice**; raising rating 20→21 costs **200 XP**. Buying from 0→5 costs **110 XP**.
- Natural 10 yields **two ordinary successes**, granting 4 Attribute XP / 2 Talent XP / 10 Skill XP / 20 Specialty XP if rolled by that source. Attribute 7–9 grants **2 XP**.
- Each natural 10 also gives **one** bootstrap success (5 XP) to the used Skill if under 5, and **one** (10 XP) to a specifically declared relevant Specialty if under 5; **both** may advance on the same roll. No additional bootstrap at rating 5+.
- XP is sourced to actual face groups, including failed Accuracy applications; equipment dice do not earn personal-source XP but can trigger a genuine bootstrap event. Calculate credits on pre-roll ratings, then level up.
- Reject a starting character with one Talent-governed Skill at 4 or with any Attribute below 5. Keep Talent starting budget and passive-defense XP open.

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
