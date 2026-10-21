"""Local Geard Lif arithmetic primitives for Elf-Books.

Uses the player-facing rules snapshot at engine/geard-lif/source/.
Resolution and Tier are PROVISIONAL upstream. These helpers deliberately do
NOT guess the not-yet-defined project success/tie, Effect-vs-Recalcitrance,
character-creation, XP, or critical-event rules.
"""
from __future__ import annotations
from dataclasses import dataclass, replace

PENALTY=(0,-1,-2,-4)
GRADES=("minor","middling","major","final")

def d10_successes(faces: list[int] | tuple[int,...]) -> int:
    """Under the upstream *tentative* convention, 7-9 =1; 10 =2."""
    if not isinstance(faces,(list,tuple)) or any(type(x)!=int or not 1<=x<=10 for x in faces):
        raise ValueError("faces must be a list/tuple of natural d10 values 1..10")
    return sum(2 if v==10 else 1 if v>=7 else 0 for v in faces)

def convert_tier(magnitude:int,source:int,target:int)->int:
    """Express rolled nonnegative result at target Tier, floor when scaling up."""
    if type(magnitude)!=int or magnitude<0 or any(type(t)!=int for t in (source,target)):
        raise ValueError("invalid magnitude or Tier")
    if source>=target:
        return magnitude * (10**(source-target))
    return magnitude // (10**(target-source))

def severity_marks(magnitude:int,resilience:int)->tuple[int,int]:
    """Return (grade index 0..3, count) for a single effect or zero (-1,0).

    Magnitude R->middling, 2R->major, 3R->final; every further full R adds
    one additional final mark, per the locked graded resource model.
    """
    if type(magnitude)!=int or magnitude<0 or type(resilience)!=int or resilience<=0:
        raise ValueError("nonnegative integer magnitude and positive resilience required")
    if magnitude==0: return -1,0
    whole=magnitude//resilience
    if whole==0: return 0,1
    if whole==1: return 1,1
    if whole==2: return 2,1
    return 3,whole-2

@dataclass(frozen=True)
class Track:
    """One resource track. Counts of occupied slots at four grades."""
    resilience:int
    marks:tuple[int,int,int,int]=(0,0,0,0)

    def __post_init__(self):
        if type(self.resilience)!=int or self.resilience<1:
            raise ValueError("positive integer resilience required")
        if not isinstance(self.marks,tuple) or len(self.marks)!=4 or any(
             type(n)!=int or n<0 or n>self.resilience for n in self.marks):
            raise ValueError("four grade counts in 0..resilience required")

    @property
    def exhausted(self)->bool:
        return self.marks[3]==self.resilience

    @property
    def penalty(self)->int:
        return next((PENALTY[i] for i in (3,2,1,0) if self.marks[i]),0)

    def _add_one(self,index:int,marks:list[int])->None:
        if marks[3]>=self.resilience:
            return
        if index==3:
            marks[index]=min(self.resilience,marks[index]+1)
            return
        if marks[index]<self.resilience:
            marks[index]+=1
            return
        marks[index]=0
        self._add_one(index+1,marks)

    def apply_effect(self,magnitude:int)->"Track":
        grade,count=severity_marks(magnitude,self.resilience)
        marks=list(self.marks)
        if grade>=0:
            for _ in range(min(count, self.resilience*4+1)):
                self._add_one(grade,marks)
        return replace(self,marks=tuple(marks))

    def recover_step(self)->"Track":
        """Take one recovery step; caller enforces action/day cadence."""
        marks=list(self.marks)
        for grade in range(4):
            if marks[grade]:
                marks[grade]-=1
                if grade>0:
                    marks[grade-1]=self.resilience
                return replace(self,marks=tuple(marks))
        return self

@dataclass(frozen=True)
class Project:
    """Locked Project dimensions, without inventing resolution mechanics."""
    complexity:int
    recalcitrance:int
    scope:int
    time_per_attempt:str
    progress:int=0

    def __post_init__(self):
        if any(type(v)!=int for v in
               (self.complexity,self.recalcitrance,self.scope,self.progress)):
            raise ValueError("integer project statistics required")
        if min(self.complexity,self.recalcitrance)<0 or self.scope<1 or not 0<=self.progress<=self.scope:
            raise ValueError("invalid project difficulty/scope/progress")
        if not isinstance(self.time_per_attempt,str) or not self.time_per_attempt.strip():
            raise ValueError("project time interval is required")

    @property
    def complete(self)->bool: return self.progress>=self.scope

    def credit(self,points:int)->"Project":
        """Credit *externally adjudicated* progress, never past scope."""
        if type(points)!=int or points<0: raise ValueError("nonnegative progress required")
        return replace(self,progress=min(self.scope,self.progress+points))
