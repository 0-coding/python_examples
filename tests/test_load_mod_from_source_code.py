import subprocess
import sys
import unittest
from pathlib import Path


class LoadModuleFromSourceCodeTest(unittest.TestCase):
    def test_example_script_runs_successfully(self):
        script_path = (
            Path(__file__).resolve().parents[1]
            / "source"
            / "load_mod_from_source_code.py"
        )

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            check=False,
            text=True,
        )

        self.assertEqual("", result.stderr)
        self.assertEqual(0, result.returncode)
        self.assertEqual("b\n", result.stdout)


if __name__ == "__main__":
    unittest.main()
