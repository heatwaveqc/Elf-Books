"""Structural and arithmetic tests of NON-OPERATIVE perk catalogue proposal."""
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

from trait_pools import Talent
from perks import PerkRequirement,qualify_for_perk
from perk_draft import finesse_potence,plan_free_reaction


class FullPerkDraftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/"design/PERK_CATALOG_DRAFT.json").read_text())
        cls.perks=cls.data["perks"]
        cls.by_id={p["id"]:p for p in cls.perks}
        cls.original=json.loads((ROOT/"design/tes_perk_seeds.json").read_text())["items"]

    def test_all_seventy_five_original_seeds_plus_five_new(self):
        self.assertEqual(self.data["status"],"DRAFT_FOR_REVIEW_NOT_ACTIVE")
        self.assertEqual(len(self.perks),80)
        self.assertEqual(len(self.by_id),80)
        self.assertEqual(len(self.original),75)
        for n,(proposal,seed) in enumerate(zip(self.perks,self.original),start=1):
            self.assertEqual(proposal["skill"],seed["skill"],msg=str(n))
            self.assertEqual(proposal["source_seed_index"],n)
            self.assertEqual(proposal["minimum_rating"],seed["original_game_skill_gate"]
                             if seed["original_game_skill_gate"] is not None else 50)
        self.assertEqual(
            [p["name"] for p in self.perks[75:]],
            ["Finesse","Light Footed","Shield Reflex",
             "Flowing Parry","Spell Synthesis"],
        )

    def test_every_draft_has_real_named_skill_attribute_and_specialties(self):
        attrs=json.loads((ROOT/"rules/attributes.json").read_text())
        attribute_ids={v for a in attrs["aspects"] for v in a["attributes"].values()}
        skills={x["id"] for x in json.loads((ROOT/"rules/skills.json").read_text())["skills"]}
        supported={"adopted_effect","draft","framework_needed","new_proposal"}
        for p in self.perks:
            with self.subTest(name=p["name"]):
                self.assertIn(p["skill"],skills)
                self.assertIn(p["attribute"],attribute_ids)
                self.assertTrue(0<=p["minimum_rating"]<=100)
                self.assertEqual(p["point_cost"],1)
                self.assertGreaterEqual(len(p["accepted_specialties"]),1)
                self.assertEqual(len(p["accepted_specialties"]),
                                 len(set(p["accepted_specialties"])))
                self.assertTrue(all(
                    isinstance(s,str) and s and s==s.lower()
                    for s in p["accepted_specialties"]))
                self.assertGreaterEqual(len(p["effect"]),35)
                self.assertIn(p["status"],supported)
                self.assertEqual(p["status"]=="framework_needed",
                                 p["dependency"] is not None)
        self.assertEqual(
            {p["skill"] for p in self.perks}, skills)
        self.assertEqual(
            {p["name"] for p in self.perks if p["status"]=="adopted_effect"},
            {"Power Bash","Dual Flurry","Deflect Arrows"}
        )

    def test_all_composite_gates_calculable_not_inventing_talent(self):
        warrior=Talent("Warrior",frozenset(
            {"one_handed","two_handed","block","heavy_armor","athletics"}),25)
        for p in self.perks:
            with self.subTest(name=p["name"]):
                req=PerkRequirement(p["name"],p["attribute"],p["skill"],
                                    frozenset(p["accepted_specialties"]),
                                    p["minimum_rating"])
                chosen=p["accepted_specialties"][0]
                no_specialty=qualify_for_perk(
                    requirement=req,attribute=p["attribute"],attribute_rating=25,
                    skill=p["skill"],skill_rating=25,talent=warrior,
                    specialty_ratings={})
                self.assertEqual(
                    no_specialty.total_rating,
                    75 if p["skill"] in warrior.governed_skills else 50,
                )
                maxed=qualify_for_perk(
                    requirement=req,attribute=p["attribute"],attribute_rating=25,
                    skill=p["skill"],skill_rating=25,talent=warrior,
                    specialty_ratings={chosen:25})
                self.assertEqual(
                    maxed.total_rating,
                    100 if p["skill"] in warrior.governed_skills else 75,
                )
                if p["minimum_rating"]>75:
                    self.assertFalse(no_specialty.meets_requirement)

    def test_finesse_excess_accuracy_transfers_to_potence_not_dice(self):
        hit=finesse_potence(
            accuracy_successes=8,static_avoidance=3,rolled_potence=4)
        self.assertEqual((hit.threshold_successes,hit.modified_potence,
                          hit.extra_dice),(5,9,0))
        matched=finesse_potence(
            accuracy_successes=3,static_avoidance=3,rolled_potence=4)
        self.assertEqual((matched.applied,matched.threshold_successes,
                          matched.modified_potence),(True,0,4))
        missed=finesse_potence(
            accuracy_successes=2,static_avoidance=3,rolled_potence=4)
        self.assertEqual((missed.applied,missed.modified_potence),(False,0))
        zero=finesse_potence(
            accuracy_successes=6,static_avoidance=4,rolled_potence=0)
        # An approved bridge can transform otherwise-zero Potence.
        self.assertEqual(zero.modified_potence,2)
        with self.assertRaises(ValueError):
            finesse_potence(
                accuracy_successes=-1,static_avoidance=3,rolled_potence=1)

    def test_three_free_reactions_cost_no_action_but_still_cost_fatigue(self):
        cases=(
            ("light_footed","dodge",dict(armor_encumbrance=3),6),
            ("shield_reflex","block",dict(defending_weapon_damage=1,
                                           defending_weapon_defense=3),3),
            ("flowing_parry","parry",dict(defending_weapon_damage=2,
                                           defending_weapon_defense=1),2),
        )
        for perk,method,kwargs,expected_hazard in cases:
            with self.subTest(perk=perk):
                reaction=plan_free_reaction(
                    perk_id=perk,method=method,already_used_this_round=False,
                    reaction_legal=True,**kwargs)
                self.assertEqual(reaction.actions_spent,0)
                self.assertEqual(reaction.fatigue_hazard_dice,expected_hazard)
                self.assertTrue(reaction.consumes_round_use)
                with self.assertRaisesRegex(ValueError,"already spent"):
                    plan_free_reaction(
                        perk_id=perk,method=method,already_used_this_round=True,
                        reaction_legal=True,**kwargs)
                with self.assertRaisesRegex(ValueError,"legal"):
                    plan_free_reaction(
                        perk_id=perk,method=method,already_used_this_round=False,
                        reaction_legal=False,**kwargs)
        with self.assertRaisesRegex(ValueError,"does not grant"):
            plan_free_reaction(
                perk_id="light_footed",method="parry",
                already_used_this_round=False,reaction_legal=True)

    def test_distinguish_compound_spell_perk_and_item_extra_effect(self):
        self.assertEqual(self.by_id["mysticism_spell_synthesis"]["skill"],"mysticism")
        self.assertEqual(self.by_id["enchanting_extra_effect"]["skill"],"enchanting")
        self.assertEqual(self.by_id["enchanting_extra_effect"]["status"],"framework_needed")
        self.assertEqual(self.by_id["smithing_arcane_blacksmith"]["status"],"framework_needed")
        self.assertIn("distinct",self.by_id["mysticism_spell_synthesis"]["effect"])
        self.assertIn("TWO",self.by_id["enchanting_extra_effect"]["effect"])


if __name__=="__main__":
    unittest.main()
