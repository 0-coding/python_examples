import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExampleScriptTestCase(unittest.TestCase):
    def run_script(self, relative_path):
        return subprocess.run(
            [sys.executable, str(ROOT / relative_path)],
            check=True,
            capture_output=True,
            text=True,
        )

    def test_load_mod_from_source_code_runs(self):
        result = self.run_script("source/load_mod_from_source_code.py")

        self.assertEqual("b\n", result.stdout)
        self.assertEqual("", result.stderr)

    def test_unittest_to_io_runs(self):
        result = self.run_script("source/unittest_to_io.py")

        self.assertIn("Ran 2 tests", result.stdout)
        self.assertIn("OK", result.stdout)
        self.assertEqual("", result.stderr)


if __name__ == "__main__":
    unittest.main()
