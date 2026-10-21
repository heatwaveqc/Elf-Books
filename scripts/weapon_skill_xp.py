"""Weapon-skill-to-damage and integer-equivalent XP calculation, PROTOTYPE ONLY."""
from __future__ import annotations
from fractions import Fraction

def skill_bonus(skill: int) -> int:
    if type(skill) is not int or not 0 <= skill <= 100:
        raise ValueError("skill must be integer 0..100")
    return skill // 5

def next_rank_xp(skill: int) -> int:
    if type(skill) is not int or not 0 <= skill < 100:
        raise ValueError("skill must be integer 0..99")
    return 5 * max(1, skill)

def total_xp(a: int, b: int) -> int:
    if type(a) is not int or type(b) is not int or not 0 <= a <= b <= 100:
        raise ValueError("invalid rank interval")
    return sum(next_rank_xp(rank) for rank in range(a,b))

def rolled_damage(dice_total: int, attribute_mod: int, skill: int, extra_flat: int = 0) -> int:
    if any(type(v) is not int for v in (dice_total, attribute_mod, extra_flat)):
        raise ValueError("integer damage inputs required")
    if dice_total < 0:
        raise ValueError("dice total must be nonnegative")
    return max(0, dice_total + attribute_mod + skill_bonus(skill) + extra_flat)

def award_damage_xp(applied_hp_loss: int) -> int:
    if type(applied_hp_loss) is not int or applied_hp_loss < 0:
        raise ValueError("actual HP loss must be nonnegative integer")
    return 2 * applied_hp_loss

def effective_hp_removed(raw_damage: int, target_hp: int, mitigation: int=0) -> int:
    if any(type(v) is not int for v in (raw_damage,target_hp,mitigation)):
        raise ValueError("damage inputs must be integers")
    if min(raw_damage,target_hp,mitigation)<0:
        raise ValueError("damage inputs must be nonnegative")
    return min(target_hp,max(0,raw_damage-mitigation))

def expected_successful_hits(start: int, end: int,
                             die_faces: int, ability_mod: int, flat: int=0) -> Fraction:
    if type(die_faces) is not int or die_faces<2:
        raise ValueError("invalid die")
    if any(type(x) is not int for x in (ability_mod,flat)):
        raise ValueError("ability modifier and flat bonus must be integers")
    # Requires one complete 5-rank block; within that block skill bonus is constant.
    if start%5 != 0 or end != start+5:
        raise ValueError("expected-hit shortcut requires a 5-rank block")
    average_damage = Fraction(die_faces+1,2)+ability_mod+skill_bonus(start)+flat
    if average_damage <= 0:
        raise ValueError("damage must be positive")
    return Fraction(total_xp(start,end),2)/average_damage

def expected_attempts_with_crits(start: int, end: int, die_faces: int,
                                 ability_mod: int, chance_to_hit: Fraction, flat: int=0) -> Fraction:
    if not Fraction(1,20) <= chance_to_hit <= 1:
        raise ValueError("hit chance must include natural-20 automatic hit")
    if start%5 != 0 or end != start+5:
        raise ValueError("requires a 5-rank block")
    avg=Fraction(die_faces+1,2)+ability_mod+skill_bonus(start)+flat
    expected_hp_per_attempt=chance_to_hit*avg+Fraction(1,20)*Fraction(die_faces+1,2)
    return Fraction(total_xp(start,end),2)/expected_hp_per_attempt
