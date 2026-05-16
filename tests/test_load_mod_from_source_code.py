import contextlib
import io
import runpy
import unittest
from pathlib import Path


class LoadModFromSourceCodeTest(unittest.TestCase):
    def test_example_executes_source_code_successfully(self):
        script_path = (
            Path(__file__).resolve().parents[1]
            / "source"
            / "load_mod_from_source_code.py"
        )
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            namespace = runpy.run_path(str(script_path))

        self.assertEqual("b\n", output.getvalue())
        self.assertEqual("b", namespace["my_name_space"]["a"])


if __name__ == "__main__":
    unittest.main()
