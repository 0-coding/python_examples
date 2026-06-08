import contextlib
import io
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExampleScriptTests(unittest.TestCase):
    def test_load_mod_from_source_code_runs_and_prints_value(self):
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            runpy.run_path(
                ROOT / "source" / "load_mod_from_source_code.py",
                run_name="__main__",
            )

        self.assertEqual("loaded from source code\n", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
