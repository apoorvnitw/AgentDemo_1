# Mission

A fast, trustworthy command-line unit converter for bench work.

## In scope
- Temperature: Celsius <-> Fahrenheit.
- Pressure: kPa <-> psi.
- CLI usage: `python convert.py VALUE FROM TO`.

## Out of scope
- Any other units.
- GUI, batch or file input.
- Absolute-zero / negative-pressure validation.

## Success
- Every row of `answer_keys/conversion.csv` matches at 2 decimals.
- Bad input gives a clear one-line error and a non-zero exit code, never a traceback.
