"""Source-tagged Geard Lif use-based advancement (working Elf-Books pacing).

Dice determine XP only on genuine in-fiction rolls. Caller verifies event
legitimacy, identity, passive awards, and duplicate-event persistence.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from trait_pools import ATTRIBUTES, Talent, MAX_RATING, dice_for_rating

XP_PER_SUCCESS = {"attribute": 2, "talent": 1, "skill": 5, "specialty": 10}
XP_COST_MULTIPLIER = 10
BOOTSTRAP_RATING_LIMIT = 5


def xp_to_next(rating: int) -> int:
    if type(rating) is not int or not 0 <= rating < MAX_RATING:
        raise ValueError("rating must be integer 0..24 to advance")
    return XP_COST_MULTIPLIER * max(1, rating)


def spend_xp(rating: int, banked_xp: int) -> tuple[int, int]:
    """Spend each rank's own XP cost. At cap, retain unspent XP as ledger history."""
    if type(rating) is not int or not 0 <= rating <= MAX_RATING:
        raise ValueError("rating out of bounds")
    if type(banked_xp) is not int or banked_xp < 0:
        raise ValueError("banked XP must be a nonnegative integer")
    while rating < MAX_RATING and banked_xp >= xp_to_next(rating):
        banked_xp -= xp_to_next(rating)
        rating += 1
    return rating, banked_xp


def _successes(faces: Sequence[int]) -> int:
    if not isinstance(faces, (list, tuple)) or any(
        type(x) is not int or not 1 <= x <= 10 for x in faces
    ):
        raise ValueError("every contributed die must be a natural d10 face 1..10")
    return sum(2 if x == 10 else 1 if x >= 7 else 0 for x in faces)


@dataclass(frozen=True)
class PracticeAward:
    xp: dict[str, int]
    natural_tens: int
    bootstrap_skill_xp: int
    bootstrap_specialty_xp: int


def award_roll_xp(
    rolls: Mapping[str, Sequence[int]],
    ratings: Mapping[str, int],
    *,
    talent_governs: bool,
    specialty_declared: bool,
) -> PracticeAward:
    """Credit actual source successes, plus one surrogate per natural 10.

    'rolls' maps attribute/talent/skill/specialty to lists of actual d10
    faces, plus optional equipment dice. A natural 10 can teach both an
    under-5 Skill and an under-5 declared Specialty on the same action.
    A roll uses pre-roll trait ratings throughout, even if the XP crosses
    the threshold for a new die. Equipment contributes no direct trait XP.
    """
    expected = set(XP_PER_SUCCESS)
    if set(ratings) != expected:
        raise ValueError("exactly four rated sources are required")
    if not expected <= set(rolls) or set(rolls) - expected - {"equipment"}:
        raise ValueError("rolls must have all four sources and optional equipment")
    for category in expected:
        count = dice_for_rating(ratings[category])
        if category == "talent" and not talent_governs:
            count = 0
        if category == "specialty" and not specialty_declared:
            count = 0
        if len(rolls[category]) != count:
            raise ValueError(f"wrong count of {category} dice for pre-roll rating")
    for faces in rolls.values():
        _successes(faces)

    xp = {
        category: _successes(rolls[category]) * XP_PER_SUCCESS[category]
        for category in XP_PER_SUCCESS
    }
    all_faces = [face for faces in rolls.values() for face in faces]
    natural_tens = sum(face == 10 for face in all_faces)
    skill_bootstrap = natural_tens * XP_PER_SUCCESS["skill"] if ratings["skill"] < 5 else 0
    specialty_bootstrap = (
        natural_tens * XP_PER_SUCCESS["specialty"]
        if specialty_declared and ratings["specialty"] < 5
        else 0
    )
    xp["skill"] += skill_bootstrap
    xp["specialty"] += specialty_bootstrap
    return PracticeAward(xp, natural_tens, skill_bootstrap, specialty_bootstrap)


def validate_starting_allocation(
    attributes: Mapping[str, int], skills: Mapping[str, int],
    talent: Talent, skill_catalog: set[str],
) -> None:
    """Minimums only; exact total creation budget is not yet selected."""
    names = {name for aspect in ATTRIBUTES.values() for name in aspect.values()}
    if set(attributes) != names:
        raise ValueError("a starting character must specify all 12 attributes")
    if any(type(v) is not int or not 5 <= v <= MAX_RATING for v in attributes.values()):
        raise ValueError("starting attributes must each be rated 5..25")
    talent.validate_catalog(skill_catalog)
    if set(skills) - skill_catalog:
        raise ValueError("unknown skill")
    if any(type(v) is not int or not 0 <= v <= MAX_RATING for v in skills.values()):
        raise ValueError("starting skill ratings must be integers 0..25")
    for skill_id in talent.governed_skills:
        if skills.get(skill_id, 0) < 5:
            raise ValueError(f"Talent-governed Skill {skill_id} must start at rating >=5")
