# 02 Pressure: validation

Pass when `pytest` is green and `tests/test_pressure.py` contains these cases. The existing temperature tests must still pass.

## Answer-key rows
Hard-coded here; group 5 reads the CSV. Check with `round(result, 2) == expected`.
- 101.325 kPa -> 14.70 psi
- 30 psi -> 206.84 kPa

## Zero and negative
- 0 kPa -> 0 psi
- 0 psi -> 0 kPa
- -10 kPa converts to a negative psi value, with no exception.

## Constant
- `KPA_PER_PSI` equals 6.894757293168.
- 1 psi -> 6.894757293168 kPa (`pytest.approx`).

## Round-trip
- `psi_to_kpa(kpa_to_psi(x))` equals x within `pytest.approx`, for several x.

## Dispatch table
- `CONVERSIONS` has exactly four keys: `("C", "F")`, `("F", "C")`, `("kPa", "psi")`, `("psi", "kPa")`.
- Each entry is the matching function: `CONVERSIONS[("kPa", "psi")](101.325)` equals `kpa_to_psi(101.325)`.
- `("C", "psi")` is not in the table.

## Guard rails
- `answer_keys/` has no diff.
- `convert.py` has no I/O and no argparse.
- The temperature functions are unchanged.
