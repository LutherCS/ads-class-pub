# Fractions

Complete the following tasks to complete class `Fraction`:

1. Constructor
   1. Modify the constructor so that it checks if the provided numerator is an integer and raises a `TypeError` if it is not.
   2. Modify the constructor so that it checks if the provided denominator is an integer and raises a `TypeError` if it is not.
   3. Modify the constructor to use function `gcd()` from the `math` module and simplify the resulting fraction whenever possible.
2. Data members
   1. Implement method `get_numerator` that returns the numerator of a fraction. Numerator must be specified as non-public member of the class.
   2. Implement method `get_denominator` that returns the denominator of a fraction. Denominator must be specified as non-public member of the class.
   3. Implement `numerator` as data descriptor (property). Be careful and use different names for data member and data descriptor.
   4. Implement `denominator` as data descriptor (property). Be careful and use different names for data member and data descriptor.
3. `str` and `repr`
   1. Implement method `__str__` to return object as a `string`.
   2. Implement method `__repr__` to return object representation.
4. Comparison
   1. Implement method `__eq__` to check if two fractions are equal and raises a `TypeError` if either object is not a `Fraction`.
   2. Implement method `__gt__` to check if one fraction is greater than another and raises a `TypeError` if either object is not a `Fraction`.
5. Arithmetic operations
   1. Implement method `__add__` that returns the result of fraction addition and raises a `TypeError` if either object is not a `Fraction`.
   2. Implement method `__sub__` that returns the result of fraction subtraction and raises a `TypeError` if either object is not a `Fraction`.
   3. Implement method `__mul__` that returns the result of fraction multiplication and raises a `TypeError` if either object is not a `Fraction`.
   4. Implement method `__truediv__` that returns the result of fraction division and raises a `TypeError` if either object is not a `Fraction`.
