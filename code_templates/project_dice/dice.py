'''
# Weekly project template #
Complete the code to simulate a dice game
WARNING: This file compiles with errors without your modifications
'''
#!/usr/bin/env python3
#encoding: UTF-8

import random
# Seeding makes randomization consistent
random.seed(42)

class Die:
    '''A die class'''
    def __init__(self, possible_values):
        self._all_values = possible_values
        self._value = None
        # Task 1: assign random value (out of the list of self._all_values) to self._value
        raise NotImplementedError('This method has not been implemented yet')

    def roll(self):
        '''Roll the die'''
        # Task 2a: assign random value (out of the list of self._all_values) to self._value
        # Task 2b: return self._value
        raise NotImplementedError('This method has not been implemented yet')

    @property
    def value(self):
        ''''value' property getter'''
        return self._value

    @value.setter
    def value(self, _):
        ''''value' property setter'''
        # Task 3: raise ValueError exception with a custom message
        raise NotImplementedError('This method has not been implemented yet')

    def __str__(self):
        '''__str__ override'''
        # Task 4: return self._value as a string
        raise NotImplementedError('This method has not been implemented yet')

class Cup:
    '''A cup class'''
    def __init__(self, num_dice, num_sides=6):
        self._dice = [Die(range(1, num_sides + 1)) for _ in range(num_dice)]

    def shake(self):
        '''Shake a cup'''
        # Task 5: roll every die in self._dice list
        raise NotImplementedError('This method has not been implemented yet')

    def remove(self, idx):
        '''Remove a die from the cup'''
        # Task 6: pop a die with index idx from the self._dice list
        raise NotImplementedError('This method has not been implemented yet')

    def add(self, die):
        '''Add a die to the cup'''
        # Task 7: append a new die to the self._dice list
        raise NotImplementedError('This method has not been implemented yet')

    def roll(self, *args):
        '''Roll the dice. Provided dice use 1-based index'''
        for i in args:
            if i > 0 and i <= len(self._dice):
                self._dice[i-1].roll()

    def __str__(self):
        '''__str__ override'''
        # Task 8: return a list of dice as a string
        raise NotImplementedError('This method has not been implemented yet')

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
    my_cup.roll(2, 4, 6)
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
