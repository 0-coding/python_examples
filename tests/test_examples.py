import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source"


class ExampleScriptTestCase(unittest.TestCase):
    def test_example_scripts_run_successfully(self):
        scripts = [
            path
            for path in sorted(SOURCE_DIR.glob("*.py"))
            if path.read_text(encoding="utf-8").strip()
        ]

        for script in scripts:
            with self.subTest(script=script.name):
                result = subprocess.run(
                    [sys.executable, str(script)],
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )

                self.assertEqual(
                    result.returncode,
                    0,
                    result.stderr or result.stdout,
                )


if __name__ == "__main__":
    unittest.main()
