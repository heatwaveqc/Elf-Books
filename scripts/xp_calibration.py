"""Candidate Elf-Books skill XP calibration (NOT adopted live mechanics).

Pure, deterministic arithmetic. Uses Fraction where expected values are non-integral.
Does not roll dice, assign character XP, or write any campaign data.
"""
from __future__ import annotations
from fractions import Fraction
from math import ceil


def next_rank_xp(current: int, k: int = 1) -> int:
    if type(current) is not int or not 0 <= current < 100:
        raise ValueError("current rank must be integer 0..99")
    if type(k) is not int or k <= 0:
        raise ValueError("K must be a positive integer")
    return max(1, current) * k


def total_xp(start: int, end: int, k: int = 1) -> int:
    if type(start) is not int or type(end) is not int or not 0 <= start <= end <= 100:
        raise ValueError("invalid skill rank range")
    if type(k) is not int or k <= 0:
        raise ValueError("K must be a positive integer")
    return sum(next_rank_xp(s,k) for s in range(start,end))


def average_die_damage(faces: int, dice: int = 1) -> Fraction:
    if type(faces) is not int or faces < 2 or type(dice) is not int or dice < 1:
        raise ValueError("invalid weapon die")
    return Fraction(dice * (faces + 1), 2)


def expected_successes(xp_needed: int, xp_per_success: Fraction) -> Fraction:
    if type(xp_needed) is not int or xp_needed < 0 or xp_per_success <= 0:
        raise ValueError("invalid XP / XP-rate")
    return Fraction(xp_needed,1) / xp_per_success


def enemy_estimate(successes: Fraction, hits_min: int=3, hits_max: int=5) -> tuple[int,int]:
    if successes < 0 or not (0 < hits_min <= hits_max):
        raise ValueError("invalid encounter assumptions")
    return ceil(successes / hits_max), ceil(successes / hits_min)


def sample_rows() -> list[dict]:
    rate=average_die_damage(8)
    rows=[]
    for a,b in ((20,25),(50,55),(95,100),(20,100)):
        xp=total_xp(a,b)
        uses=expected_successes(xp,rate)
        low,high=enemy_estimate(uses)
        rows.append({"start":a,"end":b,"xp":xp,"expected_d8_hits":float(uses),
                     "foes_min":low,"foes_max":high})
    return rows


if __name__ == "__main__":
    for row in sample_rows():
        print(row)
