import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SourceCodeExampleTestCase(unittest.TestCase):
    def test_load_mod_from_source_code_runs_successfully(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "source" / "load_mod_from_source_code.py")],
            capture_output=True,
            check=False,
            text=True,
        )

        self.assertEqual("", result.stderr)
        self.assertEqual(0, result.returncode)
        self.assertEqual("b\n", result.stdout)


if __name__ == "__main__":
    unittest.main()
