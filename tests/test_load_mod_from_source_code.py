import contextlib
import io
import runpy
import unittest
from pathlib import Path


class LoadModuleFromSourceCodeTest(unittest.TestCase):
    def test_example_runs_and_prints_assigned_value(self):
        script_path = (
            Path(__file__).resolve().parents[1]
            / "source"
            / "load_mod_from_source_code.py"
        )
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            runpy.run_path(str(script_path), run_name="__main__")

        self.assertEqual("b\n", output.getvalue())


if __name__ == "__main__":
    unittest.main()
