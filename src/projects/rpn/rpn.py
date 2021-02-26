#!/usr/bin/env python3
"""
Project `rpn` implementation

@author:
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
