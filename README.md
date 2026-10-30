# Bench unit converter

A small command-line tool for bench work. It converts:

- temperatures between Celsius (`C`) and Fahrenheit (`F`)
- pressures between kilopascals (`kPa`) and pounds per square inch (`psi`)

## Requirements

- Python 3 (developed and tested on Python 3.14.7, Windows).
- No third-party packages are needed to run the tool.

## Usage

```
python convert.py VALUE FROM TO
```

| Command | Output |
|---|---|
| `python convert.py 100 C F` | `212.00` |
| `python convert.py -40 C F` | `-40.00` |
| `python convert.py 98.6 F C` | `37.00` |
| `python convert.py 101.325 kPa psi` | `14.70` |
| `python convert.py 30 psi kPa` | `206.84` |

- Output is the bare number, rounded to 2 decimals, on one line.
- Unit names are not case-sensitive: `c`, `C`, `kpa`, `KPA` and `Psi` all work.
- Negative values are allowed, e.g. `python convert.py -40 C F`.
- `python convert.py --help` shows the usage.

Supported conversions: `C->F`, `F->C`, `kPa->psi`, `psi->kPa`.

## Errors

Bad input prints a single line starting with `error:` to stderr, prints nothing to stdout, and exits with code 1. It never prints a traceback.

| Command | Message |
|---|---|
| `python convert.py abc C F` | `error: VALUE must be a number, got 'abc'` |
| `python convert.py nan C F` | `error: VALUE must be a finite number, got 'nan'` |
| `python convert.py 100 xyz F` | `error: unknown unit 'xyz' (supported: C, F, kPa, psi)` |
| `python convert.py 100 C psi` | `error: cannot convert C to psi (supported: C->F, F->C, kPa->psi, psi->kPa)` |
| `python convert.py 100 C C` | `error: cannot convert C to C (supported: C->F, F->C, kPa->psi, psi->kPa)` |
| `python convert.py 1e308 C F` | `error: result is out of range` |
| `python convert.py 100 C` | `error: the following arguments are required: to (usage: python convert.py VALUE FROM TO)` |

## Assumptions

These points are not stated in the brief. Tell us if you want any of them changed.

- Converting a unit to itself (`C C`) is treated as an unsupported pair and gives an error.
- Values below absolute zero (e.g. `-300 C`) and negative pressures are converted, not rejected.
- `1 psi = 6.894757293168 kPa`.
- Output is rounded to 2 decimals.

## Testing

1. Install pytest (the only development dependency):
   ```
   pip install pytest
   ```
2. From the project folder run:
   ```
   python -m pytest
   ```
   Expected result: `83 passed`.

The suite covers the conversion functions, the command-line interface, every error case above, and every row of `answer_keys/conversion.csv`. That CSV (`value,from,to,expected`) is read, never modified, so you can test your own numbers by adding rows to a copy of it.

## Project layout

```
convert.py            the converter (one file, standard library only)
tests/                automated tests
answer_keys/          reference conversions used by the tests
docs/brief.md         the original brief
docs/acceptance.md    brief requirements checked against evidence
specs/                requirements and validation notes for each build phase
```
