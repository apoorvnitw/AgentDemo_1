# 02 Pressure: requirements

- `kpa_to_psi(kpa)` and `psi_to_kpa(psi)` in `convert.py`.
- Pure functions, no I/O.
- Constant: 1 psi = 6.894757293168 kPa. Define it once as `KPA_PER_PSI`.
- Formulas: psi = kPa / KPA_PER_PSI; kPa = psi * KPA_PER_PSI.
- The core returns an unrounded float. Rounding to 2 decimals happens when output is formatted (CLI group), per `specs/tech-stack.md`.
- No range validation: negative pressures still convert (out of scope per `specs/mission.md`).

## Dispatch table
- `CONVERSIONS` in `convert.py` maps `(from_unit, to_unit)` to a function.
- Pairs: `("C", "F")`, `("F", "C")`, `("kPa", "psi")`, `("psi", "kPa")`.
- Keys use the canonical unit spellings above. Case-insensitive matching belongs to the CLI group.
- An unsupported pair is simply absent from the table. Reporting it as an error belongs to the error-handling group.

## Out of scope
- CLI, argparse, unit parsing, error handling.
- Changing the temperature functions.
