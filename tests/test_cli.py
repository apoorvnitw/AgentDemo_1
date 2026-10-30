import subprocess
import sys
from pathlib import Path

import pytest

from convert import main

ROOT = Path(__file__).resolve().parent.parent


def run(capsys, *args):
    code = main(list(args))
    return code, capsys.readouterr().out


@pytest.mark.parametrize(
    "args, expected",
    [
        (("100", "C", "F"), "212.00"),
        (("-40", "C", "F"), "-40.00"),
        (("98.6", "F", "C"), "37.00"),
        (("101.325", "kPa", "psi"), "14.70"),
        (("30", "psi", "kPa"), "206.84"),
    ],
)
def test_happy_path(capsys, args, expected):
    code, out = run(capsys, *args)
    assert code == 0
    assert out == expected + "\n"


@pytest.mark.parametrize(
    "args",
    [("100", "c", "f"), ("100", "C", "f"), ("100", "c", "F")],
)
def test_temperature_units_case_insensitive(capsys, args):
    code, out = run(capsys, *args)
    assert code == 0
    assert out == "212.00\n"


@pytest.mark.parametrize(
    "args",
    [("101.325", "KPA", "PSI"), ("101.325", "kpa", "psi"), ("101.325", "kPa", "Psi")],
)
def test_pressure_units_case_insensitive(capsys, args):
    code, out = run(capsys, *args)
    assert code == 0
    assert out == "14.70\n"


def test_zero_result(capsys):
    _, out = run(capsys, "32", "F", "C")
    assert out == "0.00\n"


def test_negative_zero_is_printed_as_zero(capsys):
    _, out = run(capsys, "-0.001", "kPa", "psi")
    assert out == "0.00\n"


def test_output_is_one_line_with_two_decimals(capsys):
    _, out = run(capsys, "1", "psi", "kPa")
    assert out.count("\n") == 1
    assert len(out.strip().split(".")[1]) == 2


def test_script_entry_point():
    result = subprocess.run(
        [sys.executable, str(ROOT / "convert.py"), "100", "C", "F"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "212.00\n"
