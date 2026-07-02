import subprocess
import sys
import unittest
from pathlib import Path


class LoadModFromSourceCodeTest(unittest.TestCase):
    def test_example_runs_and_prints_loaded_value(self):
        script_path = (
            Path(__file__).resolve().parents[1]
            / "source"
            / "load_mod_from_source_code.py"
        )

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(result.stdout, "b\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
