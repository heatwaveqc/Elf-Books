import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from geard_core import d10_successes,convert_tier,severity_marks,Track,Project,resolve_project_roll,apply_resource_effect,restore_resource_effect,RESOURCE_TRACKS

class LocalCoreTests(unittest.TestCase):
    def test_tentative_randomizer_and_tier(self):
        self.assertEqual(d10_successes([1,2,6]),0)
        self.assertEqual(d10_successes([7,8,9,10,10]),7)
        with self.assertRaises(ValueError):d10_successes([0])
        self.assertEqual(convert_tier(27,0,1),5)
        self.assertEqual(convert_tier(27,1,3),1)
        self.assertEqual(convert_tier(3,5,4),15)
        self.assertEqual(convert_tier(9,1,1),9)

    def test_meet_to_beat_and_effect_grade_exact_edges(self):
        failed=resolve_project_roll(2,3,None,4)
        self.assertFalse(failed.applied)
        with self.assertRaises(ValueError):
            resolve_project_roll(2,3,1,4)
        for potence,grade,count in [(0,-1,0),(1,0,1),(3,0,1),(4,1,1),
                                    (7,1,1),(8,2,1),(11,2,1),(12,3,1),
                                    (15,3,1),(16,3,2),(24,3,4)]:
            out=resolve_project_roll(3,3,potence,4)
            self.assertTrue(out.applied)
            self.assertTrue(out.potence_rolled)
            self.assertEqual((out.mark_grade,out.mark_count),(grade,count))
        with self.assertRaises(ValueError):
            resolve_project_roll(3,3,4,0)

    def test_effect_threshold_and_personal_capacity_separate(self):
        # Health 4: 4 slots per grade, even though protection raises threshold to 6.
        base=Track(4).apply_effect(5)
        armored=Track(4).apply_effect(5,effective_threshold=6)
        self.assertEqual(base.marks,(0,1,0,0))
        self.assertEqual(armored.marks,(1,0,0,0))
        self.assertEqual(armored.resilience,4)
        self.assertEqual(Track(4).apply_effect(6,effective_threshold=6).marks,(0,1,0,0))
        self.assertEqual(Track(4).apply_effect(12,effective_threshold=6).marks,(0,0,1,0))

    def test_project_scope_capacity_independent_of_difficulty(self):
        easy=Project(3,2,2,"one day")
        hard=Project(3,6,2,"one day")
        self.assertEqual(easy.apply_effect(4).marks,(0,0,1,0))
        self.assertEqual(hard.apply_effect(4).marks,(1,0,0,0))
        self.assertEqual(hard.scope,2)
        self.assertEqual(easy.scope,2)

    def test_project_does_not_proceed_when_accuracy_fails(self):
        p=Project(3,4,2,"one week")
        self.assertEqual(p.attempt(2,None)[0],p)
        new,out=p.attempt(3,1)
        self.assertTrue(out.progressed)
        self.assertEqual(new.marks,(1,0,0,0))
        same,zero=p.attempt(3,0)
        self.assertFalse(zero.progressed)
        self.assertEqual(same,p)

    def test_project_final_exhaustion_completion(self):
        p=Project(3,4,2,"one week")
        self.assertEqual(p.attempt(3,16)[0].marks,(0,0,0,2))
        self.assertTrue(p.attempt(3,16)[0].complete)
        self.assertEqual(p.apply_effect(12).apply_effect(12).marks,(0,0,0,2))
        self.assertTrue(p.apply_effect(12).apply_effect(12).complete)
        self.assertEqual(p.apply_effect(100).marks,(0,0,0,2))

    def test_project_promotion_and_personal_recovery(self):
        p=Project(1,4,2,"one hour")
        for _ in range(3):p=p.apply_effect(1)
        self.assertEqual(p.marks,(0,1,0,0))
        for _ in range(6):p=p.apply_effect(1)
        self.assertEqual(p.marks,(0,0,1,0))
        self.assertEqual(Track(2,marks=(0,0,1,0)).recover_step().marks,(0,2,0,0))
        self.assertEqual(Track(2,marks=(0,2,0,0)).recover_step().marks,(2,1,0,0))

    def test_all_aspects_route_only_later_fast_targeted_incidents(self):
        for aspect, spec in RESOURCE_TRACKS.items():
            with self.subTest(aspect=aspect):
                fast=Track(2)
                slow=Track(2)
                # One large blow exhausts the fast resource, never double marks slow.
                final_hit=apply_resource_effect(
                    aspect=aspect,requested_resource=spec["fast"],
                    magnitude=12,fast=fast,slow=slow)
                self.assertEqual(final_hit.applied_resource,spec["fast"])
                self.assertEqual(final_hit.fast.marks,(0,0,0,2))
                self.assertEqual(final_hit.slow.marks,(0,0,0,0))
                self.assertFalse(final_hit.redirected)
                # The NEXT fast-targeted attack spills into slow.
                overflow=apply_resource_effect(
                    aspect=aspect,requested_resource=spec["fast"],
                    magnitude=2,fast=final_hit.fast,slow=final_hit.slow)
                self.assertTrue(overflow.redirected)
                self.assertEqual(overflow.applied_resource,spec["slow"])
                self.assertEqual(overflow.fast,final_hit.fast)
                self.assertEqual(overflow.slow.marks,(0,1,0,0))
                # A fresh non-Final slot reopens fast on subsequent effects.
                recovered=overflow.fast.recover_step()
                self.assertFalse(recovered.exhausted)
                resumed=apply_resource_effect(
                    aspect=aspect,requested_resource=spec["fast"],
                    magnitude=1,fast=recovered,slow=overflow.slow)
                self.assertEqual(resumed.applied_resource,spec["fast"])
                self.assertEqual(resumed.slow,overflow.slow)

    def test_overflow_uses_destination_grade_threshold_and_direct_target(self):
        fast=Track(2,marks=(0,0,0,2))
        slow=Track(2)
        overflow=apply_resource_effect(
            aspect="soul",requested_resource="attention",magnitude=5,
            fast=fast,slow=slow,fast_effective_threshold=2,
            slow_effective_threshold=6)
        self.assertEqual((overflow.applied_resource,overflow.slow.marks),
                         ("plasticity",(1,0,0,0)))
        # A supernatural direct hit to the slow track is legal even before
        # the fast track exhausts; targeting legitimacy belongs to attack mode.
        direct=apply_resource_effect(
            aspect="soul",requested_resource="plasticity",magnitude=2,
            fast=Track(2),slow=Track(2))
        self.assertEqual(direct.slow.marks,(0,1,0,0))
        self.assertFalse(direct.redirected)

    def test_routing_validates_aspect_and_shared_capacity(self):
        with self.assertRaisesRegex(ValueError,"belong"):
            apply_resource_effect(aspect="body",requested_resource="mana",
                                  magnitude=1,fast=Track(2),slow=Track(2))
        with self.assertRaisesRegex(ValueError,"share"):
            apply_resource_effect(aspect="mind",requested_resource="mana",
                                  magnitude=1,fast=Track(2),slow=Track(3))
        with self.assertRaisesRegex(ValueError,"nonnegative"):
            apply_resource_effect(aspect="mind",requested_resource="mana",
                                  magnitude=-1,fast=Track(2),slow=Track(2))

    def test_universal_restoration_across_six_personal_resources(self):
        for aspect,spec in RESOURCE_TRACKS.items():
            for resource in (spec["fast"],spec["slow"]):
                if resource=="injury":
                    injured=Track(2,marks=(1,2,1,0))
                else:
                    injured=Track(2,marks=(1,2,1,0))
                with self.subTest(aspect=aspect,resource=resource):
                    # Potence 4 at Resilience 2 means one Major healing.
                    restored=restore_resource_effect(
                        aspect=aspect,resource=resource,
                        track=injured,magnitude=4)
                    self.assertEqual(restored.marks,(1,2,0,0))
                    self.assertEqual(restored.infliction_value(),7)
                    self.assertEqual(injured.infliction_value(),16)
                    self.assertEqual(injured.marks,(1,2,1,0))

    def test_invariant_r_plus_one_conversion_and_promoted_small_hits(self):
        for R in range(1,6):
            base=R+1
            for grade in range(4):
                for amount in range(1,4):
                    initial=Track(R,marks=tuple(min(R,(grade+i)%base)
                        if i!=3 else min(R-1,(grade+i)%base)
                        for i in range(4)))
                    healed=initial.restore_marks(grade,amount)
                    self.assertEqual(healed.infliction_value(),
                        max(0,initial.infliction_value()-amount*base**grade))
                    self.assertTrue(all(0<=m<=R for m in healed.marks))
                    self.assertEqual(healed.resilience,R)
        t=Track(2)
        for _ in range(9):
            t=t.apply_effect(1)
        self.assertEqual(t.marks,(0,0,1,0))
        self.assertEqual(t.restore_marks(2).marks,(0,0,0,0))

    def test_restoration_canonicalization_from_larger_grades(self):
        # At R=2, a Final is 27 Minor-equivalents, a Major is 9.
        one_final=Track(2,marks=(0,0,0,1))
        after=one_final.restore_marks(2)
        self.assertEqual(after.marks,(0,0,2,0))
        self.assertEqual(after.infliction_value(),18)
        self.assertEqual(one_final.restore_marks(0,27).marks,(0,0,0,0))
        # Two Grade-3 effects applied as one batch or independently agree.
        initial=Track(2,marks=(1,1,0,1))
        batch=initial.restore_marks(3,2)
        sequential=initial.restore_marks(3).restore_marks(3)
        self.assertEqual(batch,sequential)
        # Healing never generates negative marks.
        self.assertEqual(initial.restore_marks(3,100).marks,(0,0,0,0))

    def test_supernatural_healing_separate_from_daily_or_turn_recovery(self):
        t=Track(2,marks=(1,2,1,0))
        magic=t.restore_marks(2,1)
        natural=t
        for _ in range(7):
            natural=natural.recover_step()
        self.assertEqual(magic.marks,(1,2,0,0))
        self.assertEqual(natural.marks,(0,0,1,0))
        # Healing Mana does not automatically undo overflow Spirit marks.
        spirit=Track(2,marks=(0,1,0,0))
        mana=Track(2,marks=(0,1,0,0))
        restored=restore_resource_effect(
            aspect="mind",resource="mana",track=mana,magnitude=2)
        self.assertEqual(restored.marks,(0,0,0,0))
        self.assertEqual(spirit.marks,(0,1,0,0))

    def test_restorative_legal_resources_and_death_boundary(self):
        dead=Track(2,marks=(0,0,0,2))
        with self.assertRaisesRegex(ValueError,"death"):
            restore_resource_effect(
                aspect="body",resource="injury",track=dead,magnitude=10)
        # An exhausted Mana track, unlike death, may be restored.
        result=restore_resource_effect(
            aspect="mind",resource="mana",track=Track(2,marks=(0,0,0,2)),
            magnitude=10)
        self.assertFalse(result.exhausted)
        for kw in (
            dict(aspect="unknown",resource="mana",track=Track(2),magnitude=1),
            dict(aspect="body",resource="mana",track=Track(2),magnitude=1),
            dict(aspect="mind",resource="mana",track=Track(2),magnitude=-1),
        ):
            with self.assertRaises(ValueError):
                restore_resource_effect(**kw)
        for grade,count in ((-2,1),(4,1),(-1,1),(0,-1)):
            with self.assertRaises(ValueError):
                Track(2).restore_marks(grade,count)

    def test_personal_exhaustion_and_cost_mark_boundaries(self):
        t=Track(4).apply_effect(24)
        self.assertEqual(t.marks,(0,0,0,4))
        self.assertTrue(t.exhausted)
        self.assertEqual(t.penalty,-4)
        self.assertEqual(severity_marks(1,4),(0,1))
        self.assertEqual(severity_marks(4,4),(1,1))
        self.assertEqual(severity_marks(8,4),(2,1))
        self.assertEqual(severity_marks(12,4),(3,1))
        self.assertEqual(severity_marks(16,4),(3,2))

if __name__=="__main__":
    unittest.main()
