"""Elf-Books four-source Geard dice pools (0..25 ratings, 1d10 per five rating levels).

One chosen Talent governs exactly five skills; ungoverned skills retain normal
Attribute, Skill and Specialty contributions. Does not derive static Avoidance.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping

ATTRIBUTES={
 "body":{"potence":"strength","accuracy":"dexterity","avoidance":"agility","resilience":"health"},
 "mind":{"potence":"intelligence","accuracy":"perception","avoidance":"wits","resilience":"will"},
 "soul":{"potence":"charisma","accuracy":"insight","avoidance":"temperance","resilience":"conviction"},
}
ATTRIBUTE_ROLE={name:role for aspect in ATTRIBUTES.values() for role,name in aspect.items()}
MAX_RATING=25
RATING_PER_DIE=5

def dice_for_rating(rating:int)->int:
    _rating(rating,"trait")
    return rating//RATING_PER_DIE

def _rating(value:int,name:str)->None:
    if type(value)!=int or not 0<=value<=MAX_RATING:
        raise ValueError(f"{name} rating must be integer 0..{MAX_RATING} (current working cap)")

@dataclass(frozen=True)
class Talent:
    name:str
    governed_skills:frozenset[str]
    rating:int

    def __post_init__(self):
        if not isinstance(self.name,str) or not self.name.strip():
            raise ValueError("Talent name required")
        if not isinstance(self.governed_skills,frozenset) or len(self.governed_skills)!=5:
            raise ValueError("Talent must govern exactly five distinct skills")
        if any(not isinstance(s,str) or not s for s in self.governed_skills):
            raise ValueError("governed skill IDs must be nonempty")
        _rating(self.rating,"Talent")

    def validate_catalog(self,catalog:set[str])->None:
        if not self.governed_skills<=catalog:
            raise ValueError("Talent contains a noncanonical skill")

@dataclass(frozen=True)
class PersonalPool:
    attribute:int
    talent:int
    skill:int
    specialty:int

    @property
    def dice(self)->int:
        return self.attribute+self.talent+self.skill+self.specialty

def compose_pool(*,attribute_name:str,role:str,attribute_rating:int,
                 talent:Talent,skill_id:str,skill_rating:int,
                 specialty_rating:int=0)->PersonalPool:
    if role not in ("accuracy","potence","avoidance","resilience"):
        raise ValueError("invalid functional role for trait pool")
    if ATTRIBUTE_ROLE.get(attribute_name)!=role:
        raise ValueError("attribute does not match the requested functional role")
    if not isinstance(skill_id,str) or not skill_id:
        raise ValueError("valid skill ID required")
    for name,value in (("Attribute",attribute_rating),("Skill",skill_rating),
                       ("Specialty",specialty_rating)):
        _rating(value,name)
    if not isinstance(talent,Talent):
        raise ValueError("one character-selected Talent must be supplied")
    return PersonalPool(dice_for_rating(attribute_rating),
                        dice_for_rating(talent.rating) if skill_id in talent.governed_skills else 0,
                        dice_for_rating(skill_rating),dice_for_rating(specialty_rating))


def validate_tier_ratings(ratings: Mapping[int,int]) -> None:
    """Tier N rating may exist only if every previous Tier is maxed at 25."""
    if not isinstance(ratings, Mapping) or 0 not in ratings:
        raise ValueError("Tier 0 rating is required")
    if any(type(k) is not int or k < 0 for k in ratings):
        raise ValueError("Tier indices must be nonnegative integers")
    for tier in range(max(ratings) + 1):
        if tier not in ratings:
            raise ValueError("cannot skip a trait Tier")
        _rating(ratings[tier], f"Tier {tier}")
        if tier and ratings[tier - 1] != MAX_RATING:
            raise ValueError("prior Tier must reach 25 before unlocking next Tier")


def compose_tier_pool(*, attribute_name: str, role: str, tier: int,
                      talent: Talent, skill_id: str,
                      ratings: Mapping[str,Mapping[int,int]],
                      specialty_declared: bool = True) -> PersonalPool:
    """Select applicable personal dice at one Tier; parents need one same-Tier die.

    There is NO rating cap between Attribute, Skill, and Specialty.
    Talent is not in either governing-die prerequisite chain.
    """
    if type(tier) is not int or tier < 0:
        raise ValueError("Tier must be nonnegative integer")
    if set(ratings) != {"attribute","talent","skill","specialty"}:
        raise ValueError("all four trait-tier rating maps required")
    for series in ratings.values():
        validate_tier_ratings(series)
    att = ratings["attribute"].get(tier, 0)
    ski = ratings["skill"].get(tier, 0)
    spe = ratings["specialty"].get(tier, 0) if specialty_declared else 0
    tal = ratings["talent"].get(tier, 0)
    if ski >= RATING_PER_DIE and att < RATING_PER_DIE:
        raise ValueError("Skill at chosen Tier needs at least one governing Attribute die")
    if spe >= RATING_PER_DIE and ski < RATING_PER_DIE:
        raise ValueError("Specialty at chosen Tier needs at least one governing Skill die")
    if att + tal + ski + spe == 0:
        raise ValueError("no available personal trait rating at chosen Tier")
    return compose_pool(
        attribute_name=attribute_name, role=role, attribute_rating=att,
        talent=Talent(talent.name,talent.governed_skills,tal),
        skill_id=skill_id,skill_rating=ski,specialty_rating=spe)
