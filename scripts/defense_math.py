"""Proposed single-method defensive AC and XP credit for Elf-Books.

This is not an approved or playable combat engine. The caller must supply
base AC excluding the selected method, its equipment/attribute contribution,
and skill. No random dice are rolled by this module.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class DefenseResult:
    ac_without_method: int
    ac: int
    hit: bool
    credited_skill: str | None
    would_hit_without_method: bool


def resolve_attack(
    *,
    roll: int,
    attack_bonus: int,
    ac_without_method: int,
    method_gear_or_attribute_bonus: int,
    defense_skill_rank: int,
    chosen_skill: str | None,
    attack_is_credible: bool = True,
) -> DefenseResult:
    """Resolve a D20 attack with at most one eligible defensive skill.

    A method may have +0 gear (Dodge, or weapon parry) and +0 skill at rank 0.
    The caller is responsible for legality of method and attack type.
    Attribute bonus may appear either in the method or baseline, never both.
    """
    if type(roll) is not int or not 1 <= roll <= 20:
        raise ValueError("roll must be integer 1..20")
    for value in (attack_bonus, ac_without_method, method_gear_or_attribute_bonus, defense_skill_rank):
        if type(value) is not int:
            raise ValueError("attack and AC values must be integers")
    if ac_without_method < 0 or method_gear_or_attribute_bonus < 0:
        raise ValueError("AC and method bonuses must not be negative in this prototype")
    if not 0 <= defense_skill_rank <= 100:
        raise ValueError("defense skill must range from 0 to 100")
    if chosen_skill is not None and chosen_skill not in {"heavy_armor", "light_armor", "block", "dodge"}:
        raise ValueError("invalid defense method")
    if chosen_skill is None and (defense_skill_rank != 0 or method_gear_or_attribute_bonus != 0):
        raise ValueError("no chosen method cannot have its own bonus")
    if type(attack_is_credible) is not bool:
        raise ValueError("credibility must be a boolean")

    method_bonus = method_gear_or_attribute_bonus + defense_skill_rank // 5
    ac = ac_without_method + method_bonus
    total = roll + attack_bonus
    if roll == 1:
        hit = False
    elif roll == 20:
        hit = True
    else:
        hit = total >= ac
    would_hit = roll == 20 or (roll != 1 and total >= ac_without_method)
    skill_saved = (
        chosen_skill is not None and attack_is_credible
        and 1 < roll < 20 and not hit and total >= ac_without_method
    )
    return DefenseResult(ac_without_method, ac, hit, chosen_skill if skill_saved else None, would_hit)


def defense_perk_breakthrough(result: DefenseResult, discovery_roll: int, perk_available: bool) -> bool:
    """Natural 20 on separate verified roll after actual defensive save; never rolls internally."""
    if type(discovery_roll) is not int or not 1 <= discovery_roll <= 20:
        raise ValueError("discovery roll must be a d20")
    if type(perk_available) is not bool:
        raise ValueError("perk_available must be boolean")
    return result.credited_skill is not None and perk_available and discovery_roll == 20
