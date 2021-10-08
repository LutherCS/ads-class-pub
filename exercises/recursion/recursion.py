#!/usr/bin/env python3
"""
`recursion` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.10
"""


def gcd(a: int, b: int) -> int:
    """Greatest Common Denominator

    :param a: a number
    :param b: another number
    :return: the greatest common denominator between `a` and `b`
    >>> gcd(1860, 2020)
    20
    >>> gcd(1861, 2021)
    1
    """
    # TODO: Implement this function
    ...


def diamond_ite(levels: int) -> None:
    """Print a diamond

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    ...


def diamond_rec(levels: int) -> None:
    """Print a diamond

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    ...


def hourglass_ite(levels: int) -> None:
    """Print a hourglass

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    ...


def hourglass_rec(levels: int) -> None:
    """Print a hourglass

    :param levels: number of levels in the diamond
    """
    # TODO: Implement this function
    ...


def main():
    """Main function"""
    print(f"GCD of 1861 and 2021 is {gcd(1861, 2021)}")
    print(f"GCD of 1860 and 2020 is {gcd(1860, 2020)}")
    print("Diamond (iterative)")
    diamond_ite(5)
    print("Diamond (recursive)")
    diamond_rec(5)
    print("Hourglass (iterative)")
    hourglass_ite(5)
    print("Hourglass (recursive)")
    hourglass_rec(5)


if __name__ == "__main__":
    main()
