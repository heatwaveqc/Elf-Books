"""Candidate K=5 actual-applied-damage XP experiment, not adopted rules."""
from __future__ import annotations
from fractions import Fraction

def xp_to_next(current_skill: int, multiplier: int = 5) -> int:
    if type(current_skill) is not int or not 0 <= current_skill < 100:
        raise ValueError("skill must be integer 0..99")
    if type(multiplier) is not int or multiplier < 1:
        raise ValueError("multiplier must be a positive integer")
    return multiplier * max(1, current_skill)

def total_required(start: int, end: int, multiplier: int = 5) -> int:
    if type(start) is not int or type(end) is not int or not 0 <= start <= end <= 100:
        raise ValueError("invalid rank range")
    return sum(xp_to_next(s, multiplier) for s in range(start, end))

def effective_damage_xp(rolled_damage: int, target_hp_before: int, mitigation: int = 0) -> int:
    """Actual HP lost; excludes raw overkill and damage blocked by mitigation.

    This function models a single target and one attributed attack only;
    the call-site must assign damage source and skill, not duplicate credit.
    """
    if any(type(x) is not int for x in (rolled_damage, target_hp_before, mitigation)):
        raise ValueError("damage, target HP, and mitigation must be integers")
    if rolled_damage < 0 or target_hp_before < 0 or mitigation < 0:
        raise ValueError("damage, target HP, and mitigation must be nonnegative")
    return min(target_hp_before, max(0, rolled_damage - mitigation))

def expected_successful_hits(required_xp: int, effective_hp_per_hit: Fraction) -> Fraction:
    if type(required_xp) is not int or required_xp < 0:
        raise ValueError("required XP must be a nonnegative integer")
    if effective_hp_per_hit <= 0:
        raise ValueError("effective HP per hit must be positive")
    return Fraction(required_xp, 1) / effective_hp_per_hit

def encounter_damage_budget(enemy_hp: int, own_damage_share: Fraction = Fraction(1)) -> Fraction:
    """Maximum damage XP for one unhealed HP pool at the given participation share."""
    if type(enemy_hp) is not int or enemy_hp < 0:
        raise ValueError("HP must be nonnegative integer")
    if not 0 <= own_damage_share <= 1:
        raise ValueError("share must be in 0..1")
    return enemy_hp * own_damage_share
