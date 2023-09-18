#!/usr/bin/env python3
"""Advanced features of basic Python"""

# List comprehension
print("List comprehensions")
numbers = [1, 2, 3, 4, 5]
print([n**2 for n in numbers])
print(", ".join([str(n) for n in numbers if n % 2 == 0]))
print("-" * 10)


# Passing arguments to a function
print("Arguments and keyword arguments")


def f1(args):
    """Argument handled as-is

    Only 1 argument is expected
    """
    print(args)


def f2(*args):
    """Arguments become an iterable

    Number of arguments can vary
    """
    print(args)


def f3(**kwargs):
    """Keyword arguments"""
    print(kwargs)


def f4(*args, **kwargs):
    """Positional and keyword arguments together"""
    print(args, kwargs)


# The following function definition is invalid.
# Keyword arguments must follow positional
# def f5(**kwargs, *args):
#     ...


print("f1(numbers)")
f1(numbers)
print("f2(numbers)")
f2(numbers)
print("f2(*numbers)")
f2(*numbers)
print("f2(1, 2, 3, 4, 5)")
f2(1, 2, 3, 4, 5)
print("f2(1, 2, 3)")
f2(1, 2, 3)
print("f3(a=1, b=2)")
f3(a=1, b=2)
print('f3(**{"a": 1, "b": 2})')
f3(**{"a": 1, "b": 2})
print("f4(*numbers, a=1, b=2)")
f4(*numbers, a=1, b=2)
