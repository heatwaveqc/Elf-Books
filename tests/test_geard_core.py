import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from geard_core import d10_successes,convert_tier,severity_marks,Track,Project,resolve_project_roll

class LocalCoreTests(unittest.TestCase):
    def test_tentative_randomizer_and_zero(self):
        self.assertEqual(d10_successes([1,2,6]),0)
        self.assertEqual(d10_successes([7,8,9,10,10]),7)
        with self.assertRaises(ValueError):d10_successes([0])

    def test_tier_conversion_is_on_roll_not_static_threshold(self):
        self.assertEqual(convert_tier(27,0,1),2)
        self.assertEqual(convert_tier(27,1,3),0)
        self.assertEqual(convert_tier(3,5,4),30)
        self.assertEqual(convert_tier(9,1,1),9)

    def test_severity_boundaries_health_4(self):
        expected=[(-1,0),(0,1),(1,1),(2,1),(3,1),(3,2),(3,4)]
        self.assertEqual([severity_marks(x,4) for x in (0,1,4,8,12,16,24)],expected)

    def test_single_strike_can_fill_fatal_slots(self):
        t=Track(4).apply_effect(24)
        self.assertEqual(t.marks,(0,0,0,4))
        self.assertTrue(t.exhausted)
        self.assertEqual(t.penalty,-4)

    def test_grade_promotion_cascades(self):
        t=Track(2)
        for _ in range(3):t=t.apply_effect(1)
        self.assertEqual(t.marks,(0,1,0,0))
        # Two further minor marks fill minor again, one more promotes middling;
        # second middling reaches cap, next promotion should cascade major.
        for _ in range(6):t=t.apply_effect(1)
        self.assertEqual(t.marks,(0,0,1,0))
        self.assertEqual(t.penalty,-2)

    def test_recovery_lowest_occupied(self):
        t=Track(2,marks=(0,0,1,0)).recover_step()
        self.assertEqual(t.marks,(0,2,0,0))
        t=t.recover_step()
        self.assertEqual(t.marks,(2,1,0,0))
        self.assertEqual(t.penalty,-1)

    def test_strict_project_application_and_progress_tiers(self):
        # Equality is NOT success. No Potence roll if Accuracy fails.
        a=resolve_project_roll(3,3,None,4)
        self.assertFalse(a.applied)
        self.assertFalse(a.potence_rolled)
        with self.assertRaises(ValueError):
            resolve_project_roll(3,3,10,4)
        self.assertEqual(resolve_project_roll(4,3,4,4).tier_upgrades,0)
        self.assertFalse(resolve_project_roll(4,3,4,4).progressed)
        for p,tier in [(5,1),(7,1),(8,2),(11,2),(12,3)]:
            out=resolve_project_roll(4,3,p,4)
            self.assertTrue(out.applied)
            self.assertTrue(out.progressed)
            self.assertEqual(out.tier_upgrades,tier)

    def test_zero_recalcitrance_unresolved_not_division_by_zero(self):
        with self.assertRaises(ValueError):
            resolve_project_roll(4,3,5,0)
        # The existing locked personal-resource Minor mark still occurs
        # at sub-Resilience magnitudes, independently of Project progress.
        self.assertEqual(severity_marks(3,4),(0,1))
        self.assertEqual(severity_marks(4,4),(1,1))

    def test_project_has_independent_dimensions(self):
        p=Project(complexity=3,recalcitrance=5,scope=100,time_per_attempt="one week")
        self.assertFalse(p.complete)
        self.assertEqual(p.credit(40).credit(200).progress,100)
        self.assertTrue(p.credit(100).complete)
        with self.assertRaises(ValueError):p.credit(-5)

if __name__=="__main__":
    unittest.main()
