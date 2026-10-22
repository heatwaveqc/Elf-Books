import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from trait_pools import Talent
from perks import (
    PERSONAL_SOURCES,
    PerkRequirement, qualify_for_perk, resolve_perk_confirmations,
)


class ElfBooksPerkTests(unittest.TestCase):
    def setUp(self):
        self.warrior = Talent("Warrior", frozenset({
            "one_handed", "two_handed", "block", "heavy_armor", "athletics"
        }), 25)
        self.specialized = PerkRequirement(
            "Master Sword Technique", "strength", "one_handed",
            frozenset({"longswords", "axes"}), 76,
        )

    def qualifying(self, perk=None, *, att=25, skill_rating=25,
                   talent=None, specialty=None, skill="one_handed"):
        return qualify_for_perk(
            requirement=perk or self.specialized,
            attribute="strength", attribute_rating=att, skill=skill,
            skill_rating=skill_rating, talent=talent or self.warrior,
            specialty_ratings=specialty or {},
        )

    def test_master_perk_requires_both_talent_and_accepted_specialty(self):
        no_specialty = self.qualifying()
        self.assertEqual(no_specialty.total_rating, 75)
        self.assertFalse(no_specialty.meets_requirement)
        just_enough = self.qualifying(specialty={"longswords": 1})
        self.assertTrue(just_enough.meets_requirement)
        self.assertEqual(just_enough.total_rating, 76)
        self.assertEqual(just_enough.qualifying_specialty, "longswords")
        # Non-governed Skill cannot obtain a >75 requirement under Tier-0 caps.
        smithing = PerkRequirement(
            "Impossible Non-Talent Master", "strength", "smithing",
            frozenset({"metalwork"}), 76,
        )
        ungoverned = self.qualifying(
            perk=smithing, skill="smithing", specialty={"metalwork": 25}
        )
        self.assertEqual(ungoverned.total_rating, 75)
        self.assertFalse(ungoverned.meets_requirement)

    def test_51_requires_talent_or_relevant_specialty_without_talent(self):
        req = PerkRequirement(
            "Smithy Technique", "strength", "smithing",
            frozenset({"metalwork"}), 51,
        )
        ungoverned = self.qualifying(perk=req, skill="smithing")
        self.assertEqual(ungoverned.total_rating, 50)
        self.assertFalse(ungoverned.meets_requirement)
        trained = self.qualifying(
            perk=req, skill="smithing", specialty={"metalwork": 1}
        )
        self.assertEqual(trained.total_rating, 51)
        self.assertTrue(trained.meets_requirement)
        irrelevant = self.qualifying(
            perk=req, skill="smithing", specialty={"longswords": 25}
        )
        self.assertEqual(irrelevant.total_rating, 50)
        self.assertFalse(irrelevant.meets_requirement)

    def test_100_requires_four_maxed_relevant_sources(self):
        req = PerkRequirement(
            "Perfect Swordsman", "strength", "one_handed",
            frozenset({"longswords"}), 100,
        )
        maxed = self.qualifying(perk=req, specialty={"longswords": 25})
        self.assertTrue(maxed.meets_requirement)
        self.assertEqual(maxed.total_rating, 100)
        self.assertFalse(self.qualifying(
            perk=req, specialty={"longswords": 24}
        ).meets_requirement)

    def test_specialties_eligible_one_only_not_all_and_attribute_locked(self):
        req = PerkRequirement(
            "Expert Blade", "strength", "one_handed",
            frozenset({"longswords", "axes"}), 90,
        )
        qual = self.qualifying(
            perk=req, specialty={"longswords": 20, "axes": 10, "shortswords": 25}
        )
        self.assertEqual(qual.specialty_rating, 20)
        self.assertEqual(qual.total_rating, 95)
        self.assertEqual(qual.qualifying_specialty, "longswords")
        with self.assertRaises(ValueError):
            qualify_for_perk(
                requirement=req, attribute="dexterity", attribute_rating=25,
                skill="one_handed", skill_rating=25, talent=self.warrior,
                specialty_ratings={"longswords": 25},
            )
        with self.assertRaises(ValueError):
            PerkRequirement("Invalid", "strength", "one_handed", frozenset(), 101)

    def test_reconfirmation_awards_both_participants_but_not_gear(self):
        original = dict(
            attribute=[10, 10, 1, 1, 9], talent=[10, 1],
            skill=[1, 10], specialty=[], equipment=[10, 1, 10, 1],
        )
        actor = dict(attribute=[10, 8], talent=[2], skill=[10], specialty=[])
        defender = dict(attribute=[1, 4], talent=[10], skill=[1], specialty=[])
        awarded = resolve_perk_confirmations(
            original_roll=original, actor_ten_confirmations=actor,
            defender_one_confirmations=defender, defender_targeted=True,
        )
        self.assertEqual(
            (awarded.actor_points, awarded.defender_points,
             awarded.actor_confirmation_attempts, awarded.defender_confirmation_attempts),
            (2, 2, 4, 4),
        )
        # Natural 10s/1s on equipment contribute no character perk opportunities.
        without_gear = {key: original[key] for key in PERSONAL_SOURCES}
        self.assertEqual(awarded, resolve_perk_confirmations(
            original_roll=without_gear, actor_ten_confirmations=actor,
            defender_one_confirmations=defender, defender_targeted=True,
        ))

    def test_actor_can_earn_multiple_and_defender_needs_actual_target(self):
        original = dict(
            attribute=[10, 10, 10, 1, 1, 1], talent=[],
            skill=[], specialty=[], equipment=[10, 1],
        )
        actor = dict(attribute=[10, 10, 10], talent=[], skill=[], specialty=[])
        defender = dict(attribute=[1, 1, 1], talent=[], skill=[], specialty=[])
        awarded = resolve_perk_confirmations(
            original_roll=original, actor_ten_confirmations=actor,
            defender_one_confirmations=defender, defender_targeted=True,
        )
        self.assertEqual((awarded.actor_points, awarded.defender_points), (3, 3))
        self.assertEqual(resolve_perk_confirmations(
            original_roll=original, actor_ten_confirmations=actor
        ).defender_points, 0)
        with self.assertRaisesRegex(ValueError, "genuine targeted defender"):
            resolve_perk_confirmations(
                original_roll=original, actor_ten_confirmations=actor,
                defender_one_confirmations=defender,
            )

    def test_confirmation_validation_does_not_allow_free_fake_ones_or_tens(self):
        original = dict(
            attribute=[10, 1], talent=[], skill=[], specialty=[], equipment=[10, 1]
        )
        actor = dict(attribute=[10], talent=[], skill=[], specialty=[])
        defender = dict(attribute=[1], talent=[], skill=[], specialty=[])
        checks = [
            dict(actor_ten_confirmations=dict(
                attribute=[10, 10], talent=[], skill=[], specialty=[])),
            dict(defender_one_confirmations=dict(
                attribute=[1, 1], talent=[], skill=[], specialty=[])),
            dict(actor_ten_confirmations=dict(
                attribute=[10], talent=[], skill=[], specialty=[], equipment=[10])),
            dict(defender_one_confirmations=dict(
                attribute=[1], talent=[], skill=[], specialty=[], equipment=[1])),
            dict(actor_ten_confirmations=dict(
                attribute=[True], talent=[], skill=[], specialty=[])),
        ]
        for change in checks:
            args=dict(
                original_roll=original, actor_ten_confirmations=actor,
                defender_one_confirmations=defender, defender_targeted=True,
            )
            args.update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                resolve_perk_confirmations(**args)

    def test_chance_is_one_percent_per_personal_die(self):
        # For one d10: P(original 10 and reroll 10) = 1/10 * 1/10.
        outcomes = [(x, y) for x in range(1, 11) for y in range(1, 11)]
        self.assertEqual(sum(x == 10 and y == 10 for x, y in outcomes), 1)
        self.assertEqual(sum(x == 1 and y == 1 for x, y in outcomes), 1)
        self.assertAlmostEqual(1 - 0.99 ** 20, 0.18209306240276923)


if __name__ == "__main__":
    unittest.main()
