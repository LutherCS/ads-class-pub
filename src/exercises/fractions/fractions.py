#!/usr/bin/env python3
"""
Implementation of the class Fraction
"""


def gcd(num_a: int, num_b: int) -> int:
    """
    Greatest Common Denominator of two integers

    Helper function to simplify fractions
    """
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    """Class Fraction"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initializer"""
        raise NotImplementedError

    def get_numerator(self) -> int:
        """Return fraction numerator"""
        raise NotImplementedError

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        """Return fraction denominator"""
        raise NotImplementedError

    denominator = property(get_denominator)

    def __str__(self) -> str:
        """Object as a string"""
        raise NotImplementedError

    def __repr__(self) -> str:
        """Object representation"""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        raise NotImplementedError

    def __gt__(self, other: object) -> bool:
        """Greater than comparison"""
        raise NotImplementedError

    def __ge__(self, other: object) -> bool:
        """Greater than or equal comparison"""
        if isinstance(other, Fraction):
            return (
                self.numerator / self.denominator >= other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions")

    def __add__(self, other: object) -> object:
        """Add two fractions"""
        raise NotImplementedError

    def __sub__(self, other: object) -> object:
        """Subtract two fractions"""
        raise NotImplementedError

    def __mul__(self, other: object) -> object:
        """Multiply two fractions"""
        raise NotImplementedError

    def __truediv__(self, other: object) -> object:
        """Divide two fractions"""
        raise NotImplementedError
