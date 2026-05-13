import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ExampleScriptTests(unittest.TestCase):
    def test_load_mod_from_source_code_runs_successfully(self):
        result = subprocess.run(
            [sys.executable, "source/load_mod_from_source_code.py"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "b\n")


if __name__ == "__main__":
    unittest.main()
