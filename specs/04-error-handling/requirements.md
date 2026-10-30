# 04 Error handling: requirements

Every bad input prints one line `error: <message>` to stderr, prints nothing to stdout, and exits 1. No traceback, ever (per `docs/brief.md` and `specs/tech-stack.md`).

## Cases and messages
- Wrong argument count (missing or extra): argparse's own message, wrapped as `error: ...`, followed by the usage hint `python convert.py VALUE FROM TO`.
- VALUE not a number (`abc`, empty string): `VALUE must be a number, got 'abc'`.
- VALUE not finite (`nan`, `inf`, `-inf`): `VALUE must be a finite number, got 'nan'`.
- Unknown unit (FROM checked first, then TO): `unknown unit 'xyz' (supported: C, F, kPa, psi)`.
- Unsupported pair, including same-unit pairs such as `C C`: `cannot convert C to psi (supported: C->F, F->C, kPa->psi, psi->kPa)`. Units in the message use their canonical spelling.
- Result overflows to infinity (e.g. `1e308 C F`): `result is out of range`.

## Design
- `ConvertError(Exception)` carries the message. `main` catches it, prints `error: <message>` to stderr and returns 1.
- A small `ArgumentParser` subclass overrides `error()` to raise `ConvertError`, so argparse failures use the same path (argparse's default exit code 2 is not used).
- `--help` / `-h` keeps argparse's normal behavior: usage on stdout, exit 0.
- The conversion functions and `CONVERSIONS` stay unchanged and pure.

## Out of scope
- Rejecting values below absolute zero or negative pressure (`specs/mission.md`).
- Reading `answer_keys/conversion.csv` (group 5).
