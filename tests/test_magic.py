import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from trait_pools import Talent
from geard_core import Track
from geard_core import RESOURCE_TRACKS
from magic import (
    casting_pools,mana_cost_resistance,resolve_mana_cost,
    mana_cost_practice_xp,counterspell_avoidance
)

class MagicTests(unittest.TestCase):
    def setUp(self):
        self.talent=Talent("Mage",frozenset({
            "alteration","conjuration","destruction","illusion","restoration"}),10)
        self.base=dict(talent={0:10},skill={0:15},specialty={0:5})
    def ratings(self,attribute):
        return dict(attribute={0:attribute},**self.base)

    def cost(self,**kwargs):
        defaults=dict(tier=0,talent=self.talent,school_id="destruction",
            will_tiers={0:10},school_skill_tiers={0:10},talent_tiers={0:10},
            specialty_tiers={0:5},specialty_declared=True)
        defaults.update(kwargs)
        return resolve_mana_cost(**defaults)

    def test_resources_mind_magic_and_soul_social(self):
        self.assertEqual(RESOURCE_TRACKS["mind"],
            {"resilience":"will","slow":"spirit","fast":"mana"})
        self.assertEqual(RESOURCE_TRACKS["soul"],
            {"resilience":"conviction","slow":"plasticity","fast":"attention"})
        self.assertEqual(RESOURCE_TRACKS["body"],
            {"resilience":"health","slow":"injury","fast":"fatigue"})
        character=json.loads((ROOT/"templates/character.json").read_text())
        for aspect,spec in RESOURCE_TRACKS.items():
            self.assertEqual(set(character["resources"][aspect]),
                             {spec["slow"],spec["fast"]})
            for name in (spec["slow"],spec["fast"]):
                self.assertEqual(character["resources"][aspect][name],[0,0,0,0])

    def test_same_school_distinct_accuracy_and_potence_attribute(self):
        pools=casting_pools(tier=0,talent=self.talent,school_id="destruction",
            accuracy_ratings=self.ratings(15),potence_ratings=self.ratings(20))
        self.assertEqual((pools.accuracy_dice,pools.potence_dice),(9,10))

    def test_mana_cost_full_sources_and_will_capacity(self):
        r=self.cost(cost_magnitude=3)
        # Will 2d + Mage Talent 2d + Destruction 2d + Firebolt 1d = 7d.
        self.assertEqual((r.resistance_dice,r.effective_threshold,
                          r.mark_capacity_per_grade),(7,3,2))
        self.assertEqual(r.new_mana.marks,(0,1,0,0))
        self.assertEqual(r.new_mana.resilience,2)
        robe=self.cost(cost_magnitude=3,robe_dice=1)
        self.assertEqual((robe.resistance_dice,robe.effective_threshold,
                          robe.mark_capacity_per_grade),(8,4,2))
        self.assertEqual(robe.new_mana.marks,(1,0,0,0))
        self.assertEqual(robe.cost_magnitude,3)

    def test_talent_and_spell_specialty_each_reduce_cost(self):
        base=self.cost(cost_magnitude=3,specialty_declared=False,
                       talent_tiers={0:0})
        mage=self.cost(cost_magnitude=3,specialty_declared=False)
        specialized=self.cost(cost_magnitude=3)
        self.assertEqual([x.resistance_dice for x in (base,mage,specialized)],
                         [4,6,7])
        self.assertEqual([x.effective_threshold for x in (base,mage,specialized)],
                         [2,3,3])
        self.assertEqual([x.mark_capacity_per_grade for x in (base,mage,specialized)],
                         [2,2,2])
        # Higher relevant Specialty, unlike adding capacity, can further raise guard.
        specialist=self.cost(cost_magnitude=3,specialty_tiers={0:10})
        self.assertEqual(specialist.effective_threshold,4)
        self.assertEqual(specialist.new_mana.marks,(1,0,0,0))

    def test_outside_talent_still_casts_but_no_talent_cost_dice(self):
        r=mana_cost_resistance(tier=0,talent=self.talent,school_id="mysticism",
            will_tiers={0:10},school_skill_tiers={0:10},
            talent_tiers={0:10},specialty_tiers={0:5},
            specialty_declared=True)
        self.assertEqual(r,(5,2))
        self.assertEqual(mana_cost_practice_xp(tier=0,talent=self.talent,
            school_id="mysticism",will_rating=10,school_skill_rating=10,
            talent_rating=10,specialty_rating=5,specialty_declared=True),
            {"will":10,"school_skill":10,"specialty":10})

    def test_cost_passive_xp_all_sources_except_robes(self):
        xp=mana_cost_practice_xp(tier=0,talent=self.talent,school_id="destruction",
            will_rating=10,school_skill_rating=10,talent_rating=5,
            specialty_rating=5,specialty_declared=True)
        self.assertEqual(xp,{"will":10,"school_skill":10,"talent":10,"specialty":10})
        advanced=mana_cost_practice_xp(tier=1,talent=self.talent,
            school_id="destruction",will_rating=5,school_skill_rating=5,
            talent_rating=5,specialty_rating=5,specialty_declared=True)
        self.assertEqual(advanced,{"will":25,"school_skill":25,
                                   "talent":25,"specialty":25})

    def test_multi_source_buff_cap_across_spell_cast_and_cost(self):
        # Unmodified Cost personal = Will 2 + Mage 2 + School 2 + Specialty 1 = 7.
        combined=self.cost(cost_magnitude=4,robe_dice=2,
            external_bonuses={"enchantment":3,"temporary_magic":2})
        self.assertEqual(combined.resistance_dice,14)
        with self.assertRaisesRegex(ValueError,"aggregate"):
            self.cost(cost_magnitude=4,robe_dice=2,
                external_bonuses={"enchantment":3,"temporary_magic":3})
        accuracy=casting_pools(tier=0,talent=self.talent,school_id="destruction",
            accuracy_ratings=self.ratings(15),potence_ratings=self.ratings(20),
            accuracy_external_bonuses={"staff":5,"ensorcellment":4},
            potence_external_bonuses={"magic_focus":10})
        self.assertEqual((accuracy.accuracy_dice,accuracy.potence_dice),(18,20))
        with self.assertRaisesRegex(ValueError,"aggregate"):
            casting_pools(tier=0,talent=self.talent,school_id="destruction",
                accuracy_ratings=self.ratings(15),potence_ratings=self.ratings(20),
                accuracy_external_bonuses={"staff":6,"ensorcellment":4})

    def test_robe_never_reduces_rolled_cost_or_increases_slots(self):
        a=self.cost(cost_magnitude=8,robe_dice=0)
        b=self.cost(cost_magnitude=8,robe_dice=2)
        self.assertEqual((a.cost_magnitude,b.cost_magnitude),(8,8))
        self.assertEqual((a.mark_capacity_per_grade,b.mark_capacity_per_grade),(2,2))
        self.assertEqual((a.new_mana.resilience,b.new_mana.resilience),(2,2))

    def test_exhausted_mana_cost_redirects_into_spirit(self):
        mana=Track(2,marks=(0,0,0,2))
        spirit=Track(2)
        result=self.cost(cost_magnitude=3,existing_mana=mana,
                         existing_spirit=spirit,robe_dice=1)
        self.assertEqual(result.applied_resource,"spirit")
        self.assertTrue(result.redirected)
        self.assertEqual(result.new_mana,mana)
        # The former Mana Cost guard would have had threshold 4, but
        # the destination Spirit threshold defaults to Will-based 2.
        self.assertEqual(result.effective_threshold,2)
        self.assertEqual(result.new_spirit.marks,(0,1,0,0))
        self.assertEqual(result.cost_magnitude,3)
        self.assertEqual(result.mark_capacity_per_grade,2)

    def test_cost_that_exhausts_mana_does_not_double_hit_spirit(self):
        first=self.cost(cost_magnitude=12)
        self.assertTrue(first.new_mana.exhausted)
        self.assertEqual(first.new_spirit.marks,(0,0,0,0))
        self.assertFalse(first.redirected)
        second=self.cost(cost_magnitude=1,
                         existing_mana=first.new_mana,
                         existing_spirit=first.new_spirit)
        self.assertEqual(second.applied_resource,"spirit")
        self.assertEqual(second.new_spirit.marks,(1,0,0,0))
        third=self.cost(cost_magnitude=1,
                        existing_mana=first.new_mana.recover_step(),
                        existing_spirit=second.new_spirit)
        self.assertEqual(third.applied_resource,"mana")
        self.assertEqual(third.new_spirit,second.new_spirit)

    def test_saved_cost_state_requires_both_tracks(self):
        with self.assertRaisesRegex(ValueError,"both saved Mana and Spirit"):
            self.cost(cost_magnitude=1,existing_mana=Track(2))
        with self.assertRaisesRegex(ValueError,"both saved Mana and Spirit"):
            self.cost(cost_magnitude=1,existing_spirit=Track(2))

    def test_will_not_conviction_governs_mana_capacity(self):
        r=self.cost(cost_magnitude=1,will_tiers={0:15})
        self.assertEqual(r.mark_capacity_per_grade,3)
        # There is intentionally no Conviction parameter in this API.

    def test_counterspell_mysticism_wits(self):
        t=Talent("Scholar",frozenset({
            "mysticism","lore","alchemy","alteration","restoration"}),10)
        ratings=dict(attribute={0:15},talent={0:10},skill={0:10},specialty={0:0})
        self.assertEqual(counterspell_avoidance(tier=0,talent=t,ratings=ratings),3)
        self.assertEqual(counterspell_avoidance(tier=0,talent=self.talent,ratings=ratings),2)

    def test_zero_effective_threshold_preserved_as_open(self):
        with self.assertRaisesRegex(ValueError,"zero Cost-resistance"):
            mana_cost_resistance(tier=0,talent=self.talent,school_id="mysticism",
                will_tiers={0:5},school_skill_tiers={0:0},talent_tiers={0:0})

    def test_skill_specialty_tier_prerequisites(self):
        with self.assertRaisesRegex(ValueError,"Attribute die"):
            mana_cost_resistance(tier=1,talent=self.talent,school_id="destruction",
                will_tiers={0:25,1:4},school_skill_tiers={0:25,1:5},
                talent_tiers={0:25,1:5})
        with self.assertRaisesRegex(ValueError,"Skill die"):
            mana_cost_resistance(tier=1,talent=self.talent,school_id="destruction",
                will_tiers={0:25,1:5},school_skill_tiers={0:25,1:4},
                talent_tiers={0:25,1:5},specialty_tiers={0:25,1:5},
                specialty_declared=True)
        with self.assertRaisesRegex(ValueError,"aggregate"):
            mana_cost_resistance(tier=0,talent=self.talent,school_id="destruction",
                will_tiers={0:5},school_skill_tiers={0:5},
                talent_tiers={0:0},robe_dice=3)

if __name__=="__main__":
    unittest.main()
