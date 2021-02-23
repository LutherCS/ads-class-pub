#!/usr/bin/env python3
"""
Exercise `recursion` driver

@authors: Roman Yasinovskyy
@version: 2021.2
"""

from recursion_functions import (
    gcd,
    hourglass_ite,
    diamond_ite,
    hourglass_rec,
    diamond_rec,
)


def main():
    """Main function"""
    print(f"GCD of 1861 and 2021 is {gcd(1861, 2021)}")
    print(f"GCD of 1860 and 2020 is {gcd(1860, 2020)}")
    print("Hourglass (iterative)")
    hourglass_ite(5)
    print("Hourglass (recursive)")
    hourglass_rec(5)
    print("Diamond (iterative)")
    diamond_ite(5)
    print("Diamond (recursive)")
    diamond_rec(5)


if __name__ == "__main__":
    main()
