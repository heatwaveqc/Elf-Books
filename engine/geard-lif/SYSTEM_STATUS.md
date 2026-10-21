# Geard Lif compatibility status — snapshot review

This is a **snapshot summary** of upstream [Raven's Heart Core Design](https://github.com/heatwaveqc/geard-lif/blob/a9c72763c41663e51d5aa03722f53658b48410d3/ai/design/RAVENS_HEART_CORE_DESIGN.md). That design document is private AI/development material **and is not copied into public Elf-Books**. The four public player-audience tiddlers are the executable reference sources. Do not portray provisional mechanics as locked simply because they appear in local files.

## Locked upstream concepts

- Projects universally describe meaningful action, **including combat**: Complexity, Recalcitrance, Scope, Time.
- Accuracy governs application versus static Avoidance/Complexity; Potence governs resulting Effect versus static Resilience/Recalcitrance. High Accuracy alone does **not** automatically amplify Effect.
- Mind/Body/Soul each have a Resilience (Will/Health/Conviction) and slow/fast resource tracks: Plasticity/Attention, Injury/Fatigue, Spirit/Mana.
- Four mark grades: Minor (0 penalty), Middling (-1), Major (-2), Final (-4), with promotion, cascading and recovery. Slow resources generally recover one step/day, fast resources one step/action.
- Resource Costs are self-targeted Effect rolls without Application, not fixed-point subtractions; no reduction of Cost rating by armor or external defenses.

## Clarified Project resolution gates

- Accuracy successes **strictly greater than** Complexity/Avoidance → application succeeds; equality fails.
- After successful application, roll **Potence independently**. Potence successes **strictly greater than** Recalcitrance/Resilience → ordinary Project progress; equality fails.
- Every full multiple of positive Recalcitrance/Resilience in a successful Potence result upgrades its progress tier by one; `floor(P/R)` upgrades. This is **defined**, though the exact credited **Scope** amount per tier remains open.
- The older, locked personal **Resource Tracks** mark chart has Minor Effects below Resilience and Middling at equality. That exception/boundary is preserved, not silently overridden by the Project gate.

## Provisional upstream formulas

- d10 pool: 7,8,9 = 1 success; 10 = 2, with other faces = 0.
- Personal dice pools from Attribute, Talent, Skill, Specialty (each provisionally capped at 5); up to 20 character dice, gear up to the personal contribution, provisional combined ceiling 40.
- Tier belongs to each quantity, not the character's level; provisional conversion 10-fold between Tiers, flooring upward and multiplying downward.
- Combat uses the project framework, but equipment, hit locations, reactions, magic effects and opposed-action details are incomplete.

## Open upstream, therefore open here

- Which attributes/skills exist, which contribute to Accuracy/Potence; the 24 Elder Scrolls labels have not yet been mapped.
- Exact d10 critical success/failure and special cases, including zero Recalcitrance; ordinary Project ties at thresholds **fail**, and static target comparison is known. Do not port natural 20 or natural 1 perk triggers unchanged.
- How each Project progress tier converts into **units of Scope**, and how the strict Project-effect gate coexists with the existing Injury/Mana mark thresholds. Do not invent damage values.
- Tier anchor calibration; high-Tier equipment Control Tier versus Effect Tier.
- Mana/Fatigue/Attention expense versus regeneration, injury dynamics and survivability.
- A new practice XP metric and perk breakthrough frequency/effect conversion for the d10 engine.
- Character sheets, NPCs/monsters, enchanting/alchemy and solo-campaign save semantics.

This document is descriptive, not a patch or silent rule change to upstream Geard Lif.
