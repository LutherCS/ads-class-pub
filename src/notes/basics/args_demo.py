#!/usr/bin/env python3

"""Argument demo"""

import sys

class FridayError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def args_demo(*args):
    print(type(args))
    print(args)
    print(len(args))
    for arg in args:
        print(arg)

def kwargs_demo(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(f"Hello {kwargs['name']}, it's {kwargs['day']}")
    for k in kwargs:
        print(k, kwargs[k])

def demo(name=None, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    if kwargs["day"] == "Friday":
        raise FridayError("Let's cancel Mondays!")

def main(argv):
    # print(f"Hello {' '.join(argv[1:])}")
    # args_demo(1, 3)
    # args_demo(1, 2, 3)
    # kwargs_demo(name="CS160", day="Friday")
    # kwargs_demo(day="Friday", name="CS160")
    # demo("CS160", 1, 2, 3, day="Friday")
    demo(1, 2, day="Friday")

if __name__ == "__main__":
    main(sys.argv)
