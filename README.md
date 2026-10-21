# Elf-Books

**Unofficial, free, noncommercial Elder Scrolls-inspired solo AI-GM RPG.** This is an adaptation of the **Geard Lif / Raven's Heart** engine, **not** a D20 or D&D-based game. This project is not affiliated with Bethesda or ZeniMax.

## Status

**FOUNDATION / NOT PLAYABLE.** A local snapshot of Geard Lif's player-facing Project, resource, tentative d10 and Tier rules is in [engine/geard-lif/](engine/geard-lif/README.md). The character/skill adapter, exact effect resolution, combat, spellcasting, use-based XP, and campaign integration still need work.

Geard Lif is the mechanical upstream; Elf-Books provides Elder Scrolls characters, magic traditions, setting, NPCs, perks, and an independent solo-GM experience. Changes to upstream engine mechanics must be reviewed and repinned, not improvised differently here.

## Start here

- [Solo-GM entrypoint](START_HERE.md) · [Contributor / AI instructions](AGENTS.md)
- [Current authority and design status](rules/RULES_INDEX.md)
- **[Local Geard Lif core rules](engine/geard-lif/README.md)** — four complete player-audience source rule pages, pinned to upstream
- [Locked vs provisional upstream mechanics](engine/geard-lif/SYSTEM_STATUS.md)
- **[Return-to-parity migration checklist](MIGRATION_BACKLOG.md)** — a concrete prioritized list
- [Foundation and conversion boundaries](rules/FOUNDATION.md)
- [24 candidate Elder Scrolls skills](rules/SKILLS.md) · [structured names](rules/skills.json)
- [75 historical Elder Scrolls perk inspirations](design/tes_perk_seeds.json) · [perk migration](rules/PERKS.md)
- [Skill-by-doing advancement design](rules/ADVANCEMENT.md)
- [Combat, Avoidance and Injury migration](rules/DEFENSE.md)
- [Magic, Mana and spell-school migration](design/MAGIC.md)
- [Lore and chronology](lore/LORE_POLICY.md) · [GM protocol](game/GM_PROTOCOL.md)
- [Character creation](game/CHARACTER_CREATION.md) · [pre-session prep](game/PRE_SESSION_PREP.md) · [private save contract](game/PERSISTENCE.md)
- [Validation and tests](game/TEST_PLAN.md) · [copyright and provenance](LEGAL.md)

## Archived former D20 version

**[archive/d20-pre-geard-lif](https://github.com/heatwaveqc/Elf-Books/tree/archive/d20-pre-geard-lif)** preserves the previous D20 rules, tests, XP equations, 0–100 skill roster, spell/defense work, and perk survey. No fork was required; that branch and its Git history are retained for comparison. **It is deprecated and is not a second current rules engine.**

Do not infer a usable campaign from passing unit tests. Production GM play remains blocked until the unresolved engine/adapter mechanics and private persistence pass the readiness gate.
