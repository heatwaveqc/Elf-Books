"""Elf-Books magic: school-linked spell rolls and full-source static Mana Cost resistance.

Casting uses Perception + School for Accuracy, Intelligence + School for
Potence, and Will + applicable Talent + School + Spell Specialty for
static Mana Cost resistance, plus qualifying cost-reducing gear.

Cost magnitude STILL rolls unmodified, no resistance roll; Mind/Will
sets Mana track capacity. Soul/Conviction governs Plasticity/Attention.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from trait_pools import Talent, compose_tier_pool, dice_for_rating, validate_tier_ratings
from geard_core import Track
from advancement import passive_xp_tenths
from attack_modes import compose_named_pool


@dataclass(frozen=True)
class SpellPools:
    accuracy_dice: int
    potence_dice: int


def casting_pools(*, tier:int, talent:Talent, school_id:str,
                  accuracy_ratings:Mapping[str,Mapping[int,int]],
                  potence_ratings:Mapping[str,Mapping[int,int]],
                  specialty_declared:bool=True,
                  accuracy_external_bonuses:Mapping[str,int]|None=None,
                  potence_external_bonuses:Mapping[str,int]|None=None)->SpellPools:
    """Same school Skill, different Accuracy/Potence Attributes."""
    a=compose_tier_pool(attribute_name="perception",role="accuracy",tier=tier,
                        talent=talent,skill_id=school_id,ratings=accuracy_ratings,
                        specialty_declared=specialty_declared)
    p=compose_tier_pool(attribute_name="intelligence",role="potence",tier=tier,
                        talent=talent,skill_id=school_id,ratings=potence_ratings,
                        specialty_declared=specialty_declared)
    acc_external=compose_named_pool(attribute="perception",skill=school_id,tier=tier,
        talent=talent,ratings=accuracy_ratings,specialty_declared=specialty_declared,
        external_bonuses=accuracy_external_bonuses)
    pot_external=compose_named_pool(attribute="intelligence",skill=school_id,tier=tier,
        talent=talent,ratings=potence_ratings,specialty_declared=specialty_declared,
        external_bonuses=potence_external_bonuses)
    assert acc_external.personal_dice == a.dice
    assert pot_external.personal_dice == p.dice
    return SpellPools(acc_external.dice,pot_external.dice)


@dataclass(frozen=True)
class ManaCostResolution:
    cost_magnitude: int
    resistance_dice: int
    effective_threshold: int
    mark_capacity_per_grade: int
    new_mana: Track


def mana_cost_resistance(*, tier:int, talent:Talent, school_id:str,
                         will_tiers:Mapping[int,int],
                         school_skill_tiers:Mapping[int,int],
                         talent_tiers:Mapping[int,int]|None=None,
                         specialty_tiers:Mapping[int,int]|None=None,
                         specialty_declared:bool=False,
                         robe_dice:int=0,
                         external_bonuses:Mapping[str,int]|None=None)->tuple[int,int]:
    """Static Will + Talent(if governed) + School + Spell Specialty + robe.

    At chosen Tier the Skill requires a Will die and the Specialty a
    School Skill die, but can have HIGHER ratings than their parents.
    Talent needn't govern Skill to permit casting, it simply adds zero.
    Robes contribute equipment dice only; threshold=floor(all dice/2).
    """
    if not isinstance(talent,Talent):
        raise ValueError("selected Talent required")
    talent_source = ({0:talent.rating} if talent_tiers is None else talent_tiers)
    specialty_source = ({0:0} if specialty_tiers is None else specialty_tiers)
    ratings={
        "attribute":will_tiers,
        "talent":talent_source,
        "skill":school_skill_tiers,
        "specialty":specialty_source,
    }
    personal=compose_tier_pool(attribute_name="will",role="resilience",tier=tier,
                               talent=talent,skill_id=school_id,ratings=ratings,
                               specialty_declared=specialty_declared)
    if type(robe_dice) is not int or robe_dice<0:
        raise ValueError("robe dice must be a nonnegative integer")
    bonuses={} if external_bonuses is None else dict(external_bonuses)
    if robe_dice:
        bonuses["cost_reducing_robe"]=bonuses.get("cost_reducing_robe",0)+robe_dice
    combined=compose_named_pool(attribute="will",skill=school_id,tier=tier,
        talent=talent,ratings=ratings,specialty_declared=specialty_declared,
        external_bonuses=bonuses)
    total=combined.dice
    threshold=total//2
    if threshold<1:
        raise ValueError("zero Cost-resistance threshold remains undefined")
    return total,threshold


def resolve_mana_cost(*, tier:int, cost_magnitude:int, talent:Talent,
                      school_id:str,will_tiers:Mapping[int,int],
                      school_skill_tiers:Mapping[int,int],
                      talent_tiers:Mapping[int,int]|None=None,
                      specialty_tiers:Mapping[int,int]|None=None,
                      specialty_declared:bool=False,
                      robe_dice:int=0,
                      external_bonuses:Mapping[str,int]|None=None,
                      existing_mana:Track|None=None)->ManaCostResolution:
    """Grade the separately rolled Cost against static resistance.

    **Will**, the Resilience of the Mind aspect, defines Mana mark slots.
    Spell Specialty/Talent/robes can change the severity THRESHOLD only.
    Cost magnitude must already be converted to the chosen resource Tier.
    """
    if type(cost_magnitude) is not int or cost_magnitude<0:
        raise ValueError("Cost must be nonnegative rolled magnitude")
    validate_tier_ratings(will_tiers)
    capacity=dice_for_rating(will_tiers.get(tier,0))
    if capacity<1:
        raise ValueError("resource mark capacity requires a Will die at chosen Tier")
    pool,threshold=mana_cost_resistance(
        tier=tier,talent=talent,school_id=school_id,
        will_tiers=will_tiers,school_skill_tiers=school_skill_tiers,
        talent_tiers=talent_tiers,specialty_tiers=specialty_tiers,
        specialty_declared=specialty_declared,robe_dice=robe_dice,
        external_bonuses=external_bonuses)
    track=Track(capacity) if existing_mana is None else existing_mana
    if track.resilience!=capacity:
        raise ValueError("Mana mark capacity must be Will-based, not gear/Talent/School")
    next_track=track.apply_effect(cost_magnitude,effective_threshold=threshold)
    return ManaCostResolution(cost_magnitude,pool,threshold,capacity,next_track)


def mana_cost_practice_xp(*, tier:int, talent:Talent, school_id:str,
                          will_rating:int, school_skill_rating:int,
                          talent_rating:int|None=None,
                          specialty_rating:int=0,
                          specialty_declared:bool=False)->dict[str,int]:
    """XP on genuine resisted Mana Cost: all four actual personal sources.

    The chosen Talent earns XP only on its governed five Skills; the
    particular spell Specialty only if declared. Gear earns no trait XP.
    """
    if not isinstance(talent,Talent):
        raise ValueError("selected Talent required")
    involved={"will":will_rating,"school_skill":school_skill_rating}
    if school_id in talent.governed_skills:
        involved["talent"]=talent.rating if talent_rating is None else talent_rating
    if specialty_declared:
        involved["specialty"]=specialty_rating
    return passive_xp_tenths(involved,tier=tier)


def counterspell_avoidance(*,tier:int,talent:Talent,
                           ratings:Mapping[str,Mapping[int,int]],
                           specialty_declared:bool=False,
                           external_bonuses:Mapping[str,int]|None=None)->int:
    """Chosen reactive counterspell uses Wits + Mysticism, Talent and Specialty.

    This remains a separate selected defense; it doesn't stack with Dodge
    or a different ward. Its timing and cost are not yet specified.
    """
    pool=compose_tier_pool(attribute_name="wits",role="avoidance",tier=tier,
                           talent=talent,skill_id="mysticism",
                           ratings=ratings,specialty_declared=specialty_declared)
    return compose_named_pool(attribute="wits",skill="mysticism",tier=tier,
        talent=talent,ratings=ratings,specialty_declared=specialty_declared,
        external_bonuses=external_bonuses).static_opposition
