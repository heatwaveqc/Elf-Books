# Roadmap and acceptance tests

## Current scaffold checks
- `python3 scripts/validate_scaffold.py` validates links/file layout, template structure, and the absence of real public campaign files.
- `python3 -m unittest discover -s tests` exercises validator happy/failure paths.
- GitHub Actions runs those checks for pushes and PRs.

These are **structural** tests; passing them does **not** declare the game playable.

## Before first real campaign
- Decide advancement formula and skill/check mapping; simulate novice/specialist/generalist/mage career paths and bounded-accuracy outcomes.
- Decide HP, damage, initiative, armor and saves without character levels.
- Build Magicka, schools, basic spell creation, spell learning, alchemy/enchanting starter rules.
- Populate source-linked era snapshot for a playable region and date.
- Create real private-store saver/loader with atomic event/checkpoint behavior; test simulated save conflicts and tool outage.
- Validate pre-session private spine and three independent clue paths; audit GM discretion and spoiler leaks.
- Run two character-creation tests and a 5-scene campaign, including a departure from the expected plot. Check that skill gain is fair and persisted.

## Quality bar
No generated outcomes based on fabricated rolls; no class-gated learning; no accidental level-based modifiers; no undated anachronisms; no leaking public campaign secrets; no broken continuation after restart. The user approves progression and combat balance before any release is called playable.
