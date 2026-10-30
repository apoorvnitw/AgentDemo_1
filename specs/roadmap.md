# Roadmap

Task groups, implemented one at a time.

## 1. Conversion core
- Pure functions for C<->F and kPa<->psi.
- A unit-pair dispatch table.
- Tests for each pair.

## 2. CLI
- argparse with `VALUE FROM TO`.
- Case-insensitive units.
- Output rounded to 2 decimals.

## 3. Error handling
- Non-numeric value, unknown unit, unsupported pair (e.g. C to psi), wrong argument count.
- Each prints `error: ...` to stderr and exits 1, with no traceback.
- Tests run the CLI via subprocess.

## 4. Answer-key test
- pytest reads `answer_keys/conversion.csv` and checks every row end to end.
- The file is read only, never modified.
