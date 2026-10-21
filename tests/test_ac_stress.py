import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from ac_stress import Scenario, archetypal_scenarios, hit_probability, modifier


class ACStressTest(unittest.TestCase):
    def test_attribute_modifier(self):
        self.assertEqual(modifier(25),7)

    def test_high_end_stack_nat20_only_even_without_base(self):
        c=archetypal_scenarios()[0]
        self.assertEqual((c.attack_bonus,c.ac(0),c.ac(10)),(32,52,62))
        self.assertAlmostEqual(c.chance(0),0.05)
        self.assertAlmostEqual(c.chance(10),0.05)

    def test_without_natural_armor(self):
        c=archetypal_scenarios()[1]
        self.assertEqual(c.ac(0),47)
        self.assertAlmostEqual(c.chance(0),0.30)
        self.assertAlmostEqual(c.chance(10),0.05)

    def test_unarmored_parity_requires_d20_midpoint(self):
        c=archetypal_scenarios()[2]
        self.assertEqual((c.attack_bonus,c.ac(0),c.ac(10)),(27,27,37))
        self.assertAlmostEqual(c.chance(0),0.95)
        self.assertAlmostEqual(c.chance(10),0.55)

    def test_defense_bonus_half_rate_as_alternative(self):
        self.assertAlmostEqual(hit_probability(32,42),0.55)

    def test_mundane_armor_converted_to_dr_as_alternative(self):
        self.assertAlmostEqual(hit_probability(32,44),0.45)

    def test_natural_one_miss_and_natural_twenty_hit(self):
        self.assertEqual(hit_probability(-100,1000),0.05)
        self.assertEqual(hit_probability(1000,0),0.95)


if __name__ == "__main__":
    unittest.main()
