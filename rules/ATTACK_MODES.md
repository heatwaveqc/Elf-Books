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
| Social persuasion | **Insight + Speechcraft** to critically evaluate, **Temperance + Speechcraft** to remain composed, **Conviction + Speechcraft** to defend explicit values | Physical defenses |
| Social deception | **Insight + Speechcraft** to discern lies, **Wits + Lore** to verify facts when applicable | Physical defenses |
| Social intimidation | **Temperance + Speechcraft** against pressure, **Conviction + Speechcraft** to stand firm | Physical defenses |
| Social reputation/shame | **Insight + Speechcraft** to challenge framing, **Conviction + Speechcraft** for identity, **Wits + Lore** to verify factual claims | Physical defenses |

In a *direct freezing Malediction*, an attacker does not conjure an interceptable ice spear: the cold directly assaults the victim, so they withstand it via the **same Health + Survival pool as adverse weather**. A physically traveling ice spear instead permits Dodge or shield Block, as does an arrow; none is normally Parried. Counterspelling remains an ability-dependent alternative, not a free defense added atop survival or Dodge.

## Default social attack modes

Four social modes are available as initial playtesting options: **Persuasion, Deception, Intimidation, Reputation**. In a consequential hostile contest the attacker's default **Accuracy** is **Insight + Speechcraft** (finding an applicable opening) and **Potence** is **Charisma + Speechcraft** (how strongly it changes the situation). Legitimate alternative Skills/methods can be defined by particular actions.

Typical immediate social strain lands on **Soul/Attention** (fast), and lasting damage to identity, belonging, or social adaptation can land on **Soul/Plasticity** (slow). **Conviction**, not Will, sets mark slots on both. Ordinary conversation does not automatically inflict resource marks: an attack requires genuine stakes, declared mode, an appropriate target and Project framing. Reputation attacks can also involve a Project representing an audience or institution, not just marks on one person's track.

These are *default attack modes*, not a final social-vulnerability, agency or status model. No automatic social mind control from high Charisma; what a completed social Project does in the fiction remains bounded by the narrative situation and separately specified action.

## Magic and equipment integration

- A targeted Destruction spell retains **Perception + Destruction** Accuracy, **Intelligence + Destruction** Potence, and **Will + Destruction** static Mana-Cost resistance. All three automatically include Mage Talent if it covers Destruction and the relevant Firebolt/Frost Specialty when possessed. See [magic](../design/MAGIC.md).
- A freezing **direct Malediction** names Health + Survival as its default *application-resistance* pool even though Health is also Body Resilience; the 12 attributes do **not** restrict defenses to only Avoidance-function attributes.
- Armor/protective effects sometimes also raise the **effective injury severity threshold** separately from attack Avoidance. Their dice bonuses must obey the combined cap, and no effect silently increases mark-slot capacity.
- External dice cap applies equally to **static spell Cost resistance** and **defense**: bonuses from robes, enchanted rings and ongoing protective spells together cannot exceed the unmodified four-source personal pool at the relevant Tier.

## Open detailed rules

Exact shield/weapon defense requirements, Parry reaction costs, counterspell timing, social consequences, duration/area applicability, and equipment price/bonus values require further design. Generic action legality and static opposition are implemented and tested in [attack_modes.py](../scripts/attack_modes.py) and [test_attack_modes.py](../tests/test_attack_modes.py). [Migration checklist](../MIGRATION_BACKLOG.md).
