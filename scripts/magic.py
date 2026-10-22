"""Elf-Books magic: one spell Potence roll supplies Effect and variable Mana Cost.

Casting uses Perception + School for Accuracy, Intelligence + School for
Potence, and Will + applicable Talent + School + Spell Specialty for
static Mana Cost resistance. A spell's Cost is that effect's SAME Potence successes
plus recorded fixed parameter surcharges, NOT a separate Cost roll.
Compound spells generate independent effect Potence and Cost incidents.
Mind/Will sets Mana/Spirit capacity; Soul/Conviction sets social tracks.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping, Sequence
from trait_pools import Talent, compose_tier_pool, dice_for_rating, validate_tier_ratings
from geard_core import Track, apply_resource_effect
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
    new_spirit: Track
    applied_resource: str
    redirected: bool


def spell_is_learned(specialty_tiers:Mapping[int,int])->bool:
    """Rating 1+ in a spell's Specialty unlocks casting (even without a die)."""
    validate_tier_ratings(specialty_tiers)
    return any(rating >= 1 for rating in specialty_tiers.values())


def spell_cost_from_potence(*, potence_successes:int,
                            parameter_surcharge:int=0)->int:
    """One shared Potence result plus FIXED designed cost-success surcharges.

    The caller must obtain the surcharge from the learned formula, never
    invent parameters during casting. This also applies after Accuracy misses.
    """
    if type(potence_successes) is not int or potence_successes < 0:
        raise ValueError("Potence successes must be a nonnegative integer")
    if type(parameter_surcharge) is not int or parameter_surcharge < 0:
        raise ValueError("fixed parameter surcharge must be a nonnegative integer")
    return potence_successes + parameter_surcharge


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
                      existing_mana:Track|None=None,
                      existing_spirit:Track|None=None,
                      spirit_effective_threshold:int|None=None)->ManaCostResolution:
    """Grade an already computed Cost magnitude against static resistance.

    Spells MUST feed this resolver the result of spell_cost_from_potence,
    rather than a separately rolled Cost value. Other Cost effects can
    continue to compute magnitudes from their own source rules.

    **Will**, the Resilience of the Mind aspect, defines Mana mark slots.
    Spell Specialty/Talent/robes can change the severity THRESHOLD only.
    Cost magnitude must already be converted to the chosen resource Tier.\n    If Mana is already exhausted BEFORE the Cost, route the whole Cost into\n    Spirit. Spirit uses its own severity threshold (default Will capacity),\n    not automatically the spell's Mana Cost-reduction robe bonuses.\n    Saved pairs must be supplied together; never silently wipe Spirit.
    """
    if type(cost_magnitude) is not int or cost_magnitude<0:
        raise ValueError("Cost must be nonnegative magnitude")
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
    if (existing_mana is None) != (existing_spirit is None):
        raise ValueError("pass both saved Mana and Spirit tracks together to preserve state")
    mana=Track(capacity) if existing_mana is None else existing_mana
    spirit=Track(capacity) if existing_spirit is None else existing_spirit
    if mana.resilience!=capacity or spirit.resilience!=capacity:
        raise ValueError("Mind/Mana and Spirit capacities must derive from Will, not gear/Talent/School")
    routed=apply_resource_effect(
        aspect="mind",requested_resource="mana",magnitude=cost_magnitude,
        fast=mana,slow=spirit,fast_effective_threshold=threshold,
        slow_effective_threshold=spirit_effective_threshold)
    actual_threshold = (capacity if spirit_effective_threshold is None
                        else spirit_effective_threshold) if routed.redirected else threshold
    return ManaCostResolution(cost_magnitude,pool,actual_threshold,capacity,
                              routed.fast,routed.slow,routed.applied_resource,
                              routed.redirected)


def resolve_spell_cast_cost(*, potence_successes:int,
                            parameter_surcharge:int,
                            spell_specialty_tiers:Mapping[int,int],
                            tier:int, talent:Talent, school_id:str,
                            will_tiers:Mapping[int,int],
                            school_skill_tiers:Mapping[int,int],
                            talent_tiers:Mapping[int,int]|None=None,
                            robe_dice:int=0,
                            external_bonuses:Mapping[str,int]|None=None,
                            existing_mana:Track|None=None,
                            existing_spirit:Track|None=None,
                            spirit_effective_threshold:int|None=None)->ManaCostResolution:
    """Use ONE Potence roll for the spell's output and Cost, even on a miss.

    This helper grades Cost independent of whether Accuracy applied:
    a missed spell still incurs its Potence plus fixed parameter surcharge.
    The learned formula's parameters are supplied by the caller.
    """
    if not spell_is_learned(spell_specialty_tiers):
        raise ValueError("spell Specialty rating 1+ is required to cast")
    return resolve_mana_cost(
        tier=tier,
        cost_magnitude=spell_cost_from_potence(
            potence_successes=potence_successes,
            parameter_surcharge=parameter_surcharge),
        talent=talent,school_id=school_id,will_tiers=will_tiers,
        school_skill_tiers=school_skill_tiers,talent_tiers=talent_tiers,
        specialty_tiers=spell_specialty_tiers,specialty_declared=True,
        robe_dice=robe_dice,external_bonuses=external_bonuses,
        existing_mana=existing_mana,existing_spirit=existing_spirit,
        spirit_effective_threshold=spirit_effective_threshold)



