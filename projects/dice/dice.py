#!/usr/bin/env python3
"""
`dice` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.9
"""

import random
from typing import Sequence

random.seed(42)


class Die:
    """Class Die"""

    def __init__(self, possible_values: Sequence) -> None:
        """
        Initializes object `Die`

        :param possible_values: allowed values of the die
        """
        self._all_values = possible_values
        self._value = random.choice(self._all_values)

    @property
    def value(self):
        """Get the die value"""
        # TODO: Implement this function
        ...

    @value.setter
    def value(self, _):
        """Value property setter"""
        raise ValueError("You must roll the die to change its value")

    def __str__(self):
        """__str__ override"""
        # TODO: Implement this function
        ...

    def roll(self):
        """Roll the die"""
        # TODO: Implement this function
        ...


class FrozenDie(Die):
    """A die that cannot be rolled"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class FrozenDie constructor"""
        super().__init__(possible_values)
        self._frozen = False

    @property
    def frozen(self) -> bool:
        """Frozen property getter"""
        # TODO: Implement this function
        ...

    @frozen.setter
    def frozen(self, new_value: bool) -> None:
        """Frozen property setter"""
        # TODO: Implement this function
        ...

    def roll(self):
        """Roll the die"""
        # TODO: Implement this function
        ...


class Cup:
    """Class Cup"""

    def __init__(self, num_dice: int, num_sides: int = 6) -> None:
        """Class FrozenDie constructor"""
        self._dice = [Die(range(1, num_sides + 1)) for _ in range(num_dice)]

    def __iter__(self):
        """Cup iterator"""
        return iter(self._dice)

    def __str__(self) -> str:
        """__str__ override"""
        # TODO: Implement this function
        ...

    def shake(self) -> None:
        """Shake a cup"""
        # TODO: Implement this function
        ...

    def add(self, die: Die) -> None:
        """Add a die to the cup"""
        # TODO: Implement this function
        ...

    def remove(self, idx: int):
        """Remove a die from the cup"""
        # TODO: Implement this function
        ...

    def roll(self, *args) -> None:
        """Roll specific dice"""
        # TODO: Implement this function
        ...


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
