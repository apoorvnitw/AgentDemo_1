# 04 Error handling: validation

Pass when `pytest` is green and `tests/test_errors.py` contains these cases. Existing tests must still pass. All error tests run the CLI as a subprocess (`python convert.py ...`).

## For every bad input below
- Exit code is 1.
- stdout is empty.
- stderr is a single line starting with `error: `.
- stderr contains no `Traceback`.

## Inputs and expected message fragments
| Arguments | stderr contains |
|---|---|
| (none) | `required` |
| `100 C` | `required` |
| `100 C F extra` | `unrecognized` |
| `abc C F` | `VALUE must be a number, got 'abc'` |
| `"" C F` | `VALUE must be a number` |
| `nan C F` | `VALUE must be a finite number` |
| `inf C F` | `VALUE must be a finite number` |
| `-inf C F` | `VALUE must be a finite number` |
| `100 xyz F` | `unknown unit 'xyz'` |
| `100 C xyz` | `unknown unit 'xyz'` |
| `100 C psi` | `cannot convert C to psi` |
| `100 psi F` | `cannot convert psi to F` |
| `100 C C` | `cannot convert C to C` |
| `1e308 C F` | `result is out of range` |

## Other checks
- Units in an unsupported-pair message use canonical spelling: `100 c PSI` mentions `C to psi`.
- Calling `main([...])` with a bad input returns 1 and does not raise `SystemExit`.
- `--help` prints usage to stdout and exits 0.
- A valid command still exits 0 with empty stderr.

## Guard rails
- `answer_keys/` has no diff.
- The conversion functions and `CONVERSIONS` are unchanged.
