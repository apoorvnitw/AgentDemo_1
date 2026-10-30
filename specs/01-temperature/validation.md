# 01 Temperature: validation

Pass when `pytest` is green and `tests/test_temperature.py` contains these cases.

## Answer-key rows
Hard-coded here; group 5 reads the CSV. Check with `round(result, 2) == expected`.
- 100 C -> 212.00
- 0 C -> 32.00
- -40 C -> -40.00
- 36.6 C -> 97.88
- 98.6 F -> 37.00

## Negative and zero
- -40 C -> -40 F
- 0 C -> 32 F
- 32 F -> 0 C

## Float precision
- 36.6 C rounds to 97.88 (not 97.87 or 97.89).

## Round-trip
- `fahrenheit_to_celsius(celsius_to_fahrenheit(x))` equals x within `pytest.approx`, for several x.

## Absolute zero
- -273.15 C -> -459.67 F and back, with no exception.

## Guard rails
- `answer_keys/` has no diff.
- `convert.py` has no I/O and no argparse.
