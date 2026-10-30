import csv
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ANSWER_KEY = ROOT / "answer_keys" / "conversion.csv"


def load_rows():
    with open(ANSWER_KEY, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


FIELDNAMES, ROWS = load_rows()


def test_csv_has_expected_header():
    assert FIELDNAMES == ["value", "from", "to", "expected"]


def test_csv_has_data_rows():
    assert ROWS


@pytest.mark.parametrize(
    "row",
    ROWS,
    ids=[f"{r['value']}-{r['from']}-to-{r['to']}" for r in ROWS],
)
def test_answer_key_row(row):
    result = subprocess.run(
        [sys.executable, str(ROOT / "convert.py"), row["value"], row["from"], row["to"]],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == row["expected"] + "\n"
