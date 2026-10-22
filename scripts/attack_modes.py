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
from geard_core import RESOURCE_TRACKS, Track, ResourceEffectOutcome, apply_resource_effect

CATALOG = Path(__file__).resolve().parents[1] / "rules" / "attack_modes.json"


@dataclass(frozen=True)
class NamedPool:
    attribute: str
    skill: str
    tier: int
    personal_dice: int
    external_dice: int
    perk_skill_dice: int = 0

    @property
    def dice(self) -> int:
        return self.personal_dice + self.external_dice + self.perk_skill_dice

    @property
    def static_opposition(self) -> int:
        return self.dice // 2


def compose_named_pool(*, attribute: str, skill: str, tier: int,
                       talent: Talent,
                       ratings: Mapping[str, Mapping[int, int]],
                       specialty_declared: bool = False,
                       external_bonuses: Mapping[str, int] | None = None,
                       perk_skill_dice: int = 0) -> NamedPool:
    """The specified Attribute+Skill are sufficient to resolve the four sources.

    External bonuses are a single aggregate cap, no matter how many sources.
    Eligibility and item-specific Control/Effect Tier must be verified by the
    action's adapter before passing these relevant bonuses to the calculator.
    The caller must also validate any `perk_skill_dice` granted by a perk.
    Extra perk-sourced rolled dice increase total dice, but NOT the personal
    base used for the external equipment/enchantment/buff cap.
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
    if type(perk_skill_dice) is not int or perk_skill_dice < 0:
        raise ValueError("perk-granted Skill-equivalent dice must be nonnegative int")
    external = sum(bonuses.values())
    # Only the actual four rated traits define external bonus allowance.
    # Perk Skill-equivalent dice belong in the final rolled pool, but they
    # NEVER expand the external cap or masquerade as gear. A caller must
    # independently validate ownership and the specific perk dice granted.
    if external > personal:
        raise ValueError("aggregate equipment/enchantment/ensorcellment/buff dice exceed unmodified personal pool")
    return NamedPool(attribute,skill,tier,personal,external,perk_skill_dice)


def load_attack_modes() -> dict[str,dict]:
    """Load only curated structured modes. No implicit generic defense fallback."""
    data=json.loads(CATALOG.read_text())
    modes=data["modes"]
    if not isinstance(modes,list) or len({m["id"] for m in modes})!=len(modes):
        raise ValueError("duplicate/invalid attack mode IDs")
    if any(not m.get("valid_defenses") and not m.get("defense_none_explicit",False) for m in modes):
        raise ValueError("contested attack mode has no declared legal defensive responses")
    for mode in modes:
        if (mode.get("typical_target_track") == "plasticity"
            or mode.get("long_term_target_track") == "plasticity"):
            if not mode.get("supernatural_attack",False):
                raise ValueError("only supernatural attacks can directly mark Plasticity")
        if mode.get("kind") == "social":
            if mode.get("typical_target_track") != "attention" or mode.get("supernatural_attack"):
                raise ValueError("ordinary social attacks must target Attention only")
        if mode.get("kind") in {"social","supernatural_social"}:
            if any(d.get("attribute") == "conviction" for d in mode.get("valid_defenses",[])):
                raise ValueError("Conviction is social Resilience/soak, not Avoidance")
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

def apply_mode_resource_effect(*, mode_id:str, magnitude:int,
                               fast:Track, slow:Track,
                               fast_effective_threshold:int|None=None,
                               slow_effective_threshold:int|None=None
                               )->ResourceEffectOutcome:
    """Keep a mode's legal DIRECT resource target, then allow exhaustion routing.

    Ordinary social modes always nominate Attention. Plasticity is reached
    only after Attention is already exhausted, without turning a mundane
    attack into a directly supernatural Plasticity attack. Mode legitimacy
    and resource routing are separate steps.
    """
    modes=load_attack_modes()
    if mode_id not in modes:
        raise ValueError("unknown attack mode")
    mode=modes[mode_id]
    target=mode.get("typical_target_track")
    matching=[aspect for aspect, resource in RESOURCE_TRACKS.items()
              if target in (resource["fast"],resource["slow"])]
    if len(matching)!=1:
        raise ValueError("mode has no recognized target resource track")
    if target=="plasticity" and not mode.get("supernatural_attack",False):
        raise ValueError("direct Plasticity effect must be supernatural")
    return apply_resource_effect(
        aspect=matching[0],requested_resource=target,magnitude=magnitude,
        fast=fast,slow=slow,
        fast_effective_threshold=fast_effective_threshold,
        slow_effective_threshold=slow_effective_threshold)
