"""Elf-Books magic bridge: school-linked spell pools and static Mana Cost resistance.

The generic Geard Lif Cost still rolls its magnitude unchanged, without
an Application roll. School-specific Will + Skill + cost-robes supply a
static severity threshold; Conviction ALONE determines Mana slot capacity.

Tier conversion and actual random Cost faces are applied by the caller.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from trait_pools import Talent,compose_tier_pool,dice_for_rating,validate_tier_ratings
from geard_core import Track
from advancement import passive_xp_tenths

@dataclass(frozen=True)
class SpellPools:
    accuracy_dice: int
    potence_dice: int

def casting_pools(*,tier:int,talent:Talent,school_id:str,
                  accuracy_ratings:Mapping[str,Mapping[int,int]],
                  potence_ratings:Mapping[str,Mapping[int,int]],
                  specialty_declared:bool=True)->SpellPools:
    """Use Perception + School for Accuracy, Intelligence + School for Potence.

    An applicable five-skill Talent and a single relevant Specialty enter
    these rolls under the ordinary four-source rules.
    """
    a=compose_tier_pool(attribute_name="perception",role="accuracy",tier=tier,
                        talent=talent,skill_id=school_id,ratings=accuracy_ratings,
                        specialty_declared=specialty_declared)
    p=compose_tier_pool(attribute_name="intelligence",role="potence",tier=tier,
                        talent=talent,skill_id=school_id,ratings=potence_ratings,
                        specialty_declared=specialty_declared)
    return SpellPools(a.dice,p.dice)

@dataclass(frozen=True)
class ManaCostResolution:
    cost_magnitude: int
    resistance_dice: int
    effective_threshold: int
    mark_capacity_per_grade: int
    new_mana: Track

def mana_cost_resistance(*,tier:int,will_tiers:Mapping[int,int],
                         school_skill_tiers:Mapping[int,int],robe_dice:int=0
                         )->tuple[int,int]:
    """Will + same school Skill + cost-reducing gear, half pool rounded down.

    Talent and spell Specialty do NOT automatically enter this static Cost
    guard; a separate named effect could explicitly make them relevant.
    """
    if type(tier) is not int or tier<0:
        raise ValueError("Tier must be nonnegative")
    validate_tier_ratings(will_tiers)
    validate_tier_ratings(school_skill_tiers)
    if type(robe_dice) is not int or robe_dice<0:
        raise ValueError("robe dice must be a nonnegative integer")
    will=dice_for_rating(will_tiers.get(tier,0))
    school=dice_for_rating(school_skill_tiers.get(tier,0))
    if school>0 and will==0:
        raise ValueError("Cost Skill dice need a Will Attribute die at the same Tier")
    personal=will+school
    if robe_dice>personal:
        raise ValueError("gear cannot exceed the personal Cost resistance dice budget")
    pool=personal+robe_dice
    threshold=pool//2
    if threshold<1:
        raise ValueError("zero Cost-resistance threshold remains undefined")
    return pool,threshold

def resolve_mana_cost(*,tier:int,cost_magnitude:int,
                      will_tiers:Mapping[int,int],
                      school_skill_tiers:Mapping[int,int],
                      conviction_tiers:Mapping[int,int],
                      robe_dice:int=0,
                      existing_mana:Track|None=None)->ManaCostResolution:
    """The Cost roll is already resolved; robes change grade, never Cost dice.

    Cost magnitude must already be converted to the target resource Tier
    by the caller. No extra resistance die roll occurs.
    """
    if type(cost_magnitude) is not int or cost_magnitude<0:
        raise ValueError("Cost must be nonnegative rolled magnitude")
    validate_tier_ratings(conviction_tiers)
    capacity=dice_for_rating(conviction_tiers.get(tier,0))
    if capacity<1:
        raise ValueError("resource mark capacity requires a Conviction die at chosen Tier")
    pool,threshold=mana_cost_resistance(
        tier=tier,will_tiers=will_tiers,
        school_skill_tiers=school_skill_tiers,robe_dice=robe_dice)
    track=Track(capacity) if existing_mana is None else existing_mana
    if track.resilience!=capacity:
        raise ValueError("Mana capacity must be based on Conviction, not robes")
    next_track=track.apply_effect(cost_magnitude,effective_threshold=threshold)
    return ManaCostResolution(cost_magnitude,pool,threshold,capacity,next_track)

def mana_cost_practice_xp(*,tier:int,will_rating:int,school_skill_rating:int
                         )->dict[str,int]:
    """XP on genuine resisted Mana Cost, before equipment grants."""
    return passive_xp_tenths({"will":will_rating,"school_skill":school_skill_rating},tier=tier)

def counterspell_avoidance(*,tier:int,talent:Talent,
                           ratings:Mapping[str,Mapping[int,int]],
                           specialty_declared:bool=False)->int:
    """Chosen reactive counterspell uses Wits + Mysticism, optionally Talent/Spec.

    This is one alternative selected defense; it doesn't add to Dodge,
    mundane Block, or a separately chosen protective ward.
    Counterspell action/cost eligibility remains to be finalized.
    """
    pool=compose_tier_pool(attribute_name="wits",role="avoidance",tier=tier,
                           talent=talent,skill_id="mysticism",
                           ratings=ratings,specialty_declared=specialty_declared)
    return pool.dice//2
