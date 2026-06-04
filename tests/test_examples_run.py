import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ExampleScriptTestCase(unittest.TestCase):
    def run_example(self, relative_path):
        return subprocess.run(
            [sys.executable, str(REPO_ROOT / relative_path)],
            check=True,
            capture_output=True,
            text=True,
        )

    def test_load_mod_from_source_code_runs(self):
        result = self.run_example("source/load_mod_from_source_code.py")

        self.assertEqual("b", result.stdout.strip())

    def test_unittest_to_io_runs(self):
        result = self.run_example("source/unittest_to_io.py")

        self.assertIn("Ran 2 tests", result.stdout)
        self.assertIn("OK", result.stdout)


if __name__ == "__main__":
    unittest.main()
