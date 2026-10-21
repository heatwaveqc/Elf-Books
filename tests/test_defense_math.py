import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from defense_math import resolve_attack, defense_perk_breakthrough


class ConsolidatedSkillTest(unittest.TestCase):
    def test_eight_each_and_complete_historical_mapping(self):
        proposed = json.loads((ROOT / "design" / "skills_v2.json").read_text())
        old = json.loads((ROOT / "rules" / "skills.json").read_text())
        names = [s["id"] for s in proposed["skills"]]
        self.assertEqual(len(names), 24)
        self.assertEqual(len(names), len(set(names)))
        for cat in ("warrior", "mage", "rogue"):
            self.assertEqual(sum(s["category"] == cat for s in proposed["skills"]), 8)
        self.assertEqual(set(proposed["historical_crosswalk"]), {s["id"] for s in old["entries"]})
        for paths in proposed["historical_crosswalk"].values():
            self.assertTrue(set(paths).issubset(set(names)))
        self.assertEqual(sum(len(s["perks"]) for s in proposed["skills"]), 48)

    def test_skills_cannot_stack(self):
        # Armor example: shield+DEX already in base; gear+training is selected method.
        armor = resolve_attack(roll=12, attack_bonus=7, ac_without_method=14,
            method_gear_or_attribute_bonus=6, defense_skill_rank=50, chosen_skill="heavy_armor")
        self.assertEqual(armor.ac,30)
        self.assertFalse(armor.hit)
        self.assertEqual(armor.credited_skill,"heavy_armor")
        block = resolve_attack(roll=12, attack_bonus=7, ac_without_method=20,
            method_gear_or_attribute_bonus=2, defense_skill_rank=40, chosen_skill="block")
        self.assertEqual(block.ac,30)
        self.assertEqual(block.credited_skill,None)  # Armor alone had already avoided the blow

    def test_gear_only_save_teaches_novice(self):
        r=resolve_attack(roll=12, attack_bonus=2, ac_without_method=10,
            method_gear_or_attribute_bonus=6, defense_skill_rank=0, chosen_skill="light_armor")
        self.assertEqual(r.credited_skill,"light_armor")

    def test_natural_rolls_never_credit_passive_defense(self):
        for roll, hit in [(1,False),(20,True)]:
            r=resolve_attack(roll=roll, attack_bonus=9, ac_without_method=10,
                method_gear_or_attribute_bonus=8, defense_skill_rank=100, chosen_skill="heavy_armor")
            self.assertEqual(r.hit,hit)
            self.assertIsNone(r.credited_skill)

    def test_ordinary_miss_not_credit(self):
        r=resolve_attack(roll=3, attack_bonus=1, ac_without_method=15,
            method_gear_or_attribute_bonus=6, defense_skill_rank=50, chosen_skill="heavy_armor")
        self.assertIsNone(r.credited_skill)

    def test_defender_discovery_requires_save_and_nat20(self):
        r=resolve_attack(roll=12,attack_bonus=7, ac_without_method=14,
            method_gear_or_attribute_bonus=6,defense_skill_rank=50,chosen_skill="heavy_armor")
        self.assertTrue(defense_perk_breakthrough(r,20,True))
        self.assertFalse(defense_perk_breakthrough(r,19,True))
        self.assertFalse(defense_perk_breakthrough(r,20,False))
        poor=resolve_attack(roll=1,attack_bonus=50,ac_without_method=14,
            method_gear_or_attribute_bonus=6,defense_skill_rank=50,chosen_skill="heavy_armor")
        self.assertFalse(defense_perk_breakthrough(poor,20,True))

    def test_threat_credibility_matters(self):
        r=resolve_attack(roll=12,attack_bonus=7,ac_without_method=14,
            method_gear_or_attribute_bonus=6,defense_skill_rank=50,chosen_skill="heavy_armor",
            attack_is_credible=False)
        self.assertIsNone(r.credited_skill)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            resolve_attack(roll=0,attack_bonus=0,ac_without_method=10,
                method_gear_or_attribute_bonus=6,defense_skill_rank=20,chosen_skill="heavy_armor")
        with self.assertRaises(ValueError):
            resolve_attack(roll=10,attack_bonus=0,ac_without_method=10,
                method_gear_or_attribute_bonus=6,defense_skill_rank=101,chosen_skill="heavy_armor")


if __name__ == "__main__":
    unittest.main()
