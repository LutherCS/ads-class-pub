#!/usr/bin/env python3
"""
Exercise `hashing` driver

@authors: Roman Yasinovskyy
@version: 2021.2
"""

from hashing_functions import (
    hash_remainder,
    hash_mid_sqr,
    hash_folding,
    hash_str,
    hash_str_weighted,
)


def main():
    """Main function"""
    keys_int = [10, 21, 32, 18, 17, 19, 42, 23, 99]
    keys_int_2 = [54, 26, 93, 17, 77, 31]
    keys_intstr = ["563-555-1234", "800-555-8080", "888-555-0000"]
    keys_intstr_2 = ["436-555-4601"]
    keys_str = [
        "pavel",
        "bruce",
        "talia",
        "harvey",
        "jim",
        "alfred",
        "lucius",
        "jonathan",
        "bane",
    ]
    keys_str_2 = ["algorithm", "logarithm"]

    print("Simple remainder")
    print([hash_remainder(x, 16) for x in keys_int])
    print([hash_remainder(x, 11) for x in keys_int_2])

    print("Mid-square")
    print([hash_mid_sqr(x, 16) for x in keys_int])
    print([hash_mid_sqr(x, 11) for x in keys_int_2])

    print("Folding")
    print([hash_folding(x, 16) for x in keys_intstr])
    print([hash_folding(x, 11) for x in keys_intstr_2])

    print("String hashing")
    print([hash_str(x, 16) for x in keys_str])
    print([hash_str(x, 11) for x in keys_str_2])

    print("Weighted string hashing")
    print([hash_str_weighted(x, 16) for x in keys_str])
    print([hash_str_weighted(x, 11) for x in keys_str_2])


if __name__ == "__main__":
    main()
