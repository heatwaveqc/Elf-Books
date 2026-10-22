import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from combat_perks import (
    plan_power_bash, plan_deflect_arrows, plan_dual_flurry,
)
from perks import resolve_perk_confirmations
from trait_pools import Talent
from geard_core import Track, apply_resource_effect


class CombatPerkPilots(unittest.TestCase):
    def setUp(self):
        self.warrior=Talent("Warrior",frozenset({
            "one_handed","two_handed","block","heavy_armor","athletics"
        }),10)
        self.ratings={
            "attribute":{0:15},"talent":{0:10},
            "skill":{0:15},"specialty":{0:5},
        }

    def test_power_bash_strength_dice_and_exact_double_hazard(self):
        p=plan_power_bash(
            strength_rating=20,added_damage_dice=4,
            weapon_damage_rating=2,normal_fatigue_hazard_dice=2)
        self.assertEqual(p.technique_damage_dice,4)
        self.assertEqual(p.weapon_damage_bonus_with_bash,6)
        self.assertEqual(p.additional_fatigue_hazard_dice,8)
        self.assertEqual(p.total_fatigue_hazard_dice,10)
        self.assertEqual(p.technique_die_source,"perk")
        # Default Damage 0 simple melee still risks 8d extra fatigue.
        zero=plan_power_bash(
            strength_rating=20,added_damage_dice=4,
            weapon_damage_rating=0,normal_fatigue_hazard_dice=0)
        self.assertEqual((zero.weapon_damage_bonus_with_bash,
                          zero.total_fatigue_hazard_dice),(4,8))

    def test_power_bash_strength_cap_and_no_refund_on_miss(self):
        for strength,allowed in ((0,0),(4,0),(5,1),(10,2),(25,5)):
            with self.subTest(strength=strength):
                p=plan_power_bash(
                    strength_rating=strength,added_damage_dice=allowed,
                    weapon_damage_rating=1,normal_fatigue_hazard_dice=1)
                self.assertEqual(p.total_fatigue_hazard_dice,1+2*allowed)
                with self.assertRaisesRegex(ValueError,"cannot exceed"):
                    plan_power_bash(
                        strength_rating=strength,added_damage_dice=allowed+1,
                        weapon_damage_rating=1,normal_fatigue_hazard_dice=1)
        # The plan is settled when the attack is DECLARED, not after Accuracy.
        miss=plan_power_bash(
            strength_rating=20,added_damage_dice=3,
            weapon_damage_rating=1,normal_fatigue_hazard_dice=1)
        self.assertEqual(miss.total_fatigue_hazard_dice,7)
        for kw in (
            dict(strength_rating=-1,added_damage_dice=0,
                 weapon_damage_rating=1,normal_fatigue_hazard_dice=1),
            dict(strength_rating=26,added_damage_dice=0,
                 weapon_damage_rating=1,normal_fatigue_hazard_dice=1),
            dict(strength_rating=15,added_damage_dice=2,
                 weapon_damage_rating=1,normal_fatigue_hazard_dice=1,
                 muscle_powered_attack=False),
        ):
            with self.assertRaises(ValueError):
                plan_power_bash(**kw)

    def test_perk_bonus_dice_do_not_confirm_character_or_gear_perks(self):
        p=plan_power_bash(
            strength_rating=20,added_damage_dice=4,
            weapon_damage_rating=2,normal_fatigue_hazard_dice=2)
        self.assertEqual(p.technique_die_source,"perk")
        original={
            "attribute":[10],"talent":[],"skill":[],"specialty":[],
            "equipment":[10,10],
        }
        # The four perk dice aren't one of the four rated character
        # source categories, and equipment is also excluded.
        award=resolve_perk_confirmations(
            original_roll=original,
            actor_ten_confirmations={"attribute":[10],"talent":[],
                "skill":[],"specialty":[]})
        self.assertEqual(award.actor_points,1)
        self.assertEqual(award.actor_confirmation_attempts,1)

    def test_deflect_arrow_expands_parry_not_normal_action_budget(self):
        p=plan_deflect_arrows(
            projectile_kind="arrow",parrying_skill="one_handed",
            talent=self.warrior,tier=0,ratings=self.ratings,
            available_actions=1,parry_capable_weapon=True,
            weapon_damage_rating=2,weapon_defense_rating=3,
            specialty_declared=True,external_bonuses={"weapon":2})
        self.assertEqual((p.reaction_actions,p.fatigue_hazard_dice),(1,3))
        self.assertEqual((p.parry_pool.personal_dice,p.parry_pool.external_dice,
                          p.parry_pool.static_opposition),(9,2,5))
        self.assertEqual(p.parry_pool.skill,"one_handed")
        self.assertEqual(p.parry_pool.attribute,"dexterity")

    def test_deflect_arrows_not_bullets_ice_spears_free_reactions(self):
        kwargs=dict(
            parrying_skill="one_handed",talent=self.warrior,
            tier=0,ratings=self.ratings,available_actions=1,
            parry_capable_weapon=True,
            weapon_damage_rating=2,weapon_defense_rating=1,
        )
        for kind in ("bullet","ice_spear","direct_malediction","thrown"):
            with self.subTest(kind=kind),self.assertRaisesRegex(ValueError,"arrows only"):
                plan_deflect_arrows(projectile_kind=kind,**kwargs)
        with self.assertRaisesRegex(ValueError,"available combat action"):
            plan_deflect_arrows(projectile_kind="arrow",
                **{**kwargs,"available_actions":0})
        with self.assertRaisesRegex(ValueError,"real Parry mode"):
            plan_deflect_arrows(projectile_kind="arrow",
                **{**kwargs,"parry_capable_weapon":False})

    def test_dual_flurry_separate_attacks_normal_costs_one_action(self):
        p=plan_dual_flurry(
            primary_weapon_hazard_dice=2,
            secondary_weapon_hazard_dice=3,
            available_actions=3,two_ready_melee_weapons=True)
        self.assertEqual((p.attack_actions,p.strikes,p.fatigue_hazards),
                         (1,2,(2,3)))
        self.assertEqual(3*p.strikes,6)
        self.assertEqual(3*sum(p.fatigue_hazards),15) # 3 attack actions
        # The two costs are independent incidents: an already-exhausted
        # fast track redirects subsequent costs to paired slow track.
        f=Track(2,marks=(0,0,0,1))
        first=apply_resource_effect(
            aspect="body",requested_resource="fatigue",magnitude=6,
            fast=f,slow=Track(2))
        self.assertEqual(first.fast.marks,(0,0,0,2))
        self.assertFalse(first.redirected)
        second=apply_resource_effect(
            aspect="body",requested_resource="fatigue",magnitude=2,
            fast=first.fast,slow=first.slow)
        self.assertEqual(second.applied_resource,"injury")
        self.assertTrue(second.redirected)

    def test_dual_flurry_requires_ready_weapons_and_action(self):
        kwargs=dict(primary_weapon_hazard_dice=2,
                    secondary_weapon_hazard_dice=2,
                    available_actions=1,two_ready_melee_weapons=True)
        with self.assertRaisesRegex(ValueError,"two ready"):
            plan_dual_flurry(**{**kwargs,"two_ready_melee_weapons":False})
        with self.assertRaisesRegex(ValueError,"one available"):
            plan_dual_flurry(**{**kwargs,"available_actions":0})
        with self.assertRaises(ValueError):
            plan_dual_flurry(**{**kwargs,"secondary_weapon_hazard_dice":-1})


if __name__=="__main__":
    unittest.main()
