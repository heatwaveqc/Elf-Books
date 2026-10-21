import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from generalized_skill_xp import threshold_tenths,quick_xp_tenths,extended_interval
from magic_defense_xp import (
    outgoing_damage_xp_tenths,magicka_spend_xp_tenths,
    worn_armor_xp_tenths,protective_spell_hp_xp_tenths,credited_avoidance
)

class AcceptedAdvancementNumbers(unittest.TestCase):
    def test_all_approved_units_use_tenths(self):
        self.assertEqual(threshold_tenths(20),1000)
        self.assertEqual(outgoing_damage_xp_tenths(12),240)
        self.assertEqual(magicka_spend_xp_tenths(8),160)
        self.assertEqual(outgoing_damage_xp_tenths(12)+magicka_spend_xp_tenths(8),400)
        self.assertEqual(worn_armor_xp_tenths(10),400)
        self.assertEqual(protective_spell_hp_xp_tenths(10),200)
        self.assertEqual(quick_xp_tenths(25,True),500)
        self.assertEqual(quick_xp_tenths(25,False),125)

    def test_avoided_attack_and_project_progress(self):
        a=credited_avoidance(natural_attack_roll=13,attack_total=23,
                            ac_without=18,ac_with=27)
        self.assertEqual(a.xp_tenths,460)
        first=extended_interval(dc=25,interval="week",progress_goal=1000,
                                progress_before=0,check_total=30)
        last=extended_interval(dc=25,interval="week",progress_goal=1000,
                                progress_before=750,check_total=30)
        self.assertEqual((first.credited_progress,last.credited_progress),(750,250))
        self.assertEqual((first.xp_tenths,last.xp_tenths),(750,250))
        self.assertEqual(first.xp_tenths+last.xp_tenths,1000)

if __name__=="__main__":
    unittest.main()
