#!/usr/bin/env python3
"""
`stacks` implementation and driver

@authors:
"""

from typing import Union

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def rev_string(my_str: str) -> str:
    """Reverse characters in a string using a stack"""
    # TODO: Implement this function
    ...


def par_checker(line: str) -> bool:
    """Textbook implementation"""
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        i = i + 1
    return balanced and stack.is_empty()


def par_checker_ext(line: str) -> bool:
    """Check if parentheses are balanced"""
    # TODO: Implement this function
    ...


def par_checker_file(filename: str) -> None:
    """Check expressions in the file"""
    # TODO: Implement this function
    ...


def base_converter(dec_num: int, base: int) -> str:
    """Convert a decimal number to any base"""
    # TODO: Implement this function
    ...


def rpn_calc(postfix_expr: str) -> Union[int, float]:
    """Evaluate a postfix expression"""
    # TODO: Implement this function
    ...


def do_math(operation: str, operand1: Union[int, float], operand2: Union[int, float]):
    """Evaluate a mathematical operation"""
    # TODO: Implement this function
    ...


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
    par_checker_file("parentheses_simple.txt")
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
