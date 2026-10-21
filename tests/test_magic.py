import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from trait_pools import Talent
from magic import casting_pools,mana_cost_resistance,resolve_mana_cost,mana_cost_practice_xp,counterspell_avoidance

class MagicTests(unittest.TestCase):
    def setUp(self):
        self.talent=Talent("Mage",frozenset({"alteration","conjuration","destruction",
                                                "illusion","restoration"}),10)
        self.base=dict(talent={0:10},skill={0:15},specialty={0:5})
    def ratings(self,attribute):
        return dict(attribute={0:attribute},**self.base)

    def test_same_school_distinct_accuracy_and_potence_attribute(self):
        pools=casting_pools(tier=0,talent=self.talent,school_id="destruction",
            accuracy_ratings=self.ratings(15),potence_ratings=self.ratings(20))
        self.assertEqual((pools.accuracy_dice,pools.potence_dice),(9,10))

    def test_mana_cost_same_school_will_static_conviction_capacity(self):
        r=resolve_mana_cost(tier=0,cost_magnitude=2,
            will_tiers={0:10},school_skill_tiers={0:10},conviction_tiers={0:15})
        self.assertEqual((r.resistance_dice,r.effective_threshold,
                          r.mark_capacity_per_grade),(4,2,3))
        self.assertEqual(r.new_mana.marks,(0,1,0,0))
        self.assertEqual(r.new_mana.resilience,3)
        protected=resolve_mana_cost(tier=0,cost_magnitude=2,
            will_tiers={0:10},school_skill_tiers={0:10},conviction_tiers={0:15},
            robe_dice=2)
        self.assertEqual((protected.effective_threshold,protected.mark_capacity_per_grade),(3,3))
        self.assertEqual(protected.new_mana.marks,(1,0,0,0))

    def test_robe_never_reduces_cost_faces_or_increases_marks(self):
        natural=resolve_mana_cost(tier=0,cost_magnitude=4,will_tiers={0:15},
            school_skill_tiers={0:10},conviction_tiers={0:10})
        robe=resolve_mana_cost(tier=0,cost_magnitude=4,will_tiers={0:15},
            school_skill_tiers={0:10},conviction_tiers={0:10},robe_dice=1)
        self.assertEqual((natural.cost_magnitude,robe.cost_magnitude),(4,4))
        self.assertEqual((natural.mark_capacity_per_grade,robe.mark_capacity_per_grade),(2,2))
        self.assertGreater(robe.effective_threshold,natural.effective_threshold)

    def test_actual_school_training_without_robe_training(self):
        # Tier 0 rounds fractional passive XP UP for Will and School separately.
        self.assertEqual(mana_cost_practice_xp(tier=0,will_rating=5,
                                                school_skill_rating=5),
                         {"will":10,"school_skill":10})
        self.assertEqual(mana_cost_practice_xp(tier=1,will_rating=5,
                                                school_skill_rating=5),
                         {"will":50,"school_skill":50})

    def test_counterspell_mysticism_wits_not_alteration(self):
        t=Talent("Scholar",frozenset({"mysticism","lore","alchemy",
                                      "alteration","restoration"}),10)
        ratings=dict(attribute={0:15},talent={0:10},skill={0:10},specialty={0:0})
        self.assertEqual(counterspell_avoidance(tier=0,talent=t,ratings=ratings),3)
        self.assertEqual(counterspell_avoidance(tier=0,talent=self.talent,ratings=ratings),2)

    def test_zero_effective_threshold_not_silently_one(self):
        with self.assertRaisesRegex(ValueError,"zero Cost-resistance"):
            mana_cost_resistance(tier=0,will_tiers={0:5},
                                 school_skill_tiers={0:0})

    def test_tier_prereqs_apply_to_cost_resistance(self):
        with self.assertRaisesRegex(ValueError,"Will Attribute"):
            mana_cost_resistance(tier=1,will_tiers={0:25,1:4},
                                 school_skill_tiers={0:25,1:5})
        with self.assertRaisesRegex(ValueError,"budget"):
            mana_cost_resistance(tier=0,will_tiers={0:5},
                                 school_skill_tiers={0:5},robe_dice=3)

if __name__=="__main__":
    unittest.main()
