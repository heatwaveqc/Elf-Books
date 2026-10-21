import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from crafting_xp import next_rank_xp,xp_required,craft_xp,d20_check_success_probability,expected_completed_units,expected_attempts

class CraftingDCXPTests(unittest.TestCase):
    def test_accepted_rank_ladder(self):
        self.assertEqual(next_rank_xp(0),5)
        self.assertEqual(xp_required(20,25),550)
        self.assertEqual(xp_required(50,55),1300)
        self.assertEqual(xp_required(95,100),2425)

    def test_one_product_many_checks_one_award(self):
        self.assertEqual(craft_xp(15),30)
        self.assertEqual(craft_xp(15,5),150)
        self.assertEqual(craft_xp(15,0),0)
        self.assertEqual(craft_xp(40),80)

    def test_d20_success_chances(self):
        self.assertEqual(d20_check_success_probability(15,3,20),Fraction(13,20))
        self.assertEqual(d20_check_success_probability(25,5,50),Fraction(11,20))
        self.assertEqual(d20_check_success_probability(40,7,95),Fraction(7,20))
        self.assertEqual(d20_check_success_probability(2,30,100),1) # natural 1 is not auto-fail
        self.assertEqual(d20_check_success_probability(90,0,0),0)

    def test_expected_crafting_pacing(self):
        self.assertEqual(expected_completed_units(20,25,15),Fraction(55,3))
        self.assertEqual(expected_completed_units(50,55,25),26)
        self.assertEqual(expected_completed_units(95,100,40),Fraction(485,16))
        self.assertEqual(expected_attempts(20,25,15,3),Fraction(1100,39))
        self.assertEqual(expected_attempts(50,55,25,5),Fraction(520,11))
        self.assertEqual(expected_attempts(95,100,40,7),Fraction(2425,28))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            next_rank_xp(100)
        with self.assertRaises(ValueError):
            craft_xp(0)
        with self.assertRaises(ValueError):
            craft_xp(15,-1)
        with self.assertRaises(ValueError):
            expected_attempts(20,25,100,3)

if __name__=="__main__":
    unittest.main()
