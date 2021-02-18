# Alea iacta est

Implement classes Die, FrozenDie, and Cup. Your program must be properly formatted (use `black` and `pylint`) and pass all the tests provided (use pytest).

1. `Die`: Assign random value (out of the list of `possible_values`) to `self._value` in the `__init__`.
1. `Die`: Implement _property_ `value` using getter and setter.
1. `Die`: `value` setter must raise `ValueError` with a custom message. You are supposed to `roll` a die to change its value.
1. `Die`: Overwrite `__str__` method.
1. `Die`: Implement method `roll` that assigns random value (out of the list of `possible_values`) to `self._value` and returns it
1. `FrozenDie`: Inherits from `Die`.
1. `FrozenDie`: Implement _property_ `frozen` using getter and setter.
1. `FrozenDie`: Implement method `roll` that returns `self._value` if the die is frozen and calls method `roll` of the superclass `Die` if the die is not frozen.
1. `Cup`: Create a cup with `num_dice` dice in it.
1. `Cup`: Overwrite `__str__` to return a list of dice as a string.
1. `Cup`: Implement method `shake` that rolls all the dice in the cup.
1. `Cup`: Implement method `add` that appends a new die to the list `self._dice`.
1. `Cup`: Implement method `remove` that removes a specific die from the cup.
1. `Cup`: Implement method `roll` that rolls specific dice in the cup.

## What to do

`python` should be `python3.9` or newer.

- Read _src/projects/dice/description.md_ (this file).
- Modify _src/projects/dice/dice\_classes.py_.
- Run _src/projects/dice/dice\_main.py_.

```bash
python src/projects/dice/dice_main.py
```

- Compare your output to that provided in _tests/projects/dice/dice\_output.txt_.
- Test your implementation.

```bash
python -m pytest tests/projects/dice/test_dice.py
```
