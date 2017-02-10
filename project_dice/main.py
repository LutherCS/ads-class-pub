'''
# Weekly project template #
Complete the code to simulate a dice game
WARNING: This file compiles with errors without your modifications
'''
#!/usr/bin/env python3
#encoding: UTF-8

import random
# Need a seed for randomization
random.seed(42)

class Die:
    '''A die class'''
    def __init__(self, possible_values_):
        self.possible_values = possible_values_
        # Task 1: assign random value (out of the list of possible_values) to self._value

    def roll(self):
        '''Roll the die'''
        # Task 2: assign random value (out of the list of possible_values) to self._value and return it

    @property
    def value(self):
        ''''value' property getter'''
        return self._value

    @value.setter
    def value(self, _):
        ''''value' property setter'''
        # Task 3: raise ValueError exception with a custom message

    @value.deleter
    def value(self):
        ''''value' property deleter'''
        del self._value

    def __str__(self):
        '''__str__ override'''
        # Task 4: return self._value as a string

class Cup:
    '''A cup class'''
    def __init__(self, num_dice_, num_sides_=6):
        self._dice = [Die(range(1, num_sides_ + 1)) for _ in range(num_dice_)]

    def shake(self):
        '''Shake a cup'''
        # Task 5: roll every die in self._dice list

    def remove(self, idx_):
        '''Remove a die from the cup'''
        # Task 6: pop a die with index idx from the self._dice list

    def add(self, die_):
        '''Add a die to the cup'''
        # Task 7: append a new die to the self._dice list

    def roll(self, *args):
        '''Roll the dice'''
        for i in args:
            if i > 0 and i <= len(args):
                self._dice[i-1].roll()

    def __str__(self):
        '''__str__ override'''
        # Task 8: return a list of dice as a string

    def __iter__(self):
        '''Cup iterator'''
        return iter(self._dice)

def main():
    '''Entry point'''
    print("Let's play a game!")
    print("Let's create a die")
    my_die = Die(range(1, 7))
    print("Rolling die 10 times")
    for i in range(10):
        my_die.roll()
        print("{:2}) {:>2}".format(i+1, str(my_die)))
    print("The last roll is {}".format(my_die.value))
    print("Trying to assign a value to a die")
    try:
        my_die.value = 7
    except ValueError as die_exception:
        print(die_exception)
    print("The last roll is (still) {}".format(my_die.value))
    print("Making a cup of 5 dice")
    my_cup = Cup(5)
    print(my_cup)
    print("Re-rolling dice 1, 2, and 3")
    my_cup.roll(1, 2, 3)
    print(my_cup)
    print("Re-rolling dice 2, 4, and 6")
    my_cup.roll(1, 2, 3)
    print(my_cup)
    print("Shaking and rolling")
    for _ in range(3):
        my_cup.shake()
        print(my_cup)
    print("Using the iterator to print dice values")
    for a_die in my_cup:
        print(a_die)
    print("Over and out")

if __name__ == "__main__":
    main()

# Task 9: the code is PEP8 compliant
# Task 10: the program is working