'''
Fraction class template
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

def gcd(a, b):
    '''Helper function to simplify fractions'''
    while a % b != 0:
        tmp = b
        b = a % tmp
        a = tmp
    return b


class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        if denom > 0:
            self.denom = denom
        else:
            raise Exception("Denominator must be a positive integer")

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __eq__(self, other_fraction):
        return self.numer * other_fraction.denom == other_fraction.numer * self.denom

    def __gt__(self, other_fraction):
        if self.numer / self.denom > other_fraction.numer / other_fraction.denom:
            return True

    def __add__(self, other_fraction):
        new_numer = self.numer * other_fraction.denom + self.denom * other_fraction.numer
        new_denom = self.denom * other_fraction.denom

        return Fraction(new_numer, new_denom)
