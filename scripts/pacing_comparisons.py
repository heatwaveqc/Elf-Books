"""Reproducible research-only solo pacing experiment; NOT a GM dice roller."""
from dataclasses import dataclass
from random import Random
from statistics import mean

@dataclass(frozen=True)
class Case:
    skill: int
    attr: int
    enchant: int
    dc: int
    goal: int
    foe_hp: int

CASES=(Case(20,3,0,15,1000,35),
       Case(50,5,0,25,2500,60),
       Case(95,7,3,40,6000,110))

def goal_tenths(s: int) -> int:
    if type(s) is not int or s not in range(0,96,5):
        raise ValueError("expected a five-rank block starting at 0..95")
    return 50*sum(max(1,x) for x in range(s,s+5))

def combat(c: Case,rng: Random) -> tuple[int,int,int]:
    """Attacks, hits, distinct opponents; 60% hit, d8 crit, HP-capped XP."""
    target=goal_tenths(c.skill)
    xp=attempts=hits=enemies=0
    hp=0
    while xp<target:
        if hp==0:
            hp=c.foe_hp
            enemies+=1
        roll=rng.randint(1,20)
        attempts+=1
        if roll<9:
            continue
        hits+=1
        damage=rng.randint(1,8)+c.attr+c.skill//5+c.enchant
        if roll==20:
            damage+=rng.randint(1,8)
        actual=min(damage,hp)
        hp-=actual
        xp+=20*actual
    return attempts,hits,enemies

def quick(c: Case,rng: Random) -> int:
    """One meaningful quick skill check per exchange; XP in tenths."""
    xp=attempts=0
    while xp<goal_tenths(c.skill):
        result=rng.randint(1,20)+c.attr+c.skill//5
        xp+=c.dc*(20 if result>=c.dc else 5)
        attempts+=1
    return attempts

def project(c: Case,rng: Random,progress_goal: int|None=None) -> tuple[int,int]:
    """Underlying weekly work intervals, project-summary chat exchanges."""
    goal=c.goal if progress_goal is None else progress_goal
    if goal<=0:
        raise ValueError("project goal must be positive")
    target=goal_tenths(c.skill)
    xp=weeks=0
    projects=1
    progress=0
    while xp<target:
        check=rng.randint(1,20)+c.attr+c.skill//5
        weeks+=1
        if check>=c.dc:
            gain=min(goal-progress,check*c.dc)
            xp+=gain
            progress+=gain
        if progress==goal:
            progress=0
            if xp<target:
                projects+=1
    return weeks,projects

def compare(trials: int=25000,seed: int=20261020) -> list[dict]:
    if type(trials) is not int or trials<=0:
        raise ValueError("positive trial count required")
    rng=Random(seed)
    output=[]
    for c in CASES:
        battles=[combat(c,rng) for _ in range(trials)]
        checks=[quick(c,rng) for _ in range(trials)]
        projects=[project(c,rng) for _ in range(trials)]
        fixed=[project(c,rng,1000) for _ in range(trials)]
        output.append(dict(skill=c.skill,xp=goal_tenths(c.skill)//10,
            combat_rounds=round(mean(x[0] for x in battles),1),
            combat_hits=round(mean(x[1] for x in battles),1),
            opponents=round(mean(x[2] for x in battles),1),
            quick_checks=round(mean(checks),1),
            matched_project_summaries=round(mean(x[1] for x in projects),1),
            matched_project_weeks=round(mean(x[0] for x in projects),1),
            fixed_goal_summaries=round(mean(x[1] for x in fixed),1),
            fixed_goal_weeks=round(mean(x[0] for x in fixed),1)))
    return output

if __name__=="__main__":
    for result in compare():
        print(result)
