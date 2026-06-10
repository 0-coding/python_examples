import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExampleScriptTestCase(unittest.TestCase):
    def run_script(self, script_name):
        return subprocess.run(
            [sys.executable, str(ROOT / "source" / script_name)],
            check=True,
            capture_output=True,
            text=True,
        )

    def test_load_mod_from_source_code_runs(self):
        result = self.run_script("load_mod_from_source_code.py")

        self.assertEqual(result.stdout, "b\n")
        self.assertEqual(result.stderr, "")

    def test_load_mod_from_file_runs(self):
        result = self.run_script("load_mod_from_file.py")

        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
