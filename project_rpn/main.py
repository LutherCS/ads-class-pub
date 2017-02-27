import random
from pythonds import Stack


def eval_expr(expr):
    s = Stack()
    for token in expr.split():
        if token in ['+', '-', '*', '/', '//', '%', '**']:
            op2 = s.pop() # this line can cause an error
            op1 = s.pop() # this line can cause an error
            result = doMath(op1, op2, token) # this line can cause an error
            s.push(result)
        elif token == '=':
            return s.pop() # this line can cause an error
        else:
            s.push(int(token))


def doMath(op1, op2, op):
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    if op == '//':
        return op1 // op2
    if op == '%':
        return op1 % op2
    if op == '**':
        return op1 ** op2


def main():
    checksum = 0
    with open("expressions.txt", 'r') as source: # this line can cause an error
        for line in source:
            print("{:30}".format(line.strip()), end = ' ')
            result = eval_expr(line.strip()) # this line can cause an error
            print(result)
            # update checksum
    print("Checksum: {:5.2f}".format(checksum))


main()