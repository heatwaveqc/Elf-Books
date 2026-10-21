"""Validation for TES perk sources/candidates (not approved perk implementations)."""
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TESPerkSurveyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=json.loads((ROOT/"design/tes_perk_candidates.json").read_text(encoding="utf8"))
        cls.roster=json.loads((ROOT/"design/skills_v2.json").read_text(encoding="utf8"))

    def test_all_current_24_skill_names_considered(self):
        skill_ids={s["id"] for s in self.roster["skills"]}
        survey_ids={p["skill"] for p in self.catalog["candidates"]}
        self.assertEqual(skill_ids,survey_ids)
        self.assertEqual(len(skill_ids),24)

    def test_categorization_and_source_links(self):
        candidates=self.catalog["candidates"]
        self.assertEqual(len(candidates),75)
        counts=Counter(p["fit"] for p in candidates)
        self.assertEqual(counts,{"direct":28,"convert":35,"reject":10,"missing":2})
        self.assertEqual(self.catalog["status"],"RESEARCH_CANDIDATES_NOT_PURCHASABLE")
        for p in candidates:
            with self.subTest(skill=p["skill"],perk=p["original"]):
                self.assertTrue(p["original"].strip())
                self.assertIn(p["fit"],self.catalog["fit_meanings"])
                self.assertTrue(p["source"].startswith("https://"))
                self.assertGreater(len(p["design_note"]),10)
                if p["minimum_skill"] is not None:
                    self.assertIs(type(p["minimum_skill"]),int)
                    self.assertTrue(0<=p["minimum_skill"]<=100)

    def test_provisional_perks_untouched_and_not_activated(self):
        self.assertEqual(sum(len(s["perks"]) for s in self.roster["skills"]),48)
        self.assertEqual(self.roster["status"],"CANDIDATE_NOT_YET_APPROVED")
        self.assertTrue(all(p["status"]=="design_only" for s in self.roster["skills"] for p in s["perks"]))
        surveyed={(p["skill"],p["original"]) for p in self.catalog["candidates"]}
        self.assertEqual(len(surveyed),len(self.catalog["candidates"]))

    def test_no_source_misrepresented_as_skyrim_for_missing_skills(self):
        entries={s:[] for s in ("unarmed","athletics","dodge","mysticism","survival","lore")}
        for p in self.catalog["candidates"]:
            if p["skill"] in entries:
                entries[p["skill"]].append(p)
        self.assertEqual(sum(p["fit"]=="missing" for v in entries.values() for p in v),2)
        self.assertTrue(all(p["fit"]!="direct" for p in entries["mysticism"]))

if __name__=="__main__":
    unittest.main()
