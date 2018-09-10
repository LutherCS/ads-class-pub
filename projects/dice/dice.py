'''
Dice dice game(s) simulator
'''
#!/usr/bin/env python3

import random
from typing import Sequence
random.seed(42)

class Die:
    '''Class Die'''
    def __init__(self, possible_values: Sequence) -> None:
        '''Class Die constructor'''
        self._all_values = possible_values
        self._value = random.choice(self._all_values)

    @property
    def value(self):
        '''Get the die value'''
        return self._value

    @value.setter
    def value(self, _):
        '''Value property setter'''
        raise ValueError("You are supposed to 'roll' a die to change its value")

    def __str__(self):
       '''__str__ override'''
       return str(self._value)

    def roll(self) -> int:
        '''Roll the die'''
        self._value = random.choice(self._all_values)
        return self._value

class FrozenDie(Die):
    '''A die that cannot be rolled'''
    def __init__(self, possible_values: Sequence) -> None:
        '''Class FrozenDie constructor'''
        super().__init__(possible_values)
        self._frozen = False

    @property
    def frozen(self) -> bool:
        '''Frozen property getter'''
        return self._value

    @frozen.setter
    def frozen(self, new_value: bool) -> None:
        '''Frozen property setter'''
        self._frozen = True

    def roll(self):
        '''Roll the die'''
        if self._frozen == True:
            return self._value
        else:
            self.roll

class Cup:
    '''Class Cup'''
    def __init__(self, num_dice: int, num_sides: int=6) -> None:
        '''Class FrozenDie constructor'''
        self._dice = [Die(range(1, num_sides + 1)) for _ in range(num_dice)]

    def __iter__(self):
        '''Cup iterator'''
        return iter(self._dice)

    def __str__(self) -> str:
        '''__str__ override'''
        return str([dice._value for dice in self._dice])

    def shake(self) -> None:
        '''Shake a cup'''
        for dice in self._dice:
            dice.roll()

    def add(self, die) -> None:
        '''Add a die to the cup'''
        self._dice.append(die)
        return self._dice



    def remove(self, idx: int):
        '''Remove a die from the cup'''
        self._dive.pop(idx)
        return self._dice

    def roll(self, *args) -> None:
        '''Roll specific dice'''
        for i in args:
            if i > 0 and i <= len(self._dice):
                self._dice[i-1].roll()

def main():
    '''Entry point'''
    print('Let\'s play a game!')
    print('Let\'s create a die')
    my_die = Die(range(1, 7))
    print('Rolling die 10 times')
    for i in range(10):
        my_die.roll()
        print('{:2}) {:>2}'.format(i + 1, str(my_die)))
    print('The last roll is {}'.format(my_die.value))
    print('Trying to assign a value to a die')
    try:
        my_die.value = 7
    except ValueError as die_exception:
        print(die_exception)
    print('The last roll is (still) {}'.format(my_die.value))
    print('Making a cup of 5 dice')
    my_cup = Cup(5)
    print(my_cup)
    print('Re-rolling dice 1, 2, and 3')
    my_cup.roll(1, 2, 3)
    print(my_cup)
    print('Re-rolling dice 2, 4, and 6')
    my_cup.roll(2, 4, 6)
    print(my_cup)
    print('Shaking and rolling')
    for _ in range(3):
        my_cup.shake()
        print(my_cup)
    print('Using the iterator to print dice values')
    for a_die in my_cup:
        print(a_die)
    print('Frozen die demo')
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


if __name__ == '__main__':
    main()
