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
