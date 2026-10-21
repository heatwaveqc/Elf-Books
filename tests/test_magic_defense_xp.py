import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from magic_defense_xp import (
  skill_rank_xp_tenths,outgoing_damage_xp_tenths,magicka_spend_xp_tenths,
  worn_armor_xp_tenths,protective_spell_hp_xp_tenths,credited_avoidance,split_effective_damage
)

class SharedMagicDefenseXP(unittest.TestCase):
    def test_rank_threshold_and_damage(self):
        self.assertEqual([skill_rank_xp_tenths(x) for x in (0,20,50,95)], [50,1000,2500,4750])
        self.assertEqual(outgoing_damage_xp_tenths(10),200)

    def test_casting_spends_once_and_utility_alternative(self):
        self.assertEqual(magicka_spend_xp_tenths(8),80)
        self.assertEqual(magicka_spend_xp_tenths(8,2),160)
        self.assertEqual(outgoing_damage_xp_tenths(12)+magicka_spend_xp_tenths(8),320)
        self.assertEqual(magicka_spend_xp_tenths(0),0)

    def test_wound_teaches_armor_and_ward_as_distinct_skills(self):
        self.assertEqual(worn_armor_xp_tenths(10),400)
        self.assertEqual(protective_spell_hp_xp_tenths(10),200)
        self.assertEqual(worn_armor_xp_tenths(10,False),0)
        self.assertEqual(protective_spell_hp_xp_tenths(10,False),0)

    def test_enemy_total_not_natural_face(self):
        credited=credited_avoidance(natural_attack_roll=13,attack_total=23,ac_without=18,ac_with=27)
        self.assertTrue(credited.happened)
        self.assertEqual(credited.xp_tenths,460)
        self.assertFalse(credited_avoidance(natural_attack_roll=13,attack_total=23,
                          ac_without=24,ac_with=27).happened)
        self.assertEqual(credited_avoidance(natural_attack_roll=1,attack_total=23,
                          ac_without=18,ac_with=27).xp_tenths,0)
        self.assertEqual(credited_avoidance(natural_attack_roll=20,attack_total=23,
                          ac_without=18,ac_with=27).xp_tenths,0)

    def test_defensive_layer_attribution_only_one_success(self):
        selected=credited_avoidance(natural_attack_roll=12,attack_total=24,ac_without=18,ac_with=27)
        spell=credited_avoidance(natural_attack_roll=12,attack_total=24,ac_without=27,ac_with=31)
        self.assertEqual((selected.xp_tenths,spell.xp_tenths),(480,0))
        selected2=credited_avoidance(natural_attack_roll=12,attack_total=29,ac_without=18,ac_with=27)
        spell2=credited_avoidance(natural_attack_roll=12,attack_total=29,ac_without=27,ac_with=31)
        self.assertEqual((selected2.xp_tenths,spell2.xp_tenths),(0,580))
        no_reaction=credited_avoidance(natural_attack_roll=12,attack_total=24,ac_without=18,ac_with=27,
                          method_legal=False)
        self.assertEqual(no_reaction.xp_tenths,0)

    def test_damage_source_split_respects_hp(self):
        share=split_effective_damage(12,[("one_handed",10),("destruction",6)])
        self.assertEqual(share,{"one_handed":10,"destruction":2})
        self.assertEqual(sum(share.values()),12)
        self.assertEqual(sum(outgoing_damage_xp_tenths(v) for v in share.values()),240)

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            worn_armor_xp_tenths(-1)
        with self.assertRaises(ValueError):
            credited_avoidance(natural_attack_roll=21,attack_total=33,ac_without=12,ac_with=23)
        with self.assertRaises(ValueError):
            credited_avoidance(natural_attack_roll=10,attack_total=33,ac_without=29,ac_with=23)
        with self.assertRaises(ValueError):
            magicka_spend_xp_tenths(-2)

if __name__=="__main__":
    unittest.main()
