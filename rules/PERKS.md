# Perk Points and Breakthroughs

**Status:** Core perk-point acquisition and spending direction agreed. Exact perk effects, unlock thresholds, artifact-specific exceptions, and complete GM/event-ledger implementation remain in development. The draft 24-skill catalog's perks are currently examples, not fully specified powers.

## Core principle

**Skill ranks and perk points are different advancement resources.** Meaningful practice awards skill XP under [ADVANCEMENT.md](ADVANCEMENT.md); critical events instead award a separate, **bankable, shared pool of perk points**.

### Earning points

| Event | Perk-point award | Qualification |
| --- | --- | --- |
| Player rolls a **natural 20** in a meaningful action using a skill | **+1 point** | A **successful** skill check or a legal attack that hits automatically on natural 20; for a check where a 20 still fails the DC, it is not a successful critical |
| Attacking opponent rolls a **natural 1** against the character | **+1 point to defender** | A **credible, resolved incoming attack** against the character, providing the defense/passive-protection breakthrough opportunity without making the defender roll another d20 |
| Special artifact / unique supernatural discovery | Specific award defined by that source | Can award a point or directly confer a named perk; uncommon exceptions are explicit story/item mechanics, not ordinary trainer services |

A natural 20 is one point **per qualifying resolved roll**, not per target struck by an area attack. One enemy natural 1 grants **at most one point to the attacked character**, even if several worn armor layers, active defensive maneuvers, protections or relevant skill systems are involved. Perk-point grants are tied to the **event**, not to one XP-earning skill.

The incoming natural 1 grants a point to the **defender** even though an attacker natural 1 is an **automatic miss** and provides **zero avoided-attack skill XP**. This is deliberately a different kind of reward. Passive combat defenses (Heavy/Light Armor, and other relevant no-defender-roll protective methods) thus have meaningful opportunities for perks. Block/Dodge can also benefit from the same qualifying threat when legally in use or selected; do not fabricate a defender skill roll merely to get a point. If no defense was necessary to survive, it still can be a dramatic critical failure **if the attack was credible**.

For multiple targets, award only to each **actual attacked character for whom the attack rolled a natural 1**; one roll shared across multiple targets is still **one qualifying roll per character actually attacked**, not a reward to bystanders. No additional award when a die is re-rolled to resolve an already-resolved event; use the actual final outcome according to the game's eventual reroll rules.

**Meaningful** means a real skill use, attack or threatening opponent with actual stakes or training conditions. Genuine risky sparring or intentionally accepting exposure **is valid**; do not introduce a blanket anti-training restriction. Actions with no relevant opponent, challenge, target or conceivable consequence do not earn a point just because a d20 was rolled. Don't award points for arbitrary extra checks added for bookkeeping. No per-session or daily artificial cap is introduced.

### Banking and spending

- Perk points enter a single **untyped character-wide pool**, **not** a bucket earmarked for the skill that critted. A One-Handed breakthrough may buy an eligible Restoration perk.
- Points can be **banked indefinitely**, including before a skill qualifies for any perks. No overflow cap is established.
- An ordinary perk costs **one point**, purchased **at player discretion** whenever the chosen perk's published skill-rank and any other prerequisites are satisfied; no follow-up critical or trainer is needed. Purchase takes effect prospectively, never retroactively modifies a roll already resolved.
- Each perk may be purchased **once** unless its specific definition explicitly says repeatable. Do not choose a perk whose skill prerequisite is missing even with plenty of banked points.
- Saving, loading, retraining skills and restoring a campaign must not re-award points for events already processed. Track point ledger entries with stable event identifiers and maintain owned-perk IDs separately from unspent points.
- **Normal trainers cannot award points, unlock perks or sell perk instruction.** They may teach skill proficiency/skill XP under separately defined training procedures. Artifacts, extraordinary rituals, rare revelations and bespoke quests may grant a point or a particular perk when an individual reward explicitly says so; whether it waives prerequisites must likewise be explicit.

### Example

A beginning character has One-Handed 20 and Restoration 10, both below the draft perk gates of 25 and 75. A natural-20 sword attack awards **+1 banked point**. Later the character trains Restoration to 25 and can spend that point on an eligible Restoration perk immediately, even though the original critical happened using a sword.

During battle, three distinct enemies roll against the character; one rolls a natural 1. The character earns **one additional point**, whether armored or actively dodging. Because that attack missed automatically, **Block/Dodge/Armor receive no avoided-hit XP** from the miss. If another attack hits and inflicts genuine HP loss while armor is worn, Armor earns its normal HP-loss XP separately.

### Frequency / balance watch (no cap adopted)

At a natural-20 frequency of 5% per qualifying d20, an active character earns on average **one point per 20 meaningful attack/check rolls**. The same 5% natural-1 frequency on credible attacks against a defender provides a comparable opportunity for passive combat builds. This is **not** a guarantee after 20 rolls. A solo combat scene can produce multiple outgoing and incoming opportunities, while a condensed multi-week project can involve many real interval rolls under one chat message. The GM must faithfully award each qualifying distinct event without making extra rolls for points.

If points accumulate much faster than eligible perk variety, revise perk availability or the global point economy in a later playtest rather than silently adding a one-per-scene cap now.

## Remaining work

1. Publish real perk actions, eligibility gates and costs in the canonical 24-skill roster (initial 25/75 hooks are provisional).
2. Specify acquisition through artifacts, exceptional discoveries and supernatural boons (point vs direct perk, any waived prerequisites, temporary vs permanent benefits).
3. Define how attack rerolls, advantage/disadvantage, natural criticals and unresolved 20s interact with points; apply a consistent final-die policy.
4. Integrate character-wide banked points, event-ID duplicate prevention and purchase transactions into private campaign persistence.
5. Ensure that passive noncombat skills have fair, relevant opportunities for breakthroughs when they do not normally generate active checks.

The perk system does **not** replace or alter the accepted numerical skill XP sources in [ADVANCEMENT.md](ADVANCEMENT.md).
