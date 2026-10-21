# Skill catalog and perk seeds — proposal

[Structured roster](skills.json) · [Progression proposal](../design/PROGRESSION.md) · [Prototype math](../scripts/skill_math.py)

**Status: candidate design; not yet playable.** The canonical roster presently contains **52 distinct rated skills** (19 Warrior, 9 Mage, 24 Rogue including nine Daggerfall language skills), each with a proposed perk at skill 25 and 75 (**104 initial perk seeds**).

## Coverage and version differences

The core union covers the independently trained player skills named in **Daggerfall, Morrowind, Oblivion, and Skyrim**, including names removed in later games (Thaumaturgy, Mysticism, Spear, Medium Armor, Unarmored, Medical, Running, Swimming, Climbing, Etiquette, Streetwise, language skills). Arena had no use-to-advance skill list. Online's class/guild/world **skill lines** and later spin-off ability systems are not directly comparable to 0–100 rated skills; harvest them as perk/ability sources in a later, clearly separate catalog rather than quietly pretending this file covers every TES franchise ability.

All historical names must remain discoverable. Where games rename or broaden skills, `historical_names` contains a crosswalk: **Marksman→Archery; Stealth→Sneak; Enchant→Enchanting; Speech→Speechcraft; Oblivion Blade→the relevant bladed weapon skill(s)**. An umbrella label does not create an extra rated skill. `Armorer` and `Smithing` remain distinct (repair vs making); `Security` and `Lockpicking` remain distinct (mechanisms/traps vs physical locks).

Overlapping *rated* weapon skills (Long Blade vs One-Handed, etc.) are distinct specializations. Before a roll, choose **one best applicable skill**; never add bonuses, progress or resource contributions under two labels for the same attempt. The ECL totals still count separate *earned* skill scores, which means cross-training can grant additional resource growth: assess this as a balance choice during playtests.

The category assignments in `skills.json` are **new game-design decisions** for Health/Magicka, not assertions that every TES title used these categories. E.g., historic Marksman is often a Stealth skill, whereas Skyrim assigns Archery to Warrior. This draft chooses Warrior for the shared ranged skill; review if that makes ranged thieves too tanky.

## Perk policy

Perk entries in the JSON are **original effect hooks** for future mechanical design, not verbatim skills from a Bethesda perk tree and not granted automatically. Two unlock milestones are seeded at 25 and 75; later we can define perks at 50 and capstones at 100 as needed. Each perk has a concrete direction but **no adjudicated dice/action-economy effect or point cost yet**. Choose whether threshold perks are automatic, purchased with earned perk points, or unlocked by trials **before** campaigns begin. Avoid strong perks whose effectiveness grows with every individual skill point *on top of* the +1 per five skill rank increase.

### Examples
| Skill | At 25 | At 75 |
| --- | --- | --- |
| One-Handed | Ready Grip | Flowing Strike |
| Block | Shield Wall | Turn the Blow |
| Smithing | Tempered Edge | Masterwork Forge |
| Sneak | Shadow Passage | Ghost Trail |
| Speechcraft | Read the Room | Careful Appeal |
| Medical | Triage | Field Surgeon |
| Destruction | Elemental Shaping | Focused Ruin |
| Conjuration | Stable Summons | Binding Circle |
| Enchanting | Stable Imprint | Soulwright |
| Daedric | Careful Listener | Cultural Interpreter |

## Sources for historical nomenclature (do not copy their prose)
- [Daggerfall Unity — legacy 35-skill enumeration](https://github.com/Interkarma/daggerfall-unity/blob/master/Assets/Scripts/API/DFCareer.cs)
- [Bethesda support — Morrowind skills](https://help.bethesda.net/app/answers/detail/a_id/17546/)
- [Bethesda support — Oblivion Remastered skills](https://help.bethesda.net/app/answers/detail/a_id/69731/)
- [Oblivion 21-skill index](https://www.gamebanshee.com/oblivion/skills.php)
- [Skyrim 18-skill list](https://gamefaqs.gamespot.com/pc/615805-the-elder-scrolls-v-skyrim/faqs/75930/skills)

Copyright caveat: source references are for factual name/coverage verification. The descriptions and perk hooks in Elf-Books are original.
