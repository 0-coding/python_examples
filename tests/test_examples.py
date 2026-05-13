import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_load_mod_from_source_code_runs_successfully():
    result = subprocess.run(
        [sys.executable, "source/load_mod_from_source_code.py"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "b\n"
