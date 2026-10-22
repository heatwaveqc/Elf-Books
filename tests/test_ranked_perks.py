"""Approved shared perk conventions: rank qualification, wildcard Specialty,
and a fixed equipment bonus cap independent of perk Skill-equivalent dice.
"""
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from perks import RankedPerk, PerkRequirement,qualify_for_perk,evaluate_next_rank
from attack_modes import compose_named_pool
from trait_pools import Talent

class RankedPerkAndCapTests(unittest.TestCase):
    def setUp(self):
        self.talent=Talent("Warrior",frozenset({
            "one_handed","two_handed","block","heavy_armor","athletics"
        }),25)

    def test_any_specialty_of_named_skill_selects_one_best(self):
        req=PerkRequirement("Weapon Finesse","dexterity","one_handed",
                            frozenset({"*"}),76)
        q=qualify_for_perk(
            requirement=req,attribute="dexterity",attribute_rating=20,
            skill="one_handed",skill_rating=15,talent=self.talent,
            specialty_ratings={"daggers":20,"swords":25})
        self.assertEqual((q.total_rating,q.specialty_rating,
                          q.qualifying_specialty),(85,25,"swords"))
        self.assertTrue(q.meets_requirement)
        # Explicit specialty names are not substituted with wildcard.
        mace=PerkRequirement("Mace Specialist","strength","one_handed",
                              frozenset({"maces"}),76)
        no_match=qualify_for_perk(
            requirement=mace,attribute="strength",attribute_rating=25,
            skill="one_handed",skill_rating=25,talent=self.talent,
            specialty_ratings={"swords":25})
        self.assertEqual(no_match.total_rating,75)
        self.assertFalse(no_match.meets_requirement)
        self.assertIsNone(no_match.qualifying_specialty)
        self.assertEqual(qualify_for_perk(
            requirement=req,attribute="dexterity",attribute_rating=20,
            skill="one_handed",skill_rating=15,talent=self.talent,
            specialty_ratings={}).specialty_rating,0)

    def test_sequential_five_ranks_with_independent_gates(self):
        # Illustrative gates, not final Finesse catalogue purchase records.
        example=RankedPerk("Finesse","dexterity","one_handed",
                           frozenset({"*"}),(20,40,60,75,90))
        result=evaluate_next_rank(
            perk=example,current_rank=0,banked_points=1,
            attribute="dexterity",attribute_rating=10,
            skill="one_handed",skill_rating=10,talent=self.talent,
            specialty_ratings={})
        self.assertEqual((result.next_rank,result.required_rating,
                          result.qualified,result.remaining_points),(1,20,True,0))
        no_points=evaluate_next_rank(
            perk=example,current_rank=0,banked_points=0,
            attribute="dexterity",attribute_rating=10,
            skill="one_handed",skill_rating=10,talent=self.talent,
            specialty_ratings={})
        self.assertFalse(no_points.qualified)
        self.assertEqual(no_points.remaining_points,0)
        # Even if threshold is met, next rank must be purchased in order.
        upper=evaluate_next_rank(
            perk=example,current_rank=4,banked_points=1,
            attribute="dexterity",attribute_rating=25,
            skill="one_handed",skill_rating=25,talent=self.talent,
            specialty_ratings={"swords":25})
        self.assertEqual((upper.next_rank,upper.required_rating,
                          upper.qualified,upper.remaining_points),(5,90,True,0))
        capped=evaluate_next_rank(
            perk=example,current_rank=5,banked_points=4,
            attribute="dexterity",attribute_rating=25,
            skill="one_handed",skill_rating=25,talent=self.talent,
            specialty_ratings={"swords":25})
        self.assertEqual((capped.next_rank,capped.qualified,
                          capped.remaining_points),(None,False,4))
        for gates in ((20,20),(-1,30),(10,101),(10,25,40,50,60,75),()):
            with self.subTest(gates=gates),self.assertRaises(ValueError):
                RankedPerk("Bad","dexterity","one_handed",frozenset({"*"}),gates)

    def test_perk_skill_dice_never_expand_equipment_bonus_cap(self):
        ratings={"attribute":{0:15},"talent":{0:10},
                 "skill":{0:15},"specialty":{0:5}}
        p=compose_named_pool(attribute="dexterity",skill="one_handed",
            tier=0,talent=self.talent,ratings=ratings,specialty_declared=True,
            external_bonuses={"sword":9},perk_skill_dice=5)
        self.assertEqual((p.personal_dice,p.external_dice,p.perk_skill_dice,
                          p.dice,p.static_opposition),(9,9,5,23,11))
        # Without perk dice this pool would be 18; equipment limit still 9.
        for illegal in (-1,1.5,True):
            with self.subTest(value=illegal),self.assertRaises(ValueError):
                compose_named_pool(
                    attribute="dexterity",skill="one_handed",
                    tier=0,talent=self.talent,ratings=ratings,
                    external_bonuses={"sword":9},
                    perk_skill_dice=illegal)
        with self.assertRaisesRegex(ValueError,"aggregate"):
            compose_named_pool(
                attribute="dexterity",skill="one_handed",
                tier=0,talent=self.talent,ratings=ratings,
                external_bonuses={"sword":10},perk_skill_dice=5)

if __name__=="__main__":
    unittest.main()
