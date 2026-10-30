import pytest

from convert import (
    CONVERSIONS,
    KPA_PER_PSI,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kpa_to_psi,
    psi_to_kpa,
)


def test_answer_key_kpa_to_psi():
    assert round(kpa_to_psi(101.325), 2) == 14.70


def test_answer_key_psi_to_kpa():
    assert round(psi_to_kpa(30), 2) == 206.84


def test_zero():
    assert kpa_to_psi(0) == 0
    assert psi_to_kpa(0) == 0


def test_negative_converts():
    assert kpa_to_psi(-10) < 0


def test_constant():
    assert KPA_PER_PSI == 6.894757293168
    assert psi_to_kpa(1) == pytest.approx(6.894757293168)


@pytest.mark.parametrize("value", [0, 1, 14.7, 101.325, 1234.5, -10])
def test_round_trip(value):
    assert psi_to_kpa(kpa_to_psi(value)) == pytest.approx(value)


def test_dispatch_table_keys():
    assert set(CONVERSIONS) == {
        ("C", "F"),
        ("F", "C"),
        ("kPa", "psi"),
        ("psi", "kPa"),
    }


def test_dispatch_table_functions():
    assert CONVERSIONS[("C", "F")] is celsius_to_fahrenheit
    assert CONVERSIONS[("F", "C")] is fahrenheit_to_celsius
    assert CONVERSIONS[("kPa", "psi")] is kpa_to_psi
    assert CONVERSIONS[("psi", "kPa")] is psi_to_kpa
    assert CONVERSIONS[("kPa", "psi")](101.325) == kpa_to_psi(101.325)


def test_unsupported_pair_absent():
    assert ("C", "psi") not in CONVERSIONS
