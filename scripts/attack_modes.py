"""Elf-Books named Attribute + Skill pools, attack modes, legal defense choices.

All applicable Talent (by governed *Skill*), one declared Specialty and external
bonuses are included automatically. The external gear/ensorcellment/enchantment/
temporary-buff dice share one aggregate cap: external <= unmodified personal.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
import json
from pathlib import Path

from trait_pools import ATTRIBUTE_ROLE, Talent, compose_tier_pool

CATALOG = Path(__file__).resolve().parents[1] / "rules" / "attack_modes.json"


@dataclass(frozen=True)
class NamedPool:
    attribute: str
    skill: str
    tier: int
    personal_dice: int
    external_dice: int

    @property
    def dice(self) -> int:
        return self.personal_dice + self.external_dice

    @property
    def static_opposition(self) -> int:
        return self.dice // 2


def compose_named_pool(*, attribute: str, skill: str, tier: int,
                       talent: Talent,
                       ratings: Mapping[str, Mapping[int, int]],
                       specialty_declared: bool = False,
                       external_bonuses: Mapping[str, int] | None = None) -> NamedPool:
    """The specified Attribute+Skill are sufficient to resolve the four sources.

    External bonuses are a single aggregate cap, no matter how many sources.
    Eligibility and item-specific Control/Effect Tier must be verified by the
    action's adapter before passing these relevant bonuses to the calculator.
    """
    if attribute not in ATTRIBUTE_ROLE:
        raise ValueError(f"unknown attribute {attribute!r}")
    personal = compose_tier_pool(
        attribute_name=attribute, role=ATTRIBUTE_ROLE[attribute], tier=tier,
        talent=talent, skill_id=skill, ratings=ratings,
        specialty_declared=specialty_declared
    ).dice
    bonuses = {} if external_bonuses is None else external_bonuses
    if not isinstance(bonuses, Mapping) or any(
        not isinstance(k, str) or not k or type(v) is not int or v < 0
        for k, v in bonuses.items()
    ):
        raise ValueError("external dice must be a source-labeled map of nonnegative ints")
    external = sum(bonuses.values())
    if external > personal:
        raise ValueError("aggregate equipment/enchantment/ensorcellment/buff dice exceed unmodified personal pool")
    return NamedPool(attribute,skill,tier,personal,external)


def load_attack_modes() -> dict[str,dict]:
    """Load only curated structured modes. No implicit generic defense fallback."""
    data=json.loads(CATALOG.read_text())
    modes=data["modes"]
    if not isinstance(modes,list) or len({m["id"] for m in modes})!=len(modes):
        raise ValueError("duplicate/invalid attack mode IDs")
    if any(not m.get("valid_defenses") and not m.get("defense_none_explicit",False) for m in modes):
        raise ValueError("contested attack mode has no declared legal defensive responses")
    return {m["id"]:m for m in modes}


def valid_defense_choices(mode_id: str) -> list[dict]:
    modes=load_attack_modes()
    if mode_id not in modes:
        raise ValueError(f"unknown attack mode {mode_id}")
    return modes[mode_id]["valid_defenses"]


def compose_mode_defense(*,mode_id:str,defense_id:str,tier:int,
                         talent:Talent,
                         ratings:Mapping[str,Mapping[int,int]],
                         specialty_declared:bool=False,
                         external_bonuses:Mapping[str,int]|None=None,
                         response_available:bool=True)->NamedPool:
    """Use exactly one expressly legal response, checking external eligibility.

    The setting adjudicates conditions (awareness, equipped shield, etc.).
    response_available=False signals that the requisite fictional condition
    or action/reaction allowance is NOT met.
    """
    choices=valid_defense_choices(mode_id)
    picked=next((x for x in choices if x["id"]==defense_id),None)
    if picked is None:
        raise ValueError(f"{defense_id} is not a legal defense for {mode_id}")
    if not response_available:
        raise ValueError("defensive response unavailable in this situation")
    return compose_named_pool(
        attribute=picked["attribute"], skill=picked["skill"],tier=tier,
        talent=talent, ratings=ratings,specialty_declared=specialty_declared,
        external_bonuses=external_bonuses
    )
