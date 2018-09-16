'''
Implementation of the class Fraction
Swopnil N. Shrestha
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
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator 
        else:
            raise TypeError("Values can only be integers")

    def get_numerator(self) -> int:
        '''Return fraction numerator'''
        return self._numerator

    def get_denominator(self) -> int:
        '''Return fraction denominator'''
        return self._denominator

    def simplify(frac: object) -> object:
      common = gcd(frac._numerator, frac._denominator)
      return Fraction(frac._numerator//common, frac._denominator//common)

    # Experimental: Setting denominator and numerator
    def set_numerator(self, new_numerator) -> None:
      '''Set fraction numerator'''
      self._numerator = new_numerator

    def set_denominator(self, new_denominator) -> None:
      '''Set fraction denominator'''
      self._denominator = new_denominator

    # Allows us to get and set the numerator and denominator without having to type in the functions
    numerator = property(get_numerator, set_numerator)
    denominator = property(get_denominator, set_denominator)

    def __str__(self) -> str:
        '''Object as a string'''

        simple = Fraction(self._numerator, self._denominator).simplify()

        if simple.numerator > simple.denominator:
            return str(simple.numerator // simple.denominator) + ' ' + \
                str(simple.numerator %  simple.denominator) + '/' + str(simple.denominator)
        else:
            return str(simple.numerator) + '/' + str(simple.denominator)

    # Backup behaviour if __str__ is missing. The goal is to be unambigious        
    def __repr__(self) -> str:
        '''Object representation'''
        return 'Fraction({}, {})'.format(self._numerator, self._denominator)

    def __eq__(self, other: object) -> bool:
        '''Equality comparison'''
        if isinstance(other, Fraction):
            return self._numerator * other._denominator == other._numerator * self._denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __gt__(self, other: object) -> bool:
        '''Greater than comparison'''
        if isinstance(other, Fraction):
            return self._numerator / self._denominator > other._numerator / other._denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __ge__(self, other: object) -> bool:
        '''Greater than or equal comparison'''
        if isinstance(other, Fraction):
            return self._numerator / self._denominator >= other._numerator / other._denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __add__(self, other: object) -> object:
        '''Add two fractions'''
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
            new_denominator = self._denominator * other._denominator
            
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Can only add two Fractions')

    # Other signifies if the other variable is a fraction
    def __sub__(self, other: object) -> object:
        '''Subtract two fractions'''
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator - self._denominator * other._numerator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Can only substract two Fractions')

    def __mul__(self, other: object) -> object:
        '''Multiply two fractions'''
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._numerator 
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Can only multiply two Fractions')

    def __truediv__(self, other: object) -> object:
        '''Divide two fractions'''
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator 
            new_denominator = self._denominator * other._numerator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError('Can only divide two Fractions') 

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

