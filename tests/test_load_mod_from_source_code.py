import subprocess
import sys
import unittest
from pathlib import Path


class LoadModuleFromSourceCodeTest(unittest.TestCase):
    def test_script_executes_source_code_and_prints_value(self):
        script = (
            Path(__file__).resolve().parents[1]
            / "source"
            / "load_mod_from_source_code.py"
        )

        completed = subprocess.run(
            [sys.executable, str(script)],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.stdout, "b\n")
        self.assertEqual(completed.stderr, "")


if __name__ == "__main__":
    unittest.main()
