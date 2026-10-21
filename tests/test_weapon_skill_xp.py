import sys
import unittest
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from weapon_skill_xp import (
    skill_bonus,next_rank_xp,total_xp,rolled_damage,award_damage_xp,
    effective_hp_removed,expected_successful_hits,expected_attempts_with_crits
)

class WeaponSkillXPTest(unittest.TestCase):
    def test_skill_adds_same_bonus_to_attack_and_damage(self):
        self.assertEqual([skill_bonus(x) for x in (0,20,24,25,50,95,100)],[0,4,4,5,10,19,20])
        self.assertEqual(rolled_damage(5,3,20),12)
        self.assertEqual(rolled_damage(5,7,95,3),34)

    def test_cost_and_equivalent_units(self):
        self.assertEqual((next_rank_xp(0),next_rank_xp(20)),(5,100))
        self.assertEqual((total_xp(20,25),total_xp(50,55),total_xp(95,100)),(550,1300,2425))
        self.assertEqual(Fraction(total_xp(20,25),2),275) # 2.5*sum(20..24)
        self.assertEqual(award_damage_xp(12),24)

    def test_pacing(self):
        self.assertEqual(expected_successful_hits(20,25,8,3),Fraction(550,23))
        self.assertEqual(expected_successful_hits(50,55,8,5),Fraction(100,3))
        self.assertEqual(expected_successful_hits(95,100,8,7,3),Fraction(2425,67))
        attempts=expected_attempts_with_crits(20,25,8,3,Fraction(3,5))
        self.assertEqual(attempts,Fraction(2200,57)) # 550 / 14.25 ≈ 38.596

    def test_actual_hp_not_overkill_or_resisted(self):
        self.assertEqual(award_damage_xp(effective_hp_removed(30,8)),16)
        self.assertEqual(award_damage_xp(effective_hp_removed(30,100,12)),36)
        self.assertEqual(award_damage_xp(effective_hp_removed(10,100,20)),0)

    def test_weapon_speed_same_finite_hp_pool(self):
        small=sum(award_damage_xp(effective_hp_removed(d,h)) for d,h in ((6,20),(6,14),(6,8),(6,2)))
        large=sum(award_damage_xp(effective_hp_removed(d,h)) for d,h in ((12,20),(12,8)))
        self.assertEqual(small,40)
        self.assertEqual(large,40)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            skill_bonus(101)
        with self.assertRaises(ValueError):
            next_rank_xp(100)
        with self.assertRaises(ValueError):
            award_damage_xp(-1)
        with self.assertRaises(ValueError):
            expected_successful_hits(21,25,8,3)

if __name__ == "__main__":
    unittest.main()
