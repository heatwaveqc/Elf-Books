import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from generalized_skill_xp import (
    threshold_tenths, offensive_damage_xp_tenths, quick_xp_tenths,
    opposed_quick_result, extended_interval, format_xp_tenths
)

class SkillXPTests(unittest.TestCase):
    def test_existing_approved_ledger_units(self):
        self.assertEqual(threshold_tenths(0),50)
        self.assertEqual(threshold_tenths(20),1000)
        self.assertEqual(threshold_tenths(95),4750)
        self.assertEqual(offensive_damage_xp_tenths(12),240)

    def test_quick_static_success_and_failure_no_rounding(self):
        self.assertEqual(quick_xp_tenths(25,True),500)
        self.assertEqual(quick_xp_tenths(25,False),125)
        self.assertEqual(format_xp_tenths(125),"12.5")
        self.assertEqual(quick_xp_tenths(25,False,meaningful=False),0)

    def test_opposed_higher_enemy_check_more_xp(self):
        easy=opposed_quick_result(actor_total=35,defender_total=12,
            actor_modifier=15,defender_modifier=5)
        hard=opposed_quick_result(actor_total=35,defender_total=30,
            actor_modifier=15,defender_modifier=5)
        self.assertEqual((easy.actor_xp_tenths,hard.actor_xp_tenths),(240,600))
        self.assertTrue(hard.success)
        loss=opposed_quick_result(actor_total=25,defender_total=27,
            actor_modifier=15,defender_modifier=5)
        self.assertEqual(loss.actor_xp_tenths,135)
        self.assertFalse(loss.success)

    def test_opposed_tie_uses_modifiers_then_reroll(self):
        win=opposed_quick_result(actor_total=25,defender_total=25,
            actor_modifier=13,defender_modifier=12)
        self.assertTrue(win.success)
        self.assertEqual(win.actor_xp_tenths,500)
        tie=opposed_quick_result(actor_total=25,defender_total=25,
            actor_modifier=13,defender_modifier=13)
        self.assertIsNone(tie.success)
        self.assertEqual(tie.actor_xp_tenths,0)
        self.assertTrue(tie.must_reroll_tie)

    def test_progress_and_overproduction_no_extra_xp(self):
        first=extended_interval(dc=25,interval="4 hours",progress_goal=1000,
            progress_before=0,check_total=30)
        self.assertEqual((first.produced_progress,first.credited_progress,first.xp_tenths),(750,750,750))
        self.assertFalse(first.completed)
        second=extended_interval(dc=25,interval="4 hours",progress_goal=1000,
            progress_before=750,check_total=30)
        self.assertEqual((second.produced_progress,second.credited_progress,second.xp_tenths),(750,250,250))
        self.assertTrue(second.completed)
        self.assertEqual(first.xp_tenths+second.xp_tenths,1000)
        after=extended_interval(dc=25,interval="4 hours",progress_goal=1000,
            progress_before=1000,check_total=30)
        self.assertEqual(after.xp_tenths,0)

    def test_failed_extended_check_no_progress_or_progress_xp(self):
        mild=extended_interval(dc=25,interval="day",progress_goal=1000,
            progress_before=100,check_total=23)
        severe=extended_interval(dc=25,interval="day",progress_goal=1000,
            progress_before=100,check_total=19)
        self.assertEqual((mild.credited_progress,mild.xp_tenths),(0,0))
        self.assertFalse(mild.failure_by_five_or_more)
        self.assertEqual(severe.total_progress,100)
        self.assertTrue(severe.failure_by_five_or_more)

    def test_no_automatic_critical_success(self):
        failure=extended_interval(dc=50,interval="week",progress_goal=1000,
            progress_before=0,check_total=20)
        self.assertFalse(failure.success)

    def test_validation(self):
        with self.assertRaises(ValueError):
            quick_xp_tenths(-1,True)
        with self.assertRaises(ValueError):
            quick_xp_tenths(25,1)
        with self.assertRaises(ValueError):
            extended_interval(dc=0,interval="day",progress_goal=1000,
                progress_before=0,check_total=10)
        with self.assertRaises(ValueError):
            extended_interval(dc=25,interval="day",progress_goal=100,
                progress_before=101,check_total=25)

if __name__=="__main__":
    unittest.main()
