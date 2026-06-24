import subprocess
import sys
import unittest
from pathlib import Path


class ExampleScriptsTestCase(unittest.TestCase):
    def test_load_mod_from_source_code_runs_successfully(self):
        repo_root = Path(__file__).resolve().parents[1]
        script = repo_root / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(script)],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.stdout, "loaded value\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
