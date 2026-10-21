import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from geard_core import d10_successes,convert_tier,severity_marks,Track,Project,resolve_project_roll

class LocalCoreTests(unittest.TestCase):
    def test_tentative_randomizer_and_tier(self):
        self.assertEqual(d10_successes([1,2,6]),0)
        self.assertEqual(d10_successes([7,8,9,10,10]),7)
        with self.assertRaises(ValueError):d10_successes([0])
        self.assertEqual(convert_tier(27,0,1),2)
        self.assertEqual(convert_tier(27,1,3),0)
        self.assertEqual(convert_tier(3,5,4),30)
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
