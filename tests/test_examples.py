import contextlib
import io
import runpy
from pathlib import Path
import unittest


class ExampleScriptTests(unittest.TestCase):
    def test_load_mod_from_source_code_runs(self):
        script_path = (
            Path(__file__).resolve().parents[1]
            / "source"
            / "load_mod_from_source_code.py"
        )

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            runpy.run_path(str(script_path))

        self.assertEqual("b\n", output.getvalue())


if __name__ == "__main__":
    unittest.main()
