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


def main():
    """Main function"""
    print("Working with Classes")
    fraction1 = Fraction(10, 4)
    print(f"Fraction 1 is {fraction1}")
    fraction2 = Fraction(10, 12)
    print(f"Fraction 2 is {fraction2}")
    fraction3 = Fraction(3, 4)
    print(f"Fraction 3 is {fraction3}")
    print(f"Its id is {id(fraction3)}")
    fraction4 = Fraction(3, 4)
    print(f"Fraction 4 is {fraction4}")
    print(f"Its id is {id(fraction4)}")

    print("Comparison")
    if fraction3 == fraction4:
        print(f"{fraction3} and {fraction4} are equal!")
    else:
        print(f"{fraction3} and {fraction4} are different!")

    print(f"{fraction1} + {fraction2} = {fraction1 + fraction2}")


if __name__ == "__main__":
    main()
