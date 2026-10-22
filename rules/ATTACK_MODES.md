# Attack modes and eligible defensive pools — working Elf-Books defaults

**Notation:** Specify only **Attribute + Skill** in ordinary rules. The pool calculator automatically adds the character's one Talent **if it governs the named Skill**, **one applicable declared Specialty under that Skill**, and relevant equipment/magical bonuses. Talents govern **five Skills**, not attributes. Ratings 0–25 produce one personal die per full five rating points at the chosen Tier. Same-Tier Attribute→Skill→Specialty minimum-one-die prerequisites remain in force.

For all pools (attacks, defenses, spellcasting, Cost resistance, social actions, environmental survival), **add up the eligible external bonus dice from every source**—equipment, clothing, shields, enchantments, ensorcellments, and temporary buffs. Together they **cannot exceed the unmodified personal dice pool** for this exact action. Example: a six-die personal Dodge pool can receive at most **six** extra dice total, even with an enchanted shield, a ring, and an active magic buff each proposing four. Bonuses must also be relevant and meet their own eligibility/Tier rules. This cap never increases marks per grade.

## Attack-mode contract

A potentially contested effect specifies its **mode**, **Accuracy pool**, any **Potence pool**, **allowed defensive pools and their conditions**, and targeted **resource track**. The target selects **one available defense** and supplies `floor((personal defense dice + legal external dice)/2)` static Application opposition. Equality means the attacker applies successfully. Only then roll Potence and determine mark severity using the relevant track's Resilience/effective grade threshold. **The mode, not the damage element, decides which defenses are possible.** Do not give universal Dodge/Block/Parry against every hostile effect.

These are working **default mode menus**, subject to weapon technique, narrative positioning and reaction availability. A nonexistent shield doesn't grant Block, an unaware target cannot use awareness-dependent evasion, and counters require a legal reaction/ability. The [structured catalog](attack_modes.json) is the authoritative list of names and conditions.

| Mode | Typical defender pools | Default exclusions |
| --- | --- | --- |
| Melee contact | **Agility + Dodge**, **Dexterity + Block**, **Dexterity + weapon Skill** for a feasible Parry | Impractical reactions, unsuitable implement |
| Arrow/thrown projectile | **Agility + Dodge**, **Dexterity + Block** with suitable shield | **Parry** |
| Ice spear / magical missile | Same Dodge/Block; **Wits + Mysticism** counterspell if permitted | **Parry** |
| Cold exposure | **Health + Survival** | Physical Block/Parry/Dodge |
| Direct freezing Malediction | **Health + Survival**, or **Wits + Mysticism** when countermagic is available | **Dodge, Block, Parry** |
| Social persuasion | **Insight + Speechcraft** to critically evaluate, **Temperance + Speechcraft** to maintain composure, **Wits + Lore** where factual verification is available | Physical defenses; Conviction as Avoidance |
| Social deception | **Insight + Speechcraft** to discern lies, **Wits + Lore** to verify facts when applicable | Physical defenses |
| Social intimidation | **Temperance + Speechcraft** to resist emotional pressure, **Insight + Speechcraft** to recognize bluffs | Physical defenses; Conviction as Avoidance |
| Social reputation/shame | **Insight + Speechcraft** to challenge framing, **Temperance + Speechcraft** to withstand shame, **Wits + Lore** to verify claims | Physical defenses; Conviction as Avoidance |
| **Supernatural identity Malediction** | **Temperance + Speechcraft** to resist intrusion, or available **Wits + Mysticism** counterspell | Physical defenses; Conviction as Avoidance |

In a *direct freezing Malediction*, an attacker does not conjure an interceptable ice spear: the cold directly assaults the victim, so they withstand it via the **same Health + Survival pool as adverse weather**. A physically traveling ice spear instead permits Dodge or shield Block, as does an arrow; none is normally Parried. Counterspelling remains an ability-dependent alternative, not a free defense added atop survival or Dodge.

## Default social attack modes

Four **mundane** social modes are the initial playtesting options: **Persuasion, Deception, Intimidation, Reputation**. Their usual Accuracy is **Insight + Speechcraft**, except physically imposing **Intimidation uses Strength + Speechcraft** to establish the threatening opening. Their typical Potence is **Charisma + Speechcraft** to establish its social effect. Cross-category Attributes are entirely legitimate when the described method fits; explicit alternatives can be defined by particular actions. The catalog separately includes a sample *supernatural identity Malediction* to test Plasticity protection.

