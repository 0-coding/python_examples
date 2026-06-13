import subprocess
import sys
import unittest
from pathlib import Path


class LoadModuleFromSourceCodeExampleTest(unittest.TestCase):
    def test_example_runs_successfully(self):
        repo_root = Path(__file__).resolve().parents[1]
        example = repo_root / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(example)],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual("loaded from source code\n", result.stdout)
        self.assertEqual("", result.stderr)


if __name__ == "__main__":
    unittest.main()
