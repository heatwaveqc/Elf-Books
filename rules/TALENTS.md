# Elf-Books Talents: five-skill custom classes

**Status:** Structure agreed: one Talent per character, exactly five governed Skills, preset or custom, and a personal progression tree. Twelve independent Geard attributes are also agreed. The **rating cap of 5, starting budget, Talent improvement and actual tree-node mechanics** remain provisional. Core upstream explanation: [Attributes and Talents](../engine/geard-lif/source/Attributes_and_Talents.tid).

## Attributes (all independent)

| Function | Body / physical | Mind / mental | Soul / social |
| --- | --- | --- | --- |
| Potence | **Strength** | **Intelligence** | **Charisma** |
| Accuracy | **Dexterity** | **Perception** | **Insight** |
| Avoidance | **Agility** | **Wits** | **Temperance** |
| Resilience | **Health** | **Will** | **Conviction** |

The three Resilience attributes belong to the twelve: **Health, Will, Conviction are not derived or additional thirteenth–fifteenth stats**. They determine each corresponding aspect's resource marks per grade. Armor and other equipment can alter injury severity thresholds, not resilience-based capacity. For static Avoidance, the relevant attribute is conceptually Agility/Wits/Temperance, but its final numerical derivation has not been chosen.

See [machine-readable attribute roster](attributes.json).

## Talent as a personal class affinity

A character chooses **exactly one named Talent** at creation. It must govern **exactly five distinct** entries from the canonical [24-skill catalog](skills.json). Choose a preset from [talents.json](talents.json) or build a **custom class Talent** with any five distinct skills and a personal name.

This is *not* a class restriction. A Nightblade can train Smithing, cast Restoration, purchase ordinary Restoration perks, and learn a Smithing Specialty despite neither skill being part of Nightblade. The only difference is that these Skills receive **no Talent dice** from Nightblade.

One legal active Accuracy/Potence pool provisionally consists of **one suitable Attribute + the chosen Talent rating if it governs the used Skill + that Skill's rating + one applicable Specialty rating**. No multiple Talents, no stacking multiple Specialties. The provisional cap is five dice per source, not an approved starting budget. Relevance selects the attribute based on *the actual action*, not automatically based on the Talent name.

**Worked examples** (illustrative ratings): a Spellsword with Talent 2, Dexterity 3, Strength 4, One-Handed 4, and Longswords Specialty 1 rolls **10d10 physical Accuracy** and **11d10 physical Potence** with a longsword. Smithing 3 without a related Specialty, using Strength 4 for a physically forceful smithing Potence roll, provides **7d10**: Talent contributes zero because Smithing is not governed.

## Initial preset options

These are **sample packages**, not rigid vocational tracks; a player can create their own any-five mix. The [structured presets](talents.json) are the authoritative names and membership.

| Talent | Five governed Skills |
| --- | --- |
| **Warrior** | One-Handed, Two-Handed, Block, Heavy Armor, Athletics |
| **Mage** | Alteration, Conjuration, Destruction, Illusion, Restoration |
| **Thief** | Sneak, Security, Legerdemain, Speechcraft, Dodge |
| **Spellsword** | One-Handed, Light Armor, Alteration, Destruction, Restoration |
| **Battlemage** | Destruction, Alteration, Heavy Armor, One-Handed, Enchanting |
| **Nightblade** | Sneak, Illusion, One-Handed, Security, Legerdemain |
| **Ranger** | Archery, Survival, Sneak, Light Armor, Athletics |
| **Artificer** | Smithing, Enchanting, Alchemy, Lore, Mysticism |
| **Monk** | Unarmed, Dodge, Restoration, Athletics, Illusion |
| **Crusader** | Heavy Armor, One-Handed, Block, Restoration, Speechcraft |
| **Scholar** | Lore, Mysticism, Alteration, Alchemy, Speechcraft |
| **Scout** | Archery, Survival, Athletics, Dodge, Lore |

Custom Talent creation only needs a name and five skill IDs; no *race, origin, morality, or faction* limits apply by default.

## The separate Talent progression tree

A Talent also owns an **additional advancement tree**, representing its distinctive cross-skill synergies and vocation. Its basic tree contract is:

- One character-selected Talent = **one** available Talent tree, in addition to all ordinary Skill perk options.
- A **custom Talent gets a genuine custom tree**, not a missing/penalized tree.
- Talent progress, tree-node eligibility, costs, ranks, choices and effects require separate balancing. Do **not** pretend these nodes are already published or that they automatically consume the bankable general-perk points.
- Ordinary Skill XP and skill perks for all 24 skills remain available whether governed or not. The previously preferred **bankable perk-point** concept survives independently until a specific Talent-tree currency rule is decided.
- Possible branches for later testing: **Integration** (synergies between two of the five governed Skills); **Technique** (narrow specialty capability); **Identity** (a signature move/quality). These are *design seeds*, not mechanical grants.

## Outstanding decisions

1. **Starting budgets and actual trait-rating progression**: the 0–5 individual rating cap, personal total pool ceiling and equipment caps are upstream provisional.
2. **How a Talent learns** from varied use of five governed skills; ensure extra dice do not grow faster than challenge capacity and don't incentivize selecting only the highest-volume combat skills.
3. **How the Talent tree awards nodes** (level thresholds, choices, use-based triggers or perk points); custom-tree generation requirements, GM consistency and documentation.
4. **Attribute-selection and static defenses**: four roles named, but which aspect applies to a particular legal roll, how Avoidance is calculated, and how armor adjusts severity remain to be settled.
5. **Talent change or retraining** after character creation: one Talent at a time, but whether extraordinary circumstances allow replacing the five governed skills is not decided.

Unit-tested pool calculation and five-skill validation: [trait_pools.py](../scripts/trait_pools.py). No actual live campaign character creation until the other P0 blockers are settled.
