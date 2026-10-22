"""Regression tests: Elf Books keeps practice XP, Geard Lif core does not."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class AdvancementAdapterSplitTest(unittest.TestCase):
    def test_elf_books_rating_and_xp_profile(self):
        attributes = json.loads((ROOT / "rules/attributes.json").read_text(encoding="utf-8"))
        self.assertEqual(attributes["status"], "ELF_BOOKS_0_TO_25_USE_XP_ADAPTER")
        self.assertEqual(attributes["rating"]["min"], 0)
        self.assertEqual(attributes["rating"]["max"], 25)
        self.assertEqual(attributes["rating"]["dice_per_five"], 1)
        self.assertEqual(attributes["rating"]["starting_floor"], 5)
        self.assertEqual(attributes["rating"]["xp_per_success"], 2)
        self.assertEqual(attributes["adapter"]["base_core_trait_rating_range"], [0, 5])
        self.assertEqual(attributes["adapter"]["base_core_advancement"], "Drive Marks")
        self.assertEqual(attributes["adapter"]["rating_multiplier_vs_core"], 5)

    def test_pinned_source_is_historical_adapter_reference(self):
        manifest = json.loads((ROOT / "engine/geard-lif/UPSTREAM.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["source_repository"], "heatwaveqc/geard-lif")
        self.assertEqual(manifest["advancement_adapter"]["name"], "elf-books-use-xp-0-to-25")
        self.assertEqual(manifest["advancement_adapter"]["core_current"], "geard-lif-drive-marks-0-to-5")
        self.assertTrue(manifest["advancement_adapter"]["explicit_override_of_legacy_imported_advancement"])
        self.assertEqual(len(manifest["upstream_commit"]), 40)

    def test_elf_advancement_overrides_base(self):
        text = (ROOT / "rules/ADVANCEMENT.md").read_text(encoding="utf-8")
        self.assertIn("**0–25 integer rating**", text)
        self.assertIn("source", text.lower())
        self.assertIn("natural 10", text)
        self.assertIn("Drive Mark", text)


if __name__ == "__main__":
    unittest.main()
