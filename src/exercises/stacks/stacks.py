#!/usr/bin/env python3
"""Stack exercise"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def rev_string(my_str):
    """Reverse characters in a string using a stack"""
    raise NotImplementedError


def par_checker(line):
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


def par_checker_ext(line):
    """Check if parentheses are balanced"""
    raise NotImplementedError


def par_checker_file(filename):
    """Check expressions in the file"""
    raise NotImplementedError


def base_converter(dec_num, base):
    """Convert a decimal number to any base"""
    raise NotImplementedError


def rpn_calc(postfix_expr):
    """Evaluate a postfix expression"""
    raise NotImplementedError


def do_math(op, op1, op2):
    """Evaluate a mathematical operation"""
    raise NotImplementedError
