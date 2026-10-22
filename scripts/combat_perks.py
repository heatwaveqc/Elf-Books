"""Elf Books combat-perk effect pilots against current Geard Lif combat modes.

Pure planning helpers, not a complete round engine. Exact purchase gates,
specialties, individual equipment statistics, and enchanting are separate.
A technique's extra damage dice are tagged 'perk', not four character-trait
source dice nor equipment dice. They do not by themselves confirm character
perk points or make equipment eligible for deed enchantments.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from attack_modes import NamedPool, compose_named_pool
from trait_pools import Talent, MAX_RATING, RATING_PER_DIE


def _nonnegative(value: int, label: str) -> None:
    if type(value) is not int or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")


@dataclass(frozen=True)
class PowerBashPlan:
    technique_damage_dice: int
    weapon_damage_bonus_with_bash: int
    normal_fatigue_hazard_dice: int
    additional_fatigue_hazard_dice: int
    total_fatigue_hazard_dice: int
    technique_die_source: str = "perk"


def plan_power_bash(
    *, strength_rating: int, added_damage_dice: int,
    weapon_damage_rating: int, normal_fatigue_hazard_dice: int,
    muscle_powered_attack: bool = True,
) -> PowerBashPlan:
    """Extra damage k up to Strength DICE; additional fatigue Cost is 2*k.

    This is a declared exertion-bearing muscle-powered attack such as a
    shield bash. Geard's simple-melee default hazard is max(0, weapon
    Damage), but weapon modes may specify a different base hazard.
    The added 2*k Fatigue Cost applies for an attempt even when it misses.
    This is a technique's personal trained output, not new item stats.
    """
    if type(strength_rating) is not int or not 0 <= strength_rating <= MAX_RATING:
        raise ValueError("Strength rating must be 0..25")
    _nonnegative(added_damage_dice, "added damage dice")
    _nonnegative(normal_fatigue_hazard_dice, "normal hazard")
    if type(weapon_damage_rating) is not int:
        raise ValueError("weapon Damage rating must be an integer")
    if type(muscle_powered_attack) is not bool or not muscle_powered_attack:
        raise ValueError("Power Bash requires a muscle-powered exertion-bearing attack")
    strength_dice = strength_rating // RATING_PER_DIE
    if added_damage_dice > strength_dice:
        raise ValueError("Power Bash extra dice cannot exceed Strength dice")
    additional = 2 * added_damage_dice
    return PowerBashPlan(
        technique_damage_dice=added_damage_dice,
        weapon_damage_bonus_with_bash=weapon_damage_rating + added_damage_dice,
        normal_fatigue_hazard_dice=normal_fatigue_hazard_dice,
        additional_fatigue_hazard_dice=additional,
        total_fatigue_hazard_dice=normal_fatigue_hazard_dice + additional,
    )


@dataclass(frozen=True)
class DeflectArrowsPlan:
    parry_pool: NamedPool
    reaction_actions: int
    fatigue_hazard_dice: int


def plan_deflect_arrows(
    *, projectile_kind: str, parrying_skill: str, talent: Talent,
    tier: int, ratings: Mapping[str, Mapping[int,int]],
    available_actions: int, parry_capable_weapon: bool,
    weapon_damage_rating: int, weapon_defense_rating: int,
    specialty_declared: bool = False,
    external_bonuses: Mapping[str,int] | None = None,
) -> DeflectArrowsPlan:
    """Let a parry-capable weapon Parry an ARROW as a paid ordinary defense.

    Attack mode's global projectile menu still forbids ordinary Parry.
    Having the Deflect Arrows perk is the exception; this helper is only
    invoked once the character owns it. It does NOT permit Parry vs
    gunfire, a physical ice-spear magic missile, or direct maledictions.
    Defensive action and normal parrying-item Fatigue Cost are unchanged.
    """
    if projectile_kind != "arrow":
        raise ValueError("Deflect Arrows currently permits arrows only")
    if parrying_skill not in {"one_handed","two_handed"}:
        raise ValueError("Deflect Arrows needs a legal wielded weapon Parry Skill")
    if type(parry_capable_weapon) is not bool or not parry_capable_weapon:
        raise ValueError("held weapon must have a real Parry mode")
    _nonnegative(available_actions, "available actions")
    if available_actions < 1:
        raise ValueError("Parry reaction requires an available combat action")
    for rating in (weapon_damage_rating, weapon_defense_rating):
        if type(rating) is not int:
            raise ValueError("weapon mode ratings must be integers")
    pool=compose_named_pool(
        attribute="dexterity", skill=parrying_skill, tier=tier,
        talent=talent, ratings=ratings,
        specialty_declared=specialty_declared,
        external_bonuses=external_bonuses,
    )
    hazard=max(0,weapon_damage_rating,weapon_defense_rating)
    return DeflectArrowsPlan(
        parry_pool=pool, reaction_actions=1, fatigue_hazard_dice=hazard
    )


@dataclass(frozen=True)
class DualFlurryPlan:
    attack_actions: int
    strikes: int
    fatigue_hazards: tuple[int,int]


def plan_dual_flurry(
    *, primary_weapon_hazard_dice: int,
    secondary_weapon_hazard_dice: int,
    available_actions: int, two_ready_melee_weapons: bool,
) -> DualFlurryPlan:
    """One attack action, TWO real strike resolutions, each with normal Cost.

    Each strike gets a separate Accuracy/Potence roll against one legitimate
    target and a separate attempted-attack Fatigue Cost even if missed.
    Costs are separate incidents; apply marks before the next strike so
    fatigue penalties/fast-to-slow overflow may affect it. This grants no
    additional reactions, passive defenses or round actions.
    """
    _nonnegative(primary_weapon_hazard_dice, "primary hazard")
    _nonnegative(secondary_weapon_hazard_dice, "secondary hazard")
    _nonnegative(available_actions, "available actions")
    if type(two_ready_melee_weapons) is not bool or not two_ready_melee_weapons:
        raise ValueError("Dual Flurry requires two ready usable melee weapons")
    if available_actions < 1:
        raise ValueError("Dual Flurry requires one available attack action")
    return DualFlurryPlan(
        attack_actions=1, strikes=2,
        fatigue_hazards=(primary_weapon_hazard_dice,secondary_weapon_hazard_dice),
    )
