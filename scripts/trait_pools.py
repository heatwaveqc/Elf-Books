"""Elf-Books four-source Geard dice pools (0..25 ratings, 1d10 per five rating levels).

One chosen Talent governs exactly five skills; ungoverned skills retain normal
Attribute, Skill and Specialty contributions. Does not derive static Avoidance.
"""
from __future__ import annotations
from dataclasses import dataclass

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
    if role not in ("accuracy","potence"):
        raise ValueError("this helper resolves active Accuracy/Potence pools only")
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
