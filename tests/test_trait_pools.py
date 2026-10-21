import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"scripts"))
from trait_pools import Talent, compose_pool, ATTRIBUTES, dice_for_rating

class TalentPoolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = {s["id"] for s in
                      json.loads((ROOT/"rules/skills.json").read_text())["skills"]}
        cls.data = json.loads((ROOT/"rules/talents.json").read_text())
        cls.attrs = json.loads((ROOT/"rules/attributes.json").read_text())

    def test_twelve_independent_attributes_across_three_aspects(self):
        names = [value for aspect in self.attrs["aspects"]
                 for value in aspect["attributes"].values()]
        self.assertEqual(len(names), 12)
        self.assertEqual(len(set(names)), 12)
        self.assertEqual(set(names), {
            value for aspect in ATTRIBUTES.values() for value in aspect.values()})
        self.assertEqual({a["attributes"]["resilience"] for a in self.attrs["aspects"]},
                         {"health", "will", "conviction"})

    def test_preset_and_custom_packages(self):
        self.assertEqual(len(self.skills), 24)
        for preset in self.data["presets"]:
            talent = Talent(preset["name"], frozenset(preset["skills"]), 10)
            talent.validate_catalog(self.skills)
            self.assertEqual(len(preset["skills"]), 5)
            self.assertEqual(len(set(preset["skills"])), 5)
        custom = Talent("Ashlander Ranger", frozenset({
            "archery", "survival", "lore", "alchemy", "alteration"}), 15)
        custom.validate_catalog(self.skills)

    def test_one_die_per_five_levels(self):
        expected = [(0,0),(4,0),(5,1),(9,1),(10,2),(14,2),(15,3),
                    (19,3),(20,4),(24,4),(25,5)]
        self.assertEqual([(r, dice_for_rating(r)) for r, _ in expected], expected)
        for bad in (-1,26,1.5,True):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                dice_for_rating(bad)

    def test_talent_bonus_and_skill_not_locked_out(self):
        t = Talent("Spellsword", frozenset({
            "one_handed","light_armor","alteration","destruction","restoration"}), 10)
        hit = compose_pool(attribute_name="dexterity",role="accuracy",
                           attribute_rating=15,talent=t,skill_id="one_handed",
                           skill_rating=20,specialty_rating=5)
        effect = compose_pool(attribute_name="strength",role="potence",
                              attribute_rating=20,talent=t,skill_id="one_handed",
                              skill_rating=20,specialty_rating=5)
        self.assertEqual((hit.attribute,hit.talent,hit.skill,hit.specialty),(3,2,4,1))
        self.assertEqual((hit.dice,effect.dice),(10,11))
        smith = compose_pool(attribute_name="strength",role="potence",
                             attribute_rating=20,talent=t,skill_id="smithing",
                             skill_rating=15)
        self.assertEqual((smith.dice,smith.talent),(7,0))
        self.assertEqual(compose_pool(attribute_name="intelligence",role="potence",
                         attribute_rating=25,talent=t,skill_id="alchemy",
                         skill_rating=25,specialty_rating=25).dice,15)

    def test_invalid_packages_and_attribute_function(self):
        with self.assertRaises(ValueError):
            Talent("Too few", frozenset({"archery","smithing"}), 5)
        with self.assertRaises(ValueError):
            Talent("Invalid",frozenset({
                "archery","smithing","alchemy","fake","dodge"}),5).validate_catalog(self.skills)
        t = Talent("Warrior",frozenset({
            "one_handed","two_handed","block","heavy_armor","athletics"}), 10)
        with self.assertRaises(ValueError):
            compose_pool(attribute_name="health",role="accuracy",attribute_rating=15,
                         talent=t,skill_id="block",skill_rating=10)
        with self.assertRaises(ValueError):
            compose_pool(attribute_name="dexterity",role="accuracy",attribute_rating=26,
                         talent=t,skill_id="block",skill_rating=10)

if __name__ == "__main__":
    unittest.main()
