#!/usr/bin/env python3
"""
Reverse Polish Notation
"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


def postfix_eval(postfix_expr: str) -> int:
    # TODO: Evaluate an expression
    raise NotImplementedError


def do_math(op: str, op1: int, op2: int) -> int:
    # TODO: Process arithmetic operations
    raise NotImplementedError


def rpn_calc(filename: str) -> int:
    # TODO: Read lines from the file and pass them to the postfix_eval
    raise NotImplementedError


def main():
    """Main function"""
    checksum = rpn_calc("data/projects/rpn/rpn_input_1.txt")
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
