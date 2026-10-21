# Elder Scrolls perk conversion survey — first pass

**Status: SOURCE-GROUNDED DESIGN SHORTLIST ONLY, NOT PLAYABLE PERKS.** This is a starting point for reviewing the actual Elder Scrolls games, **not** a wholesale adoption of every perk or an alteration to the 48 existing provisional perk seeds. The annotated [75-candidate source crosswalk](tes_perk_candidates.json) retains names, source game, original skill gate, a short independent mechanic summary, link to its source, and `direct/convert/reject/missing` classification.

## Sources and scope

- [Skyrim vanilla perk database](https://www.gamebanshee.com/skyrim/skills.php), linking all **18** original perk trees. These pages give original names, requirements, and behavior; **ignore Ordinator and other modded overhaul trees** for this initial vanilla survey.
- [Oblivion mastery bonuses](https://steamcommunity.com/sharedfiles/filedetails/?id=1092346033), including Acrobatics, Athletics and Hand to Hand, as secondary source; these were automatically earned *in Oblivion*, whereas Elf-Books spends bankable perk points, so we borrow the *effect* not that progression method.
- The 24-skill mapping is the existing [candidate skills roster](skills_v2.json). Six skills have no one-to-one Skyrim perk tree: **Unarmed, Athletics, Dodge, Mysticism, Survival, Lore**.
- Only record small independent summaries and source names; do not paste the copyrighted descriptions or whole perk-tree entries.

**Fit classifications:** `direct` = original concept can carry over nearly unchanged once its ordinary rules objects (ingredients, spell duration, legal target, inventory) exist; `convert` = clearly TES-inspired but substantial numerical/D20 timing modification required; `reject` = copy would break our core rules or grant implausible world-level effects; `missing` = no vanilla tree to copy. **A 'direct' perk isn't executable until the underlying game subsystem exists.**

## 24-skill mapping

| Elf-Books skill | Game source | Best near-direct candidates | Conversion / caution |
| --- | --- | --- | --- |
| One-Handed | Skyrim One-Handed | None truly literal | **Critical Charge**, **Dual Flurry**, **Hack and Slash** require sprint/extra-attack/bleed rules; **Armsman** percentage damage redundant with built-in skill damage |
| Two-Handed | Skyrim Two-Handed | None truly literal | **Sweep** is an attractive multi-target maneuver but needs D20 facing/area and action economy; **Barbarian** flat percentage damage redundant |
| Archery | Skyrim Archery | **Hunter's Discipline** (recover more ammunition) | **Ranger** and **Power Shot** need movement/condition rules; **Steady Hand** time slowdown must become turn-based benefit |
| Block | Skyrim Block | **Power Bash** as an unlocked maneuver | **Deflect Arrows**, **Elemental Protection**, **Block Runner** need exact reaction/move interactions |
| Heavy Armor | Skyrim Heavy Armor | **Conditioning** (no encumbrance), **Cushioned** (less fall damage) | **Juggernaut** multiplying equipment AC rejected: overloads no-base-10 defenses |
| Unarmed | Oblivion Hand to Hand | No literal transplant | Ghost striking, disarming power attacks and knockdown provide concrete maneuver seeds |
| Athletics | Oblivion Athletics/Acrobatics | Attacking during a jump could fit here | Stamina-regeneration perks unusable because Elf-Books has **no Stamina**; decide whether jumping attacks are Athletics or Dodge |
| Smithing | Skyrim Smithing; Oblivion Armorer | **Arcane Blacksmith** (improve enchanted items) | **Dwarven/Daedric Smithing** recipes may be skill-gated but shouldn't ignore actual recipe/material DC |
| Alteration | Skyrim Alteration | No truly literal numerical effect | **Stability** duration, **Mage Armor** flesh protection, **Atronach** spell absorption need Magicka and AC rules |
| Conjuration | Skyrim Conjuration | **Summoner** range, **Atromancy** longer summons, **Soul Stealer** bound weapon Soul Trap | **Twin Souls** greatly affects combat action economy, check before adoption |
| Destruction | Skyrim Destruction | **Rune Master** extends rune placement range | **Impact** on spell staggering needs a saving throw or condition implementation |
| Illusion | Skyrim Illusion | **Quiet Casting** (no audible casting) | **Master of the Mind** expands valid targets, requiring exact immunity and resistance definitions |
| Mysticism | Oblivion Mysticism; Skyrim school migration | No direct standalone modern tree | Spell absorption and soul/detection mechanics are in other trees; don't pretend there's a Skyrim Mysticism perk list |
| Restoration | Skyrim Restoration | **Ward Absorb** (wards recharge Magicka) | **Avoid Death** 250-HP restoration must scale to our HP economy; **Respite** targets nonexistent Stamina |
| Alchemy | Skyrim Alchemy | **Green Thumb**, **Experimenter**, **Concentrated Poison**, **Purity** | Percentage potency buffs could be adapted, but need potion effect construction and stacking |
| Enchanting | Skyrim Enchanting | **Extra Effect** (2 enchantments/item) | **Soul Squeezer/Siphon** need soul-gem charge accounting; potency percentages require caps |
| Light Armor | Skyrim Light Armor | **Unhindered** (worn armor has no encumbrance penalty) | **Deft Movement** percent-hit-negation threatens our AC system; **Wind Walker** Stamina perk unusable |
| Dodge | Oblivion Acrobatics | Jumping attack movement is plausible | Rapid dodge-roll needs reaction/action rules; original Acrobatics granted its Dodge ability automatically |
| Sneak | Skyrim Sneak | **Light Foot**, **Silence** (no extra noise while running) | **Shadow Warrior** disengage/hide midcombat needs detection timing; 6× sneak-damage would be excessive |
| Security | Skyrim Lockpicking | **Quick Hands**, **Wax Key**, **Unbreakable** | **Treasure Hunter** alters preexisting world loot and is wrong for grounded GM world inventories |
| Legerdemain | Skyrim Pickpocket | **Poisoned**, **Misdirection**, **Perfect Touch** | Requires precise target awareness, carried/worn object access, and existing theft checks |
| Speechcraft | Skyrim Speech | **Merchant** (unusual inventory categories may be bartered) | Bribery and Investor need social/world economy; global **Master Trader** adds currency to every merchant (reject) |
| Survival | None directly | None | Design from TES hunting, travel, gathering, mundane first aid, or complementary ESO lines **after** defining skill |
| Lore | None directly | None | Design from research, historical expertise, script translation and occult scholarship; don't relabel Alchemy's Experimenter without justification |

## Shortlist to prototype first

The following are the **lowest-conversion examples** worth immediate mechanical drafts. Original skill thresholds are recorded as reference; none is yet an approved Elf-Books prerequisite. A normal perk costs one earned point under [PERKS.md](../rules/PERKS.md):

| Perk | Source rank | Proposed Elf-Books rule in plain terms | Integration dependency |
| --- | ---: | --- | --- |
| **Quiet Casting** (Illusion) | 50 | Spellcasting is not audible merely because it is casting, across schools | What other sensory signs/verbal components are required |
| **Green Thumb** (Alchemy) | 70 | Each genuine plant-gathering harvest yields twice as many usable ingredients | Gathering/supply tables |
| **Concentrated Poison** (Alchemy) | 60 | One coating affects twice its usual number of successful weapon hits | Poison effects and charge consumption |
| **Purity** (Alchemy) | 100 | Separate unwanted opposite-sign alchemical effects when making potions/poisons | Ingredient effect engine |
| **Arcane Blacksmith** (Smithing) | 60 | Improve enchanted equipment by working on the item without removing its enchantment | Tempering and enchantment preservation |
| **Extra Effect** (Enchanting) | 100 | Enchant the same item with two independent effects under normal crafting requirements | Enchantment capacity and item limits |
| **Quick Hands** (Security) | 40 | Picking a lock does not automatically reveal the action to observers | Detection and suspicion |
| **Wax Key** (Security) | 50 | Opening a copyable key lock can yield a matching key copy | Key/lock ownership and material requirements |
| **Poisoned** (Legerdemain) | 40 | Secretly deposit a prepared poison on a target, to activate by the existing poison rules | Poison application and contest |
| **Misdirection** (Legerdemain) | 70 | Attempt to steal an equipped/readied weapon without the target automatically noticing | Difficulty and situational constraints |
| **Light Foot** (Sneak) | 40 | A careful stealthy movement avoids triggering ordinary floor pressure plates | Deliberately not all magical or sentient traps |
| **Silence** (Sneak) | 70 | Moving at ordinary walking/running speed introduces no *additional* noise penalty | It doesn't confer total invisibility |
| **Conditioning** (Heavy Armor) | 70 | Worn heavy armor has no encumbrance cost | Carrying other weight still matters |
| **Cushioned** (Heavy Armor) | 50 | Wearing a full heavy suit halves falling damage | Falling damage formula |
| **Unhindered** (Light Armor) | 50 | Worn light armor does not contribute to encumbrance | Light armor still affords its normal protection |
| **Hunter's Discipline** (Archery) | 50 | Recover twice the usual usable ammunition after an encounter | Recovery supply bookkeeping |

## Do not blindly copy these systems

1. **Percentage damage trees:** Skyrim's `Armsman`, `Barbarian`, and `Overdraw` grant repeated +20% increments, eventually up to +100%. Elf-Books already grants **+floor(skill/5) flat damage**. Copying those on top produces excessive high-skill power and accelerates 2×effective-damage XP. Likewise `Juggernaut` and `Agile Defender` multiply armor rating despite our balanced additive AC.
2. **Stamina-based perks:** There is no Stamina pool. Restoring, regenerating, or reducing Stamina expenditure has no straightforward literal effect.
3. **Slowed time / zoom:** In a turn-based chat game, `Quick Reflexes`, `Steady Hand` and `Eagle Eye` need action or aiming effects, rather than pretending an extra real-time control exists.
4. **Chance-based extra criticals:** In Elf-Books, meaningful natural 20s produce **bankable perk points**, and credible attackers' natural 1s similarly benefit defenders. A perk increasing ordinary critical *damage* is different from producing extra perk-point-generating 'natural 20' events. Never let a 10% 'critical chance' invent unrolled natural 20s.
5. **Stun/paralysis/dual wield:** D20 conditions, extra attacks and spell duration must be calibrated before `Impact`, `Sweep`, `Twin Souls`, `Shield Charge` or `Dual Flurry` become available.
6. **GM world continuity:** No `Treasure Hunter` / `Golden Touch` fabricating loot already in a chest, or `Master Trader` retroactively changing every merchant's finances. Social/market perks affect the PC's options, rather than rewriting established NPC inventories.

## Porting policy to discuss

- **Preserve original perk name and theme** wherever possible; minor clarifying wording is fine. Don't turn every original perk into an unrelated new design just to fit a neat tree.
- **Prefer original Skyrim skill gate** (e.g. Quiet Casting 50) as the starting *candidate*, but user approval is required and 24-skill category mapping can adjust it.
- **Don't automatically import Skyrim constellation parent links.** Elf-Books already gates purchases by **skill rank** and pays **one bankable point per perk**. Bring forward prerequisites only when they describe an actual technique dependency (for instance, improved shield bash requires being able to bash).
- **Do not automatically grant Oblivion mastery benefits at rank thresholds**, because the established Elf-Books model requires spent perk points. Use Oblivion for the *effect vocabulary*, not its automatic acquisition rule.
- Preserve the existing **48 prototype perk hooks** in `design/skills_v2.json` as historical design seeds. This survey replaces none until the user chooses what to port.
- **Next pass:** promote a small approved subset into full perk definitions (source name, target skill, threshold, point cost, prerequisite, operative D20 trigger/action, resolution, duration, stacking, XP interaction, GM persistence), then test combinations with the skill/AC systems.

**Catalog count (research-only):** 75 surveyed entries across the 24 skill mappings: **28 near-direct, 35 needing conversion, 10 rejected, 2 without a vanilla counterpart**. These are counted *candidates*, including explicit reject examples and duplicated jump-attack inspiration, not 75 finalized perks.