def validate_spell_design(*, effect_count:int, has_multi_effect_design_perk:bool)->None:
    """The perk gates DESIGN of compound formulae, not casting a known one."""
    if type(effect_count) is not int or effect_count < 1:
        raise ValueError("spell formula must contain at least one effect")
    if type(has_multi_effect_design_perk) is not bool:
        raise ValueError("design perk possession must be boolean")
    if effect_count > 1 and not has_multi_effect_design_perk:
        raise ValueError("multi-effect spell design requires the compound-spell perk")


def resolve_compound_spell_costs(
        *, components:Sequence[tuple[int,int]],
        spell_specialty_tiers:Mapping[int,int],
        tier:int, talent:Talent, school_id:str,
        will_tiers:Mapping[int,int],
        school_skill_tiers:Mapping[int,int],
        talent_tiers:Mapping[int,int]|None=None,
        robe_dice:int=0,
        external_bonuses:Mapping[str,int]|None=None,
        existing_mana:Track|None=None,
        existing_spirit:Track|None=None,
        spirit_effective_threshold:int|None=None)->tuple[ManaCostResolution,...]:
    """Each component has independent Potence, Cost, resistance and overflow.

    components contains (ALREADY ROLLED potence successes, FIXED surcharge)
    pairs in resolution order. Surcharges must already include the design's
    +1 for any additional component, as well as that component's parameters.
    This helper handles one-school formulas. Cross-school competence mapping
    and application/resistance against targets await their own adapter.
    A person may cast a genuinely LEARNED compound formula even without
    possessing the perk needed to invent one.
    """
    if not components:
        raise ValueError("a compound spell must have at least one component")
    if (existing_mana is None) != (existing_spirit is None):
        raise ValueError("pass both saved Mana and Spirit tracks together")
    current_mana=existing_mana
    current_spirit=existing_spirit
    results=[]
    for component in components:
        if len(component)!=2:
            raise ValueError("each component needs Potence successes and surcharge")
        potence, surcharge = component
        result=resolve_spell_cast_cost(
            potence_successes=potence,parameter_surcharge=surcharge,
            spell_specialty_tiers=spell_specialty_tiers,
            tier=tier,talent=talent,school_id=school_id,
            will_tiers=will_tiers,school_skill_tiers=school_skill_tiers,
            talent_tiers=talent_tiers,robe_dice=robe_dice,
            external_bonuses=external_bonuses,
            existing_mana=current_mana,existing_spirit=current_spirit,
            spirit_effective_threshold=spirit_effective_threshold)
        results.append(result)
        current_mana=result.new_mana
        current_spirit=result.new_spirit
    return tuple(results)



@dataclass(frozen=True)
class CurseTick:
    damage_magnitude: int
    curse_active: bool
    broken_by_resistance: bool


def resolve_curse_tick(*, stored_potence:int, resistance_successes:int,
                       curse_active:bool=True)->CurseTick:
    """First successful active resistance PERMANENTLY ends this curse.

    This is a post-roll adapter: an actual method-appropriate active defense
    must already have been rolled. A failure takes the stored Potence as
    damage and remains active. A success meets or beats stored Potence,
    prevents current damage and ends the curse forever. Subsequent ticks
    cannot restart it. Duration expiry, dispels and subject death are
    handled by the surrounding effect ledger, not by this helper.
    No caster Potence or Mana reroll is made per tick.
    """
    if type(stored_potence) is not int or stored_potence < 0:
        raise ValueError("stored Potence must be nonnegative integer")
    if type(resistance_successes) is not int or resistance_successes < 0:
        raise ValueError("resistance successes must be nonnegative integer")
    if type(curse_active) is not bool:
        raise ValueError("curse active flag must be boolean")
    if not curse_active:
        return CurseTick(0,False,False)
    if resistance_successes >= stored_potence:
        return CurseTick(0,False,True)
    return CurseTick(stored_potence,True,False)



@dataclass(frozen=True)
class HealingEffectGrade:
    """Grade of healing work applied through normal recovery steps."""
    applied: bool
    grade: int
    mark_equivalents: int


