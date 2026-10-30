import argparse
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


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="convert.py",
        description="Convert temperatures (C, F) and pressures (kPa, psi).",
    )
    parser.add_argument("value", type=float)
    parser.add_argument("from_unit", metavar="from")
    parser.add_argument("to_unit", metavar="to")
    args = parser.parse_args(argv)

    pair = (UNITS[args.from_unit.lower()], UNITS[args.to_unit.lower()])
    result = round(CONVERSIONS[pair](args.value), 2) + 0.0
    print(f"{result:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
