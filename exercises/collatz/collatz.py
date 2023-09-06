#!/usr/bin/env python3
"""
`collatz` implementation and driver

@authors: 
@version: 2023.9
"""


def collatz(number: int) -> tuple[int, int]:
    """
    Calculates stopping time and max trajectory point

    :param number: number to analyze
    :returns: tuple of (steps, max trajectory point)

    >>> collatz(42)
    (9, 64)
    >>> collatz(1861)
    (38, 5584)
    >>> collatz(1862)
    (38, 4192)
    """
    # TODO: Implement this function
    ...


def main() -> None:
    """Main function"""
    for n in [42, 1861, 1862]:
        steps, max_point = collatz(n)
        print(
            f"Number: {n:5d} "
            + f"| Stopping distance: {steps:>5d} "
            + f"| Highest point: {max_point:>5d}"
        )


if __name__ == "__main__":
    main()