**All mundane social attacks target Soul/Attention (fast), never Plasticity directly. Only supernatural attacks may target Plasticity directly. However, if Attention was already exhausted before a new mundane social effect, the entire subsequent Attention-targeted effect overflows into Plasticity.** Long-term mundane reputation, relationship and identity consequences are still possible through narrative outcomes, institutions and Projects—not direct Plasticity injury. **Conviction provides both Soul resource mark capacity and baseline mark-severity resistance (soak), never ordinary social Avoidance**: avoid the pressure using Insight, Temperance or other applicable methods rather than treating resilience as evasion. Ordinary conversation does not automatically inflict marks; consequences require real stakes and a legitimate Project or contested effect.

These are *default attack modes*, not a final social-vulnerability, agency or status model. No automatic social mind control from high Charisma; what a completed social Project does in the fiction remains bounded by the narrative situation and separately specified action.

## Magic and equipment integration

- A targeted Destruction spell retains **Perception + Destruction** Accuracy, **Intelligence + Destruction** Potence, and **Will + Destruction** static Mana-Cost resistance. All three automatically include Mage Talent if it covers Destruction and the relevant Firebolt/Frost Specialty when possessed. See [magic](../design/MAGIC.md).
- A freezing **direct Malediction** names Health + Survival as its default *application-resistance* pool even though Health is also Body Resilience; the 12 attributes do **not** restrict defenses to only Avoidance-function attributes.
- Armor/protective effects sometimes also raise the **effective injury severity threshold** separately from attack Avoidance. Their dice bonuses must obey the combined cap, and no effect silently increases mark-slot capacity.
- External dice cap applies equally to **static spell Cost resistance** and **defense**: bonuses from robes, enchanted rings and ongoing protective spells together cannot exceed the unmodified four-source personal pool at the relevant Tier.

## Open detailed rules

Exact shield/weapon defense requirements, Parry reaction costs, counterspell timing, social consequences, duration/area applicability, and equipment price/bonus values require further design. Generic action legality and static opposition are implemented and tested in [attack_modes.py](../scripts/attack_modes.py) and [test_attack_modes.py](../tests/test_attack_modes.py). [Migration checklist](../MIGRATION_BACKLOG.md).

## Universal fast-resource exhaustion routing

**A hit that *first exhausts* the fast resource stays on that resource. The *next* incoming fast-targeted effect redirects to the same aspect's slow resource.** This includes natural hazards, hostile attacks, social contests, and self-Costs: **Fatigue → Injury**, **Mana → Spirit**, **Attention → Plasticity**. The effect keeps its complete magnitude and is graded against the **actual slow destination's threshold**, not necessarily the mitigation that protected the fast resource. It cannot hit both in one incident. Once fast recovers below exhaustion, normal routing resumes.

This means ordinary intimidation still names **Attention**, passes the ordinary social legality check, and can damage **Plasticity indirectly by overflow** after Attention exhaustion. It does not become a supernatural Plasticity-targeted attack. The sample supernatural identity Malediction can target Plasticity *directly* even if Attention is available. [Tested attack-mode adapter](../scripts/attack_modes.py).

## Perk-only exception: Deflect Arrows

Without perks, `launched_projectile` arrows allow Dodge or eligible shield Block, **not ordinary Parry**. A defender possessing **Deflect Arrows** can instead choose an eligible **Dexterity + One-Handed/Two-Handed Parry** with a real parrying weapon **against an arrow** as their **one selected defense**, paying the ordinary **one action** and the parry weapon's normal **Fatigue Cost = max(0, Damage, Defense)**. This is an **opt-in perk exception**, not a modification of the default catalog mode. It grants no free reaction and no assumed Parry against bullets, magical ice spears or direct Maledictions. See [combat perk pilot](../design/COMBAT_PERK_PILOTS.md) and [tested adapter](../scripts/combat_perks.py).

**Perk dice and external cap:** Extra dice granted by a legitimate skill perk are logged as `perk_skill` and contribute to the final action or defensive roll, but **cannot increase the combined external equipment/magic bonus limit**. Calculate the underlying Attribute + governed Talent + Skill + eligible Specialty **rated personal pool** first; combined eligible equipment/buff/enchantment modifiers still cannot exceed that pool, regardless of added perk Skill-equivalent dice. The [named pool calculator](../scripts/attack_modes.py) now distinguishes `personal_dice`, `external_dice` and `perk_skill_dice`; a perk is separately responsible for authorizing its number of dice.
