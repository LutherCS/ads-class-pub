'''Reverse Polish Notation'''

#!/usr/bin/env python3


class Stack:
    '''Stack implementation'''
    def __init__(self):
        self._items = []
    def is_empty(self):
        return self._items == []
    def size(self):
        return len(self._items)
    def push(self, new_item):
        self._items.append(new_item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]


class StackError(Exception):
    '''Stack errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class TokenError(Exception):
    '''Token errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def rev_string(my_str):
    '''Reverse characters in a string without using a stack'''
    # TODO: Task 1
    pass

def rev_string_s(my_str):
    '''Reverse characters in a string using a stack'''
    # TODO: Task 2
    pass

def par_checker(phrase):
    '''Textbook implementation'''
    s = Stack()
    balanced = True
    index = 0
    while index < len(phrase) and balanced:
        symbol = phrase[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def par_checker_file(filename):
    '''Check expressions in the file'''
    # TODO: Task 3
    pass

def base_converter(decimal, base):
    '''Convert any decimal number to any base'''
    # TODO: Task 4
    pass

def rpn_calc(postfix_expr):
    '''Evaluate a postfix expression'''
    # TODO: Task 5
    pass

def do_math(operation, op1, op2):
    '''Process basic operations'''
    if operation == "+":
        return op1 + op2
    elif operation == "-":
        return op1 - op2
    elif operation == "*":
        return op1 * op2
    elif operation == "/":
        return op1 / op2
    else:
        raise TokenError("Unknown operation: {}".format(operation))
