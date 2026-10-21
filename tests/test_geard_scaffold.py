"""Safety tests for the Geard Lif local snapshot and GM template."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_scaffold import validate_scaffold

class GeardScaffoldValidation(unittest.TestCase):
    def test_clean_geard_migration_scaffold(self):
        self.assertEqual(validate_scaffold(ROOT),[])

    def _replica(self,root):
        dest=Path(root)/"copy"
        shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns(".git","__pycache__"))
        return dest

    def test_no_private_upstream_content_leak(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=self._replica(tmp)
            imported=dest/"engine/geard-lif/source/Resource_Tracks.tid"
            imported.write_text(imported.read_text().replace(
                "geard-audience: player","geard-audience: gm"),encoding="utf-8")
            self.assertTrue(any("player-audience" in e for e in validate_scaffold(dest)))

    def test_invalid_engine_template_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=self._replica(tmp)
            path=dest/"templates/campaign.json"
            v=json.loads(path.read_text())
            v["engine"]["id"]="d20"
            path.write_text(json.dumps(v))
            self.assertTrue(any("must use local Geard Lif" in e for e in validate_scaffold(dest)))

    def test_no_private_campaigns_on_public_main(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=self._replica(tmp)
            (dest/"campaigns").mkdir()
            self.assertTrue(any("public repo" in e for e in validate_scaffold(dest)))

if __name__=="__main__":
    unittest.main()
