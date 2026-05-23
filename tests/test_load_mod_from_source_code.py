import subprocess
import sys
import unittest
from pathlib import Path


class LoadModFromSourceCodeTestCase(unittest.TestCase):
    def test_example_runs_and_prints_loaded_value(self):
        repo_root = Path(__file__).resolve().parents[1]

        result = subprocess.run(
            [sys.executable, str(repo_root / "source" / "load_mod_from_source_code.py")],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual("", result.stderr)
        self.assertEqual(0, result.returncode)
        self.assertEqual("b\n", result.stdout)


if __name__ == "__main__":
    unittest.main()
