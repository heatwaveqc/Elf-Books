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

## Tier and passive XP acceptance

- Same-Tier governing-die prerequisites: Dexterity Tier 1 **5**, One-Handed Tier 1 **25**, Longswords Tier 1 **20** is legal; Dexterity Tier 1 **4** bars the latter dice, and Skill Tier 1 **4** bars Specialty dice. Talent Tier 1 **25** does **not** substitute for missing Attribute dice. No cap requires child rating ≤ parent rating.
- A trait cannot purchase Tier 1 until its Tier 0 rating is 25. Tier 1 rating 20→21 costs **1,000 XP**, versus Tier 0 **200 XP**. Source rewards multiply by 5 **once**, not again after Tier-scaled Effect magnitude.
- Test choice between keeping maxed Talent XP to unlock Tier 1 and cascading **unchanged raw XP** to the first unmaxed Attribute/Skill/Specialty. No double award and no arbitrary related-skill recipient.
- Static four-die Dodge = **2**. Agility rating 10 + Talent 5 + Dodge 5 + Specialty 0 passive awards **1 / 1 / 1 / 0 whole XP** at Tier 0, rounded up per contributing trait. Test the Tier 1+ exact formula and genuine resource-Cost events.

## Spell Cost and rounding tests

- At Tier 0, a rating 5/11/15 participant receives **1/2/2 whole passive XP** (rounded up per source); zero earns zero. At Tier 1, ratings 5/11/15 earn **2.5/5.5/7.5 XP** exactly (do not round; save tenths).
- Static defense **floors the combined dice/2**, not per-source halves: one total die 0, two dice 1, three dice 1, four dice 2.
- Destruction Accuracy uses **Perception + applicable Talent + Destruction + Spell Specialty**, Potence **Intelligence + the same three**, and its rolled self-Cost is measured against static **Will + the same Talent + Destruction + relevant Spell Specialty + eligible cost-reducing robes**; **Will** sets the independent Mind/Mana mark capacity. Cost dice themselves are never reduced by robes, and no extra resistance roll occurs.
- Default counterspell uses **Wits + Mysticism** as a chosen alternative static Avoidance. Appropriate Talent/Specialty are applicable where legitimate; counterspell reaction cost and timing remain unsettled.

## Mind/Soul resource swap and all-source magic Cost resistance

- Mind/Will owns Spirit (slow), Mana (fast), while Soul/Conviction owns Plasticity (slow), Attention (fast); Body/Health Injury/Fatigue unchanged. Verify character template and validator both enforce exact assignment.
- Test Perception + applicable Talent + Destruction + Firebolt Specialty for Accuracy; Intelligence + same three for Potence; **Will + same Talent + same Skill + same Specialty** for static Cost resistance.
- With Will 10, Mage Talent 10, Destruction 10, Firebolt 5, **7 personal dice** give static resistance 3 and **two Mana marks per grade**. One robe die raises resistance to 4, not capacity. A rolled Cost 3 is therefore Middling without the robe and Minor with it.
- Tests must show both **governing Talent** and **specific spell Specialty** affect cost severity, that off-Talent spells do not gain Talent dice, and that *all four applicable personal sources* receive eligible passive Cost XP (equipment never does).
- Persisted Mana marks belong to **Mind**, not Soul; changing the schema does not implicitly migrate any live character's mark histories.

## Named pool, contested attack modes and bonuses

- Test shorthand Attribute + Skill automatically contributes governed Talent and one relevant declared Specialty. Health + Survival must be allowed as a defensive pool even though Health is a Resilience attribute.
- Cold weather and a direct freezing Malediction both defend with **Health + Survival**; launched ice spears/arrows normally allow Dodge/Block and exclude default Parry. Counterspelling is a separate available reaction, not an additive defense.
- The four social modes (persuasion, deception, intimidation, reputation) specify valid social defense pools and directly pressure **Attention only**; only supernatural identity attacks directly mark **Plasticity**. Conviction controls their capacity/severity, not ordinary Avoidance.
- Combined shield, enchanted ring, ensorcellment and temporary magic **external dice sum must not exceed the unmodified personal dice**, even when each bonus separately is under that limit. Check applied to static defenses, spell Cost, ordinary casting and mundane actions.

## Fivefold advancement and supernatural social boundary

- Verify **Tier effectiveness, XP costs and XP rewards are all fivefold per Tier**. Tier 0 rating 20→21 costs 200 XP; Tier 1 **1,000**; Tier 2 **5,000**. Cross-Tier successes 27 Tier 0→1 convert to 5, 27 Tier 1→3 convert to 1, and 3 Tier 5→4 convert to 15.
- Tier 1 passive practice at rating 5 yields **2.5 XP**; at rating 11 yields **5.5 XP**. Fractional higher-Tier awards are stored in integer tenths, not rounded away. Tier 0 still rounds passive XP upward per participating trait.
- Validate all mundane social modes target Attention only, with no `long_term_target_track: plasticity` or Conviction-based Avoidance. Physically imposing Intimidation application is **Strength + Speechcraft**, while ordinary defenses use Temperance/Insight. A separate supernatural identity Malediction *may* directly mark Plasticity using its own declared defensive pool; Conviction still supplies Soul soak/capacity.
