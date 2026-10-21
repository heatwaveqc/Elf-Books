# Elder Scrolls spell construction — Geard Lif adapter

**Adopted design:** Every individual spell is a School Specialty. One Potence roll supplies both its actual Effect magnitude and the variable part of its Mana Cost. Fixed spell parameters add Cost-success surcharges. Studying a spell is self-governing through Specialty XP, not a Scope-bearing design Project. **Still open:** final parameter price calibration, exact turn/tick timing, non-damage templates, cross-School compound rules and spell-by-spell balance. Persistent damage and separately resisted multi-effect spells are approved Elf-Books adaptations. Generic non-spell Geard Lif Costs are unchanged.

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

**Extended range, larger area, multiple targets, longer duration, speed and multiple effects** use **fixed, nonnegative Cost-success surcharges**, with draft bands in [Spell Parameters](SPELL_PARAMETERS.md). Record them in the learned formula. **There is no weight parameter**: heavy-object motion resolves as the spell's Potence doing work against an ordinary movement Project with the required Complexity, Recalcitrance, Scope and Time. The spell *design* still has no Scope progress track. The numeric surcharge schedule is provisional pending tests.

These fixed surcharges are **not Potence dice**, do **not** improve the effect, and do **not** make failed Accuracy succeed. A caster can voluntarily omit Potence dice before rolling to make the same known formula less powerful and reduce only the variable Cost; the fixed parameter surcharge remains. **Damaging duration applies injury every turn** using the stored cast Potence, without new caster Potence/Mana rolls each tick. Stationary hazardous areas cannot move after placement; a single-target affliction remains on its original target. Mundane ongoing harm needs a credible action or condition to stop it, while supernatural ongoing curses permit a fresh active resistance each damaging turn, **ending the curse permanently on first success**. **Multiple effects require a spell-design perk**. Components roll separate Potence (not shared/split), resolve target resistance separately, and **each pays its own Mana Cost** against its own Cost resistance; components can cause Mana→Spirit overflow within one casting. Further details in [Spell Parameters](SPELL_PARAMETERS.md).

## One Potence roll **per effect** powers that effect AND determines its Cost

| Function | Named pool | Resolution |
| --- | --- | --- |
| Application | **Perception + School** | Roll Accuracy if the effect needs an application test. Compare to the valid static defense or Complexity. |
| Effect | **Intelligence + School** | Roll Potence **once for each separately resolved component**, even on a missed application. On successful application, the relevant component successes are its output magnitude. A one-effect spell has one roll. |
| Mana Cost | **Will + School** | **No independent Cost roll.** Each component has a separate self-Cost incident, raw magnitude = **that component's Potence successes + its fixed designed surcharges**; grade each against static Cost resistance. |

Include one applicable Talent and the actual spell Specialty automatically in each named pool. Unknown spells (Specialty 0) cannot be cast. A self-targeted effect may not need Accuracy, but still rolls Potence and pays Cost. **Misses still cost Mana**: an Accuracy miss suppresses the target effect, **not** the Potence/Cost roll. Potence zero may still incur the positive parameter surcharge.

Each actual component Potence roll awards **one set of active source-tagged XP**, never extra active XP for also causing Cost. Each real separate Cost resistance may separately award the usual *passive* XP. Persistent damage does not reroll caster Potence or reaward caster XP on later turns.

**Static Mana Cost resistance** = `floor((Will dice + eligible governed Talent dice + School dice + relevant Spell Specialty dice + eligible cost-reducing external dice) / 2)`. Sum and floor once; the shared cap on all external dice applies. Neither better Skill nor equipment reduces rolled Potence successes or the fixed parameter surcharge; they may raise the **Cost severity threshold**.

**Mana and Spirit capacity** = `floor(Will rating / 5)` slots per grade at the chosen Tier. The School, Talent, Specialty, robe and other protections do **not** add slots. The zero-static-threshold edge is still OPEN.

