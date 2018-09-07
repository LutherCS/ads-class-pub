'''
Implementation of the class Fraction
'''
#!/usr/bin/env python3


def gcd(num_a, num_b):
    '''Helper function to simplify fractions'''
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    '''Class Fraction'''
    def __init__(self, numerator: int, denominator: int) -> None:
        '''Constructor'''
        raise NotImplementedError

    def get_numerator(self) -> int:
        '''Return fraction numerator'''
        raise NotImplementedError

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        '''Return fraction denominator'''
        raise NotImplementedError

    denominator = property(get_denominator)

    def __str__(self) -> str:
        '''Object as a string'''
        if self.numerator > self.denominator:
            return str(self.numerator // self.denominator) + ' ' + \
                str(self.numerator % self.denominator) + '/' + str(self.denominator)
        else:
            return str(self.numerator) + '/' + str(self.denominator)

    def __repr__(self) -> str:
        '''Object representation'''
        return 'Fraction({}, {})'.format(self.numerator, self.denominator)

    def __eq__(self, other: object) -> bool:
        '''Equality comparison'''
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __gt__(self, other: object) -> bool:
        '''Greater than comparison'''
        if isinstance(other, Fraction):
            return self.numerator / self.denominator > other.numerator / other.denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __ge__(self, other: object) -> bool:
        '''Greater than or equal comparison'''
        if isinstance(other, Fraction):
            return self.numerator / self.denominator >= other.numerator / other.denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __add__(self, other: object) -> object:
        '''Add two fractions'''
        raise NotImplementedError

    def __sub__(self, other: object) -> object:
        '''Subtract two fractions'''
        raise NotImplementedError

    def __mul__(self, other: object) -> object:
        '''Multiply two fractions'''
        raise NotImplementedError

    def __truediv__(self, other: object) -> object:
        '''Divide two fractions'''
        raise NotImplementedError


if __name__ == "__main__":
    print("Working with Classes")
    fr_1 = Fraction(10, 4)
    print("Fraction 1 is %s" % fr_1)
    fr_2 = Fraction(10, 12)
    print("Fraction 2 is %s" % fr_2)
    fr_3 = Fraction(3, 4)
    print("Fraction 3 is %s" % fr_3)
    print("Its id is %s" % id(fr_3))
    fr_4 = Fraction(3, 4)
    print("Fraction 4 is %s" % fr_4)
    print("Its id is %s" % id(fr_4))

    print("Comparison")
    if fr_3 == fr_4:
        print("%s and %s are equal!" % (fr_3, fr_4))
    else:
        print("%s and %s are different!" % (fr_3, fr_4))

    print("%s + %s = %s" % (fr_1, fr_2, fr_1 + fr_2))
