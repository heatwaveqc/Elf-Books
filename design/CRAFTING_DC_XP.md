# Crafting and task DC as skill XP — design candidate

**Status:** The core XP threshold and offensive damage award are agreed. **Crafting XP = 2 × DC per finished work unit remains a proposal, not an adopted rule.** Compare the earlier [weapon/XP prototype](WEAPON_SKILL_DAMAGE_XP.md), now accepted in principle, and [defenses](../rules/DEFENSE.md).

## Already accepted advancement math

```text
XP to advance from skill S to S+1 = 5 × max(1, S)
Offensive skill XP from attributable HP loss = 2 × effective HP lost
```

Relevant weapon skill adds `floor(S/5)` to attack **and flat damage**. Damage means applied HP loss, not pre-resistance output or overkill. Critical attacks double eligible weapon damage dice, not flat skill modifiers. Distinguish independently attributable offensive spells, weapon damage, poison, summons or other riders rather than double-crediting the same HP twice.

## Two possible sources of crafting XP

### A. Value-based (Skyrim inspiration)

Skyrim Smithing experience is nonlinear in item gold value, roughly `25 + 3 × item_value^0.65` for a crafted item in its patched rules. Earlier Skyrim Alchemy gives XP heavily weighted by potion value. Source: https://en.uesp.net/wiki/Skyrim:Smithing and https://en.uesp.net/wiki/Skyrim:Alchemy .

**Pros:** More elaborate/material-intensive goods often have greater market value; ties reward to real useful outputs, not arbitrary rolls. **Cons:** Gold, scarcity, enchanted worth, and merchant markups can vastly exceed technical difficulty. Two items of equal skill challenge may have very different Septim prices. Smithing and potion-making then require different price calibration. For Elf-Books, if price contributes at all, use a fixed recipe/intrinsic **Septim base value**, not player-adjusted selling price, and separate costly materials from workmanship.

### B. DC-based (preferred prototype)

A proposed common noncombat award:

```text
XP per completed qualifying work unit = 2 × intrinsic task DC
```

Use the **predeclared DC of the challenge**, not the resulting total roll, margin of success, item's sale price or character's current adjusted skill bonus. A *work unit* is a genuine deliverable or completed step consuming actual resources/time: forge one finished tool, make one potion batch of defined quantity, finish one meaningful stage of a monumental construction, decipher a document, persuade a faction to take an action. **A roll is an adjudication tool, not an XP unit.**

Making 20 actual iron daggers counts as 20 genuine work units, even if a single pooled roll resolves the work order. Making one dagger via 20 gratuitous intermediate checks counts as **one** unit. Repetition is allowed: TES-style mass-production is legitimate skill practice if it consumes time and materials. Do not arbitrarily deny all advancement for practicing a low-DC task; the growing XP requirement naturally makes simple repetition slower at high skill.

If materials are consumed on a genuine failed attempt, some practice XP might be reasonable; the failure fraction **is not decided**. The trial calculator awards full XP only for successfully completed units; partial outputs/progress need an explicit quality and loss rule. Do not add unlimited XP for intentionally impossible rolls with no practical work.

### Numerical comparison for K=5

Assume normal d20 skills use `roll + governing_attribute_mod + floor(S/5)` vs a declared difficulty. D20 checks do **not** normally auto-fail on a natural 1 (although a separate critical success may be a perk trigger if it succeeds).

| Skill range | Representative task DC | Total XP required | XP per completed unit | Units to +5 (expected approximation) | Illustrative success chance | Attempts to +5 (approx.) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 20→25, attribute +3 | 15 | 550 | 30 | 18.3 | 65% | 28.2 |
| 50→55, attribute +5 | 25 | 1,300 | 50 | 26.0 | 55% | 47.3 |
| 95→100, attribute +7 | 40 | 2,425 | 80 | 30.3 | 35% | 86.6 |

These are **calibration ratios**, not exact expected stopping times. Skill/rating and possible techniques may change inside an interval, but `floor(S/5)` stays constant for each shown five-rank block. Failure costs, retries, extra work units, and natural-20 perk bonuses aren't included. DC 40 exceeds the usual 5e **nearly impossible DC30** benchmark; Elf-Books needs 35–45+ mastery tasks because it grants +20 from skill alone (versus 5e proficiency capped +6).

Reference DCs from the 5.2 SRD (5 very easy, 10 easy, 15 medium, 20 hard, 25 very hard, 30 nearly impossible): https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.pdf .

## Key design principle

**DC measures difficulty, not impact, value, or duration.** This is strong for standardizing *how hard something was to accomplish*, but a six-week mural and a ten-minute lock can have the same DC while representing radically different practice. Use predeclared work units/milestones to represent genuine long projects, **not automatic XP each time a die is rolled**. A successful consequential negotiation or investigation may justify a defined complete task award, not merely XP for each spoken sentence.

Illustrative use:
- A mundane DC10 smithing object gives **20 XP** on completion, even if its creator has become expert.
- An intricate DC20 mechanism gives **40 XP** per finished work unit.
- A master DC40 magical machine stage gives **80 XP** on substantive completion.
- If a player makes five genuine DC15 potions, give **5 × 30 = 150 XP**, independent of whether five separate dice are rolled.

## What remains to decide

1. Is **2 × DC** a good overall XP rate compared with 2 × actual HP dealt by an offensive skill, or should it be multiplied by a time/complexity coefficient?
2. Should failed substantial attempts earn a fraction of potential XP, and if so when? Failure must still involve actual work/resources rather than no-cost die rolling.
3. How is the size of a finished batch/major multi-day project set in an objective way so a single roll cannot subdivide itself into unlimited XP?
4. Do high-value crafted items award **additional** value-based XP, or does item DC already include the real expertise needed?
5. Should social, security, lore, survival and athletics use the same DC-based rule as smithing, while magical schools use effect/resource-based XP?
6. How do we set DCs beyond 30 in a game where skill 100 grants +20? Masterwork challenges must be meaningfully harder without making ordinary tasks unrealistically dangerous.

Run encounter and crafting-economy tests before adopting numeric DC awards; spell and defensive award magnitudes also remain open.
