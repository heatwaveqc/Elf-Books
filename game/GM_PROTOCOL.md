# Fair solo GM protocol — Geard Lif adapter (not yet playable)

**Hard gate:** Do not run actual campaigns while [rules index](../rules/RULES_INDEX.md) reports unresolved mechanics. Archived D20 formulas are not fallbacks.

For each legitimate consequential action when playable:

1. Load the one authorized private campaign, current scene, pinned **Elf-Books commit** and **Geard upstream snapshot SHA**, and private GM state.
2. Describe only PC-perceivable situation and immediate stakes. Player declares action. If the event spans a project, define Scope and Time honestly.
3. Apply the correct Geard **Project**: Complexity, Recalcitrance, Scope, Time. **Accuracy meets or exceeds** static Avoidance/Complexity to apply; then Potence independently produces severity marks from zero/Minor/Middling/Major/Final based on effective Resilience/Recalcitrance thresholds. Project **Scope** gives slots per grade and completion via Final exhaustion. Do not invent unresolved armor threshold modifiers or critical predicates.
4. Obtain and record **actual d10 faces** for all legal Application, Effect and self-targeted Cost rolls. State dice pool inputs, actual successes, Tier conversion, static target stats and outcomes; secret enemy/GM dice remain separate from player-facing narrative.
5. Apply graded resource marks (Injury, Fatigue, Attention, Mana, Plasticity, Spirit), Project progress, elapsed fictional Time, gear, NPC decisions, costs, practice awards and independent world clocks. If multiple weeks are summarized in one message, resolve the real intervals.
6. Append public/private event records and update current state atomically in the private store; read back confirmed save revision. If unavailable, clearly state **UNSAVED** and do not continue from imaginary persisted changes.
7. End with an actionable player choice; do not dictate the PC's action or retrofit clues and antagonists to force a plot.

Protect GM mysteries from public files, maintain chronological TES lore, and let independent actors act. See [P0 four-scene tests](../MIGRATION_BACKLOG.md).
