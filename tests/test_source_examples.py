import io
import runpy
import unittest
from contextlib import redirect_stdout
from pathlib import Path


class SourceExampleTestCase(unittest.TestCase):
    def test_load_mod_from_source_code_runs(self):
        example_path = (
            Path(__file__).resolve().parents[1]
            / "source"
            / "load_mod_from_source_code.py"
        )

        output = io.StringIO()
        with redirect_stdout(output):
            runpy.run_path(str(example_path), run_name="__main__")

        self.assertEqual("b\n", output.getvalue())


if __name__ == "__main__":
    unittest.main()
