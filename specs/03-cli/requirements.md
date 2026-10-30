# 03 CLI: requirements

- `python convert.py VALUE FROM TO` prints the converted value and exits 0.
- `main(argv=None) -> int` in `convert.py` does the work; the script entry point is `sys.exit(main())`.
- Parsing uses argparse (stdlib only, per `specs/tech-stack.md`). VALUE is parsed as a float and may be negative (`-40`).
- Units are case-insensitive. `UNITS` maps lowercase spellings to the canonical ones used by `CONVERSIONS`: `c`->`C`, `f`->`F`, `kpa`->`kPa`, `psi`->`psi`.
- Output is the bare number rounded to 2 decimals (e.g. `212.00`, `14.70`), one line on stdout.
- Negative zero is printed as `0.00`, never `-0.00`.
- The conversion functions stay pure; only `main` does I/O.

## Out of scope
- Friendly errors, exit code 1, rejecting bad input (group 4). argparse defaults apply until then.
- Changing the conversion functions or `CONVERSIONS`.
