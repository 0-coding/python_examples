import contextlib
import io
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class ExampleScriptTests(unittest.TestCase):
    def test_load_mod_from_source_code_runs(self):
        stream = io.StringIO()

        with contextlib.redirect_stdout(stream):
            runpy.run_path(
                str(ROOT / "source" / "load_mod_from_source_code.py"),
                run_name="__main__",
            )

        self.assertEqual("b\n", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
