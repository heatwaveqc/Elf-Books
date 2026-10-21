"""Elf-Books shared spell/armor/avoidance XP math (DESIGN PROTOTYPE).

Outputs XP in integer tenths. These awards may be tuned later:
  damage source: 2 XP per actual target HP lost [accepted core]
  armor:         4 XP per real HP lost [candidate]
  guard spell:   2 XP per real HP lost while relevant [candidate]
  avoided blow:  2 XP per full attack total [candidate]
  Magicka:       1 XP per actual MP spent by default [candidate, compare 2]
"""
from dataclasses import dataclass

def _whole_nonnegative(value: int, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value

def skill_rank_xp_tenths(rank: int) -> int:
    if type(rank) is not int or not 0 <= rank < 100:
        raise ValueError("rank must be integer 0..99")
    return 50 * max(1, rank)

def outgoing_damage_xp_tenths(actual_hp_removed: int) -> int:
    return 20 * _whole_nonnegative(actual_hp_removed, "HP damage")

def magicka_spend_xp_tenths(actual_mp_spent: int, xp_per_mp: int = 1) -> int:
    _whole_nonnegative(xp_per_mp,"Magicka multiplier")
    return _whole_nonnegative(actual_mp_spent,"Magicka spent") * 10 * xp_per_mp

def worn_armor_xp_tenths(actual_hp_lost: int, wearing_relevant_armor: bool = True) -> int:
    if type(wearing_relevant_armor) is not bool:
        raise ValueError("armor relevance must be boolean")
    return 40 * _whole_nonnegative(actual_hp_lost,"HP lost") if wearing_relevant_armor else 0

def protective_spell_hp_xp_tenths(actual_hp_lost: int, active_and_relevant: bool = True) -> int:
    if type(active_and_relevant) is not bool:
        raise ValueError("spell relevance must be boolean")
    return 20 * _whole_nonnegative(actual_hp_lost,"HP lost") if active_and_relevant else 0

@dataclass(frozen=True)
class Avoidance:
    happened: bool
    xp_tenths: int
    attack_total: int
    reason: str

def credited_avoidance(*, natural_attack_roll: int, attack_total: int, ac_without: int,
                       ac_with: int, method_legal: bool = True, credible: bool = True) -> Avoidance:
    """Apply one defensively relevant AC increment.

    For armor/block/dodge pass AC without and with the selected trained
    method; for spell AC use those before/after spell. All modifiers,
    equipment and alternate AC sources must be resolved by the caller.
    """
    for name,value in (("natural roll",natural_attack_roll),("attack total",attack_total),
                       ("AC without",ac_without),("AC with",ac_with)):
        if type(value) is not int:
            raise ValueError(f"{name} must be an integer")
    if not 1 <= natural_attack_roll <= 20:
        raise ValueError("natural roll must be 1..20")
    if ac_with < ac_without:
        raise ValueError("AC improvement may not reduce AC")
    if type(method_legal) is not bool or type(credible) is not bool:
        raise ValueError("method_legal and credible must be boolean")
    if not method_legal or not credible:
        return Avoidance(False,0,attack_total,"not_eligible")
    if natural_attack_roll == 1:
        return Avoidance(False,0,attack_total,"automatic_miss")
    if natural_attack_roll == 20:
        return Avoidance(False,0,attack_total,"automatic_hit")
    prevented = ac_without <= attack_total < ac_with
    if not prevented:
        return Avoidance(False,0,attack_total,"not_decisive")
    return Avoidance(True,20 * max(0,attack_total),attack_total,"defense_prevented_hit")

def split_effective_damage(hp_before: int, source_damage: list[tuple[str, int]]) -> dict[str,int]:
    """Assign single-target actual HP lost to independent damage sources, in resolution order.

    No source receives more than HP available after prior sources. Damage
    inputs are *post-mitigation* shares; caller determines order and types.
    """
    hp=_whole_nonnegative(hp_before,"HP before")
    out: dict[str,int]={}
    for name,value in source_damage:
        if not isinstance(name,str) or not name:
            raise ValueError("damage source name required")
        _whole_nonnegative(value,"source damage")
        loss=min(hp,value)
        hp-=loss
        out[name]=out.get(name,0)+loss
    return out
