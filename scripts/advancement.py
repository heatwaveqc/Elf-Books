"""Source-tagged Geard Lif use-based advancement (working Elf-Books pacing).

Dice determine XP only on genuine in-fiction rolls. Caller verifies event
legitimacy, identity, passive awards, and duplicate-event persistence.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from trait_pools import ATTRIBUTES, Talent, MAX_RATING, dice_for_rating, compose_tier_pool, validate_tier_ratings

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


def tier_multiplier(tier: int) -> int:
    if type(tier) is not int or tier < 0:
        raise ValueError("Tier must be a nonnegative integer")
    return 10 ** tier


def xp_to_next_at_tier(rating: int, tier: int) -> int:
    """Cost in BASE XP for the next rating point at selected Tier."""
    return xp_to_next(rating) * tier_multiplier(tier)


def spend_tier_xp_tenths(ratings: Mapping[int,int], tier: int,
                         bank_tenths: int) -> tuple[dict[int,int],int]:
    """Spend integer tenths of base XP; never auto-up-tier.

    Callers explicitly select a Tier. Lower-Tier ratings never leak into
    this tier's dice pool. Tier T+1 becomes purchasable only with T at 25.
    """
    validate_tier_ratings(ratings)
    mult=tier_multiplier(tier)
    if type(bank_tenths) is not int or bank_tenths<0:
        raise ValueError("bank must be nonnegative integer tenths of XP")
    out=dict(ratings)
    if tier not in out:
        if tier!=max(out)+1 or out[tier-1]!=MAX_RATING:
            raise ValueError("prior Tier must be 25 before unlocking next Tier")
        out[tier]=0
    while out[tier] < MAX_RATING:
        cost_tenths=xp_to_next_at_tier(out[tier],tier)*10
        if bank_tenths<cost_tenths:
            break
        bank_tenths-=cost_tenths
        out[tier]+=1
    return out,bank_tenths


def award_tier_roll_xp(rolls: Mapping[str,Sequence[int]], *,
                       attribute_name: str, role: str,
                       tier: int, talent: Talent, skill_id: str,
                       ratings: Mapping[str,Mapping[int,int]],
                       specialty_declared: bool) -> PracticeAward:
    """Scale the XP from actual Tier-specific source dice exactly once."""
    compose_tier_pool(
        attribute_name=attribute_name,role=role,tier=tier,talent=talent,
        skill_id=skill_id,ratings=ratings,specialty_declared=specialty_declared)
    snapshot={key: series.get(tier,0) for key,series in ratings.items()}
    original=award_roll_xp(
        rolls,snapshot,talent_governs=skill_id in talent.governed_skills,
        specialty_declared=specialty_declared)
    multiplier=tier_multiplier(tier)
    return PracticeAward(
        {source:amount*multiplier for source,amount in original.xp.items()},
        original.natural_tens,
        original.bootstrap_skill_xp*multiplier,
        original.bootstrap_specialty_xp*multiplier)


CASCADE_ORDER=("talent","attribute","skill","specialty")


def cascade_xp_tenths(*, source: str, amount_tenths: int,
                      tier: int, ratings: Mapping[str,Mapping[int,int]],
                      specialty_declared: bool,
                      choice: str="cascade") -> tuple[str,int]:
    """Select ONE destination for already-earned raw XP, no multiplier.

    Choice 'bank' keeps XP with its source for future Tier purchasing.
    'cascade' passes through maxed traits to the first nonmaxed usable
    narrower trait. A missing/not-yet-unlockable destination stops
    cascade and preserves XP at its last eligible owner.
    """
    tier_multiplier(tier)
    if source not in CASCADE_ORDER or choice not in {"cascade","bank"}:
        raise ValueError("invalid source or XP allocation choice")
    if type(amount_tenths) is not int or amount_tenths<0:
        raise ValueError("XP must be nonnegative integer tenths")
    if set(ratings)!=set(CASCADE_ORDER):
        raise ValueError("all four source tiers required")
    for series in ratings.values():
        validate_tier_ratings(series)
    if choice=="bank":
        return source,amount_tenths
    dest=source
    while ratings[dest].get(tier,0)==MAX_RATING:
        idx=CASCADE_ORDER.index(dest)
        if idx+1>=len(CASCADE_ORDER):
            break
        next_source=CASCADE_ORDER[idx+1]
        if next_source=="specialty" and not specialty_declared:
            break
        next_ratings=ratings[next_source]
        if tier>0 and (tier-1 not in next_ratings or
                       next_ratings[tier-1]!=MAX_RATING):
            break
        dest=next_source
    return dest,amount_tenths


def static_defense_value(contributing_ratings: Mapping[str,int]) -> int:
    """Static defense = floor(total eligible personal dice / 2).

    Floor ONCE after summing, not separately by each participating trait.
    Equipment/other modifiers belong to the relevant adapter.
    """
    if not contributing_ratings:
        raise ValueError("defense must identify participating traits")
    return sum(dice_for_rating(r) for r in contributing_ratings.values())//2


def passive_xp_tenths(contributing_ratings: Mapping[str,int],
                      tier: int=0) -> dict[str,int]:
    """Award per-trait passive XP in tenths, rounding UP at Tier 0 only.

    Tier 0: ceil(rating / 10) whole XP per participating trait.
    Tier >=1: exactly rating/10 * 10**tier XP (always an integer).
    Existing rating and actual source participation determine the award;
    never apply the active 2/1/5/10 success multipliers again.
    """
    multiplier=tier_multiplier(tier)
    if not contributing_ratings:
        raise ValueError("passive event must identify participating traits")
    result={}
    for source,rating in contributing_ratings.items():
        dice_for_rating(rating)
        result[source]=10*((rating+9)//10) if tier==0 else rating*multiplier
    return result
