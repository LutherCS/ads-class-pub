# Fractions

Complete the following tasks:

1. Modify the constructor of the class `Fraction` so that it checks if the provided numerator and denominator are both integers. If either is not an integer, the constructor should raise a `TypeError` exception.

1. Expand the textbook implementation of the class `Fraction` and add methods `get_numerator` and `get_denominator` that return the numerator and denominator of a fraction. Numerator and denominator must be specified as non-public members of the class `Fraction`.

1. Implement `numerator` and `denominator` as data descriptors (properties).

1. Expand the textbook implementation of the class `Fraction` and implement the remaining simple arithmetic operators (`__sub__`, `__mul__`, and `__truediv__`).

1. Use the provided function `gcd()` to simplify the resulting fraction whenever possible.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/exercises/fractions/description.md_ (this file).
- Modify _src/exercises/fractions/fractions.py_.
- Run _src/exercises/fractions/fractions_main.py_.

```bash
python3 src/exercises/fractions/fractions_main.py
```

- Compare your output to that provided in _tests/exercises/fractions/fractions_output.txt_.
- Test your implementation.

```bash
python3 -m pytest tests/exercises/fractions/test_fractions.py
```
