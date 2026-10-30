import pytest

from convert import celsius_to_fahrenheit, fahrenheit_to_celsius


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (100, 212.00),
        (0, 32.00),
        (-40, -40.00),
        (36.6, 97.88),
    ],
)
def test_answer_key_c_to_f(celsius, expected):
    assert round(celsius_to_fahrenheit(celsius), 2) == expected


def test_answer_key_f_to_c():
    assert round(fahrenheit_to_celsius(98.6), 2) == 37.00


def test_negative_and_zero():
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(0) == 32
    assert fahrenheit_to_celsius(32) == 0


def test_float_precision():
    assert round(celsius_to_fahrenheit(36.6), 2) == 97.88


@pytest.mark.parametrize("value", [-273.15, -40, 0, 36.6, 100, 1234.5])
def test_round_trip(value):
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(value)) == pytest.approx(value)


def test_absolute_zero_still_converts():
    assert round(celsius_to_fahrenheit(-273.15), 2) == -459.67
    assert fahrenheit_to_celsius(-459.67) == pytest.approx(-273.15)
