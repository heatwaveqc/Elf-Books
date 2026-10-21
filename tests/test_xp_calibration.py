import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from xp_calibration import average_die_damage, next_rank_xp, total_xp, expected_successes, enemy_estimate, sample_rows
from defense_core import defense_outcome


class XPCalibrationTest(unittest.TestCase):
    def test_rank_cost_and_endgame(self):
        self.assertEqual(next_rank_xp(0),1)
        self.assertEqual(next_rank_xp(95),95)
        self.assertEqual(total_xp(95,100),485)
        self.assertEqual(total_xp(20,100),4760)
        self.assertEqual(total_xp(20,25),110)
        self.assertEqual(total_xp(50,55),260)

    def test_average_d8_and_ranges(self):
        self.assertEqual(average_die_damage(8),Fraction(9,2))
        self.assertEqual(expected_successes(485,Fraction(9,2)),Fraction(970,9))
        self.assertEqual(enemy_estimate(Fraction(970,9)),(22,36))
        self.assertEqual([(r["foes_min"],r["foes_max"]) for r in sample_rows()],
                         [(5,9),(12,20),(22,36),(212,353)])

    def test_k_scaling(self):
        self.assertEqual(total_xp(95,100,k=2),970)
        with self.assertRaises(ValueError):
            next_rank_xp(100)
        with self.assertRaises(ValueError):
            next_rank_xp(15,k=0)

    def test_armor_plus_reaction_consume(self):
        # Heavy gear 8, shield 2, CON+7, Heavy Armor 100 = AC 37 (no base 10)
        r=defense_outcome(method="heavy_armor",skill_rank=100,attribute_mod=7,
                         armor_mod=8,shield_mod=2,other_legal_mod=0,
                         attack_roll=17,attack_bonus=20,worn_armor="heavy_armor",hp_lost=3)
        self.assertEqual(r.ac,37)
        self.assertTrue(r.hit)
        self.assertEqual(r.armor_hp_loss_xp,3)
        self.assertFalse(r.reaction_consumed)

    def test_high_end_5e_equipment_matchup(self):
        # +3 plate 8+3, +3 shield 2+3, CON +7, skill100 +20 => AC43
        r=defense_outcome(method="heavy_armor",skill_rank=100,attribute_mod=7,
                         armor_mod=11,shield_mod=5,other_legal_mod=0,
                         attack_roll=12,attack_bonus=30,worn_armor="heavy_armor")
        self.assertEqual(r.ac,43)
        self.assertFalse(r.hit)
        r2=defense_outcome(method="heavy_armor",skill_rank=100,attribute_mod=7,
                          armor_mod=11,shield_mod=5,other_legal_mod=0,
                          attack_roll=13,attack_bonus=30,worn_armor="heavy_armor")
        self.assertTrue(r2.hit)

    def test_reaction_use_and_armor_xp_on_failed_block(self):
        r=defense_outcome(method="block",skill_rank=35,attribute_mod=3,
                         armor_mod=6,shield_mod=2,other_legal_mod=0,
                         attack_roll=19,attack_bonus=10,worn_armor="heavy_armor",hp_lost=11)
        self.assertTrue(r.hit)
        self.assertEqual(r.armor_hp_loss_xp,11)
        self.assertTrue(r.reaction_consumed)
        with self.assertRaises(ValueError):
            defense_outcome(method="block",skill_rank=35,attribute_mod=3,
                            armor_mod=6,shield_mod=2,other_legal_mod=0,
                            attack_roll=7,attack_bonus=10,worn_armor="heavy_armor",
                            reaction_available=False)
        exempt=defense_outcome(method="block",skill_rank=35,attribute_mod=3,
                         armor_mod=6,shield_mod=2,other_legal_mod=0,
                         attack_roll=7,attack_bonus=10,worn_armor="heavy_armor",
                         reaction_available=False,free_reaction_perk=True)
        self.assertFalse(exempt.reaction_consumed)
        self.assertTrue(exempt.selected_defense_xp_eligible)

    def test_enemys_natural_one_not_defensive_xp_but_damage_trains_armor(self):
        a=defense_outcome(method="dodge",skill_rank=100,attribute_mod=7,
                         armor_mod=0,shield_mod=0,other_legal_mod=0,
                         attack_roll=1,attack_bonus=50)
        self.assertFalse(a.hit)
        self.assertFalse(a.selected_defense_xp_eligible)
        b=defense_outcome(method="heavy_armor",skill_rank=100,attribute_mod=7,
                         armor_mod=8,shield_mod=2,other_legal_mod=0,
                         attack_roll=20,attack_bonus=0,worn_armor="heavy_armor",hp_lost=13)
        self.assertTrue(b.hit)
        self.assertEqual(b.armor_hp_loss_xp,13)


if __name__=="__main__":
    unittest.main()
