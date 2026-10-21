# Skill XP — first calibration pass (proposals, not approved numbers)

**Purpose:** Select unit scales using equal-opportunity benchmarks rather than reflexively awarding one point per die roll. The 24-skill candidate is in [skills_v2.json](skills_v2.json) and the agreed defense formula is [rules/DEFENSE.md](../rules/DEFENSE.md).

## Rank cost: candidate K = 1

```text
XP to move from rating s to s+1 = max(1, s) × K
rating 0..100; no class levels; no compulsory proficiency-by-level
```

Keep **K** a campaign-calibration parameter pending player approval. `K=1` is a transparent starting hypothesis, not the final setting. Carry surplus XP into the next skill rank. At maximum 100, new XP cannot raise the rating. One consequential event credits one canonical skill per skill domain; do not re-credit overlapped historical aliases.

Total XP from rating a up to b (where 1 ≤ a < b ≤100) is `K × (a + (a+1) + ... + (b-1))`.

## Benchmark: one-handed d8 baseline

Take a nonmagical one-handed d8 weapon. If **each consequential hit** earns the weapon's *base rolled damage*, **ignoring attributes, magic, smithing, perks and overkill**, the average successful hit is 4.5 practice XP. No extra learning roll is needed. This is a practice-rate assumption, not an instruction to pretend that every attack always hits.

| Skill advancement | Total required XP, K=1 | Average successful d8 hits | Enemies at 3–5 qualifying hits each |
| --- | ---: | ---: | ---: |
| 20→25 | 110 | 24.4 | ~5–9 |
| 50→55 | 260 | 57.8 | ~12–20 |
| 95→100 | 485 | 107.8 | ~22–36 |
| 20→100 | 4,760 | 1,057.8 | ~212–353 |

The enemy column is a rough **illustration** assuming 3–5 *successful qualifying hits* per enemy. It does not include misses, area attacks, bonus attacks, or special damage; neither does it assume all fights have one opponent. It's primarily for comparing expected careers. A stronger base weapon such as 1d12 grows its user faster unless normalized, so **the influence of weapon base die on training rate is a consequential design choice**.

The previously rejected successful-learning-check model needed 485 *successful learning checks* merely for 95→100, ≈1,078 total checks at 45% success. This output-based trial requires ~108 successful d8 hits over the same range.

## Candidate experience sources

| Family | Candidate formula / unit | Calibration risk |
| --- | --- | --- |
| One-/Two-Handed, Archery, Unarmed | Base weapon damage **on consequential successful hits** | d12 vs d4 speed mismatch; natural-20 damage crits must not double skill XP just because damage doubles |
| Heavy/Light Armor | **Actual HP damage taken** while wearing relevant armor; trial 1 XP per actual HP | Damage severity drives faster learning and genuine danger; not penalized simply for intentionally taking hits |
| Block/Dodge | Base/nominal threat damage of a **credible attack actually prevented by selected defense** | Rare defense success compared with attacks; tests must match perk and XP pacing |
| Destruction | Nominal cost of purposeful spell / trial divisor **4** | Expensive spells can outpace weapon use; test with low/medium/high spells and actual casting limits |
| Restoration | Useful HP restored or meaningful effect removed, plus appropriate nominal-cost weighting | Healing cannot create reward from restoring nonexistent HP; recovery out of combat still valid |
| Other magical schools | Spell nominal Magicka cost / trial divisor **4**, only if effect mattered | Cost-reduction perks shouldn't reduce practice; no trivial empty-room spam requirement |
| Smithing, Alchemy, Enchanting | Crafted object's genuine challenge, material difficulty and economic value | One legendary item should yield more than a trivial iron dagger; item values alone encourage exploits |
| Security, Sneak, Legerdemain, Speechcraft, Survival, Lore, Athletics | Consequential challenge XP: **5 minor / 15 standard / 30 major / 60 exceptional** (illustrative tiers) | A single social resolution can substitute for an entire fight; don't reward every sentence, step or repeated trivial check |

The trial magic ratio **20 nominal Magicka / 4 = 5 XP**, close to one normal d8 weapon hit; 80 nominal Magicka costs grant 20 XP, but consume a substantial resource. Compare caster-rest and recharge frequency before approving.

One average 3–5-hit enemy yields ~13.5–22.5 weapon XP. A standard noncombat challenge of **15 XP** is therefore in the same rough band as one defeated enemy, while a major social or research result can earn **30 XP** without requiring twenty repetitive die rolls. A minor real task can still teach; no arbitrary requirement that every accomplishment be life-or-death.

**Armor XP is based on HP actually lost, without an arbitrary encounter cap.** Risky intentional practice may therefore be rational. Genuine resource loss and opponent agency make that a valid choice, not automatically an exploit. Non-harmful simulation practice and formal training need separate, time-based values.

## Required design decisions before these values become rules

1. Confirm `K=1` (or a calibrated alternative) against actual low/mid/high skill play.
2. Weapon XP from base **rolled** damage versus fixed expected base damage; compare unarmed and fast low-die weapons.
3. Decide if armor earns *only* actual-HP XP or also a smaller benefit when equipment deflects a blow. Agreed core: damage taken always counts regardless of selected defense.
4. Pick Magicka divisor and skill-specific effect weighting; avoid burst spells advancing several ranks per cast unless intentionally desired.
5. Decide how often noncombat accomplishments qualify; avoid shortchanging social skills relative to a combatant making many attacks.
6. Define training, instruction, specializations, critical perk breakthrough and defensive critical timing separately from ordinary skill XP.
7. Run a full encounter-level simulation with chance-to-hit, resources, damage taken and rest; per-success math is only a first benchmark.

**Do not activate campaigns** until the values are approved, integrated into skill ledger/persistence, and validated.
