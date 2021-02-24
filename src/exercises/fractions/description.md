# Fractions

Complete the following tasks to complete class `Fraction`:

1. Modify the constructor so that it checks if the provided numerator is an integer and raises a `TypeError` if it is not.
2. Modify the constructor so that it checks if the provided denominator is an integer and raises a `TypeError` if it is not.
3. Modify the constructor to use the provided function `gcd()` and simplify the resulting fraction whenever possible.
4. Implement method `get_numerator` that returns the numerator of a fraction. Numerator must be specified as non-public member of the class.
5. Implement method `get_denominator` that returns the denominator of a fraction. Denominator must be specified as non-public member of the class.
6. Implement `numerator` as data descriptor (property). Be careful and use different names for data member and data descriptor.
7. Implement `denominator` as data descriptor (property). Be careful and use different names for data member and data descriptor.
8. Implement method `__str__` to return object as a `string`.
9. Implement method `__repr__` to return object representation.
10. Implement method `__eq__` to check if two fractions are equal and raises a `TypeError` if either object is not a `Fraction`.
11. Implement method `__gt__` to check if one fraction is greater than another and raises a `TypeError` if either object is not a `Fraction`.
12. Implement method `__add__` that returns the result of fraction addition and raises a `TypeError` if either object is not a `Fraction`.
13. Implement method `__sub__` that returns the result of fraction subtraction and raises a `TypeError` if either object is not a `Fraction`.
14. Implement method `__mul__` that returns the result of fraction multiplication and raises a `TypeError` if either object is not a `Fraction`.
15. Implement method `__truediv__` that returns the result of fraction division and raises a `TypeError` if either object is not a `Fraction`.

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
