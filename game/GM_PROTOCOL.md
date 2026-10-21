# Fair solo GM protocol — Geard Lif adapter (not yet playable)

**Hard gate:** Do not run actual campaigns while [rules index](../rules/RULES_INDEX.md) reports unresolved mechanics. Archived D20 formulas are not fallbacks.

For each legitimate consequential action when playable:

1. Load the one authorized private campaign, current scene, pinned **Elf-Books commit** and **Geard upstream snapshot SHA**, and private GM state.
2. Describe only PC-perceivable situation and immediate stakes. Player declares action. If the event spans a project, define Scope and Time honestly.
3. Apply the correct Geard **Project**: Complexity, Recalcitrance, Scope, Time. **Accuracy meets or exceeds** static Avoidance/Complexity to apply; then Potence independently produces severity marks from zero/Minor/Middling/Major/Final based on effective Resilience/Recalcitrance thresholds. Project **Scope** gives slots per grade and completion via Final exhaustion. Do not invent unresolved armor threshold modifiers or critical predicates.
4. Obtain and record **actual d10 faces** for all legal Application, Effect and self-targeted Cost rolls. State dice pool inputs, actual successes, Tier conversion, static target stats and outcomes; secret enemy/GM dice remain separate from player-facing narrative.
5. Award XP on genuine source-tagged d10s (**2 Attribute / 1 Talent / 5 Skill / 10 Specialty XP per success**) and per-natural-10 Skill/Specialty bootstrap when below rating five; calculate before rank-up, deduplicate event IDs, and apply graded resource marks (Injury, Fatigue, Attention, Mana, Plasticity, Spirit), Project progress, elapsed fictional Time, gear, NPC decisions, costs, practice awards and independent world clocks. If multiple weeks are summarized in one message, resolve the real intervals.
6. Append public/private event records and update current state atomically in the private store; read back confirmed save revision. If unavailable, clearly state **UNSAVED** and do not continue from imaginary persisted changes.
7. End with an actionable player choice; do not dictate the PC's action or retrofit clues and antagonists to force a plot.

Protect GM mysteries from public files, maintain chronological TES lore, and let independent actors act. See [P0 four-scene tests](../MIGRATION_BACKLOG.md).

**When play is eventually enabled:** record the *chosen Tier* of each roll and the same-Tier governing-Attribute/Skill die gates; no silent import of lower-Tier personal dice. Award raw XP with one `10^Tier` multiplier and let the player bank maxed-source XP for up-tier advancement or cascade it along Talent→Attribute→Skill→Specialty. For genuine selected passive defense or Cost resistance, credit `rating/10×10^Tier` XP only to participants, in **integer tenths**. Verify all spend/cascade and selection against the pinned campaign state. Static defensive value is half of contributed dice, exact until a rounding rule is approved.

**Rounding and common magic:** floor half of **total** legal defensive dice when building static Avoidance/Cost resistance. Tier-0 passive XP rounds `rating/10` **up per actually used trait**; Tier 1+ is integral. A Destruction cast rolls Perception+Destruction Accuracy and Intelligence+Destruction Potence (with applicable Talent/Specialty); its independent rolled Mana Cost is graded against **static Will+Destruction+eligible cost-reduction robes**, with **Conviction determining Mana mark capacity**. Default countermagic is chosen Wits+Mysticism, not stacked with Dodge. Do not invent spell Cost dice or counterspell reaction timings not yet defined.
