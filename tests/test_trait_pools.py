import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from trait_pools import Talent,compose_pool,ATTRIBUTES

class TalentPoolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills={s["id"] for s in json.loads((ROOT/"rules/skills.json").read_text())["skills"]}
        cls.data=json.loads((ROOT/"rules/talents.json").read_text())
        cls.attr=json.loads((ROOT/"rules/attributes.json").read_text())

    def test_twelve_independent_attributes_across_three_aspects(self):
        self.assertEqual(len(self.attr["aspects"]),3)
        names=[name for s in self.attr["aspects"] for name in s["attributes"].values()]
        self.assertEqual(len(names),12)
        self.assertEqual(len(set(names)),12)
        self.assertEqual(set(names),set(ATTRIBUTES["body"].values())|
                         set(ATTRIBUTES["mind"].values())|set(ATTRIBUTES["soul"].values()))
        self.assertEqual({s["attributes"]["resilience"] for s in self.attr["aspects"]},
                         {"health","will","conviction"})

    def test_prebuilt_and_custom_five_distinct_skills(self):
        self.assertEqual(len(self.skills),24)
        self.assertGreaterEqual(len(self.data["presets"]),6)
        for p in self.data["presets"]:
            with self.subTest(talent=p["name"]):
                t=Talent(p["name"],frozenset(p["skills"]),2)
                t.validate_catalog(self.skills)
                self.assertEqual(len(p["skills"]),5)
                self.assertEqual(len(set(p["skills"])),5)
        custom=Talent("Ashlander Ranger",frozenset({"archery","survival","lore",
                                                      "alchemy","alteration"}),3)
        custom.validate_catalog(self.skills)

    def test_talent_is_not_a_class_lock(self):
        t=Talent("Spellsword",frozenset({"one_handed","light_armor","alteration",
                                        "destruction","restoration"}),2)
        accuracy=compose_pool(attribute_name="dexterity",role="accuracy",
                              attribute_rating=3,talent=t,skill_id="one_handed",
                              skill_rating=4,specialty_rating=1)
        potence=compose_pool(attribute_name="strength",role="potence",
                             attribute_rating=4,talent=t,skill_id="one_handed",
                             skill_rating=4,specialty_rating=1)
        self.assertEqual((accuracy.dice,potence.dice),(10,11))
        smith=compose_pool(attribute_name="strength",role="potence",
                           attribute_rating=4,talent=t,skill_id="smithing",
                           skill_rating=3)
        self.assertEqual((smith.dice,smith.talent),(7,0))
        self.assertEqual(compose_pool(attribute_name="intelligence",role="potence",
                        attribute_rating=5,talent=t,skill_id="alchemy",
                        skill_rating=5,specialty_rating=5).dice,15)

    def test_invalid_packages_and_role_abuse(self):
        with self.assertRaises(ValueError):
            Talent("Too few",frozenset({"archery","smithing"}),1)
        with self.assertRaises(ValueError):
            Talent("Invalid",frozenset({"archery","smithing","alchemy","fake","dodge"}),1).validate_catalog(self.skills)
        t=Talent("Warrior",frozenset({"one_handed","two_handed","block","heavy_armor","athletics"}),2)
        with self.assertRaises(ValueError):
            compose_pool(attribute_name="health",role="accuracy",attribute_rating=3,
                         talent=t,skill_id="block",skill_rating=2)
        with self.assertRaises(ValueError):
            compose_pool(attribute_name="dexterity",role="accuracy",attribute_rating=6,
                         talent=t,skill_id="block",skill_rating=2)

if __name__=="__main__":
    unittest.main()
