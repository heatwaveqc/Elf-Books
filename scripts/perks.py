"""Elf Books: bankable perk eligibility and source-tagged double-d10 breakthroughs.

The Geard Lif 0-5/Drive Mark core does NOT determine Elf-Books perks.
Uses Elf Books' 0-25 four-source rating model. Equipment never generates
character perk points. Confirmation dice have no effect on actual actions,
ordinary source XP, natural-ten bootstrap, or equipment deed enchantments.

This module is pure arithmetic/validation: a calling GM or event ledger must
confirm consequential action, real hostile targeting, event uniqueness, and
persist the rolled original and confirmation faces exactly once.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from trait_pools import MAX_RATING, Talent

PERSONAL_SOURCES = ("attribute", "talent", "skill", "specialty")
PERK_SKILL_SOURCE = "perk_skill"  # perk-created dice receive Skill awards


def _validate_rating(value: int, name: str) -> None:
    if type(value) is not int or not 0 <= value <= MAX_RATING:
        raise ValueError(f"{name} must be an integer 0..{MAX_RATING}")


def _validate_faces(faces: Sequence[int]) -> None:
    if not isinstance(faces, (list, tuple)) or any(
        type(face) is not int or face < 1 or face > 10 for face in faces
    ):
        raise ValueError("all dice must be recorded as natural d10 faces 1..10")


@dataclass(frozen=True)
class PerkRequirement:
    """A specific Attribute+Skill, one permissible Specialty, and a threshold."""
    name: str
    attribute: str
    skill: str
    accepted_specialties: frozenset[str]
    minimum_rating: int

    def __post_init__(self) -> None:
        if any(
            not isinstance(value, str) or not value.strip()
            for value in (self.name, self.attribute, self.skill)
        ):
            raise ValueError("perk name, Attribute and Skill must be named")
        if not isinstance(self.accepted_specialties, frozenset) or any(
            not isinstance(s, str) or not s.strip() for s in self.accepted_specialties
        ):
            raise ValueError("permitted Specialties must be a set of named Specialties")
        if type(self.minimum_rating) is not int or not 0 <= self.minimum_rating <= 100:
            raise ValueError("perk threshold must be integer 0..100")


@dataclass(frozen=True)
class PerkQualification:
    total_rating: int
    meets_requirement: bool
    talent_rating: int
    specialty_rating: int
    qualifying_specialty: str | None


def qualify_for_perk(
    *, requirement: PerkRequirement, attribute: str, attribute_rating: int,
    skill: str, skill_rating: int, talent: Talent,
    specialty_ratings: Mapping[str, int],
) -> PerkQualification:
    """Sum actual 0..25 ratings, not dice, one permitted Specialty at most.

    A Talent contributes only when it actually governs this Skill. One
    eligible known Specialty supplies its rating (max of allowed matches,
    never sum multiple Specialties). The accepted set may contain "*"
    to accept ANY Specialty legitimately belonging to the named Skill.
    specialty_ratings must be pre-filtered to the named Skill by caller.
    Attribute and Skill must match the perk's exact declared prereqs.
    Equipment, magical, and perk-generated bonus dice add no rating.
    """
    if not isinstance(requirement, PerkRequirement):
        raise ValueError("perk requirement is required")
    if attribute != requirement.attribute or skill != requirement.skill:
        raise ValueError("attribute and skill must match perk requirement")
    _validate_rating(attribute_rating, "Attribute rating")
    _validate_rating(skill_rating, "Skill rating")
    if not isinstance(talent, Talent):
        raise ValueError("a character's starting Talent is required")
    if not isinstance(specialty_ratings, Mapping):
        raise ValueError("Specialty ratings must be keyed by Specialty name")
    for name, value in specialty_ratings.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Specialty IDs must be named")
        _validate_rating(value, f"Specialty {name}")
    # "*" is the wildcard for ANY legitimately possessed Specialty
    # belonging to this perk's named Skill. Caller must supply only
    # Specialties of that Skill, never an unrelated Skill's specialisms.
    # One actual Specialty contributes at most once; no combining ratings.
    any_specialty = "*" in requirement.accepted_specialties
    eligible = sorted(
        (name for name in specialty_ratings
         if any_specialty or name in requirement.accepted_specialties),
        key=lambda name: (-specialty_ratings[name], name),
    )
    selected = eligible[0] if eligible else None
    specialty = specialty_ratings[selected] if selected is not None else 0
    governed = talent.rating if skill in talent.governed_skills else 0
    total = attribute_rating + governed + skill_rating + specialty
    return PerkQualification(
        total_rating=total,
        meets_requirement=total >= requirement.minimum_rating,
        talent_rating=governed,
        specialty_rating=specialty,
        qualifying_specialty=selected if specialty > 0 else None,
    )


@dataclass(frozen=True)
class RankedPerk:
    """Sequential one-point rank purchases, each with its own 0..100 gate.

    This is a general mechanism only; particular multi-rank perks and
    their thresholds remain catalogue-level decisions until adopted.
    """
    name: str
    attribute: str
    skill: str
    accepted_specialties: frozenset[str]
    rank_requirements: tuple[int, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.rank_requirements, tuple) or not 1 <= len(self.rank_requirements) <= 5:
            raise ValueError("ranked perk must define 1 through 5 sequential ranks")
        previous = -1
        for value in self.rank_requirements:
            if type(value) is not int or not 0 <= value <= 100 or value <= previous:
                raise ValueError("rank prerequisites must strictly increase within 0..100")
            previous = value
        PerkRequirement(self.name,self.attribute,self.skill,
                        self.accepted_specialties,self.rank_requirements[0])


@dataclass(frozen=True)
class NextRankPurchase:
    next_rank: int | None
    required_rating: int | None
    qualified: bool
    remaining_points: int


def evaluate_next_rank(*, perk:RankedPerk,current_rank:int,banked_points:int,
                       attribute:str,attribute_rating:int,
                       skill:str,skill_rating:int,talent:Talent,
                       specialty_ratings:Mapping[str,int])->NextRankPurchase:
    """Return whether the next consecutive rank is available and affordable.

    Owning rank 1 is required to buy rank 2; upgrades spend one point each.
    Rating eligibility is rechecked for the *next* rank, with the ordinary
    Attribute+governed Talent+Skill+one accepted Specialty formula. No
    equipment/perk dice contribute to this prerequisite rating.
    """
    if not isinstance(perk,RankedPerk):
        raise ValueError("perk must be a RankedPerk")
    if type(current_rank) is not int or not 0 <= current_rank <= len(perk.rank_requirements):
        raise ValueError("invalid current rank")
    if type(banked_points) is not int or banked_points < 0:
        raise ValueError("perk-point bank cannot be negative")
    if current_rank == len(perk.rank_requirements):
        return NextRankPurchase(None,None,False,banked_points)
    requirement=PerkRequirement(
        perk.name,perk.attribute,perk.skill,perk.accepted_specialties,
        perk.rank_requirements[current_rank],
    )
    qualifying=qualify_for_perk(
        requirement=requirement,attribute=attribute,
        attribute_rating=attribute_rating,skill=skill,skill_rating=skill_rating,
        talent=talent,specialty_ratings=specialty_ratings,
    )
    available=qualifying.meets_requirement and banked_points >= 1
    return NextRankPurchase(
        current_rank+1,requirement.minimum_rating,available,
        banked_points-1 if available else banked_points,
    )


@dataclass(frozen=True)
class ConfirmedPerkAward:
    actor_points: int
    defender_points: int
    actor_confirmation_attempts: int
    defender_confirmation_attempts: int


def resolve_perk_confirmations(
    *, original_roll: Mapping[str, Sequence[int]],
    actor_ten_confirmations: Mapping[str, Sequence[int]],
    defender_one_confirmations: Mapping[str, Sequence[int]] | None = None,
    defender_targeted: bool = False,
) -> ConfirmedPerkAward:
    """Check each personal original 10 for actor and each personal 1 for target.

    Actor rerolls own natural 10s exactly once; each confirmation 10 gives
    one bankable perk point. A defender legitimately targeted by this
    hostile roll rerolls the attacker's ORIGINAL personal 1s exactly once;
    each confirmation 1 gives that defender one bankable perk point.
    There is no per-roll point cap.

    Skill-equivalent `perk_skill` bonus dice are INCLUDED for actor 10s
    and threatened defender 1s and are kept in a separate provenance key.
    Equipment dice are excluded from BOTH character perk triggers. Rerolls do not change
    Accuracy/Potence or XP and do not themselves trigger further rerolls.
    This function handles one actual roll/one actual threatened defender;
    the caller must not award the same original faces repeatedly to
    multiple targets or recycle the same event ID.
    """
    if type(defender_targeted) is not bool:
        raise ValueError("defender_targeted must be boolean")
    if not isinstance(original_roll, Mapping):
        raise ValueError("roll needs source-tagged original faces")
    if set(original_roll) - set(PERSONAL_SOURCES) - {"equipment", PERK_SKILL_SOURCE}:
        raise ValueError("unknown original die source")
    if not set(PERSONAL_SOURCES) <= set(original_roll):
        raise ValueError("all four personal sources must be present")
    for faces in original_roll.values():
        _validate_faces(faces)
    eligible = (*PERSONAL_SOURCES, PERK_SKILL_SOURCE) if PERK_SKILL_SOURCE in original_roll else PERSONAL_SOURCES
    for confirmations in (actor_ten_confirmations, defender_one_confirmations):
        if confirmations is None:
            continue
        if not isinstance(confirmations, Mapping) or set(confirmations) != set(eligible):
            raise ValueError("confirmations must match personal and perk_skill sources exactly; no gear")
        for faces in confirmations.values():
            _validate_faces(faces)
    if defender_targeted != (defender_one_confirmations is not None):
        raise ValueError("defender confirmations require a genuine targeted defender")
    actor_points = 0
    defender_points = 0
    actor_attempts = 0
    defender_attempts = 0
    for source in eligible:
        first = original_roll[source]
        actor_faces = actor_ten_confirmations[source]
        expected_tens = sum(face == 10 for face in first)
        if len(actor_faces) != expected_tens:
            raise ValueError(f"{source}: reroll exactly each original personal 10 once")
        actor_attempts += expected_tens
        actor_points += sum(face == 10 for face in actor_faces)
        if defender_one_confirmations is not None:
            defender_faces = defender_one_confirmations[source]
            expected_ones = sum(face == 1 for face in first)
            if len(defender_faces) != expected_ones:
                raise ValueError(f"{source}: defender rerolls each attacker personal 1 once")
            defender_attempts += expected_ones
            defender_points += sum(face == 1 for face in defender_faces)
    return ConfirmedPerkAward(actor_points, defender_points, actor_attempts, defender_attempts)
