# Acceptance record

Checks the original brief (`docs/brief.md`) against the delivered tool.

> A command-line converter for bench work: temperatures between C and F, pressures between kPa and psi. Usage: python convert.py VALUE FROM TO. Wrong input must give a clear error, not a traceback.

## Requirements against evidence

| # | Requirement from the brief | Result | Evidence |
|---|---|---|---|
| 1 | Convert temperature C to F and F to C | Met | `tests/test_temperature.py` (14 tests); `100 C F` gives `212.00`, `98.6 F C` gives `37.00` |
| 2 | Convert pressure kPa to psi and psi to kPa | Met | `tests/test_pressure.py` (14 tests); `101.325 kPa psi` gives `14.70`, `30 psi kPa` gives `206.84` |
| 3 | Usage is `python convert.py VALUE FROM TO` | Met | `tests/test_cli.py` (15 tests), including a run of the script as a subprocess |
| 4 | Wrong input gives a clear error | Met | `tests/test_errors.py` (31 tests): 14 kinds of bad input each print one `error: ...` line to stderr and exit 1 |
| 5 | Wrong input never shows a traceback | Met | Every error test asserts `Traceback` is absent from stderr; stdout is empty on error |

## Reference conversions

All 7 rows of `answer_keys/conversion.csv` pass. `tests/test_answer_keys.py` (9 tests) runs each row through the real command line and compares the output text to the expected value.

| Value | From | To | Expected | Result |
|---|---|---|---|---|
| 100 | C | F | 212.00 | Pass |
| 0 | C | F | 32.00 | Pass |
| -40 | C | F | -40.00 | Pass |
| 36.6 | C | F | 97.88 | Pass |
| 98.6 | F | C | 37.00 | Pass |
| 101.325 | kPa | psi | 14.70 | Pass |
| 30 | psi | kPa | 206.84 | Pass |

That test was also checked to be able to fail: temporarily changing the kPa/psi constant made exactly the two pressure rows fail, and the temperature rows kept passing.

## Test run

`python -m pytest` reports **83 passed** (14 temperature, 14 pressure, 15 command line, 31 errors, 9 answer key).

Environment: Python 3.14.7, pytest 9.2.0, Windows 11.

## Decisions the brief left open

| Topic | What the tool does |
|---|---|
| Same-unit conversion (`C C`) | Error: unsupported pair |
| Values below absolute zero, negative pressure | Converted, not rejected |
| Output format | Bare number, 2 decimals, one line; negative zero is shown as `0.00` |
| Unit spelling | Case-insensitive |
| `nan`, `inf`, and results too large to represent | Error |
| psi/kPa factor | 1 psi = 6.894757293168 kPa |

## Not covered

- Python versions other than 3.14.7, and operating systems other than Windows, were not tested.
- The tool has no installer or packaging; it is run directly as `python convert.py`.
