import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class LoadModFromSourceCodeTestCase(unittest.TestCase):
    def test_script_runs_and_prints_loaded_value(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "source" / "load_mod_from_source_code.py")],
            capture_output=True,
            check=False,
            text=True,
        )

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)
        self.assertEqual("b\n", result.stdout)


if __name__ == "__main__":
    unittest.main()
