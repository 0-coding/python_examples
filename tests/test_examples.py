import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_load_mod_from_source_code_example_runs():
    result = subprocess.run(
        [sys.executable, str(ROOT / "source" / "load_mod_from_source_code.py")],
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout == "b\n"
    assert result.stderr == ""
