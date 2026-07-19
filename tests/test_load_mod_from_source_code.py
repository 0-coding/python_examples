import subprocess
import sys
import unittest
from pathlib import Path


class LoadModuleFromSourceCodeTestCase(unittest.TestCase):
    def test_script_executes_source_in_namespace(self):
        project_root = Path(__file__).resolve().parents[1]
        script = project_root / "source" / "load_mod_from_source_code.py"

        result = subprocess.run(
            [sys.executable, str(script)],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "b\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
