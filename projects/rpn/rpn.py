#!/usr/bin/env python3
"""
`rpn` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.9
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


def postfix_eval(postfix_expr: str) -> float:
    """Evaluate a postfix expression

    :param postfix_expr: an expression (line) to evaluate
    :return: floating-point result of the evaluation
    >>> postfix_eval("1 2 +")
    3
    >>> postfix_eval("1 2 -")
    -1
    >>> postfix_eval("2 3 *")
    6
    >>> postfix_eval("1 2 /")
    0.5
    >>> postfix_eval("1 2 //")
    0
    >>> postfix_eval("2 3 **")
    8
    """
    # TODO: Implement this function
    ...


def do_math(operation: str, operand1: int, operand2: int) -> float:
    """Perform a math operation

    Note that an expression "1 2 /" means $2 / 1$, not $1 / 2$
    :param operation: arithmetic operation
    :param operand1: first operand
    :param operand2: second operand
    :return: the result of the operation
    >>> do_math("+", 1, 2)
    3
    >>> do_math("-", 1, 2)
    -1
    >>> do_math("*", 2, 3)
    6
    >>> do_math("/", 1, 2)
    0.5
    >>> do_math("//", 1, 2)
    0
    >>> do_math("**", 2, 3)
    8
    """
    # TODO: Implement this function
    ...


def rpn_calc(filename: str) -> float:
    """Reverse Polish Notation calculator

    :param filename: name of the file to process
    :return: sum of the results of all *valid* expressions
    """
    # TODO: Implement this function
    ...


def main():
    """Main function"""
    filename = "projects/rpn/rpn_1.in.txt"
    print(f"Processing {filename}")
    checksum = rpn_calc(filename)
    print(f"Checksum is {checksum:.2f}")
    print("*" * 30)
    filename = "projects/rpn/rpn_2.in.txt"
    print(f"Processing {filename}")
    checksum = rpn_calc(filename)
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
