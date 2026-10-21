"""Crafting DC XP candidate, with agreed five-times-skill rank costs.

This is a deterministic calibration tool, not a live skill progression service.
"""
from __future__ import annotations
from fractions import Fraction

def next_rank_xp(rank: int) -> int:
    if type(rank) is not int or not 0 <= rank < 100:
        raise ValueError("rank must be integer 0..99")
    return 5*max(1,rank)

def xp_required(start: int, end: int) -> int:
    if type(start) is not int or type(end) is not int or not 0 <= start <= end <= 100:
        raise ValueError("invalid rank interval")
    return sum(next_rank_xp(rank) for rank in range(start,end))

def craft_xp(dc: int, completed_units: int = 1, multiplier: int = 2) -> int:
    """XP for real deliverables, NOT per dice roll.

    A batch of five qualifying objects returns five awards; an item
    assembled using five needless rolls earns only one item award.
    """
    if type(dc) is not int or not 1 <= dc <= 100:
        raise ValueError("DC must be integer 1..100")
    if type(completed_units) is not int or completed_units < 0:
        raise ValueError("completed_units must be nonnegative integer")
    if type(multiplier) is not int or multiplier <= 0:
        raise ValueError("multiplier must be positive integer")
    return dc * completed_units * multiplier

def d20_check_success_probability(dc: int, attribute_mod: int, rank: int) -> Fraction:
    """Normal 5e-style ability check: natural 1 isn't automatic failure."""
    if type(dc) is not int or not 1 <= dc <= 100:
        raise ValueError("invalid DC")
    if type(attribute_mod) is not int:
        raise ValueError("attribute modifier must be integer")
    if type(rank) is not int or not 0 <= rank <= 100:
        raise ValueError("invalid skill")
    successes=sum((roll+attribute_mod+rank//5)>=dc for roll in range(1,21))
    return Fraction(successes,20)

def expected_completed_units(start: int, end: int, dc: int, multiplier: int = 2) -> Fraction:
    return Fraction(xp_required(start,end),craft_xp(dc,1,multiplier))

def expected_attempts(start: int, end: int, dc: int, attribute_mod: int,
                      multiplier: int = 2) -> Fraction:
    if start % 5 or end != start+5:
        raise ValueError("expected-attempt approximation is for 5-rank blocks")
    p=d20_check_success_probability(dc,attribute_mod,start)
    if p == 0:
        raise ValueError("attempt impossible under ordinary 1d20 check")
    return expected_completed_units(start,end,dc,multiplier)/p
