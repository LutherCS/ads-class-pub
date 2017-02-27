

```python
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
```

    1 6 0 + + =                    7
    1 6 0 - - =                    -5
    1 6 0 * * =                    0
    1 6 0 / / =                    


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-d9b3a0fbf004> in <module>()
         45 
         46 
    ---> 47 main()
    

    <ipython-input-1-d9b3a0fbf004> in main()
         39         for line in source:
         40             print("{:30}".format(line.strip()), end = ' ')
    ---> 41             result = eval_expr(line.strip()) # this line can cause an error
         42             print(result)
         43             # update checksum


    <ipython-input-1-d9b3a0fbf004> in eval_expr(expr)
          9             op2 = s.pop() # this line can cause an error
         10             op1 = s.pop() # this line can cause an error
    ---> 11             result = doMath(op1, op2, token) # this line can cause an error
         12             s.push(result)
         13         elif token == '=':


    <ipython-input-1-d9b3a0fbf004> in doMath(op1, op2, op)
         25         return op1 * op2
         26     if op == '/':
    ---> 27         return op1 / op2
         28     if op == '//':
         29         return op1 // op2


    ZeroDivisionError: division by zero



```python

```
