# Elf-Books Talents: five-skill custom classes

**Status:** Structure agreed: one starting Talent per character, exactly five governed Skills, preset or custom, **with no starting-Talent perk tree**. Twelve independent Geard attributes are also agreed. The **working 0–25 rating scale and 10×-rating XP curve** are specified; total starting budget, passive-defense XP and Talent tree-node mechanics remain open. Core upstream explanation: [Attributes and Talents](../engine/geard-lif/source/Attributes_and_Talents.tid).

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

One legal active Accuracy/Potence pool consists of **floor(Attribute/5) + floor(Talent/5) if it governs the used Skill + floor(Skill/5) + floor(applicable Specialty/5)**. Each rating is 0–25 and supplies up to five dice; this is a working calibration, not an approved starting budget. No multiple Talents, no stacking multiple Specialties. Relevance selects the attribute based on *the actual action*, not automatically based on the Talent name.

**Worked examples** (illustrative ratings): a Spellsword with Talent 10, Dexterity 15, Strength 20, One-Handed 20, and Longswords Specialty 5 rolls **10d10 physical Accuracy** and **11d10 physical Potence** with a longsword. Smithing 15 without a related Specialty, using Strength 20 for a physically forceful smithing Potence roll, provides **7d10**: Talent contributes zero because Smithing is not governed.

**Starting character floor:** All five Skills named in the chosen Talent begin at **rating 5 or higher**, giving at least one die apiece; other Skills and Specialties may start at zero. All twelve Attributes begin at least rating 5. See [advancement](ADVANCEMENT.md) for the 2/1/5/10 XP multipliers and natural-10 bootstrap.

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

## Starting Talents versus acquired supernatural trees

**An ordinary starting Talent is not a perk tree.** Its five governed Skills get the Talent's extra dice, and its **actual 0–25 rating** can contribute to an eligible Skill perk's combined rating. It has **no personal nodes, perk ranks or private perk-point currency**. This holds for the twelve presets and custom five-skill packages.

Every Skill has its own independently accessible perk selection. Eligibility is based on the perk's named **Attribute + the starting Talent (only if it governs that Skill) + Skill + one permitted Specialty**, using actual ratings. Talent/Attribute/Skill/Specialty each cap at 25, so requirements above 75 need both governing Talent and an appropriate Specialty; the Talent-less ceiling is 75. See [Perks](PERKS.md).

**Acquired supernatural Talents** such as **vampirism and lycanthropy** can have their own condition-specific perk trees as later additions. They do not erase/replace the single initial five-skill Talent. Their ratings, costs, interactions with normal trait pools, and exact trees are not yet written; **never stack two Talent dice contributions** merely because such a tree exists.

## Outstanding decisions

1. **Starting budget and advancement pacing**: ratings are 0–25, one die per five levels, with a working 10×-rating XP cost and 2/1/5/10 source multipliers. The exact character creation point budget, equipment rules and long-term balance are open.
2. **Talent XP**: its own contributed dice earn one XP per success on governed skills; monitor how rapidly five-skill breadth advances its rating. The separate Talent progression **tree** remains undefined.
3. **Supernatural tree progression:** vampires/werewolves may obtain acquired condition-specific perks, but their die contributions and progression are still undefined.
4. **Attribute-selection and static defenses**: four roles named, but which aspect applies to a particular legal roll, how Avoidance is calculated, and how armor adjusts severity remain to be settled.
5. **Talent change or retraining** after character creation: one Talent at a time, but whether extraordinary circumstances allow replacing the five governed skills is not decided.

Unit-tested pool calculation and five-skill validation: [trait_pools.py](../scripts/trait_pools.py). No actual live campaign character creation until the other P0 blockers are settled.

**Universal shorthand:** Specify Attribute + Skill only. A Talent applies when it governs the named **Skill** (not the Attribute); an applicable Specialty under that Skill also contributes. One shared gear/temporary magic cap equal to unmodified personal dice applies to each pool. See [Attack Modes](ATTACK_MODES.md).
