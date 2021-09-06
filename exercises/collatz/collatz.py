#!/usr/bin/env python3
"""
`collatz` implementation and driver

@authors: 
"""


def collatz(number: int) -> tuple[int, int]:
    """
    Calculates stopping time and max trajectory point

    :param number: number to analyze
    :returns: tuple of (steps, max trajectory point)

    >>> collatz(27)
    (111, 9232)
    >>> collatz(42)
    (8, 64)
    >>> collatz(2021)
    (63, 6064)
    """
    # TODO: Implement this function
    ...


def main() -> None:
    """Main function"""
    for n in [27, 42, 2021]:
        result = collatz(n)
        print(
            f"Number: {n:5d} "
            + f"| Stopping distance: {result[0]:>5d} "
            + f"| Highest point: {result[1]:>5d}"
        )


if __name__ == "__main__":
    main()
