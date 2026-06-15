import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = REPO_ROOT / "source"


class ExampleScriptTestCase(unittest.TestCase):
    def run_example(self, script_name):
        return subprocess.run(
            [sys.executable, str(SOURCE_DIR / script_name)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )

    def test_load_module_from_source_code_runs(self):
        result = self.run_example("load_mod_from_source_code.py")

        self.assertEqual(result.stdout, "b\n")
        self.assertEqual(result.stderr, "")

    def test_unittest_to_io_runs(self):
        result = self.run_example("unittest_to_io.py")

        self.assertIn("Test output\n", result.stdout)
        self.assertIn("Ran 2 tests", result.stdout)
        self.assertIn("OK", result.stdout)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
