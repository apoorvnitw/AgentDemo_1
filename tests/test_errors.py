import subprocess
import sys
from pathlib import Path

import pytest

from convert import main

ROOT = Path(__file__).resolve().parent.parent


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(ROOT / "convert.py"), *args],
        capture_output=True,
        text=True,
    )


BAD_INPUTS = [
    ((), "required"),
    (("100", "C"), "required"),
    (("100", "C", "F", "extra"), "unrecognized"),
    (("abc", "C", "F"), "VALUE must be a number, got 'abc'"),
    (("", "C", "F"), "VALUE must be a number"),
    (("nan", "C", "F"), "VALUE must be a finite number"),
    (("inf", "C", "F"), "VALUE must be a finite number"),
    (("-inf", "C", "F"), "VALUE must be a finite number"),
    (("100", "xyz", "F"), "unknown unit 'xyz'"),
    (("100", "C", "xyz"), "unknown unit 'xyz'"),
    (("100", "C", "psi"), "cannot convert C to psi"),
    (("100", "psi", "F"), "cannot convert psi to F"),
    (("100", "C", "C"), "cannot convert C to C"),
    (("1e308", "C", "F"), "result is out of range"),
]


@pytest.mark.parametrize("args, fragment", BAD_INPUTS)
def test_bad_input_is_a_clean_error(args, fragment):
    result = run_cli(*args)
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Traceback" not in result.stderr
    lines = result.stderr.strip().splitlines()
    assert len(lines) == 1
    assert lines[0].startswith("error: ")
    assert fragment in lines[0]


def test_unsupported_pair_uses_canonical_unit_names():
    result = run_cli("100", "c", "PSI")
    assert "cannot convert C to psi" in result.stderr


@pytest.mark.parametrize("args, _fragment", BAD_INPUTS)
def test_main_returns_1_without_raising(capsys, args, _fragment):
    assert main(list(args)) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.startswith("error: ")


def test_help_exits_zero_with_usage_on_stdout():
    result = run_cli("--help")
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()


def test_valid_command_has_empty_stderr():
    result = run_cli("100", "C", "F")
    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == "212.00\n"
