import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExampleScriptTests(unittest.TestCase):
    def test_load_mod_from_source_code_runs(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "source" / "load_mod_from_source_code.py")],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "1\n")


if __name__ == "__main__":
    unittest.main()
