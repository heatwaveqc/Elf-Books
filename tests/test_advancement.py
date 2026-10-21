import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"scripts"))
from trait_pools import Talent, dice_for_rating, ATTRIBUTES
from advancement import (
    XP_PER_SUCCESS, award_roll_xp, spend_xp, validate_starting_allocation, xp_to_next
)

class AdvancementTests(unittest.TestCase):
    def setUp(self):
        self.talent = Talent("Spellsword", frozenset({
            "one_handed","light_armor","alteration","destruction","restoration"
        }), 5)
        self.skills = {s["id"] for s in
                       json.loads((ROOT/"rules/skills.json").read_text())["skills"]}

    def test_cost_ratings_and_overflow(self):
        self.assertEqual([xp_to_next(r) for r in (0,1,2,3,4,5,20)],
                         [10,10,20,30,40,50,200])
        self.assertEqual(spend_xp(0,110),(5,0))
        self.assertEqual(spend_xp(20,199),(20,199))
        self.assertEqual(spend_xp(20,200),(21,0))
        self.assertEqual(spend_xp(24,250),(25,10))
        self.assertEqual(spend_xp(25,1000),(25,1000))
        with self.assertRaises(ValueError):
            xp_to_next(25)

    def test_attribute_success_is_two_xp(self):
        self.assertEqual(XP_PER_SUCCESS,
                         {"attribute":2,"talent":1,"skill":5,"specialty":10})
        award = award_roll_xp(
            {"attribute":[10,8],"talent":[7],"skill":[],"specialty":[]},
            {"attribute":10,"talent":5,"skill":0,"specialty":0},
            talent_governs=True,specialty_declared=True
        )
        self.assertEqual(award.xp,{"attribute":6,"talent":1,"skill":5,"specialty":10})
        self.assertEqual(award.natural_tens,1)
        self.assertEqual(award.bootstrap_skill_xp,5)
        self.assertEqual(award.bootstrap_specialty_xp,10)

    def test_one_ten_can_bootstrap_both_from_zero_and_preserve_source(self):
        award=award_roll_xp(
            {"attribute":[10,10],"talent":[6],"skill":[],"specialty":[]},
            {"attribute":10,"talent":5,"skill":0,"specialty":0},
            talent_governs=True,specialty_declared=True)
        self.assertEqual(award.xp["attribute"],8)
        self.assertEqual(award.xp["skill"],10)
        self.assertEqual(award.xp["specialty"],20)
        self.assertEqual(spend_xp(0,award.xp["specialty"]),(2,0))

    def test_trained_skill_no_bootstrap_specialty_still_bootstraps(self):
        award=award_roll_xp(
            {"attribute":[8,10],"talent":[5],"skill":[10],"specialty":[]},
            {"attribute":10,"talent":5,"skill":5,"specialty":0},
            talent_governs=True,specialty_declared=True)
        self.assertEqual(award.xp["attribute"],6)
        self.assertEqual(award.xp["talent"],0)
        self.assertEqual(award.xp["skill"],10)
        self.assertEqual(award.xp["specialty"],20)
        self.assertEqual((award.bootstrap_skill_xp,award.bootstrap_specialty_xp),(0,20))

    def test_not_governed_not_denied_roll_or_skill_learning(self):
        award=award_roll_xp(
            {"attribute":[7,10],"talent":[],"skill":[],"specialty":[]},
            {"attribute":10,"talent":5,"skill":0,"specialty":0},
            talent_governs=False,specialty_declared=True)
        self.assertEqual(award.xp,{"attribute":6,"talent":0,"skill":5,"specialty":10})

    def test_equipment_10_can_trigger_learning_but_not_trait_source_xp(self):
        award=award_roll_xp(
            {"attribute":[1,3],"talent":[],"skill":[],"specialty":[],
             "equipment":[10]},
            {"attribute":10,"talent":5,"skill":0,"specialty":0},
            talent_governs=False,specialty_declared=True)
        self.assertEqual(award.xp,{"attribute":0,"talent":0,"skill":5,"specialty":10})

    def test_undeclared_specialty_does_not_receive_bootstrap(self):
        award=award_roll_xp(
            {"attribute":[10,5],"talent":[],"skill":[],"specialty":[]},
            {"attribute":10,"talent":5,"skill":0,"specialty":0},
            talent_governs=False,specialty_declared=False)
        self.assertEqual(award.bootstrap_specialty_xp,0)
        self.assertEqual(award.bootstrap_skill_xp,5)

    def test_pre_roll_ratings_and_exact_face_counts_enforced(self):
        args=dict(ratings={"attribute":10,"talent":5,"skill":0,"specialty":0},
                  talent_governs=True,specialty_declared=True)
        with self.assertRaises(ValueError):
            award_roll_xp({"attribute":[10],"talent":[7],"skill":[],"specialty":[]},**args)
        with self.assertRaises(ValueError):
            award_roll_xp({"attribute":[10,10],"talent":[7],"skill":[8],"specialty":[]},**args)

    def test_starting_character_governed_skills_must_have_first_die(self):
        attributes={name:10 for aspect in ATTRIBUTES.values() for name in aspect.values()}
        skills={skill:0 for skill in self.skills}
        for skill in self.talent.governed_skills:
            skills[skill]=5
        validate_starting_allocation(attributes,skills,self.talent,self.skills)
        self.assertEqual(dice_for_rating(skills["one_handed"]),1)
        self.assertEqual(dice_for_rating(skills["smithing"]),0)
        skills["alteration"]=4
        with self.assertRaisesRegex(ValueError,"alteration"):
            validate_starting_allocation(attributes,skills,self.talent,self.skills)
        skills["alteration"]=5
        attributes["will"]=4
        with self.assertRaisesRegex(ValueError,"attributes"):
            validate_starting_allocation(attributes,skills,self.talent,self.skills)

if __name__ == "__main__":
    unittest.main()
