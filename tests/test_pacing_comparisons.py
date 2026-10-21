import sys
import unittest
from random import Random
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from pacing_comparisons import CASES,goal_tenths,combat,quick,project,compare

class SoloPacingTests(unittest.TestCase):
    def test_xp_goals(self):
        self.assertEqual([goal_tenths(x.skill)//10 for x in CASES],[550,1300,2425])
        with self.assertRaises(ValueError):
            goal_tenths(99)

    def test_reproducible_nonempty_runs(self):
        for c in CASES:
            self.assertEqual(combat(c,Random(12)),combat(c,Random(12)))
            self.assertGreater(quick(c,Random(12)),0)
            weeks,projects=project(c,Random(12))
            self.assertGreaterEqual(weeks,projects)
            self.assertGreaterEqual(projects,1)

    def test_much_larger_projects_need_fewer_chat_summaries(self):
        c=CASES[2]
        a=project(c,Random(123),1000)
        b=project(c,Random(123),6000)
        self.assertGreater(a[1],b[1])

    def test_calibration_bands(self):
        rows=compare(trials=1000,seed=52)
        for item,cb,qb,wb,projects in zip(rows,
            [(39,53),(56,74),(65,85)],
            [(20,31),(34,46),(52,67)],
            [(25,40),(30,46),(39,60)],
            [6,6,5]):
            self.assertLess(cb[0],item["combat_rounds"])
            self.assertGreater(cb[1],item["combat_rounds"])
            self.assertLess(qb[0],item["quick_checks"])
            self.assertGreater(qb[1],item["quick_checks"])
            self.assertLess(wb[0],item["matched_project_weeks"])
            self.assertGreater(wb[1],item["matched_project_weeks"])
            self.assertEqual(item["matched_project_summaries"],projects)

if __name__=="__main__":
    unittest.main()
