"""Tier prerequisites, raw-XP cascade and passive practice arithmetic."""
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

from trait_pools import Talent, compose_tier_pool, validate_tier_ratings
from advancement import (award_tier_roll_xp,cascade_xp_tenths,
    passive_xp_tenths,static_defense_value,spend_tier_xp_tenths,
    xp_to_next_at_tier)


class TierAdvancementTests(unittest.TestCase):
    def setUp(self):
        self.talent=Talent("Spellsword",frozenset({
            "one_handed","light_armor","alteration","destruction","restoration"}),25)

    @staticmethod
    def tiered(attribute={0:25,1:5},talent={0:25,1:0},
               skill={0:25,1:25},specialty={0:25,1:20}):
        return dict(attribute=dict(attribute),talent=dict(talent),
                    skill=dict(skill),specialty=dict(specialty))

    def pool(self,ratings,tier=1):
        return compose_tier_pool(attribute_name="dexterity",role="accuracy",
                                 tier=tier,talent=self.talent,skill_id="one_handed",
                                 ratings=ratings)

    def test_high_skill_specialty_not_capped_by_attribute(self):
        pool=self.pool(self.tiered())
        self.assertEqual((pool.attribute,pool.talent,pool.skill,pool.specialty),
                         (1,0,5,4))
        self.assertEqual(pool.dice,10)

    def test_one_governing_die_required_for_skill(self):
        with self.assertRaisesRegex(ValueError,"Attribute die"):
            self.pool(self.tiered(attribute={0:25,1:4}))

    def test_one_skill_die_required_for_specialty(self):
        with self.assertRaisesRegex(ValueError,"Skill die"):
            self.pool(self.tiered(skill={0:25,1:4}))

    def test_talent_has_no_gate_and_can_have_more_dice(self):
        pool=self.pool(self.tiered(talent={0:25,1:25}))
        self.assertEqual(pool.dice,15)
        # A Talent cannot rescue a Tier 1 Skill with zero Tier 1 Attribute dice.
        with self.assertRaisesRegex(ValueError,"Attribute die"):
            self.pool(self.tiered(attribute={0:25,1:4},talent={0:25,1:25}))

    def test_lower_tier_stays_available_and_dice_not_borrowed(self):
        ratings=self.tiered(attribute={0:25,1:5},skill={0:25,1:5},
                            specialty={0:25,1:0})
        self.assertEqual(self.pool(ratings,tier=0).dice,20)
        self.assertEqual(self.pool(ratings,tier=1).dice,2)

    def test_cannot_purchase_next_tier_until_previous_max(self):
        with self.assertRaisesRegex(ValueError,"prior Tier"):
            validate_tier_ratings({0:24,1:0})
        with self.assertRaisesRegex(ValueError,"skip"):
            validate_tier_ratings({0:25,2:1})
        validate_tier_ratings({0:25,1:25,2:5})
        with self.assertRaisesRegex(ValueError,"prior Tier"):
            spend_tier_xp_tenths({0:24},1,100000)
        bought,left=spend_tier_xp_tenths({0:25},1,1000)
        self.assertEqual((bought,left),({0:25,1:1},0))
        self.assertEqual(xp_to_next_at_tier(20,0),200)
        self.assertEqual(xp_to_next_at_tier(20,1),2000)
        self.assertEqual(xp_to_next_at_tier(20,2),20000)

    def test_tier_awards_scale_once_and_respect_origin(self):
        ratings=self.tiered(attribute={0:25,1:5},talent={0:25},
                             skill={0:25,1:5},specialty={0:25,1:0})
        faces={"attribute":[10],"talent":[],"skill":[7],"specialty":[]}
        outcome=award_tier_roll_xp(faces,attribute_name="dexterity",
                 role="accuracy",tier=1,talent=self.talent,
                 skill_id="one_handed",ratings=ratings,specialty_declared=True)
        self.assertEqual(outcome.xp,{"attribute":40,"talent":0,
                                     "skill":50,"specialty":100})
        self.assertEqual(outcome.natural_tens,1)
        self.assertEqual(outcome.bootstrap_specialty_xp,100)
        # Note: specialty total is a 10× scaled bootstrap credit at Tier 1.
        self.assertEqual(outcome.xp["specialty"],100)

    def test_bootstrap_both_skill_and_specialty_in_new_tier(self):
        ratings=self.tiered(attribute={0:25,1:5},talent={0:25},
                            skill={0:25,1:0},specialty={0:25,1:0})
        outcome=award_tier_roll_xp(
                 {"attribute":[10],"talent":[],"skill":[],"specialty":[]},
                 attribute_name="dexterity",role="accuracy",tier=1,
                 talent=self.talent,skill_id="one_handed",ratings=ratings,
                 specialty_declared=True)
        self.assertEqual(outcome.xp,{"attribute":40,"talent":0,
                                    "skill":50,"specialty":100})

    def test_cascade_raw_xp_without_reapplying_success_multiplier(self):
        ratings=self.tiered(attribute={0:25},talent={0:25},
                            skill={0:15},specialty={0:5})
        result=cascade_xp_tenths(source="talent",amount_tenths=30,tier=0,
                  ratings=ratings,specialty_declared=True)
        self.assertEqual(result,("skill",30))
        self.assertEqual(cascade_xp_tenths(source="talent",amount_tenths=30,
                  tier=0,ratings=ratings,specialty_declared=True,choice="bank"),
                  ("talent",30))
        # At maxed Skill, continuation goes to its declared Specialty.
        ratings["skill"]={0:25}
        self.assertEqual(cascade_xp_tenths(source="attribute",
                  amount_tenths=40,tier=0,ratings=ratings,
                  specialty_declared=True),("specialty",40))
        self.assertEqual(cascade_xp_tenths(source="attribute",
                  amount_tenths=40,tier=0,ratings=ratings,
                  specialty_declared=False),("skill",40))

    def test_cascade_respects_unlocked_recipient_and_does_not_duplicate(self):
        ratings=self.tiered(attribute={0:25,1:25},talent={0:25,1:25},
                            skill={0:20},specialty={0:15})
        self.assertEqual(cascade_xp_tenths(source="talent",amount_tenths=10,
                  tier=1,ratings=ratings,specialty_declared=True),
                  ("attribute",10))
        # No transfer to the un-unlocked Tier 1 Skill (Tier 0 Skill <25).
        self.assertEqual(cascade_xp_tenths(source="attribute",amount_tenths=10,
                  tier=1,ratings=ratings,specialty_declared=True),
                  ("attribute",10))

    def test_passive_defense_half_pool_and_fractional_xp(self):
        involved={"agility":10,"talent":5,"dodge":5,"specialty":0}
        self.assertEqual(static_defense_value(involved),Fraction(2,1))
        self.assertEqual(passive_xp_tenths(involved),{
            "agility":10,"talent":5,"dodge":5,"specialty":0})
        self.assertEqual(passive_xp_tenths(involved,tier=1)["talent"],50)
        self.assertEqual(static_defense_value({"agility":5}),Fraction(1,2))
        self.assertEqual(passive_xp_tenths({"conviction":15},tier=0),
                         {"conviction":15})
        # 15 tenths is 1.5 XP for resisting real Mana Costs.

if __name__=="__main__":
    unittest.main()
