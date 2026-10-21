# Elder Scrolls spell construction — Geard Lif adapter

**Adopted design:** Every individual spell is a School Specialty. One Potence roll supplies both its actual Effect magnitude and the variable part of its Mana Cost. Fixed spell parameters add Cost-success surcharges. Studying a spell is self-governing through Specialty XP, not a Scope-bearing design Project. **Still open:** exact parameter price table, sustained effects, multi-effect allocation, non-damage templates and other spell-by-spell balance. Generic non-spell Geard Lif Costs are unchanged.

See [resource tracks](../engine/geard-lif/source/Resource_Tracks.tid), [advancement](../rules/ADVANCEMENT.md), and [named action pools](../engine/geard-lif/source/Named_Action_Pools_and_Defense_Modes.tid). Mind/Will owns Mana and Spirit; Soul/Conviction owns Attention and Plasticity. There are no d20 spell slots or numeric MP.

## Learning, studying and inventing spells

- A **specific designed formula** (effect(s), relevant School, range, area, targets, duration and other parameters) is a distinct **Specialty** under its School Skill. Materially altered parameters constitute a different formula; they are not improvised free of study.
- **Specialty rating 0** means **unknown and uncastable**. To learn or invent it, undertake a genuine **Intelligence + School Skill** study roll, declaring that spell Specialty as the learning target.
- Each study attempt requires **one hour**. Default **research difficulty 5** is **Complexity 5**, not Recalcitrance: Complexity checks whether the research attempt attains its immediate objective; Recalcitrance grades marks in a Scope-based Project, which we explicitly do **not** use here. Successful studies may establish concrete understanding in the fiction, but there is **no extra completion bar** beyond purchasing Specialty rating 1.
- All meaningful study rolls earn ordinary source-die XP, even when Accuracy falls short of Complexity 5. Every natural 10 in that roll grants the declared **under-5 spell Specialty** a surrogate Specialty learning success (**10 XP at Tier 0**) and may also bootstrap an under-5 School Skill, under the standard advancement rules. Do not award learning XP for consequence-free manufactured reroll loops.
- **Purchase Specialty rating 1** using study-earned XP (10 XP to go 0→1 at Tier 0). **This is learning the spell** and unlocks casting. Ratings **1–4** permit casting but add no Specialty dice; rating **5** adds the first die. Existing Tier gates still govern contributions.
- A known spell may be studied to improve its Specialty, with the same **one-hour Intelligence + School** rolls. Genuine use also develops the spell through ordinary XP. Once the Specialty has rating 5+, its source dice earn normal Specialty XP instead of sub-5 bootstrap.
- Where multiple Schools or unusual effects are involved, which School houses the Specialty remains to be decided. Studying does not grant a new Talent or change a class.

## Constructing the spell

Inspired by classic Elder Scrolls spellmaking and the **parameter-priced flexible magic** approach of **GURPS Thaumatology / Ritual Path Magic**, formulas declare their **effect, delivery, power, range, area, number of targets, duration and any combined effects** when designed. This is a design inspiration, not a port of another game's exact copyrighted pricing table.

**Extended range, larger area, multiple targets, longer duration, and multiple effects** are priced as **fixed, nonnegative Cost-success surcharges**. Costs are recorded in the learned formula **before casting**, in the spell's applicable Tier. Efficient scaling should make larger area, target counts and duration grow in sensible *bands* rather than rigidly multiplying expense per creature or second. Precise bands and prices are **OPEN**; do not invent them ad hoc in live play.

These fixed surcharges are **not Potence dice**, do **not** improve the effect, and do **not** make failed Accuracy succeed. A caster can voluntarily omit Potence dice before rolling to make the same known formula less powerful and reduce only the variable Cost; the fixed parameter surcharge remains. Combined-effect output distribution, sustained upkeep and whether an unusual effect needs a base surcharge are still open.

## One Potence roll powers the spell AND determines Cost

