"""Exploratory Elf-Books math: category ECL and *superseded* learning checks.

Use-based practice XP is the new design direction in design/USE_BASED_ADVANCEMENT.md.
This old learn() function is retained ONLY for comparative calibration and tests.
Not authoritative rules. External dice only; does not create random results.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "rules" / "skills.json"


def load_catalog() -> dict:
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def normalized_skills(ratings: dict[str, int], catalog: dict | None = None) -> dict[str, int]:
    data = load_catalog() if catalog is None else catalog
    ids = {entry["id"] for entry in data["entries"]}
    unknown = set(ratings) - ids
    if unknown:
        raise ValueError(f"unknown/alias skill IDs (aliases cannot receive ratings): {sorted(unknown)}")
    if any(type(score) is not int or score < 0 or score > 100 for score in ratings.values()):
        raise ValueError("each skill rating must be an integer 0..100")
    return {key: value for key, value in ratings.items()}


def skill_bonus(score: int) -> int:
    if type(score) is not int or not 0 <= score <= 100:
        raise ValueError("skill must be an integer 0..100")
    return score // 5


def category_ecl(scores: list[int]) -> Fraction:
    if any(type(s) is not int or not 0 <= s <= 100 for s in scores):
        raise ValueError("invalid category skill rating")
    if not scores:
        return Fraction(0)
    return min(Fraction(sum(scores), 20), Fraction(max(scores), 5))


@dataclass(frozen=True)
class Pools:
    warrior_ecl: Fraction
    mage_ecl: Fraction
    rogue_ecl: Fraction
    health_ecl: Fraction
    magicka_ecl: Fraction
    health: int
    magicka: int


def derived_pools(ratings: dict[str, int], con_mod: int, wis_mod: int, catalog: dict | None = None) -> Pools:
    data = load_catalog() if catalog is None else catalog
    normalized = normalized_skills(ratings, data)
    if type(con_mod) is not int or type(wis_mod) is not int:
        raise ValueError("attribute modifiers must be integers")
    if min(5 + con_mod, 5 + wis_mod) < 1:
        raise ValueError("pool multiplier must be positive")
    groups = {"warrior": [], "mage": [], "rogue": []}
    for item in data["entries"]:
        groups[item["category"]].append(normalized.get(item["id"], 0))
    w = category_ecl(groups["warrior"])
    m = category_ecl(groups["mage"])
    r = category_ecl(groups["rogue"])
    he = w + r / 2
    me = m + r / 2
    return Pools(w, m, r, he, me, int((5 + con_mod) * he), int((5 + wis_mod) * me))


@dataclass(frozen=True)
class LearningResult:
    skill: int
    progress: int
    advanced: bool
    source: str


def learn(skill: int, progress: int, attribute_modifier: int, natural_roll: int, dc: int) -> LearningResult:
    """Apply one already-approved meaningful learning opportunity.

    A roll of natural 20 advances a full rank; otherwise pass attribute-only
    DC and accumulate successes equal to the current rank. Rolls must be real
    and independently recorded by the caller; this function never rolls dice.
    """
    skill_bonus(skill)  # validates range and type
    if type(progress) is not int or progress < 0:
        raise ValueError("progress must be a nonnegative integer")
    if type(natural_roll) is not int or not 1 <= natural_roll <= 20:
        raise ValueError("learning roll must be actual d20 in 1..20")
    if type(dc) is not int or type(attribute_modifier) is not int:
        raise ValueError("DC and modifier must be integers")
    if skill == 100:
        return LearningResult(100, 0, False, "capped")
    if progress >= max(1, skill):
        raise ValueError("invalid stored progress; already meets advancement threshold")
    if natural_roll == 20:
        return LearningResult(skill + 1, 0, True, "natural_20")
    if natural_roll + attribute_modifier < dc:
        return LearningResult(skill, progress, False, "no_progress")
    next_progress = progress + 1
    if next_progress >= max(1, skill):
        return LearningResult(skill + 1, 0, True, "practice_threshold")
    return LearningResult(skill, next_progress, False, "practice_success")
