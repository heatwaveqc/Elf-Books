# Elder Scrolls magic on Geard Lif — working cast and Cost bridge

Use the [local Geard Lif resource rules](../engine/geard-lif/source/Resource_Tracks.tid). **Mana and Spirit belong to Mind, governed by Will**; Soul/Conviction instead governs social and identity resilience via **Plasticity and Attention**. The six tracks remain graded, not fixed HP/MP pools. D20 spell slots are retired.

## School-based casting: three applications of the same four sources

| Spell function | Relevant attribute | Other eligible personal contributions | Resolution |
| --- | --- | --- | --- |
| Spell aiming/application | **Perception** | Applicable Talent + School Skill + Spell Specialty | Roll **Accuracy** |
| Damage/effect | **Intelligence** | Applicable Talent + same School Skill + Spell Specialty | Roll **Potence** |
| Resist Magicka (Mana) Cost | **Will** | Applicable Talent + same School Skill + Spell Specialty | **Static Cost resistance**, no resistance roll |

For a Destruction spell, the Skill is **Destruction** for *all three*. The character's chosen five-skill Talent contributes **when it governs Destruction**, including the self-Cost; it never prohibits using another school. The **one relevant, declared Spell Specialty** (e.g. Firebolt) contributes to all three when applicable. Both can substantially reduce the actual severity of repeated Costs. Tier prerequisites stay in force: a Skill needs at least one same-Tier Attribute die; a Specialty needs one same-Tier Skill die. Talent neither gates nor caps either.

The spell itself still rolls its **Cost rating** as an independent unopposed Effect (no Application roll). Do **not** subtract the caster's Will, Talent, Skill, Specialty or robe bonus from that Cost's dice or rolled successes.

**Static Cost resistance** = `floor((Will dice + applicable Talent dice + School Skill dice + declared Spell Specialty dice + legal cost-reducing equipment dice) / 2)`. All eligibility/rating conversions happen **before** summing and flooring once. Compare the unchanged rolled Cost magnitude against that effective threshold using ordinary graded mark rules.

**Mana mark capacity** is separately `floor(Will rating / 5)` slots at each of the four grades at the resource's Tier. Mind's **Spirit** track also uses Will for mark capacity. Soul's **Plasticity** and **Attention** instead have `floor(Conviction rating / 5)` slots per grade. **Talent, Skill, Specialty and robes may improve the static Cost threshold but never increase these slot capacities.** Robe/equipment dice generate no personal XP.

### Example: Firebolt and cost-reducing robes

At Tier 0, Will **10** (2 dice), a governed Mage Talent **10** (2 dice), Destruction **10** (2 dice), and Firebolt Specialty **5** (1 die) give **7 resistance dice**, static resistance **3**. Will 10 supplies **two Mana slots per grade**, regardless of this pool's total.

A separately rolled Cost of **3** successes inflicts **one Middling Mana mark**. Robes adding one eligible Cost-resistance die bring the total to **8 dice**, static resistance **4**, making the *same* Cost result **one Minor Mana mark**, with exactly **two** Mana slots per grade still available. The +1 robe die is illustrative, not a published item stat.

## Countering hostile magic

When a defender may use a reactive counterspell, the normal Elf-Books option is **Wits + Mysticism**, with an applicable Talent and counterspell Specialty. This yields a *selected alternative* static Avoidance, `floor(total dice / 2)`, not something automatically stacked with Dodge or an independent ward. **Mysticism** fits the Oblivion dispelling tradition; Restoration can represent Skyrim-like wards and Alteration can protect the body. Exact timing, reaction limits and counterspell Costs remain open.

## Costs, XP, and remaining spell mechanics

- **On a genuine Magicka Cost**, each *actually contributing personal resistance trait*—Will, School Skill, governed Talent, and declared Spell Specialty—may receive passive practice XP: `ceil(rating/10)` at Tier 0, exact `rating/10 × 10^Tier` at higher Tiers. The spell's active Accuracy/Potence dice separately earn their usual source XP. No invented resistance roll or robe XP.
- **Oakflesh** raises the effective Injury-grade threshold without increasing Health capacity. The specific protection bonus is unfinished.
- Restoration recovery, summoning, duration, concentration, area, range, school-specific spell Costs, resource-exhaustion consequences, and ward mechanics still require content design.
- The existing zero-static-Cost-threshold case remains open; don't silently divide by zero or invent free spellcasting.

See the [tested helper](../scripts/magic.py), [unit tests](../tests/test_magic.py), and [migration checklist](../MIGRATION_BACKLOG.md).

## Missile versus direct magical effect

A flying ice spear is a projectile and normally permits Dodge or a suitable Block, not Parry. A *nonmissile freezing Malediction* directly affects the target and uses **Health + Survival**, exactly like cold weather. The defender may alternatively select Wits + Mysticism only where an available counterspell reaction permits it. See [Attack Modes](../rules/ATTACK_MODES.md). All eligible cost-reducing robes, enchantments, ensorcellments and temporary spell buffs share **one aggregate external-dice cap equal to unmodified personal Cost resistance dice**; it never increases Will's Mana-mark capacity.
