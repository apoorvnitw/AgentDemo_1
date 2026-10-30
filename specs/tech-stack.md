# Tech stack

- Python 3.14, standard library only (argparse). No runtime dependencies.
- pytest 9.x for tests. `pytest.ini` sets `pythonpath = .`.

## Layout
- `convert.py` at the repo root.
- `tests/` for pytest tests.
- `scripts/` for helpers.
- `answer_keys/` is a read-only reference. Never edit it.

## Conventions
- Output is rounded to 2 decimals (e.g. `97.88`, `14.70`).
- Units are case-insensitive (`c`/`C`, `kpa`/`kPa`/`KPA`, `PSI`/`psi`).
- Errors go to stderr as `error: <message>` with exit code 1. Never a traceback.
