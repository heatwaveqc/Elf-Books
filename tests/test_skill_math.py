import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from skill_math import load_catalog, normalized_skills, skill_bonus, category_ecl, derived_pools, learn


class SkillsTest(unittest.TestCase):
    def test_catalog_names_categories_and_perks(self):
        data=load_catalog()
        ids=[s["id"] for s in data["entries"]]
        self.assertEqual(len(ids),52)
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual({c:sum(x["category"]==c for x in data["entries"]) for c in ("warrior","mage","rogue")},
                         {"warrior":19,"mage":9,"rogue":24})
        self.assertTrue(all(len(x["perks"])==2 for x in data["entries"]))
        self.assertEqual({p["unlocks_at"] for x in data["entries"] for p in x["perks"]}, {25,75})
        self.assertTrue(all(x["attribute"] in {"str","dex","con","int","wis","cha"} for x in data["entries"]))
        self.assertTrue(all(set(p["maps_to"]).issubset(set(ids)) for p in data["historical_names"].values()))
        self.assertTrue(all(a not in ids for a in data["historical_names"]))

    def test_conversion_and_inputs(self):
        self.assertEqual([skill_bonus(x) for x in (0,4,5,24,25,50,99,100)],[0,0,1,4,5,10,19,20])
        for illegal in (-1, 101, 20.5, True):
            with self.assertRaises(ValueError):
                skill_bonus(illegal)
        with self.assertRaises(ValueError):
            normalized_skills({"stealth":40})  # must use rated 'sneak'
        with self.assertRaises(ValueError):
            normalized_skills({"sneak":101})

    def test_category_cap_and_mix(self):
        self.assertEqual(category_ecl([100]),Fraction(5))
        self.assertEqual(category_ecl([100,100,100,100]),Fraction(20))
        self.assertEqual(category_ecl([100]*20),Fraction(20))
        self.assertEqual(category_ecl([]),Fraction(0))
        p=derived_pools({
            "one_handed":40,"block":30,"heavy_armor":20,
            "destruction":40,"restoration":20,
            "sneak":20,"speechcraft":20
        },2,3)
        self.assertEqual((p.warrior_ecl,p.mage_ecl,p.rogue_ecl),(Fraction(9,2),Fraction(3),Fraction(2)))
        self.assertEqual((p.health_ecl,p.magicka_ecl),(Fraction(11,2),Fraction(4)))
        self.assertEqual((p.health,p.magicka),(38,32))

    def test_rogue_only_is_half_both(self):
        r={x["id"]:100 for x in load_catalog()["entries"] if x["category"]=="rogue"}
        p=derived_pools(r,0,0)
        self.assertEqual(p.rogue_ecl,20)
        self.assertEqual(p.health_ecl,10)
        self.assertEqual(p.magicka_ecl,10)

    def test_mix_can_exceed_twenty_ecl(self):
        data=load_catalog()
        r={x["id"]:100 for x in data["entries"] if x["category"] in ("warrior","rogue")}
        self.assertEqual(derived_pools(r,0,0).health_ecl,30)

    def test_zero_skills_no_base_pool_yet(self):
        p=derived_pools({},3,2)
        self.assertEqual((p.health,p.magicka),(0,0))

    def test_learning_crit_and_practice(self):
        self.assertEqual(learn(50,0,0,20,25).skill,51)
        self.assertEqual(learn(1,0,3,12,15).skill,2)
        self.assertEqual(learn(3,1,3,12,15).progress,2)
        self.assertEqual(learn(3,2,3,12,15).skill,4)
        self.assertEqual(learn(3,2,3,11,15).progress,2)
        self.assertEqual(learn(99,98,0,20,99).skill,100)
        self.assertEqual(learn(100,0,0,20,15).skill,100)

    def test_learning_rejects_invalid_history(self):
        with self.assertRaises(ValueError):
            learn(15,15,1,14,15)
        with self.assertRaises(ValueError):
            learn(15,0,1,21,15)


if __name__=="__main__":
    unittest.main()
