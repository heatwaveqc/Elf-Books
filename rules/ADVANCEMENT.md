# Use-based advancement — Elf-Books working rules

**Current experimental calibration, implemented and unit-tested:** [source upstream Geard Lif page](../engine/geard-lif/source/Use_Based_Trait_Advancement.tid). Numbers are approved for preliminary balance testing, not a promise that campaign pacing is final. D20/HP-based XP is archived.

## Rating, dice and XP cost

Every Attribute, Talent, Skill, and Specialty has a **0–25 integer rating**. Each complete five rating levels gives one d10 when the trait is applicable:

`personal source dice = floor(rating / 5)`, up to five dice from each category and 20 personal dice total. Outside the character's five-skill Talent, the Talent contributes **zero** but the other traits function normally.

Buying the next one-point increase from current rating `r` costs **`10 × max(1,r)` XP** (cap at rating 25), spent in sequence with overflow retained. Example: **20→21 costs 200 XP**; starting from zero, reaching rating five costs **110 XP** total.

## Practice XP from actual rolled faces

Maintain which d10 came from **Attribute, Talent, Skill and (one declared applicable) Specialty**. Attribute dice earn **2 XP per rolled success**, Talent **1**, Skill **5**, Specialty **10**. Under the current d10 randomizer, 7–9 = 1 success, 10 = 2; each 10 therefore earns double *ordinary* source XP. Award that XP from each source's own successful dice, even if the overall Accuracy attempt fails. **Do not** award separate XP from *total* successes as well.

| Source | XP for 7–9 | XP for a natural 10 |
| --- | ---: | ---: |
| Attribute | **2** | **4** |
| Talent (only governed skill) | **1** | **2** |
| Skill | **5** | **10** |
| Specialty (declared) | **10** | **20** |

A Talent is only one character-chosen package of five Skills; ordinary other Skills remain learnable.

## Natural-ten bootstrap: Skill **and** Specialty

A rating from **0 through 4** adds no personal dice. During a consequential action, **each natural 10 on any rolled die** generates one additional *surrogate learning success* toward the **used Skill** (5 XP), and **the applicable Specialty declared for that action** (10 XP), **if each recipient is currently rated below 5**.

- **Both** can receive this XP from **the same natural 10**. A Skill at rating 5+ does **not** bootstrap, but a named Specialty at 0–4 still can.
- Only one relevant Specialty is declared for a roll. Do not distribute learning XP to every possible Specialty. No additional bootstrap XP is credited to a trait already rating 5+.
- The natural 10 still supplies **two ordinary roll successes to the die's source**. Bootstrap adds **one** learning success to an under-5 Skill/Specialty, not two. Equipment dice can cause the breakthrough but do not themselves accrue character-trait XP.
- Calculate dice and awards from the **pre-roll rating snapshot**, then apply earned XP/rank increases. Do not let mid-roll rating increases retroactively add dice.
- Practice must represent real in-fiction activity. Genuine study, combat and Project work count; empty reroll loops do not. One chat message may contain many actual, separately resolved actions or weeks of work.

A zero-rated Skill may be learned **outside the Talent** through this method; a zero-rated Specialty may be learned under any suitable Skill. There is no skill-class lock.

## Starting characters and defensive practice

- All **twelve Attributes start at least rating 5**.
- When selecting a Talent (preset or custom), **all five governed Skills begin at rating 5 or higher**. This automatically grants at least one Skill die for each; **non-governed Skills and all Specialties may start at zero**. Talent's initial rating and the complete creation budget remain open. See [character creation](../game/CHARACTER_CREATION.md).
- **Health, Will and Conviction** are independent Attributes; the effective numerical personal Resilience and mark capacity at each grade are their dice-equivalent ratings `floor(attribute/5)`. Armor affects the **effective Injury threshold**, not capacity.
- Ordinary passive defense and self-Cost resistance, including real exertion resisting Fatigue, should train Resilience/Avoidance appropriately. **The passive XP quantities and attribution are still undecided**; do not fabricate active die results for passive values.
- The separate **Talent progression tree**, passive armor Skill awards, and bankable critical-based **perk points** remain independent, pending later mechanics.

Code and tests: [advancement.py](../scripts/advancement.py), [trait_pools.py](../scripts/trait_pools.py), [test_advancement.py](../tests/test_advancement.py). The old 2 XP per HP, MP and 0–100 skill XP system is archived on [archive/d20-pre-geard-lif](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif).
