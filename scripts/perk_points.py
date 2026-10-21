"""Perk-point acquisition/spending reference model for Elf-Books.

Supports accepted mechanics: one untyped bankable point for meaningful natural
20 critical successes, or credible opponent natural 1 attacks. Trainers never
grant points. Extraordinary artifact point or direct-perk rewards are explicit.
Game-state integration and perk catalog are still pending.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from typing import Literal

EventKind = Literal["own_skill_check", "own_attack", "incoming_attack"]

@dataclass(frozen=True)
class PerkBank:
    points: int = 0
    earned_total: int = 0
    owned_perks: frozenset[str] = frozenset()
    resolved_events: frozenset[str] = frozenset()

def _event_id(event_id: str) -> None:
    if not isinstance(event_id, str) or not event_id.strip():
        raise ValueError("event_id must be a nonempty stable string")

def _rank(rank: int) -> None:
    if type(rank) is not int or not 0 <= rank <= 100:
        raise ValueError("skill rank must be an integer 0..100")

def natural_critical_event(bank: PerkBank, *, event_id: str, kind: EventKind,
                           natural_roll: int, meaningful: bool,
                           succeeded: bool=False) -> PerkBank:
    """One event -> at most one point, even if many protective methods apply.

    No awarded defensive XP from an attacking natural 1 is implied here.
    Own non-attack checks require a real successful result on natural 20.
    The automatic nat20 attack hit is represented by succeeded=True.
    """
    _event_id(event_id)
    if kind not in ("own_skill_check", "own_attack", "incoming_attack"):
        raise ValueError("unknown critical kind")
    if type(natural_roll) is not int or not 1 <= natural_roll <= 20:
        raise ValueError("natural_roll must be 1..20")
    if type(meaningful) is not bool or type(succeeded) is not bool:
        raise ValueError("meaningful and succeeded must be booleans")
    if event_id in bank.resolved_events:
        return bank
    gain=bool(meaningful and (
        (kind in ("own_skill_check", "own_attack") and natural_roll==20 and succeeded) or
        (kind=="incoming_attack" and natural_roll==1)
    ))
    return replace(bank, points=bank.points+int(gain),earned_total=bank.earned_total+int(gain),
                   resolved_events=bank.resolved_events|{event_id})

def artifact_point(bank: PerkBank, *, event_id: str) -> PerkBank:
    """Explicit artifact/unique-story reward; ordinary trainers must not call this."""
    _event_id(event_id)
    if event_id in bank.resolved_events:
        return bank
    return replace(bank,points=bank.points+1,earned_total=bank.earned_total+1,
                   resolved_events=bank.resolved_events|{event_id})

def spend_perk_point(bank: PerkBank, *, perk_id: str, required_rank: int,
                     current_rank: int, other_reqs_met: bool=True) -> PerkBank:
    if not isinstance(perk_id,str) or not perk_id.strip():
        raise ValueError("perk_id must be a nonempty string")
    _rank(required_rank)
    _rank(current_rank)
    if type(other_reqs_met) is not bool:
        raise ValueError("other_reqs_met must be boolean")
    if perk_id in bank.owned_perks:
        raise ValueError("perk already owned")
    if bank.points<1:
        raise ValueError("no unspent perk points")
    if current_rank<required_rank or not other_reqs_met:
        raise ValueError("perk requirements not yet met")
    return replace(bank,points=bank.points-1,owned_perks=bank.owned_perks|{perk_id})

def exceptional_direct_perk(bank: PerkBank, *, event_id: str, perk_id: str,
                            requirements_met: bool, explicitly_waives_requirements: bool=False) -> PerkBank:
    """For bespoke artifact/quest rewards; not available to trainers by default."""
    _event_id(event_id)
    if not isinstance(perk_id,str) or not perk_id.strip():
        raise ValueError("perk_id must be a nonempty string")
    if type(requirements_met) is not bool or type(explicitly_waives_requirements) is not bool:
        raise ValueError("requirement flags must be booleans")
    if event_id in bank.resolved_events:
        return bank
    if perk_id in bank.owned_perks:
        raise ValueError("perk already owned")
    if not requirements_met and not explicitly_waives_requirements:
        raise ValueError("prerequisite waiver must be explicit")
    return replace(bank,owned_perks=bank.owned_perks|{perk_id},
                   resolved_events=bank.resolved_events|{event_id})
