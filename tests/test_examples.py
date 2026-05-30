import subprocess
import sys
import unittest
from pathlib import Path


class ExampleScriptTestCase(unittest.TestCase):
    def test_load_mod_from_source_code_runs_successfully(self):
        script = Path(__file__).resolve().parents[1] / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual("1\n", result.stdout)
        self.assertEqual("", result.stderr)


if __name__ == "__main__":
    unittest.main()
