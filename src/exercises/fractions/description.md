# Fractions

Complete the following tasks and submit your source file(s) to KATIE.

1. Modify the constructor of the class `Fraction` so that it checks if the provided numerator and denominator are both integers. If either is not an integer, the constructor should raise a `TypeError` exception.

1. Expand the textbook implementation of the class `Fraction` and add methods `get_numerator` and `get_denominator` that return the numerator and denominator of a fraction. Numerator and denominator must be specified as non-public members of the class `Fraction`.

1. Implement `numerator` and `denominator` as data descriptors (properties).

1. Expand the textbook implementation of the class `Fraction` and implement the remaining simple arithmetic operators (`__sub__`, `__mul__`, and `__truediv__`).

1. Use the provided function `gcd()` to simplify the resulting fraction whenever possible.


## What to do

- Read *src/exercises/fractions/description.md* (this file).

- Modify *src/exercises/fractions/fractions.py*.

- Run the modified file.
```
python3 src/exercises/fractions/fractions.py
```

- Compare your output to that provided in *tests/exercises/fractions/fractions_output.txt*.

- Test your implementation.
```
python3 -m pytest tests/exercises/fractions/test_fractions.py
```
