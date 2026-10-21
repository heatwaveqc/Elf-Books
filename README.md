# Elf-Books

**Unofficial, free, noncommercial Elder Scrolls-inspired solo AI-GM RPG.** This is an adaptation of the **Geard Lif / Raven's Heart** engine, **not** a D20 or D&D-based game. This project is not affiliated with Bethesda or ZeniMax.

## Status

**FOUNDATION / NOT PLAYABLE.** A local snapshot of Geard Lif's player-facing Project, resource, tentative d10 and Tier rules is in [engine/geard-lif/](engine/geard-lif/README.md). The twelve attributes, five-skill Talent model and 24-skill vocabulary are defined, and the 0–25 source-dice XP model is now implemented for active rolls, with all twelve starting Attributes >=5 and five governed starting Skills >=5; complete budgets, many reaction/equipment values, Talent trees, full combat, full spell lists and persistence still need work.

Geard Lif is the mechanical upstream; Elf-Books provides Elder Scrolls characters, magic traditions, setting, NPCs, perks, and an independent solo-GM experience. Changes to upstream engine mechanics must be reviewed and repinned, not improvised differently here.

## Start here

- [Solo-GM entrypoint](START_HERE.md) · [Contributor / AI instructions](AGENTS.md)
- [Current authority and design status](rules/RULES_INDEX.md)
- **[Local Geard Lif core rules](engine/geard-lif/README.md)** — seven player-facing core-rule pages, pinned to upstream
- [Locked vs provisional upstream mechanics](engine/geard-lif/SYSTEM_STATUS.md)
- **[Return-to-parity migration checklist](MIGRATION_BACKLOG.md)** — a concrete prioritized list
- [Foundation and conversion boundaries](rules/FOUNDATION.md)
- **[Twelve attributes and five-skill Talents](rules/TALENTS.md)** · [12 presets and custom-class schema](rules/talents.json)
- [24 Elder Scrolls skills](rules/SKILLS.md) · [structured names](rules/skills.json)
- [75 historical Elder Scrolls perk inspirations](design/tes_perk_seeds.json) · [perk migration](rules/PERKS.md)
- **[Use-based XP, Trait Tier governing-die prerequisites, raw XP cascade and passive resistance learning](rules/ADVANCEMENT.md)**
- [Combat, Avoidance and Injury migration](rules/DEFENSE.md)
- [Magic, Mana and spell-school migration](design/MAGIC.md)
- [Lore and chronology](lore/LORE_POLICY.md) · [GM protocol](game/GM_PROTOCOL.md)
- [Character creation](game/CHARACTER_CREATION.md) · [pre-session prep](game/PRE_SESSION_PREP.md) · [private save contract](game/PERSISTENCE.md)
- [Validation and tests](game/TEST_PLAN.md) · [copyright and provenance](LEGAL.md)

## Archived former D20 version

**[archive/d20-pre-geard-lif](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif)** preserves the previous D20 rules, tests, XP equations, 0–100 skill roster, spell/defense work, and perk survey. No fork was required; that branch and its Git history are retained for comparison. **It is deprecated and is not a second current rules engine.**

Do not infer a usable campaign from passing unit tests. Production GM play remains blocked until the unresolved engine/adapter mechanics and private persistence pass the readiness gate.

**Combat and social resistance:** [Attack modes and legal defenses](rules/ATTACK_MODES.md) include projectiles, direct cold curses, environmental cold and four social modes. Shorthand automatically applies relevant Talent and Specialty; all items and temporary magic share one aggregate external-dice cap equal to unmodified personal dice.
