import subprocess
import sys
from pathlib import Path
import unittest


class LoadModFromSourceCodeTestCase(unittest.TestCase):
    def test_example_executes_source_code_successfully(self):
        repo_root = Path(__file__).resolve().parents[1]
        script = repo_root / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "b\n")


if __name__ == "__main__":
    unittest.main()
