import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from perk_points import (
    PerkBank,natural_critical_event,artifact_point,
    spend_perk_point,exceptional_direct_perk
)

class PerkPointRules(unittest.TestCase):
    def test_meaningful_successful_nat20_earns_shared_point(self):
        first=natural_critical_event(PerkBank(),event_id="attack-01",kind="own_attack",
                                     natural_roll=20,meaningful=True,succeeded=True)
        self.assertEqual((first.points,first.earned_total),(1,1))
        # Bank untyped points for different skill, after later leveling up.
        with self.assertRaises(ValueError):
            spend_perk_point(first,perk_id="restoration_25",required_rank=25,current_rank=20)
        purchased=spend_perk_point(first,perk_id="restoration_25",required_rank=25,current_rank=25)
        self.assertEqual(purchased.points,0)
        self.assertIn("restoration_25",purchased.owned_perks)

    def test_nat20_check_failing_dc_gets_no_critical_success_point(self):
        b=natural_critical_event(PerkBank(),event_id="check-high-dc",kind="own_skill_check",
                                 natural_roll=20,meaningful=True,succeeded=False)
        self.assertEqual(b.points,0)
        self.assertEqual(b.earned_total,0)

    def test_passive_defensive_nat1_is_point_not_skill_xp(self):
        b=natural_critical_event(PerkBank(),event_id="enemy-swing-1",kind="incoming_attack",
                                 natural_roll=1,meaningful=True)
        self.assertEqual(b.points,1)
        # Multiple relevant layers must never pay multiple points for same event.
        twice=natural_critical_event(b,event_id="enemy-swing-1",kind="incoming_attack",
                                     natural_roll=1,meaningful=True)
        self.assertEqual(twice.points,1)
        # Credible sparring is still real training.
        spar=natural_critical_event(twice,event_id="sparring-swing-2",kind="incoming_attack",
                                   natural_roll=1,meaningful=True)
        self.assertEqual(spar.points,2)

    def test_trivial_rolls_and_normal_misses_do_not_award(self):
        b=natural_critical_event(PerkBank(),event_id="trivial",kind="own_attack",
                                 natural_roll=20,meaningful=False,succeeded=True)
        b=natural_critical_event(b,event_id="normal-miss",kind="incoming_attack",
                                 natural_roll=5,meaningful=True)
        b=natural_critical_event(b,event_id="trivial-enemy",kind="incoming_attack",
                                 natural_roll=1,meaningful=False)
        self.assertEqual(b.points,0)

    def test_artifact_points_are_bankable_no_duplication(self):
        a=artifact_point(PerkBank(),event_id="artifact-quest-01")
        self.assertEqual(a.points,1)
        self.assertEqual(artifact_point(a,event_id="artifact-quest-01").points,1)

    def test_artifact_direct_grants_require_explicit_waiver(self):
        a=PerkBank()
        with self.assertRaises(ValueError):
            exceptional_direct_perk(a,event_id="relic-1",perk_id="special_perk",
                                    requirements_met=False)
        b=exceptional_direct_perk(a,event_id="relic-1",perk_id="special_perk",
                                  requirements_met=False,explicitly_waives_requirements=True)
        self.assertEqual(b.points,0)
        self.assertIn("special_perk",b.owned_perks)
        self.assertEqual(exceptional_direct_perk(b,event_id="relic-1",perk_id="special_perk",
                                  requirements_met=False,explicitly_waives_requirements=True),b)

    def test_qualifier_and_uniqueness_guardrails(self):
        with self.assertRaises(ValueError):
            natural_critical_event(PerkBank(),event_id="",kind="incoming_attack",
                                   natural_roll=1,meaningful=True)
        with self.assertRaises(ValueError):
            natural_critical_event(PerkBank(),event_id="e",kind="own_attack",
                                   natural_roll=21,meaningful=True,succeeded=True)
        a=artifact_point(PerkBank(),event_id="gift")
        b=spend_perk_point(a,perk_id="block_25",current_rank=25,required_rank=25)
        with self.assertRaises(ValueError):
            spend_perk_point(b,perk_id="block_25",current_rank=25,required_rank=25)

if __name__=="__main__":
    unittest.main()
