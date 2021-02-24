#!/usr/bin/env python3
"""
`stacks` driver

@authors: Roman Yasinovskyy
@version: 2021.2
"""

from stacks import (
    base_converter,
    par_checker,
    par_checker_ext,
    par_checker_file,
    rev_string,
    rpn_calc,
)


def main():
    """Main function"""
    print("Reversing a string")
    s = "Hello world"
    print(f"Original: {s}")
    print(f"Reversed: {rev_string(s)}")

    print("Checking parentheses")
    exp = "()({}{[][]<>}{[]})"
    if par_checker(exp):
        print(f"Simple checker says: {exp} is balanced")
    else:
        print(f"Simple checker says: {exp} is not balanced")
    if par_checker_ext(exp):
        print(f"Extended checker says: {exp} is balanced")
    else:
        print(f"Extended checker says: {exp} is not balanced")
    print("Checking a file using the simple checker")
    par_checker_file("data/exercises/stacks/parentheses_simple.txt")
    print("Base converter")
    n = 160
    print(f"{n} in binary is {base_converter(n, 2)}")
    print(f"{n} in octal is {base_converter(n, 8)}")
    print(f"{n} in hexadecimal is {base_converter(n, 16)}")
    bases = [0, 1, 3, 42]
    for b in bases:
        try:
            print(f"{n} in base {b} is {base_converter(n, b)}")
        except ValueError as ve:
            print(ve)
    print("RPN Calculator")
    expressions = [
        "2 3 +",
        "2 3 -",
        "3 2 -",
        "2 3 *",
        "3 2 /",
        "1 2 + 3 - 4 5 + / 16 +",
    ]
    for e in expressions:
        print(f"{e} = {rpn_calc(e)}")


if __name__ == "__main__":
    main()
