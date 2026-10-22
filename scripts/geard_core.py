"""Local Geard Lif math: two-stage application and unified graded marks.

Player-facing Geard rules pinned under engine/geard-lif/source/.
The d10 randomizer and cross-scale Tier conversion are provisional upstream.
Armor/effect modifiers, advancement and GM state integration remain separate.
"""
from __future__ import annotations
from dataclasses import dataclass, replace

RESOURCE_TRACKS = {
    "mind": {"resilience": "will", "slow": "spirit", "fast": "mana"},
    "body": {"resilience": "health", "slow": "injury", "fast": "fatigue"},
    "soul": {"resilience": "conviction", "slow": "plasticity", "fast": "attention"},
}

PENALTY=(0,-1,-2,-4)
GRADES=("minor","middling","major","final")

def d10_successes(faces:list[int] | tuple[int,...])->int:
    """Tentative d10: 7-9 -> one success; 10 -> two."""
    if not isinstance(faces,(list,tuple)) or any(type(x)!=int or not 1<=x<=10 for x in faces):
        raise ValueError("faces must be natural d10 rolls 1..10")
    return sum(2 if x==10 else 1 if x>=7 else 0 for x in faces)

def convert_tier(magnitude:int,source:int,target:int)->int:
    """Provisional scale conversion; rolled value changes, target stays static."""
    if type(magnitude)!=int or magnitude<0 or type(source)!=int or type(target)!=int:
        raise ValueError("integer magnitude/tier required")
    if source>=target:
        return magnitude*5**(source-target)
    return magnitude//5**(target-source)

def severity_marks(magnitude:int,threshold:int)->tuple[int,int]:
    """Return (grade 0..3, count). Any positive effect gets at least Minor.

    Grade 0 Minor if 0 < P < R; 1 Middling at R; 2 Major at 2R;
    3 Final at 3R; floor(P/R)-2 Final marks when P >= 3R.
    A protection-adjusted threshold affects grade, never mark capacity.
    """
    if type(magnitude)!=int or magnitude<0 or type(threshold)!=int or threshold<=0:
        raise ValueError("nonnegative magnitude and positive threshold required")
    if magnitude==0:
        return (-1,0)
    multiples=magnitude//threshold
    if multiples==0: return (0,1)
    if multiples==1: return (1,1)
    if multiples==2: return (2,1)
    return (3,multiples-2)

def _add_one(marks:list[int],capacity:int,grade:int)->None:
    """Grade-capacity promotion; stop when Final is exhausted."""
    if marks[3]>=capacity: return
    if grade==3:
        marks[3]=min(capacity,marks[3]+1)
    elif marks[grade]<capacity:
        marks[grade]+=1
    else:
        marks[grade]=0
        _add_one(marks,capacity,grade+1)

def _apply_marks(marks:tuple[int,int,int,int],capacity:int,
                 grade:int,count:int)->tuple[int,int,int,int]:
    result=list(marks)
    if grade>=0:
        for _ in range(min(count,4*capacity+1)):
            _add_one(result,capacity,grade)
    return tuple(result)

def _valid_marks(marks:object,capacity:int)->bool:
    return (isinstance(marks,tuple) and len(marks)==4 and
            all(type(x)==int and 0<=x<=capacity for x in marks))

@dataclass(frozen=True)
class Track:
    """Personal track: slots per grade = Resilience.

    Effective severity threshold is normally Resilience too, but armor/wards
    may change that threshold *without* changing track capacity.
    """
    resilience:int
    marks:tuple[int,int,int,int]=(0,0,0,0)

    def __post_init__(self):
        if type(self.resilience)!=int or self.resilience<1:
            raise ValueError("positive integer resilience required")
        if not _valid_marks(self.marks,self.resilience):
            raise ValueError("four grade counts must be between zero and resilience")

    @property
    def exhausted(self)->bool: return self.marks[3]==self.resilience

    @property
    def penalty(self)->int:
        return next((PENALTY[i] for i in (3,2,1,0) if self.marks[i]),0)

    def apply_effect(self,magnitude:int,*,effective_threshold:int|None=None)->"Track":
        threshold=self.resilience if effective_threshold is None else effective_threshold
        grade,count=severity_marks(magnitude,threshold)
        return replace(self,marks=_apply_marks(self.marks,self.resilience,grade,count))

    def infliction_value(self)->int:
        """Count resource marks in Minor equivalents, using promotion base R+1."""
        base=self.resilience+1
        return sum(mark*base**grade for grade,mark in enumerate(self.marks))

    def restore_marks(self,grade:int,count:int=1)->"Track":
        """Universally restore supernatural mark-equivalents, not recovery steps.

        Graded restoration undoes the value of mark infliction/promotion.
        A grade-g restorative mark is (R+1)**g Minor equivalents, where R is
        resource Resilience and mark capacity. Subtract the total, clamping
        to zero, then rebuild the canonical four-grade mark distribution.
        A caller controls Application, potency grade, target legality and
        exceptional dead-resource restrictions (e.g. Injury resurrection).
        """
        if type(grade) is not int or grade not in (-1,0,1,2,3):
            raise ValueError("restoration grade must be -1 or 0..3")
        if type(count) is not int or count<0:
            raise ValueError("restoration count must be a nonnegative integer")
        if grade == -1:
            if count != 0:
                raise ValueError("zero-effect restoration cannot contain marks")
            return self
        if count == 0:
            return self
        base=self.resilience+1
        remaining=max(0,self.infliction_value()-count*base**grade)
        marks=[]
        for _ in range(4):
            marks.append(remaining%base)
            remaining//=base
        if remaining:
            raise ValueError("restoration remainder exceeded four-grade track")
        return replace(self,marks=tuple(marks))

    def restore_effect(self,magnitude:int)->"Track":
        """Resolve supernatural restorative Potence versus base Resilience.

        Potence must have passed its applicable Application and Tier
        conversion before calling this; no armor/ward effective threshold
        raises a patient's restoration Recalcitrance. Ordinary timed
        recovery remains separately defined in recover_step().
        """
        grade,count=severity_marks(magnitude,self.resilience)
        return self.restore_marks(grade,count)

    def recover_step(self)->"Track":
        """One recovery step; the caller enforces per-action or per-day timing."""
        marks=list(self.marks)
        for grade in range(4):
            if marks[grade]:
                marks[grade]-=1
                if grade>0: marks[grade-1]=self.resilience
                return replace(self,marks=tuple(marks))
        return self

