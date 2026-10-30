# 03 CLI: validation

Pass when `pytest` is green and `tests/test_cli.py` contains these cases. Existing tests must still pass.

## Happy path (call `main([...])` and read stdout with `capsys`)
- `100 C F` prints `212.00` and returns 0.
- `-40 C F` prints `-40.00` (negative VALUE is accepted).
- `98.6 F C` prints `37.00`.
- `101.325 kPa psi` prints `14.70`.
- `30 psi kPa` prints `206.84`.

## Case-insensitive units
- `100 c f`, `100 C f` and `100 c F` all print `212.00`.
- `101.325 KPA PSI` and `101.325 kpa psi` print `14.70`.

## Formatting
- Output is exactly one line with exactly 2 decimals.
- `32 F C` prints `0.00`.
- A tiny negative result prints `0.00`, not `-0.00` (e.g. `-0.001 kPa psi`).

## Script entry point
- Running `python convert.py 100 C F` as a subprocess prints `212.00` and exits 0.

## Guard rails
- `answer_keys/` has no diff.
- The conversion functions and `CONVERSIONS` are unchanged.
