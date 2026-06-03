import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class SourceCodeLoadingExampleTest(unittest.TestCase):
    def test_load_mod_from_source_code_runs_successfully(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "source" / "load_mod_from_source_code.py")],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.stdout.strip(), "loaded from source code")


if __name__ == "__main__":
    unittest.main()