| Function | Named pool | Resolution |
| --- | --- | --- |
| Application | **Perception + School** | Roll Accuracy if the effect needs an application test. Compare to the valid static defense or Complexity. |
| Effect | **Intelligence + School** | Roll Potence **once**, even on a missed application. On a successful application, its actual successes are the spell's output magnitude. |
| Mana Cost | **Will + School** | **No independent spell Cost roll.** Raw Cost magnitude = **rolled Potence successes + fixed designed parameter surcharges**; grade it against static Cost resistance. |

Include one applicable Talent and the actual spell Specialty automatically in each named pool. Unknown spells (Specialty 0) cannot be cast. A self-targeted effect may not need Accuracy, but still rolls Potence and pays Cost. **Misses still cost Mana**: an Accuracy miss suppresses the target effect, **not** the Potence/Cost roll. Potence zero may still incur the positive parameter surcharge.

The shared Potence result awards **one set of active source-tagged XP**, never two. Genuine Cost resistance may separately award the usual *passive* resistance XP.

**Static Mana Cost resistance** = `floor((Will dice + eligible governed Talent dice + School dice + relevant Spell Specialty dice + eligible cost-reducing external dice) / 2)`. Sum and floor once; the shared cap on all external dice applies. Neither better Skill nor equipment reduces rolled Potence successes or the fixed parameter surcharge; they may raise the **Cost severity threshold**.

**Mana and Spirit capacity** = `floor(Will rating / 5)` slots per grade at the chosen Tier. The School, Talent, Specialty, robe and other protections do **not** add slots. The zero-static-threshold edge is still OPEN.

**Example:** Intelligence 15 (3d) + Mage Talent 10 (2d) + Destruction 10 (2d) + learned Firebolt Specialty 5 (1d) gives **8 Potence dice**. Will 10 (2d) + Talent 10 (2d) + Destruction 10 (2d) + Firebolt 5 (1d) gives **7 Cost-resistance dice** (threshold **3**), and two Mana slots per grade. Four Potence successes on a simple, surcharge-free hit mean effect magnitude **4** against the target and Cost magnitude **4** against the caster: **Middling Mana**. If a designed area version hypothetically adds **+2 Cost successes**, output remains **4** while Cost becomes **6**, yielding **Major Mana**. **+2 is merely illustrative, not an approved area-price entry.** On a miss, the effect is absent but the Cost remains. Eligible cost-reduction robes alter resistance threshold, not Cost magnitude or slots.

## Non-damage effects and defenses

Every spell does something; Potence supplies effective output for damaging magic, healing, protective thresholds, Open Lock, levitation, summons, social/identity magic, and other effects. Specific conversions (e.g. how Potence controls healing and how duration interacts with protection) remain open and need calibration. Oakflesh raises effective Injury severity resistance, not Health-mark capacity.

A launched ice spear allows eligible Dodge/Block, not ordinary projectile Parry. A direct freezing Malediction uses **Health + Survival**, like cold exposure. Reactive countermagic, when legitimately available, defaults to **Wits + Mysticism** as an *alternative* defense, not stacked with Dodge. Reaction timing and counterspell Cost remain open.

Supernatural spells may directly target Plasticity if the specific effect explicitly does so; ordinary magical attack origins do not automatically make identity attacks.

**Mana exhaustion:** When Mana was **already exhausted before** a Cost incident, redirect the entire **Potence-plus-surcharge** magnitude to Spirit, regrading it against Spirit's effective threshold. A Cost that first exhausts Mana stays there, and Mana-only reduction gear does not automatically protect Spirit. Recovery of a Final Mana slot reopens ordinary Mana routing.

## Implementation status

[Code helper](../scripts/magic.py), [tests](../tests/test_magic.py), [migration backlog](../MIGRATION_BACKLOG.md). The spell Cost adapter must use one rolled Potence result plus fixed parameters, not its earlier separate independent spell Cost roll. Numeric surcharge tables, multi-effect behavior, non-damage balancing and persistent campaign execution are not yet complete.
