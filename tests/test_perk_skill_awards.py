"""Perk-generated dice retain provenance but score as Skill dice for rewards."""
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from advancement import award_roll_xp, award_tier_roll_xp
from perks import resolve_perk_confirmations
from trait_pools import Talent


class PerkSkillAwards(unittest.TestCase):
    def test_finesse_faces_give_skill_xp_and_actor_defender_confirmations(self):
        # One base Attribute die, one Talent, one Skill; bonus perk dice
        # from an independently validated Finesse margin.
        rolls=dict(attribute=[8], talent=[7], skill=[3],
                   specialty=[], perk_skill=[10, 1, 7, 4, 10],
                   equipment=[10, 1])
        ratings=dict(attribute=5,talent=5,skill=5,specialty=0)
        result=award_roll_xp(
            rolls,ratings,talent_governs=True,specialty_declared=False)
        # Perk dice contribute 2 + 0 + 1 + 0 + 2 = FIVE Skill successes.
        self.assertEqual(result.xp["skill"],25)
        self.assertEqual(result.xp["attribute"],2)
        self.assertEqual(result.xp["talent"],1)
        self.assertEqual(result.natural_tens,3) # two perk, one gear
        rewards=resolve_perk_confirmations(
            original_roll=rolls,
            actor_ten_confirmations=dict(
                attribute=[],talent=[],skill=[],specialty=[],
                perk_skill=[10,2]),
            defender_one_confirmations=dict(
                attribute=[],talent=[],skill=[],specialty=[],
                perk_skill=[1]),
            defender_targeted=True,
        )
        self.assertEqual((rewards.actor_points,rewards.defender_points),(1,1))
        self.assertEqual((rewards.actor_confirmation_attempts,
                          rewards.defender_confirmation_attempts),(2,1))

    def test_perk_faces_can_bootstrap_undeveloped_skill_specialty(self):
        rolls=dict(attribute=[6],talent=[],skill=[],specialty=[],
                   perk_skill=[10,7],equipment=[10])
        result=award_roll_xp(
            rolls,dict(attribute=5,talent=0,skill=0,specialty=0),
            talent_governs=False,specialty_declared=True)
        # Two scored perk Skill successes (10=2,7=1) = 15 XP PLUS
        # two natural-10 surrogate bootstrap awards (1 from gear).
        self.assertEqual(result.xp["skill"],25)
        self.assertEqual(result.bootstrap_skill_xp,10)
        self.assertEqual(result.xp["specialty"],20)
        self.assertEqual(result.bootstrap_specialty_xp,20)
        self.assertEqual(result.natural_tens,2)

    def test_tier_award_applies_existing_multiplier_once(self):
        talent=Talent("Warrior",frozenset({
            "one_handed","two_handed","block","heavy_armor","athletics"}),25)
        ratings={
            "attribute":{0:25,1:5},
            "talent":{0:25,1:5},
            "skill":{0:25,1:5},
            "specialty":{0:25,1:5},
        }
        award=award_tier_roll_xp(
            dict(attribute=[7],talent=[5],skill=[7],specialty=[7],
                 perk_skill=[10,7],equipment=[10]),
            attribute_name="dexterity",role="accuracy",
            tier=1,talent=talent,skill_id="one_handed",
            ratings=ratings,specialty_declared=True)
        # Skill = base 1 success + perk (2+1) = 4, => 20 * 5 = 100.
        self.assertEqual(award.xp["skill"],100)
        self.assertEqual(award.xp["specialty"],50)
        self.assertEqual(award.natural_tens,2)

    def test_perk_source_requires_exactly_one_confirmation_per_face(self):
        orig=dict(attribute=[],talent=[],skill=[],specialty=[],
                  perk_skill=[1,10,10,7],equipment=[1,10])
        good_actor=dict(attribute=[],talent=[],skill=[],specialty=[],
                        perk_skill=[7,10])
        good_defender=dict(attribute=[],talent=[],skill=[],specialty=[],
                           perk_skill=[1])
        award=resolve_perk_confirmations(
            original_roll=orig,
            actor_ten_confirmations=good_actor,
            defender_one_confirmations=good_defender,
            defender_targeted=True)
        self.assertEqual((award.actor_points,award.defender_points),(1,1))
        for bad in (
            dict(attribute=[],talent=[],skill=[],specialty=[],perk_skill=[10]),
            dict(attribute=[],talent=[],skill=[],specialty=[],perk_skill=[10,10,10]),
            dict(attribute=[],talent=[],skill=[],specialty=[],perk_skill=[True,10]),
            dict(attribute=[],talent=[],skill=[],specialty=[],perk_skill=[10,10],
                 equipment=[10]),
        ):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                resolve_perk_confirmations(
                    original_roll=orig,actor_ten_confirmations=bad,
                    defender_one_confirmations=good_defender,defender_targeted=True)

    def test_equipment_only_roll_cannot_earn_character_perk_points(self):
        roll=dict(attribute=[],talent=[],skill=[],specialty=[],equipment=[10,1])
        confirmations=dict(attribute=[],talent=[],skill=[],specialty=[])
        p=resolve_perk_confirmations(
            original_roll=roll,actor_ten_confirmations=confirmations,
            defender_one_confirmations=confirmations,defender_targeted=True)
        self.assertEqual((p.actor_points,p.defender_points),(0,0))
        result=award_roll_xp(
            roll,dict(attribute=0,talent=0,skill=0,specialty=0),
            talent_governs=False,specialty_declared=True)
        # Pre-existing gear-ten bootstrap is a different, still-active rule.
        self.assertEqual(result.bootstrap_skill_xp,5)
        self.assertEqual(result.bootstrap_specialty_xp,10)


if __name__=="__main__":
    unittest.main()
