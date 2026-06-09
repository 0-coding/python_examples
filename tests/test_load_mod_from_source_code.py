import subprocess
import sys
from pathlib import Path
from unittest import TestCase


class LoadModFromSourceCodeTest(TestCase):
    def test_script_executes_source_code_without_crashing(self):
        script = Path(__file__).resolve().parents[1] / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(script)],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "1\n")