**Example:** Intelligence 15 (3d) + Mage Talent 10 (2d) + Destruction 10 (2d) + learned Firebolt Specialty 5 (1d) gives **8 Potence dice**. Will 10 (2d) + Talent 10 (2d) + Destruction 10 (2d) + Firebolt 5 (1d) gives **7 Cost-resistance dice** (threshold **3**), and two Mana slots per grade. Four Potence successes on a simple, surcharge-free hit mean effect magnitude **4** against the target and Cost magnitude **4** against the caster: **Middling Mana**. If a designed area version hypothetically adds **+2 Cost successes**, output remains **4** while Cost becomes **6**, yielding **Major Mana**. **+2 is merely illustrative, not an approved area-price entry.** On a miss, the effect is absent but the Cost remains. Eligible cost-reduction robes alter resistance threshold, not Cost magnitude or slots.

## Continuing damage and compound effects

**Continuing harmful magic is real damage, not mere duration of appearance.** A successfully established damaging spell with duration deals the original recorded Potence each turn during exposure. Damaging area spells are anchored to their casting location and **cannot move**; victims can escape. A physically burning single victim can take a relevant action to extinguish the fire (or use a condition such as immersion); a wasting/other supernatural curse on one victim requires an appropriate **active resistance roll before each damaging turn**, against recorded cast Potence. **The first successful resistance breaks the curse permanently**, preventing the current damage and all later ticks. Failed resistance takes recorded Potence damage and the curse continues until broken, expiry, dispelling, or subject death. Subject-affixed harm follows that same subject, never retargets or becomes a moving area. Mana/XP are paid/earned for the actual initial casting only, not on fabricated Potence rolls every tick.

**Multiple distinct magical effects require a spell-design perk.** The resulting formula remains a learnable Specialty. Each component has its **own Potence roll, appropriate target resistance, and separate full Mana Cost incident**, including its individually assigned fixed parameters. The later effect may hit Spirit if earlier components exhausted Mana. Independent real rolls provide genuine training; never reuse one Potence total or grant each effect all of another effect's successes. A designer needs the perk; a separate perk prerequisite to **learn/cast** a finished compound spell is not imposed. Cross-School Specialty ownership remains to be settled. See [working schedule and examples](SPELL_PARAMETERS.md).

## Non-damage effects and defenses

Every spell does something; Potence supplies effective output for damaging magic, healing, protective thresholds, Open Lock, levitation, summons, social/identity magic, and other effects. Specific conversions (e.g. how Potence controls healing and how duration interacts with protection) remain open and need calibration. Oakflesh raises effective Injury severity resistance, not Health-mark capacity.

A launched ice spear allows eligible Dodge/Block, not ordinary projectile Parry. A direct freezing Malediction uses **Health + Survival**, like cold exposure. Reactive countermagic, when legitimately available, defaults to **Wits + Mysticism** as an *alternative* defense, not stacked with Dodge. Reaction timing and counterspell Cost remain open.

Supernatural spells may directly target Plasticity if the specific effect explicitly does so; ordinary magical attack origins do not automatically make identity attacks.

**Mana exhaustion:** When Mana was **already exhausted before** a Cost incident, redirect the entire **Potence-plus-surcharge** magnitude to Spirit, regrading it against Spirit's effective threshold. A Cost that first exhausts Mana stays there, and Mana-only reduction gear does not automatically protect Spirit. Recovery of a Final Mana slot reopens ordinary Mana routing.

## Implementation status

[Code helper](../scripts/magic.py), [tests](../tests/test_magic.py), [migration backlog](../MIGRATION_BACKLOG.md). The spell Cost adapter must use one rolled Potence result plus fixed parameters, not its earlier separate independent spell Cost roll. A **provisional** surcharge schedule and compound Cost sequencing are included in this adapter; final surcharge balance, non-damage effect interpretation, ongoing-effect action timing, cross-School combinations and persistent campaign execution are not yet complete.
