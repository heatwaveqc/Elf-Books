"""Structural smoke tests for the Elf-Books scaffold and preflight gate."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_scaffold import validate_campaign, validate_scaffold


class ScaffoldTest(unittest.TestCase):
    def test_templates_and_docs(self):
        self.assertEqual(validate_scaffold(ROOT), [])

    def sample(self, folder):
        path = Path(folder) / "elf-example1"
        (path / "gm").mkdir(parents=True)
        (path / "characters").mkdir()
        names = {
            "campaign.json": "campaign.json", "state.json": "state.json",
            "world.json": "world.json", "threads.json": "threads.json",
            "gm/secrets.json": "gm-secrets.json",
            "characters/test.json": "character.json",
        }
        for dest, template in names.items():
            obj = json.loads((ROOT / "templates" / template).read_text())
            if dest == "campaign.json":
                obj["id"] = "elf-example1"
            elif dest == "characters/test.json":
                obj["campaign_id"] = "elf-example1"
            else:
                obj["campaign_id"] = "elf-example1"
            (path / dest).write_text(json.dumps(obj), encoding="utf-8")
        (path / "events.jsonl").write_text("", encoding="utf-8")
        return path

    def test_incomplete_active_campaign_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.sample(tmp)
            camp_path = path / "campaign.json"
            obj = json.loads(camp_path.read_text())
            obj["status"] = "active"
            camp_path.write_text(json.dumps(obj))
            errors = validate_campaign(path)
            self.assertTrue(any("preflight" in e for e in errors))
            self.assertTrue(any("approved advancement model" in e for e in errors))

    def test_draft_campaign_structurally_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.sample(tmp)
            self.assertEqual(validate_campaign(path), [])

    def test_corrupted_event_sequence_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.sample(tmp)
            (path / "events.jsonl").write_text('{"seq":2}\n')
            self.assertTrue(any("event sequence" in e for e in validate_campaign(path)))


if __name__ == "__main__":
    unittest.main()
