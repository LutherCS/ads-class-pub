#!/usr/bin/env python3
"""
Dice game(s) simulator
"""

import random
from dice_classes import Die, FrozenDie, Cup

random.seed(42)


def main():
    """Entry point"""
    print("Let's play a game!")
    print("Let's create a die")
    my_die = Die(range(1, 7))
    print("Rolling die 10 times")
    for i in range(10):
        my_die.roll()
        print(f"{i + 1:2}) {str(my_die):>2}")
    print(f"The last roll is {my_die.value}")
    print("Trying to assign a value to a die")
    try:
        my_die.value = 7
    except ValueError as die_exception:
        print(die_exception)
    print(f"The last roll is (still) {my_die.value}")
    print("Making a cup of 5 dice")
    my_cup = Cup(5)
    print(my_cup)
    print("Re-rolling dice 1, 2, and 3")
    my_cup.roll(1, 2, 3)
    print(my_cup)
    print("Re-rolling dice 2, 4, and 6")
    my_cup.roll(2, 4, 6)
    print(my_cup)
    print("Shaking and rolling")
    for _ in range(3):
        my_cup.shake()
        print(my_cup)
    print("Using the iterator to print dice values")
    for a_die in my_cup:
        print(a_die)
    print("Frozen die demo")
    frozen_die = FrozenDie(range(1, 7))
    print(frozen_die)
    print(frozen_die.frozen)
    frozen_die.roll()
    print(frozen_die)
    frozen_die.frozen = True
    print(frozen_die.frozen)
    for _ in range(3):
        frozen_die.roll()
        print(frozen_die)


if __name__ == "__main__":
    main()
