import subprocess
import sys
import unittest
from pathlib import Path


class LoadModuleFromSourceCodeTest(unittest.TestCase):
    def test_script_executes_source_and_prints_value(self):
        repo_root = Path(__file__).resolve().parents[1]
        script_path = repo_root / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "b\n")


if __name__ == "__main__":
    unittest.main()
