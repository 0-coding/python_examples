import contextlib
import io
import pathlib
import runpy
import unittest


class ExampleScriptTest(unittest.TestCase):
    def test_load_mod_from_source_code_runs(self):
        script_path = pathlib.Path(__file__).resolve().parents[1] / "source" / "load_mod_from_source_code.py"
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            runpy.run_path(str(script_path), run_name="__main__")

        self.assertEqual(output.getvalue(), "loaded from source code\n")


if __name__ == "__main__":
    unittest.main()
