import contextlib
import io
import pathlib
import runpy
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class ExampleScriptTests(unittest.TestCase):
    def test_load_mod_from_source_code_runs(self):
        stream = io.StringIO()

        with contextlib.redirect_stdout(stream):
            runpy.run_path(str(ROOT / "source" / "load_mod_from_source_code.py"))

        self.assertEqual("b\n", stream.getvalue())

    def test_unittest_to_io_runs(self):
        stream = io.StringIO()

        with contextlib.redirect_stdout(stream):
            runpy.run_path(
                str(ROOT / "source" / "unittest_to_io.py"), run_name="__main__"
            )

        self.assertIn("Test output", stream.getvalue())
        self.assertIn("OK", stream.getvalue())
