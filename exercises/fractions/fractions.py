#!/usr/bin/env python3
"""
`fractions` implementation and driver

@authors:
"""


from functools import total_ordering


def gcd(num_a: int, num_b: int) -> int:
    """
    Calculates the greatest Common Denominator of two integers

    Helper function to simplify fractions
    """
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


@total_ordering
class Fraction:
    """Class Fraction"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initializer

        :param numerator: numerator of the fraction
        :param denominator: denominator of the fraction
        :raises: `TypeError` is either numerator or denominator is not an integer
        """
        # TODO: Implement this function
        ...

    def get_numerator(self) -> int:
        """
        Fraction numerator getter

        :returns: fraction numerator
        """
        # TODO: Implement this function
        ...

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        """
        Fraction denominator getter

        :returns: fraction denominator
        """
        # TODO: Implement this function
        ...

    denominator = property(get_denominator)

    def __str__(self) -> str:
        """
        Converts Fraction to a string

        :returns: fraction as a string
        """
        # TODO: Implement this function
        ...

    def __repr__(self) -> str:
        """
        Fraction representation

        :returns: fraction representation
        """
        # TODO: Implement this function
        ...

    def __eq__(self, other: object) -> bool:
        """
        Compares two object for equality

        :param other: another object
        :returns: `True` is two objects are equal, `False` otherwise
        :raises: `TypeError` if another object is not a `Fraction`
        """
        # TODO: Implement this function
        ...

    def __gt__(self, other: object) -> bool:
        """
        Compares if one object is greater than another

        :param other: another object
        :returns: `True` is this objects is greater, `False` otherwise
        :raises: `TypeError` if another object is not a `Fraction`
        """
        # TODO: Implement this function
        ...

    def __add__(self, other: object) -> object:
        """
        Adds two fractions

        :param other: another object
        :returns: sum of two fractions
        :raises: `TypeError` if another object is not a `Fraction`
        """
        # TODO: Implement this function
        ...

    def __sub__(self, other: object) -> object:
        """
        Subtracts two fractions

        :param other: another object
        :returns: difference of two fractions
        :raises: `TypeError` if another object is not a `Fraction`
        """
        # TODO: Implement this function
        ...

    def __mul__(self, other: object) -> object:
        """
        Multiplies two fractions

        :param other: another object
        :returns: product of two fractions
        :raises: `TypeError` if another object is not a `Fraction`
        """
        # TODO: Implement this function
        ...

    def __truediv__(self, other: object) -> object:
        """
        Divides two fractions

        :param other: another object
        :returns: result of division of two fractions
        :raises: `TypeError` if another object is not a `Fraction`
        """
        # TODO: Implement this function
        ...


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
