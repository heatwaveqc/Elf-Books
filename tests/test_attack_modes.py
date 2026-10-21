import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from trait_pools import Talent
from attack_modes import (compose_named_pool,compose_mode_defense,
                          valid_defense_choices,load_attack_modes)

class ModeAndGearTests(unittest.TestCase):
    def setUp(self):
        self.talent=Talent("Scout",frozenset({
            "archery","survival","athletics","dodge","lore"}),10)
    @staticmethod
    def ratings(attribute=10,skill=10,talent=10,specialty=5):
        return {"attribute":{0:attribute},"talent":{0:talent},
                "skill":{0:skill},"specialty":{0:specialty}}

    def test_every_named_response_uses_valid_attribute_and_24_skills(self):
        modes=load_attack_modes()
        catalog={s["id"] for s in json.loads((ROOT/"rules/skills.json").read_text())["skills"]}
        all_attributes={x for a in json.loads((ROOT/"rules/attributes.json").read_text())["aspects"]
                        for x in a["attributes"].values()}
        self.assertGreaterEqual(len(modes),9)
        for mode in modes.values():
            with self.subTest(mode=mode["id"]):
                self.assertTrue(mode["valid_defenses"])
                for defense in mode["valid_defenses"]:
                    self.assertIn(defense["attribute"],all_attributes)
                    self.assertIn(defense["skill"],catalog)
                    self.assertTrue(defense["condition"])

    def test_cold_environment_and_direct_freeze_share_resistance(self):
        environment=next(x for x in valid_defense_choices("cold_exposure")
                         if x["id"]=="endure_cold")
        curse=next(x for x in valid_defense_choices("direct_freezing_malediction")
                   if x["id"]=="endure_cold")
        self.assertEqual((environment["attribute"],environment["skill"]),
                         ("health","survival"))
        self.assertEqual((curse["attribute"],curse["skill"]),
                         ("health","survival"))
        for bad in ("dodge","block","parry_one_handed"):
            self.assertNotIn(bad,[x["id"] for x in valid_defense_choices("direct_freezing_malediction")])
            with self.assertRaisesRegex(ValueError,"not a legal defense"):
                compose_mode_defense(mode_id="direct_freezing_malediction",
                    defense_id=bad,tier=0,talent=self.talent,ratings=self.ratings())
        r=compose_mode_defense(mode_id="direct_freezing_malediction",
            defense_id="endure_cold",tier=0,talent=self.talent,ratings=self.ratings())
        # Health 2d + Survival 2d + Scout Talent 2d = 6d; no specialty.
        self.assertEqual((r.dice,r.static_opposition),(6,3))

    def test_ice_spear_and_arrow_not_parriable(self):
        for mid in ("launched_projectile","ice_spear_projectile"):
            ids={x["id"] for x in valid_defense_choices(mid)}
            self.assertIn("dodge",ids)
            self.assertIn("block",ids)
            self.assertFalse(any("parry" in x for x in ids))
        melee={x["id"] for x in valid_defense_choices("melee_contact")}
        self.assertIn("parry_one_handed",melee)

    def test_social_menus_are_method_specific(self):
        modes=load_attack_modes()
        for mid in ("social_persuasion","social_deception","social_intimidation","social_reputation"):
            m=modes[mid]
            self.assertEqual(m["kind"],"social")
            self.assertEqual(m["typical_target_track"],"attention")
            self.assertEqual(m["long_term_target_track"],"plasticity")
            self.assertGreaterEqual(len(m["valid_defenses"]),2)
            for defense in m["valid_defenses"]:
                self.assertNotIn(defense["skill"],{"block","dodge","one_handed"})
        r=compose_mode_defense(mode_id="social_intimidation",
            defense_id="stand_firm",tier=0,talent=self.talent,
            ratings=self.ratings(specialty=0))
        # Conviction 2d + Speechcraft 2d; no Scout talent
        self.assertEqual((r.dice,r.static_opposition),(4,2))

    def test_auto_talent_and_specialty(self):
        a=compose_named_pool(attribute="agility",skill="dodge",tier=0,
            talent=self.talent,ratings=self.ratings(),specialty_declared=True)
        b=compose_named_pool(attribute="agility",skill="dodge",tier=0,
            talent=self.talent,ratings=self.ratings(),specialty_declared=False)
        c=compose_named_pool(attribute="health",skill="block",tier=0,
            talent=self.talent,ratings=self.ratings(),specialty_declared=True)
        self.assertEqual((a.personal_dice,b.personal_dice,c.personal_dice),(7,6,5))

    def test_external_total_cap_includes_magical_buffs_and_enchantments(self):
        personal=compose_named_pool(attribute="agility",skill="dodge",tier=0,
            talent=self.talent,ratings=self.ratings(),specialty_declared=True)
        self.assertEqual(personal.personal_dice,7)
        buffed=compose_named_pool(attribute="agility",skill="dodge",tier=0,
            talent=self.talent,ratings=self.ratings(),specialty_declared=True,
            external_bonuses={"shield":2,"enchantment":3,"temporary_magic":1,
                              "ensorcellment":1})
        self.assertEqual((buffed.personal_dice,buffed.external_dice,buffed.dice,
                          buffed.static_opposition),(7,7,14,7))
        with self.assertRaisesRegex(ValueError,"aggregate"):
            compose_named_pool(attribute="agility",skill="dodge",tier=0,
                talent=self.talent,ratings=self.ratings(),specialty_declared=True,
                external_bonuses={"shield":2,"enchantment":3,"temporary_magic":2,
                                  "ensorcellment":1})

    def test_off_talent_and_unspecialized_capped_lower(self):
        r=compose_named_pool(attribute="conviction",skill="speechcraft",tier=0,
            talent=self.talent,ratings=self.ratings(specialty=0),
            external_bonuses={"charm":4})
        self.assertEqual((r.personal_dice,r.external_dice),(4,4))
        with self.assertRaisesRegex(ValueError,"aggregate"):
            compose_named_pool(attribute="conviction",skill="speechcraft",tier=0,
                talent=self.talent,ratings=self.ratings(specialty=0),
                external_bonuses={"charm":5})

    def test_reaction_availability_and_no_skill_to_skip_tier_gate(self):
        with self.assertRaisesRegex(ValueError,"unavailable"):
            compose_mode_defense(mode_id="launched_projectile",
                defense_id="block",tier=0,talent=self.talent,
                ratings=self.ratings(),response_available=False)
        with self.assertRaisesRegex(ValueError,"Attribute die"):
            compose_named_pool(attribute="health",skill="survival",tier=1,
                talent=self.talent,
                ratings={"attribute":{0:25,1:4},"talent":{0:25,1:15},
                         "skill":{0:25,1:10},"specialty":{0:25,1:10}},
                specialty_declared=True,external_bonuses={"magic_item":10})

    def test_zero_personal_cannot_be_amplified(self):
        t=Talent("Other",frozenset({
            "alchemy","conjuration","illusion","mysticism","restoration"}),0)
        with self.assertRaisesRegex(ValueError,"no available personal"):
            compose_named_pool(attribute="agility",skill="dodge",tier=0,
                talent=t,ratings=self.ratings(attribute=0,skill=0,talent=0,specialty=0),
                external_bonuses={"magic_buff":1})

if __name__=="__main__":
    unittest.main()
