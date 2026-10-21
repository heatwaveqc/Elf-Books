# Spell parameters — preliminary surcharge schedule

**Status:** Working test-price schedule, **not final balancing**. Governing design decisions are adopted in [Magic](MAGIC.md); precise costs remain subject to testing. All prices below are **fixed Cost-success equivalents** recorded in a spell's formula at design time. They are not additional Potence successes, not discounts from effect strength and not user-selectable parameters at casting. Design inspiration: GURPS Thaumatology's parameter approach; **no GURPS cost tables are reproduced**.

| Parameter | Working Cost-success surcharge | Notes |
| --- | --- | --- |
| Range | Self, touch or ≤10 m: +0; ≤30 m: +1; ≤100 m: +2; ≤300 m: +3; ≤1 km: +4. Roughly ×3 reach per further +1. | Range is where the spell initially reaches or places its effect. |
| Area | **+1 per metre of radius**, rounding up; single target/point +0. | Fixed-location damaging area effects may pulse every turn while active; they **do not move**. |
| Multiple named targets | First +0, 2 +1, 3–4 +2, 5–8 +3, 9–16 +4; +1 per subsequent doubling. | Use **either area or named-target targeting**, not both for the same coverage. |
| Duration | Instant or ≤10 seconds +0; ≤1 minute +1; ≤10 minutes +2; ≤1 hour +3; ≤1 day +4; ≤1 week +5; ≤1 month +6. | Repeated **damaging** effects require at least **+1** for non-instant duration, even within ten seconds (provisional minimum). |
| Movement speed | ≤1 m/s +0; ≤2 m/s +1; ≤4 m/s +2; ≤8 m/s +3; double speed per further +1. | Applies to movement spells, **not moving a persistent damaging zone**. |
| Selective area | +2 | Distinguishes allies/bystanders from valid targets in the defined area. |
| Additional distinct effects | +1 on **each additional component**, beyond the first. | Formula can only be **designed by a mage with the required multi-effect spellmaking perk**. Each component rolls Potence and pays Cost **separately**. |

**No weight surcharge.** When magic lifts or transports a heavy object, its Potence is **work against the movement Project**, whose Complexity, Recalcitrance, Scope and Time incorporate the object's difficulty. No duplicate surcharge for mass. Non-damage utility spells also use Potence in their actual Project/effect resolution.

## Duration with harmful effects — adopted operation

A damaging spell with a designed non-instant duration may inflict its original **cast Potence magnitude again each turn**; it is **not** limited to cosmetic persistence.

- **Stationary damaging area:** the area is anchored where placed, cannot chase foes or be relocated. Exposure each turn triggers the spell's stated harm. Ordinary movement can remove the victim from danger. Movement of the zone would require a **separately designed special effect**, not free duration.
- **Single-target physical continuing harm** (e.g., ignited clothing/body): attaches to the original subject, cannot retarget, and must declare a credible **physical action or condition** to extinguish/remove it (e.g., immersion in water or actively extinguishing flames). Which action succeeds depends on the situation; do not force an arbitrary saving throw instead of a plausible solution.
- **Single-target supernatural continuing harm** (e.g., wasting curse): stays attached to the original victim. The victim must make a **new active, method-appropriate resistance roll BEFORE EACH damaging instance**. Defender successes meeting or exceeding the spell's recorded Potence magnitude **end the curse permanently and prevent that turn's damage**; failure inflicts damage at recorded Potence and the same curse continues. The first successful resistance breaks the curse, rather than merely suppressing one tick. Choose the legal Attribute + Skill by the attack mode. This is a deliberate repeat-resistance exception to ordinary static defenses; final opposition calibration remains **OPEN**.
- Unless otherwise designed, **Potence is rolled once at casting**, and that magnitude is recorded as the continuing effect's strength. **Do not reroll caster Potence or re-charge Mana each turn** simply because a persistent spell pulses; its purchased duration accounts for ongoing delivery. The caster earns XP from the real initial Potence roll, not fictional repeated rolls. Defenders can earn XP from actual resistance attempts under normal rules.
- A damaging supernatural curse ends immediately on **its first successful resistance**, and otherwise when the maximum duration expires, it is dispelled, or its subject dies. Area effects and physical burns end by their own removal conditions. The actual length of a combat turn and tick/activation timing remain a core combat-integration task.

**Curse balance:** Maximum duration does not guarantee damage for its whole length. With eight defender dice and a stored Potence of 4, an active defense succeeds about **58.01%** per turn. Five consecutive failures occur about **1.31%** of the time; ten about **0.017%** (independent, unchanged pool, target survives). The bet is whether the curse kills the target before the first successful resistance. Exact duration bands remain provisional.

## Multi-effect spell construction — adopted operation

The **perk is a design prerequisite**, not automatically a separate license required to cast a pre-existing learned multi-effect formula. A spell with several effects is still one learnable Specialty/formula; cross-School construction/practice eligibility remains to be defined.

For a combined Fire + Weakness spell, for example:

1. The designer must have the multi-effect spellmaking perk **when constructing the formula**.
2. Cast the learned combined formula as one declared spellcasting action; resolve application by the effects' delivery/defense rules (one delivery check may serve multiple components only when those components really share that mode).
3. For **each** component, roll its applicable **Potence separately**, and let the recipient resolve **its own resistance** against that component. One shared total is **not split** among components, and an effect does **not** grant its full successes to other effects.
4. **Each component generates an independent Mana Cost incident**, magnitude = **its own Potence successes + its own assigned fixed parameter surcharges**; compare against the caster's Cost resistance independently. Subsequent components check whether Mana was already exhausted and can spill into Spirit *within the same cast*. The **+1 additional-effect surcharge** belongs to that additional component.
5. These genuinely separate Potence source dice and genuine Cost-resistance events award their normal distinct XP; no double XP on a single roll and no free bonus rolls. Reusing one School/Spell Specialty across components of different colleges remains **OPEN**.

The independent Potence and Cost results make complexity both a training opportunity and an endurance hazard. There is **no pooled single compound Cost mark**.

## Evaluation cases

- **3 m fire field:** radius +3; an instantaneous hit uses initial Potence only, while the ≤10-second continuing field adds a provisional +1 duration. Stationary, same saved Potence each turn, targets can leave.
- **One-hour wasting curse:** duration +3 with one original Potence/Cost event, but before each damage tick the original victim actively resists the recorded Potence. **The first successful resistance destroys the curse**, preventing that tick and every later tick even if much of the designed duration remains. Failure damages and lets it continue.
- **Dual-effect spell:** the first component is priced and resisted normally; the second contributes at least +1 and creates its own Potence roll, defender resistance and Cost resistance. Check post-component Mana exhaustion before the next component.
