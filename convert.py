import argparse
import math
import sys


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


KPA_PER_PSI = 6.894757293168


def kpa_to_psi(kpa):
    return kpa / KPA_PER_PSI


def psi_to_kpa(psi):
    return psi * KPA_PER_PSI


CONVERSIONS = {
    ("C", "F"): celsius_to_fahrenheit,
    ("F", "C"): fahrenheit_to_celsius,
    ("kPa", "psi"): kpa_to_psi,
    ("psi", "kPa"): psi_to_kpa,
}


UNITS = {
    "c": "C",
    "f": "F",
    "kpa": "kPa",
    "psi": "psi",
}


class ConvertError(Exception):
    pass


class ConverterParser(argparse.ArgumentParser):
    def error(self, message):
        raise ConvertError(f"{message} (usage: python convert.py VALUE FROM TO)")


def parse_value(text):
    try:
        value = float(text)
    except ValueError:
        raise ConvertError(f"VALUE must be a number, got {text!r}") from None
    if not math.isfinite(value):
        raise ConvertError(f"VALUE must be a finite number, got {text!r}")
    return value


def parse_unit(text):
    try:
        return UNITS[text.lower()]
    except KeyError:
        supported = ", ".join(UNITS.values())
        raise ConvertError(f"unknown unit {text!r} (supported: {supported})") from None


def convert(value, from_unit, to_unit):
    pair = (from_unit, to_unit)
    if pair not in CONVERSIONS:
        supported = ", ".join(f"{a}->{b}" for a, b in CONVERSIONS)
        raise ConvertError(
            f"cannot convert {from_unit} to {to_unit} (supported: {supported})"
        )
    result = CONVERSIONS[pair](value)
    if not math.isfinite(result):
        raise ConvertError("result is out of range")
    return result


def main(argv=None):
    parser = ConverterParser(
        prog="convert.py",
        description="Convert temperatures (C, F) and pressures (kPa, psi).",
    )
    parser.add_argument("value")
    parser.add_argument("from_unit", metavar="from")
    parser.add_argument("to_unit", metavar="to")
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0].startswith("-") and argv[0] not in ("-h", "--help", "--"):
        argv.insert(0, "--")  # a leading-dash VALUE such as -inf is a value, not a flag
    try:
        args = parser.parse_args(argv)
        value = parse_value(args.value)
        from_unit = parse_unit(args.from_unit)
        to_unit = parse_unit(args.to_unit)
        result = round(convert(value, from_unit, to_unit), 2) + 0.0
    except ConvertError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(f"{result:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
