import sys
import unittest
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from actual_damage_xp import xp_to_next, total_required, effective_damage_xp, expected_successful_hits, encounter_damage_budget

class ActualDamageXP(unittest.TestCase):
    def test_fivefold_rank_cost(self):
        self.assertEqual(xp_to_next(0),5)
        self.assertEqual(xp_to_next(95),475)
        self.assertEqual(total_required(95,100),2425)
        self.assertEqual(total_required(20,25),550)
        self.assertEqual(total_required(50,55),1300)
        self.assertEqual(total_required(20,100),23800)

    def test_true_hp_lost_and_overkill(self):
        self.assertEqual(effective_damage_xp(30,8),8)
        self.assertEqual(effective_damage_xp(30,100,12),18)
        self.assertEqual(effective_damage_xp(10,100,11),0)
        self.assertEqual(effective_damage_xp(12,0),0)

    def test_same_hp_pool_different_hit_sizes(self):
        dagger=sum(effective_damage_xp(x,hp) for x,hp in ((6,20),(6,14),(6,8),(6,2)))
        greatsword=sum(effective_damage_xp(x,hp) for x,hp in ((12,20),(12,8)))
        self.assertEqual(dagger,20)
        self.assertEqual(greatsword,20)

    def test_pacing_break_even(self):
        xp=total_required(95,100)
        self.assertEqual(expected_successful_hits(xp,Fraction(45,2)),Fraction(970,9))
        self.assertGreater(expected_successful_hits(xp,Fraction(29,2)),Fraction(970,9))
        self.assertEqual(encounter_damage_budget(50),50)
        self.assertEqual(encounter_damage_budget(50,Fraction(1,2)),25)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            xp_to_next(100)
        with self.assertRaises(ValueError):
            effective_damage_xp(5,-1)
        with self.assertRaises(ValueError):
            encounter_damage_budget(50, Fraction(3,2))

if __name__ == "__main__":
    unittest.main()
