import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ExampleScriptsTestCase(unittest.TestCase):
    def test_load_mod_from_source_code_runs(self):
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "source" / "load_mod_from_source_code.py")],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual("1\n", result.stdout)


if __name__ == "__main__":
    unittest.main()