def grade_healing_potence(
        *, patient_health_resilience:int, potence_successes:int,
        willing_and_accessible:bool,
        accuracy_successes:int|None=None,
        application_opposition:int|None=None)->HealingEffectGrade:
    """Classify inverse-Injury healing against the PATIENT'S base Health.

    Willing/accessible patients need no Application roll. Otherwise an
    actual legal defense/Avoidance threshold must be supplied for the
    Malediction-like Application roll. Unlike ordinary non-spell Projects,
    the spell's Potence must already have been rolled even if Application
    misses, because its Mana Cost uses that same result. Applying the
    graded outcome reuses Track.recover_step(), without new wound rules.
    """
    from geard_core import severity_marks
    if type(willing_and_accessible) is not bool:
        raise ValueError("willing_and_accessible must be boolean")
    if type(patient_health_resilience) is not int or patient_health_resilience<1:
        raise ValueError("patient Health resilience must be positive integer")
    if type(potence_successes) is not int or potence_successes<0:
        raise ValueError("healing Potence must be nonnegative integer")
    if willing_and_accessible:
        if accuracy_successes is not None or application_opposition is not None:
            raise ValueError("automatic healing Application must omit to-hit inputs")
        applied=True
    else:
        if (type(accuracy_successes) is not int or accuracy_successes<0
                or type(application_opposition) is not int or application_opposition<0):
            raise ValueError("opposed healing requires real Application and legal opposition")
        applied=accuracy_successes>=application_opposition
    if not applied:
        return HealingEffectGrade(False,-1,0)
    grade,count=severity_marks(potence_successes,patient_health_resilience)
    return HealingEffectGrade(True,grade,count)



def healing_steps_for_grade(*, health_resilience:int,
                            healing_grade:int, grade_mark_count:int)->int:
    """Convert healing marks to the equivalent number of natural recovery steps.

    An isolated grade-g wound in an R-slot track takes 1 + R + ... + R**g
    normal recovery steps to clear, because each demotion fills every slot
    at the next lower grade. No new wound-removal mechanism is introduced.
    """
    if type(health_resilience) is not int or health_resilience<1:
        raise ValueError("Health resilience must be a positive integer")
    if type(healing_grade) is not int or healing_grade not in (-1,0,1,2,3):
        raise ValueError("healing grade must be -1 or 0..3")
    if type(grade_mark_count) is not int or grade_mark_count<0:
        raise ValueError("healing mark count must be nonnegative")
    if healing_grade == -1:
        if grade_mark_count:
            raise ValueError("no-effect healing cannot contain marks")
        return 0
    if grade_mark_count == 0:
        return 0
    if healing_grade != 3 and grade_mark_count != 1:
        raise ValueError("non-Final healing gives one mark equivalent")
    return grade_mark_count * sum(health_resilience**g for g in range(healing_grade+1))


def apply_healing_recovery(*, injury:Track, healing:HealingEffectGrade)->Track:
    """Player shortcut: remove a matching-grade wound mark directly.

    If there is no mark of that grade, convert that healing mark into the
    equivalent number of ordinary Track.recover_step() calls. Resolve each
    Final healing mark separately. A direct high-grade removal can differ
    in mixed-wound states from only using natural recovery; this is an
    intentional at-table simplification, not a mathematically identical
    state transition in all cases.
    """
    if not isinstance(injury,Track):
        raise ValueError("injury must be a Track")
    if not isinstance(healing,HealingEffectGrade):
        raise ValueError("healing must be a HealingEffectGrade")
    if injury.exhausted:
        raise ValueError("exhausted Injury is death; ordinary healing cannot resurrect")
    if not healing.applied:
        return injury
    # Validate grade/count consistently even if an exact-grade wound exists.
    healing_steps_for_grade(
        health_resilience=injury.resilience,healing_grade=healing.grade,
        grade_mark_count=healing.mark_equivalents)
    if healing.grade == -1 or healing.mark_equivalents == 0:
        return injury
    result=injury
    for _ in range(healing.mark_equivalents):
        if not any(result.marks):
            break
        if result.marks[healing.grade]:
            marks=list(result.marks)
            marks[healing.grade]-=1
            result=Track(result.resilience,tuple(marks))
        else:
            steps=healing_steps_for_grade(
                health_resilience=result.resilience,healing_grade=healing.grade,
                grade_mark_count=1)
            for _ in range(steps):
                next_step=result.recover_step()
                if next_step==result:
                    break
                result=next_step
    return result


def oakflesh_effective_injury_threshold(
        *, base_health_resilience:int,
        protection_potence_successes:int)->int:
    """Flat protection added to the target's Injury severity threshold.

    This DOES NOT increase Health, the Injury track's slots, or Avoidance,
    and does not settle stacking with armor/other flesh spells. Potence
    must be the actual successful spell effect at the relevant Tier.
    """
    if type(base_health_resilience) is not int or base_health_resilience<1:
        raise ValueError("base Health resilience must be positive integer")
    if type(protection_potence_successes) is not int or protection_potence_successes<0:
        raise ValueError("protection Potence must be nonnegative integer")
    return base_health_resilience+protection_potence_successes


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
