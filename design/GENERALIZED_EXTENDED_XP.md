# Generalized skill checks, extended projects and XP

**Approved award rates:** The numeric quick- and extended-check rules are consolidated in [ADVANCEMENT.md](../rules/ADVANCEMENT.md): quick success 2×DC, meaningful failure 0.5×DC, and extended 0.1×credited progress. This document retains its earlier proposal language and explains the adjudication and design rationale.

**Defensive application:** [MAGIC_DEFENSE_XP.md](MAGIC_DEFENSE_XP.md) proposes 2× the attacker's *full result* for a meaningful defense-mediated avoidance; this extends quick-check effective-DC thinking to combat without inventing a fresh d20 roll.

**Pacing follow-up:** [simulated solo-chat comparisons](SOLO_PACING_COMPARISON.md) investigate XP by player exchange versus in-world weeks and demonstrate why project goals must be grounded in real work. The 0.1 XP/progress and quick 2×DC/0.5×DC rates remain trials, not finalized.

**Rule design status:** The player selected D&D 3.5-style extended progress for *all* substantial skill projects: a **DC**, a **fixed interval**, a **progress goal**, and `Progress Gained = Check Result × DC` on a successful interval check. The XP multiplier for actual project progress is **not yet final**. For quick checks, **2×DC on success** and **0.5×DC on failure** are the current candidate rates. Opposed checks use the opponent's actual check result as the effective DC. Existing approved XP threshold and combat formula are unchanged.

## Accepted underlying XP scale

```text
XP to next skill rank = 5 × max(1, current skill)
Weapon offensive XP = 2 × actual enemy HP removed
Weapon skill contribution = floor(skill / 5) to attack and flat damage
```

The game can store XP in **integer tenths** (`xp_tenths`) to handle a failed DC 25 check granting 12.5 XP and an extended project making progress of 257, granting 25.7 XP if the proposed 1 XP/10 progress rate is chosen. One skill rank requires `50 × max(1, current skill)` tenths; weapon damage awards `20 × actual HP removed` tenths. No floating point or rounding losses are needed.

## Quick checks — proposed XP rate

Only **one meaningful attempted objective** awards quick-check XP. Don't equate it to each die roll or multiple rolls against one unchanged obstacle.

```text
Quick check succeeds: skill XP = 2 × effective DC
Quick check fails:    skill XP = 0.5 × effective DC
```

A real failure can teach despite not accomplishing the objective, but it must involve a **genuine attempt with a credible possibility of learning**: e.g. alerting a guard, committing effort, losing materials, revealing information or encountering a genuinely difficult physical problem. Trying to talk a rock into becoming an emperor, repeatedly rolling an impossible challenge from the same unchanged position, or making unnecessary checks inside one task is not new meaningful practice. This is eligibility, not a blanket once-per-day award cap.

For static obstacles the effective DC is the task's **predeclared intrinsic DC**, not the roll total, margin, or intentionally added arbitrary penalties. The ordinary D20 skill check still uses the appropriate skill rating and attribute bonus. **Natural 1 isn't normally auto-failure for skill checks**; the existing perk-critical discovery system is a separate question.

### Opposed checks

In a genuine opposed check, `effective DC = opponent's actual resolved check total`. The **higher total wins**; 3.5-style ties go to the higher check modifier, then reroll if those also tie. Make sure the XP decision uses the **actual winner**, not an invented `>=` rule for a tie.

Example: guard Perception total 27 and thief Legerdemain total 29 → theft succeeds and thief earns **54 XP**. On a thief result 25, the attempt fails and awards **13.5 XP** instead. The guard may also earn their own relevant skill XP for genuinely resisting or spotting a thief; if the guard is the winner, their XP award is based on the thief's total. The two sides' rewards are independent. Rerolls used only to resolve tied contests do not multiply XP awards.

Opposed check totals can occasionally be zero/negative from strong penalties. For XP accounting, use `max(0, opposed check total)` as effective DC; preserve the raw total for adjudicating the contest. The truly high opponent roll / close win naturally awards more XP, which is a desirable risk/reward feature. Meaningfulness and consequence, not the rival's inflated DC alone, still determine whether an opportunity earns XP.

## Extended checks — generalize 3.5 Craft

