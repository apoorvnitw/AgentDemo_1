# 01 Temperature: requirements

- `celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)` in `convert.py`.
- Pure functions, no I/O.
- Formulas: F = C * 9/5 + 32; C = (F - 32) * 5/9.
- The core returns an unrounded float. Rounding to 2 decimals happens when output is formatted (CLI group), per `specs/tech-stack.md`.
- No range validation: values below absolute zero still convert (out of scope per `specs/mission.md`).

## Out of scope
- CLI, argparse, unit parsing, error handling.
- Pressure.
