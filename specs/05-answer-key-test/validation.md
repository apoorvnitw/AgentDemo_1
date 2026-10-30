# 05 Answer-key test: validation

Pass when `pytest` is green and `tests/test_answer_keys.py` contains these checks. Existing tests must still pass.

## Per-row check
- Every row of `answer_keys/conversion.csv` becomes one test case, run through the CLI as a subprocess.
- For each row: exit code 0, empty stderr, and stdout equals `expected` plus a newline.

## File checks
- The CSV has the header `value,from,to,expected`.
- The CSV has at least one data row (the test must not pass by running zero cases).

## Test can fail (mutation check, done by hand and not committed)
- With `KPA_PER_PSI` temporarily changed, the `kPa`/`psi` rows fail and the temperature rows still pass.
- After `git checkout convert.py`, `pytest` is green again.

## Guard rails
- `answer_keys/` has no diff.
- `convert.py` has no diff relative to `main` at the end of this phase.