Each project must record **before starting**:
- Skill, goal/output, intrinsic DC, interval of genuine work, total progress required (positive), current credited progress, failure consequences, resources, and owner/participants.
- The GM fixes interval, DC and progress goal based on real task scope; the player can't shorten intervals merely to roll more dice, or inflate a task's DC or goal to farm XP.
- Each **complete, meaningful work interval** permits a check using the project DC.
- On success, calculate `produced_progress = check_result × DC`. Credit `min(produced_progress, remaining_progress)` to the project; only that **credited progress** earns XP. On failed checks, no progress is made and therefore no progress-based XP is earned, although they may have appropriate setbacks.
- Failure by 5+ may cost materials for actual crafting, following the 3.5 inspiration; for research, stealth, negotiations, enchantment and other projects, define an appropriate consequence rather than declaring that all endeavors lose physical materials. Failure by 4 or less simply does not make progress by default.
- Finish when accumulated credited progress reaches the fixed goal. Do not award XP again for the completed outcome **in addition** to progress XP unless a separate distinct skill use is justified.

### Calibration candidate: 1 XP per 10 progress

```text
Progress XP (tenths) = credited progress
Thus 750 actual progress earns 75.0 XP.
```

| Project interval | DC | Check result | Raw progress | Progress credited | Candidate XP |
| --- | ---: | ---: | ---: | ---: | ---: |
| Forge an elaborate Dwemer component (work goal 1,000) | 25 | 30 | 750 | 750 | 75 |
| Next interval, same project (250 progress remains) | 25 | 30 | 750 | 250 | 25 |
| Full project completion | 25 | — | — | 1,000 total | **100 total** |
| Failed interval of that same project | 25 | 23 | 0 | 0 | 0 |

This has a nice property: two skilled artisans may complete the same fixed-goal project in different numbers of intervals, but the project yields the **same total progress XP**, divided across their actual contributions. Faster completion can improve XP **per hour**, not artificially create more total XP per item by overshooting the goal.

### Interval normalization — the important trap

The original 3.5 Craft rule explicitly records **weekly progress in silver pieces** but **daily progress in copper pieces**. Thus a result of 30 × DC 25 yields **750 sp** of progress for a full week's check versus **750 cp** for a day's check: different units for different intervals. Source: https://www.d20srd.org/srd/skills/craft.htm .

For Elf-Books, use *abstract progress* and predeclare the project interval and progress goal as a coherent package (day, week, 4 hours, etc.). Do **not** let someone retroactively divide a weekly interval into seven independently paid daily intervals while leaving the project's progress targets and XP rate unchanged. When switching a project's interval for compelling fictional reasons, the GM must also convert progress-unit scale and reward scalar consistently; **never award XP merely for a bookkeeping conversion**. The original 3.5 daily/week unit relation is 10:1, not a universal number of equal work-hours.

**Progress-unit integrity** matters if we make 1/10 progress the universal XP award: goals must be grounded in actual labor rather than an arbitrary economy-denominated price chosen for the XP outcome. A project's completion progress represents authentic work and is spent/credited only once. For guild research, long social campaigns and enchantments, a high project DC means difficult work; a high goal means *more* work, not merely more valuable objects.

## Design implications and outstanding choices

1. **XP progress scalar:** 1 XP/10 credited progress is the leading candidate, not settled. Tune it against real crafting time/materials, combat XP and current `5 × current skill` thresholds.
2. **Failed quick check**: 0.5×DC currently proposed. A failed extended interval gets no progress-based XP. Should it also receive a *limited* attempt/learning award from genuine failed work, or is 0 XP appropriate? Avoid double paying the same interval as a separate quick check.
3. **Time realism:** The 3.5 Craft interval unit choice has enormous effects on XP/hour. Define project templates/normalization before treating number of intervals as comparable across unrelated projects.
4. **Opposed skill mapping:** The 24-skill candidate currently routes ordinary observation to Survival; clarify whether Perception needs its own rated skill rather than assigning XP to bare Wisdom checks. This is a roster-design issue, not a reason to block the general XP mechanism.
5. **Skill growth feedback:** a more capable character gets a higher check result, creates more progress per interval, and gains more XP per *interval*, but project total XP stays fixed. Test a novice and master completing identical tasks.
6. **Project interruption, teamwork, passive opposition and incremental setbacks** require a state model. XP must be committed atomically with credited progress to avoid earning it twice after restoring a save.
7. **Quick checks vs extended tasks:** A single major milestone shouldn't be freely converted into a dozen quick checks, and trivial low-risk activities aren't reclassified as projects solely to manufacture more XP.

### Historical rules references

- D&D 3.5 SRD [Craft](https://www.d20srd.org/srd/skills/craft.htm): original price-based progress, daily copper vs weekly silver and failure/materials.
- D&D 3.5 SRD [Using Skills](https://www.d20srd.org/srd/skills/usingSkills.htm): opposed results, tie resolution, skill checks' nonautomatic natural 1/20, and retry semantics.

This is original Elf-Books adaptation text. The 3.5 OGL SRD is a **reference**, not a new declaration that all its text is covered by the 5.2 CC BY license already cited in [LEGAL.md](../LEGAL.md).
