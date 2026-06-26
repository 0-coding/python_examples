import subprocess
import sys
import unittest
from pathlib import Path


class ExampleScriptTests(unittest.TestCase):
    def test_load_mod_from_source_code_runs_successfully(self):
        repo_root = Path(__file__).resolve().parents[1]
        script = repo_root / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual("b\n", result.stdout)


if __name__ == "__main__":
    unittest.main()
