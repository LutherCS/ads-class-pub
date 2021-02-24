#!/usr/bin/env python3
"""
`fractions` testing

@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.2
"""

import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.exercises.fractions import Fraction


def test_init():
    """Testing init"""
    fraction = Fraction(1, 3)
    assert isinstance(fraction, Fraction)


def test_init_simplification():
    """Testing init with gcd"""
    fraction = Fraction(4, 6)
    assert fraction == Fraction(2, 3)


def test_init_numerator_error():
    """Testing numerator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1.5, 2)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Numerator must be an integer number"


def test_init_numerator_error_2():
    """Testing numerator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction("1", 2)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Numerator must be an integer number"


def test_init_denominator_error():
    """Testing denominator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 2.5)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Denominator must be an integer number"


def test_init_denominator_error_2():
    """Testing denominator error"""
    with pytest.raises(TypeError) as excinfo:
        new_fraction = Fraction(1, "2")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Denominator must be an integer number"


def test_get_numerator():
    """Testing numerator getter"""
    fraction = Fraction(1, 3)
    assert fraction.get_numerator() == 1


def test_get_numerator_2():
    """Testing numerator property"""
    fraction = Fraction(1, 3)
    assert fraction.numerator == 1


def test_get_denominator():
    """Testing denominator getter"""
    fraction = Fraction(1, 3)
    assert fraction.get_denominator() == 3


def test_get_denominator_2():
    """Testing denominator property"""
    fraction = Fraction(1, 3)
    assert fraction.denominator == 3


def test_str():
    """Testing __str__method"""
    fraction = Fraction(6, 4)
    assert str(fraction) == "1 1/2"


def test_repr():
    """Testing __repr__method"""
    fraction = Fraction(6, 4)
    assert repr(fraction) == "Fraction(3, 2)"


def test_eq():
    """Testing equality operator"""
    fraction1 = Fraction(1, 3)
    fraction2 = Fraction(2, 6)
    assert fraction1 == fraction2


def test_eq_error():
    """Testing equality operator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 3) == 1
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Can only compare Fractions"


def test_gt():
    """Testing greater-than operator"""
    assert Fraction(1, 3) > Fraction(1, 4)
    assert Fraction(1, 2) < Fraction(2, 3)


def test_gt_error():
    """Testing greater-than operator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 3) > 1
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Can only compare Fractions"


def test_ge():
    """Testing greater-than-or-equal operator"""
    assert Fraction(1, 3) >= Fraction(1, 4)
    assert Fraction(1, 3) >= Fraction(2, 6)
    assert Fraction(1, 2) <= Fraction(2, 3)
    assert Fraction(1, 2) <= Fraction(2, 4)


def test_ge_error():
    """Testing greater-than-or-equal operator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 3) >= 1
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Can only compare Fractions"


def test_add():
    """Testing addition operator"""
    assert (Fraction(1, 3) + Fraction(2, 3)) == Fraction(1, 1)


def test_add_error():
    """Testing addition operator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 3) + "1"
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Can only add two Fractions"


def test_sub():
    """Testing subtraction operator"""
    assert (Fraction(1, 3) - Fraction(2, 3)) == Fraction(-1, 3)


def test_sub_error():
    """Testing subtraction operator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 3) - "1"
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Can only subtract two Fractions"


def test_mul():
    """Testing multiplication operator"""
    assert (Fraction(1, 3) * Fraction(2, 3)) == Fraction(2, 9)


def test_mul_error():
    """Testing multiplication operator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 3) * "1"
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Can only multiply two Fractions"


def test_truediv():
    """Testing true division operator"""
    assert (Fraction(1, 3) / Fraction(2, 3)) == Fraction(1, 2)


def test_truediv_error():
    """Testing true division operator error"""
    with pytest.raises(TypeError) as excinfo:
        Fraction(1, 3) / "1"
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Can only divide two Fractions"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