@dataclass(frozen=True)
class ResourceEffectOutcome:
    """Result of one incident; targets remain tracked by their aspect's names."""
    aspect: str
    requested_resource: str
    applied_resource: str
    fast: Track
    slow: Track

    @property
    def redirected(self) -> bool:
        return self.requested_resource != self.applied_resource


def apply_resource_effect(*, aspect: str, requested_resource: str,
                          magnitude: int, fast: Track, slow: Track,
                          fast_effective_threshold: int | None = None,
                          slow_effective_threshold: int | None = None
                          ) -> ResourceEffectOutcome:
    """Apply one personal resource effect; route already-exhausted fast to slow.

    Check exhaustion at the START of this incident. It is not a splitting
    mechanism: the hit that finishes fast stays fast, and only a later hit
    can mark slow. Regrade the unchanged magnitude with the DESTINATION
    track's appropriate effective threshold. Explicit slow targeting is
    unchanged. The same routing applies to rolled self-Cost magnitudes.
    """
    if aspect not in RESOURCE_TRACKS:
        raise ValueError("unknown resource aspect")
    info = RESOURCE_TRACKS[aspect]
    if requested_resource not in (info["fast"], info["slow"]):
        raise ValueError("resource target must belong to selected aspect")
    if not isinstance(fast, Track) or not isinstance(slow, Track):
        raise ValueError("both aspect resource tracks must be Track objects")
    if fast.resilience != slow.resilience:
        raise ValueError("paired tracks must share their aspect Resilience")
    if type(magnitude) is not int or magnitude < 0:
        raise ValueError("effect magnitude must be a nonnegative integer")
    redirect = requested_resource == info["fast"] and fast.exhausted
    actual = info["slow"] if redirect else requested_resource
    if actual == info["fast"]:
        fast = fast.apply_effect(magnitude, effective_threshold=fast_effective_threshold)
    else:
        slow = slow.apply_effect(magnitude, effective_threshold=slow_effective_threshold)
    return ResourceEffectOutcome(aspect,requested_resource,actual,fast,slow)


@dataclass(frozen=True)
class ProjectRollOutcome:
    """A complete Project attempt; grade is -1 for zero/no Effect."""
    applied:bool
    potence_rolled:bool
    mark_grade:int
    mark_count:int

    @property
    def progressed(self)->bool: return self.mark_count>0

def resolve_project_roll(accuracy_successes:int,application_opposition:int,
                         potence_successes:int|None,effect_opposition:int)->ProjectRollOutcome:
    """Meet it to beat it: Accuracy >= opposition permits Potence.

    Any positive Potence produces a mark. A threshold exactly matched gives
    Middling. Effect opposition zero still awaits an upstream special case.
    """
    if any(type(x)!=int or x<0 for x in
           (accuracy_successes,application_opposition,effect_opposition)):
        raise ValueError("roll successes/opposition must be nonnegative integers")
    if effect_opposition==0:
        raise ValueError("zero Effect threshold has no settled grade rule")
    if accuracy_successes<application_opposition:
        if potence_successes is not None:
            raise ValueError("failed Application must not roll Potence")
        return ProjectRollOutcome(False,False,-1,0)
    if type(potence_successes)!=int or potence_successes<0:
        raise ValueError("successful Application requires Potence successes")
    grade,count=severity_marks(potence_successes,effect_opposition)
    return ProjectRollOutcome(True,True,grade,count)

@dataclass(frozen=True)
class Project:
    """Non-character Project: Recalcitrance controls grade; Scope = slots/grade."""
    complexity:int
    recalcitrance:int
    scope:int
    time_per_attempt:str
    marks:tuple[int,int,int,int]=(0,0,0,0)

    def __post_init__(self):
        if any(type(x)!=int for x in (self.complexity,self.recalcitrance,self.scope)):
            raise ValueError("integer project dimensions required")
        if min(self.complexity,self.recalcitrance)<0 or self.scope<1:
            raise ValueError("nonnegative opposition and positive Scope required")
        if not isinstance(self.time_per_attempt,str) or not self.time_per_attempt.strip():
            raise ValueError("project interval required")
        if not _valid_marks(self.marks,self.scope):
            raise ValueError("mark slots must be in 0..Scope at each grade")

    @property
    def complete(self)->bool: return self.marks[3]==self.scope

    def apply_effect(self,magnitude:int)->"Project":
        """Apply an already-successful Potence result; no implicit Accuracy."""
        grade,count=severity_marks(magnitude,self.recalcitrance)
        return replace(self,marks=_apply_marks(self.marks,self.scope,grade,count))

    def attempt(self,accuracy_successes:int,potence_successes:int|None
                )->tuple["Project",ProjectRollOutcome]:
        out=resolve_project_roll(accuracy_successes,self.complexity,
                                 potence_successes,self.recalcitrance)
        if not out.progressed:
            return self,out
        return replace(self,marks=_apply_marks(self.marks,self.scope,
                                              out.mark_grade,out.mark_count)),out
