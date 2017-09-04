'''
Testing the class Point
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __str__(self):
        return '({}, {})'.format(self._x, self._y)
    
    def __eq__(self, other):
        return self._x == other.x and self._y == other.y
    
    def distance(self, other):
        return math.sqrt((self._x - other.x)**2 + (self._y - other.y)**2)

import math
import unittest
from unittest.mock import patch
from io import StringIO


class TestPoint(unittest.TestCase):
    '''Testing class Point'''

    def setUp(self):
        '''Setting up'''
        self.point_1 = Point(1, 3)
        self.point_2 = Point(1, 3)
        self.point_3 = Point(2, 4)

    def test_init(self):
        '''Testing init'''
        self.assertEqual(self.point_1, Point(1, 3))

    def test_get_x(self):
        '''Testing x getter'''
        self.assertEqual(self.point_1.x, 1)

    def test_get_y(self):
        '''Testing y getter'''
        self.assertEqual(self.point_1.y, 3)

    def test_eq(self):
        '''Testing __eq__ method'''
        self.assertEqual(self.point_1, self.point_2)
        self.assertNotEqual(self.point_1, self.point_3)

    def test_str(self):
        '''Testing __str__method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.point_1)
        self.assertEqual(output.getvalue().strip(), '(1, 3)')

    @unittest.expectedFailure
    def test_distance(self):
        '''Testing distance method'''
        self.assertAlmostEqual(self.point_1.distance(self.point_3), math.sqrt(2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
