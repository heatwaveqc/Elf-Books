# Skill-based advancement — candidates for decision

**Design status: OPEN.** The mandatory default is classless, with no required character levels. This file records competing implementation choices, not a rule to use during a session.

## Goals
- Learning by use, risk, study, instruction and genuine experiences; no repetitive action spam.
- An optional starting occupation (Battlemage, Nightblade, Witchhunter) is just a template.
- A character can change vocation organically and learn any reasonable skill without permanent class restrictions.
- Skill scale and advancement must map cleanly to d20 bounded accuracy; progression must never inadvertently add +1 to a d20 roll for every one-point skill increment.
- All characters can improve noncombat as well as combat/magic capability; do not reward only rolling dice repeatedly.
- Higher mastery grows progressively harder; high-risk/high-stakes applications may teach more, but routine work can still matter.
- Failed meaningful attempts may teach something; an LLM adjudicates fictional relevance, not arbitrary proficiency gating.

## Candidate A: every meaningful use builds progress
- Award progress on a consequential use in a genuine scene; greater novelty/difficulty raises gain, regardless of success.
- At defined thresholds, advance the skill by a small amount, with rising costs.
- Most predictable pacing and least roll variance; requires anti-farming and pacing limits.

## Candidate B: meaningful use triggers a chance to learn
- One qualifying use produces a bounded chance of a small increase. Difficulty and current mastery affect probability.
- Supports the “you learned something unexpectedly” feeling; variance and farming need control.
- Save the random roll and its context; never secretly adjust outcomes to satisfy pacing.

## Candidate C: blended practice and breakthrough
- Qualifying uses add progress, and particularly novel or difficult situations may trigger an extra breakthrough roll.
- Baseline predictable with occasional surprises; greatest bookkeeping burden.

## Advancement triggering — independent of model
A **meaningful use** should change the situation or expose actual stakes, novelty, difficulty, or consequence. Do not award practice from safe repeated button-pressing, self-created no-risk checks, trivial attacks on harmless targets, or manufactured failed rolls. Allow practical work, mentorship, reading, training and research as *separate* routes with their own time/resource limits. Track a short rationale and event ID for each award.

Possible anti-exploit protections: one ordinary award per skill per consequential scene, diminishing returns on repeated problem types, training time gates, and higher costs near mastery. Avoid prohibiting routine work categorically: mundane professions should be trainable without adventuring.

## Design questions to decide together
1. Exact representation and cap for a skill (TES-like 0–100 or direct d20 rank)?
2. Every meaningful use, probabilistic use, or blended?
3. Do difficult failures grant full practice, partial, or none?
4. How much repeated experience qualifies within a scene/day/session?
5. Should skill milestones offer optional perks? How are abilities, HP and Magicka earned *without* class levels?
6. Pacing target: how many real scenes for a novice to become competent, and for a master?
7. Can policies differ by campaign, and how do we compare their power curves?

## Evaluation before adoption
Simulate representative advancement logs: a fighter using one skill often, a generalist, a scholar, a pacifist and a mage. Compare capability after 10/50/200 consequential encounters; measure expected progress, variance, mastery time and exploit incentives. Define time-based training separately. Lock one initial reference scheme only after these tests.
