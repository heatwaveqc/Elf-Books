# Elder Scrolls magic on Geard Lif — working cast and Cost bridge

Use the [local Geard Lif rules](../engine/geard-lif/README.md), especially [Resource Tracks](../engine/geard-lif/source/Resource_Tracks.tid). This is **not** the former D20 spell economy: no fixed MP subtraction or spell slots.

## School-based three-part cast

Each spell has a **school Skill**, which is used for all three sides of its operation:

| Spell function | Attribute + school Skill | Mode |
| --- | --- | --- |
| Hit/apply spell | **Perception + that school** | Rolled Accuracy vs chosen target's effective Avoidance |
| Effect/damage | **Intelligence + that school** | Rolled Potence vs effective target Resilience |
| Resist personal Magicka (Mana) Cost | **Will + that same school** | **Static** resistance = floor(total qualifying dice/2); no additional resistance roll |

For targeted Destruction spells, all three use the **Destruction** Skill; there is **no need to switch to Restoration/Mysticism** to resist the spell's self-Cost. Standard five-skill Talent and one appropriate named spell Specialty can contribute to the two **active casting** rolls when genuinely applicable. By default, the self-Cost resistance uses the specified **Will + School Skill only** (plus applicable cost-reducing gear); Talent/Spell Specialty do **not** silently increase resistance.

**The spell's Cost magnitude is still rolled independently, unchanged**, with **no Application roll**, under Geard Lif. Compare the rolled magnitude (after any separately legal Tier conversion) to the **static effective Cost threshold**. Resisting that Cost does **not** mean rolling another pool. The same Minor/Middling/Major/Final grade rules apply. No armor-like mitigation removes dice from the Cost roll.

**Crucially:** **Conviction** determines the number of available **Mana marks at every grade**, via its own Resilience rating. It is **not** replaced by Will; Will and the School Skill determine *only the effective severity threshold for that particular Cost*. A cost-reducing robe adds eligible **equipment dice to the Will + School Cost-resistance pool before halving and rounding down**. It does **not** give more Mana mark slots, lower the original Cost dice or grant equipment practice XP. The current provisional equipment dice ceiling (at most personal dice contributed) still applies. The actual robe bonuses remain to be priced.

### Illustrative Destruction Cost

At Tier 0, Will 10 contributes **2 dice**, Destruction 10 **2 dice**: 4 dice, hence static Cost resistance **2**. Conviction 15 provides **3 slots per Mana grade**. A Cost that rolled **2** successes therefore inflicts **one Middling Mana mark**. Add robes granting two legal resistance dice: the static resistance is now **3**; the same rolled Cost 2 causes **one Minor Mana mark**, while mark capacity stays at **3 per grade**.

The zero-static-threshold edge case remains open, rather than silently imposing one mark or an unstated minimum.

## Defending against hostile magic

When the defender can legitimately attempt a reactive **counterspell**, use **Wits + Mysticism** as the normal defensive package, plus their chosen Talent if it governs Mysticism and any applicable counterspell Specialty. Treat the result as a chosen static defensive option: `floor(total qualifying dice / 2)`, **not an additional bonus stacked on Dodge**. Spell Accuracy **meets or exceeds** this opposition to land the spell. Reaction availability, counterspell costs, timing, and interaction with persistent wards still need definitions.

**School rationale:** Mysticism is a better TES fit for direct Dispel/countermagic (see [Oblivion Mysticism](https://cs.uesp.net/wiki/mysticism) and [Oblivion's Dispel spell list](https://www.gamebanshee.com/oblivion/spells/mysticismnovice.php)). Restoration remains home to Skyrim-style wards; Alteration to flesh/altered-body protection and other alteration effects. Particular spells/perks can specify a justified different method.

## Other magical effects and scope

- **Oakflesh-like protection** raises the effective **Injury grade threshold**, never Health mark capacity.
- **Restoration** can perform recovery work consistent with the existing graded resource engine; detailed Potence-to-recovery and timing still need definitions.
- **Conjuration, Illusion, Alteration, Mysticism**, and optionally **Alchemy/Enchanting** all use the universal Project system; custom time, control, duration, and scope still need conversion.
- **Passive practice XP:** on a genuine rolled Destruction Cost, Will and Destruction can each receive their Tier-specific **passive** XP (`ceil(rating/10)` at Tier 0; `rating/10×10^Tier` at Tier 1+). The caster may also earn separate source-tagged active XP from the casting Accuracy/Potence dice; do not invent defensive rolls or give robe dice personal XP.
- **Tier gating:** School dice at the selected Tier require at least one governing Attribute die at that Tier. The same skill can participate in Accuracy, Potence and Cost checks with their respective governing Attributes. Higher-Tier Costs still respect the selected resource Tier and Cost Effect conversion.

See [prototype cast/Cost arithmetic](../scripts/magic.py) and [magic tests](../tests/test_magic.py). Full live casting, Cost dice configuration, spell lists, reaction costs, Wards and balance need a later pass. [Return-to-parity backlog](../MIGRATION_BACKLOG.md).
