'''
Reverse Polish Notation
'''
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
    checksum = rpn_calc('data/projects/rpn/rpn_input_1.txt')
    print('Checksum is %.2f' % checksum)


if __name__ == '__main__':
    main()
