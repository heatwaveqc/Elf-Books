"""Core accepted AC expression and prototype defense XP attribution.

This is not the complete combat system. Reaction/free-perk eligibility and
equipment legality are inputs; the LLM GM must not infer a nonexistent perk.
"""
from dataclasses import dataclass
from typing import Literal

Method=Literal["heavy_armor","light_armor","block","dodge","untrained"]


@dataclass(frozen=True)
class DefenseOutcome:
    ac: int
    hit: bool
    reaction_consumed: bool
    selected_defense_xp_eligible: bool
    armor_hp_loss_xp: int


def defense_outcome(*, method: Method, skill_rank: int, attribute_mod: int,
                    armor_mod: int, shield_mod: int, other_legal_mod: int,
                    attack_roll: int, attack_bonus: int,
                    reaction_available: bool=True, free_reaction_perk: bool=False,
                    worn_armor: str|None=None, hp_lost: int=0,
                    credible: bool=True) -> DefenseOutcome:
    """Defensive skill contributes floor(skill/5), without an innate 10.

    All gear modifiers are externally determined (e.g. plate +8, not AC 18).
    Attribute mod is selected using CON/DEX/STR by the caller.
    """
    if method not in ("heavy_armor","light_armor","block","dodge","untrained"):
        raise ValueError("unrecognized defense")
    if any(type(x) is not int for x in (skill_rank,attribute_mod,armor_mod,shield_mod,other_legal_mod,
                                        attack_roll,attack_bonus,hp_lost)):
        raise ValueError("expected integer values")
    if not 0 <= skill_rank <= 100 or not 1 <= attack_roll <= 20 or hp_lost < 0:
        raise ValueError("skill 0..100, attack d20 1..20, HP loss nonnegative required")
    if method == "untrained" and skill_rank:
        raise ValueError("untrained fallback cannot apply trained skill")
    if worn_armor not in (None,"heavy_armor","light_armor"):
        raise ValueError("worn armor must be heavy/light/none")
    if method in ("heavy_armor","light_armor") and worn_armor != method:
        raise ValueError("cannot use armor defense without wearing matching armor")
    if type(reaction_available) is not bool or type(free_reaction_perk) is not bool or type(credible) is not bool:
        raise ValueError("reaction/perk/credibility must be booleans")
    needs_reaction = method in ("block","dodge") and not free_reaction_perk
    if needs_reaction and not reaction_available:
        raise ValueError("chosen defense needs unavailable reaction")
    gear=armor_mod+shield_mod+other_legal_mod
    ac=gear+attribute_mod+skill_rank//5
    total=attack_roll+attack_bonus
    hit=attack_roll==20 or (attack_roll!=1 and total>=ac)
    qualifies=(method in ("block","dodge") and credible and 1<attack_roll<20 and
               gear <= total < ac)
    return DefenseOutcome(ac=ac,hit=hit,reaction_consumed=needs_reaction,
                          selected_defense_xp_eligible=qualifies,
                          armor_hp_loss_xp=hp_lost if worn_armor else 0)
