"""Generalized Elf-Books extended progress / skill XP model.

XP is denominated in integer TENTHS throughout; normal XP displays /10.
Active weapon combat XP and rank thresholds here only bridge existing agreed math.
The 2x DC quick award, half-DC failed award, and progress/10 extended
award remain proposed values until approved in rules/RULES_INDEX.md.
"""
from __future__ import annotations
from dataclasses import dataclass

XP_SCALE = 10

def threshold_tenths(current_rank: int) -> int:
    if type(current_rank) is not int or not 0 <= current_rank < 100:
        raise ValueError("skill rank must be integer 0..99")
    return 50 * max(1, current_rank)

def offensive_damage_xp_tenths(applied_hp_loss: int) -> int:
    if type(applied_hp_loss) is not int or applied_hp_loss < 0:
        raise ValueError("applied HP loss must be a nonnegative integer")
    return 20 * applied_hp_loss

def quick_xp_tenths(effective_dc: int, success: bool, meaningful: bool = True) -> int:
    if type(effective_dc) is not int or effective_dc < 0:
        raise ValueError("effective DC must be a nonnegative integer")
    if type(success) is not bool or type(meaningful) is not bool:
        raise ValueError("success/meaningful must be booleans")
    if not meaningful:
        return 0
    return effective_dc * (20 if success else 5)


@dataclass(frozen=True)
class OpposedResolution:
    success: bool | None
    effective_dc: int
    actor_xp_tenths: int
    must_reroll_tie: bool


def opposed_quick_result(*, actor_total: int, defender_total: int,
                         actor_modifier: int, defender_modifier: int,
                         meaningful: bool = True) -> OpposedResolution:
    """3.5 opposed totals: higher total wins, then higher bonus, then reroll.

    This returns zero XP for an unresolved tie pending actual fresh rolls.
    The caller must not award XP more than once for the eventual contest.
    """
    for v in (actor_total, defender_total, actor_modifier, defender_modifier):
        if type(v) is not int:
            raise ValueError("check results/modifiers must be integers")
    if type(meaningful) is not bool:
        raise ValueError("meaningful must be boolean")
    if actor_total > defender_total:
        success = True
    elif actor_total < defender_total:
        success = False
    elif actor_modifier > defender_modifier:
        success = True
    elif actor_modifier < defender_modifier:
        success = False
    else:
        return OpposedResolution(None, max(0, defender_total), 0, True)
    dc = max(0, defender_total)
    return OpposedResolution(success, dc, quick_xp_tenths(dc, success, meaningful), False)


@dataclass(frozen=True)
class ExtendedResult:
    dc: int
    interval: str
    check_total: int
    success: bool
    produced_progress: int
    credited_progress: int
    total_progress: int
    required_progress: int
    xp_tenths: int
    completed: bool
    failure_by_five_or_more: bool


def extended_interval(*, dc: int, interval: str, progress_goal: int,
                      progress_before: int, check_total: int) -> ExtendedResult:
    """One real project interval. Credits no more than remaining progress."""
    for v in (dc, progress_goal, progress_before, check_total):
        if type(v) is not int:
            raise ValueError("numeric work inputs must be integers")
    if dc <= 0 or progress_goal <= 0 or not 0 <= progress_before <= progress_goal:
        raise ValueError("positive DC/goal and valid progress required")
    if not isinstance(interval, str) or not interval.strip():
        raise ValueError("nonempty work interval required")
    success = check_total >= dc
    produced = max(0, check_total * dc) if success else 0
    credited = min(produced, progress_goal - progress_before)
    total = progress_before + credited
    return ExtendedResult(
        dc=dc, interval=interval, check_total=check_total, success=success,
        produced_progress=produced, credited_progress=credited,
        total_progress=total, required_progress=progress_goal,
        xp_tenths=credited, completed=total==progress_goal,
        failure_by_five_or_more=(not success and check_total <= dc-5)
    )


def format_xp_tenths(value: int) -> str:
    if type(value) is not int or value < 0:
        raise ValueError("nonnegative integer tenths required")
    return f"{value // 10}.{value % 10}"
