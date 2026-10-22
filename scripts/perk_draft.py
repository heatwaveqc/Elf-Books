"""NON-OPERATIVE playtest helpers for proposed Finesse/free-reaction perks.

These are intentionally limited to local calculations, not the official
purchase gate or a complete Geard Lif combat engine. The source of legal
defense modes/action pools is the existing combat/attack-modes adapter.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class FinesseEffect:
    applied: bool
    threshold_successes: int
    rolled_potence: int
    bonus_faces: tuple[int, ...]
    bonus_potence_successes: int
    modified_potence: int
    extra_dice: int


def finesse_potence(*,accuracy_successes:int,static_avoidance:int,
                   rolled_potence:int,bonus_faces:tuple[int,...]|list[int],
                   application_allowed:bool=True)->FinesseEffect:
    """Roll ONE actual extra Potence d10 per net Accuracy success.

    After Accuracy successfully meets static Avoidance, the surplus
    successes determine the NUMBER OF BONUS DICE rolled in the Potence
    pool. Each bonus face produces ordinary d10 successes: 1-6 -> 0,
    7-9 -> 1, 10 -> 2. These are perk-sourced dice and cannot be
    recorded as Attribute/Talent/Skill/Specialty or equipment dice for
    breakthrough XP, perk-point confirmations, or deed enchantments.

    Caller records the original rolled Potence success magnitude and
    exactly the required bonus die faces from the same actual Effect
    resolution. The bonus never changes the ordinary melee Fatigue hazard.
    """
    for name,val in (("Accuracy",accuracy_successes),
                     ("Avoidance",static_avoidance),("Potence",rolled_potence)):
        if type(val) is not int or val<0:
            raise ValueError(f"{name} must be a nonnegative integer")
    if type(application_allowed) is not bool:
        raise ValueError("application_allowed must be boolean")
    if not isinstance(bonus_faces,(tuple,list)) or any(
        type(face) is not int or face<1 or face>10 for face in bonus_faces
    ):
        raise ValueError("bonus_faces must contain actual d10 faces 1..10")
    applied=application_allowed and accuracy_successes>=static_avoidance
    margin=accuracy_successes-static_avoidance if applied else 0
    if len(bonus_faces)!=margin:
        raise ValueError("roll exactly one Finesse Potence die per surplus Accuracy success")
    bonus_successes=sum(2 if face==10 else 1 if face>=7 else 0
                        for face in bonus_faces)
    return FinesseEffect(
        applied=applied,threshold_successes=margin,
        rolled_potence=rolled_potence,bonus_faces=tuple(bonus_faces),
        bonus_potence_successes=bonus_successes,
        modified_potence=(rolled_potence+bonus_successes) if applied else 0,
        extra_dice=margin,
    )


@dataclass(frozen=True)
class FreeReaction:
    name: str
    method: str
    actions_spent: int
    fatigue_hazard_dice: int
    consumes_round_use: bool


FREE_METHODS={
    "light_footed":"dodge",
    "shield_reflex":"block",
    "flowing_parry":"parry",
}


def plan_free_reaction(*,perk_id:str,method:str,already_used_this_round:bool,
                       reaction_legal:bool,defending_weapon_damage:int=0,
                       defending_weapon_defense:int=0,armor_encumbrance:int=0)->FreeReaction:
    """One free action-cost Dodge/Block/Parry, not a free fatigue Cost.

    The GM/action manager must check actual mode, awareness, equipment,
    timing and whether the perk was bought. It must record the use in
    a per-round ledger. Defending with the normal reaction remains legal
    and separate, provided an action is available.
    """
    if perk_id not in FREE_METHODS or method != FREE_METHODS[perk_id]:
        raise ValueError("this perk does not grant the requested defense method")
    for label,v in (("weapon Damage",defending_weapon_damage),
                    ("weapon Defense",defending_weapon_defense),
                    ("Encumbrance",armor_encumbrance)):
        if type(v) is not int:
            raise ValueError(f"{label} rating must be an integer")
    if type(already_used_this_round) is not bool or type(reaction_legal) is not bool:
        raise ValueError("used/available are boolean inputs")
    if already_used_this_round:
        raise ValueError("free reaction already spent this round")
    if not reaction_legal:
        raise ValueError("defense must be legal and actually available")
    hazard=(max(0,2*armor_encumbrance) if method=="dodge"
            else max(0,defending_weapon_damage,defending_weapon_defense))
    return FreeReaction(perk_id,method,0,hazard,True)
