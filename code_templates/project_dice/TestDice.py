'''
Testing the classes Die and Cup
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import random
import unittest
from unittest.mock import patch
from io import StringIO
from Dice import Die, Cup


class TestDiceMethods(unittest.TestCase):
    '''Testing module Dice'''

    def setUp(self):
        '''Setting up'''
        random.seed(42)
        self.die = Die(range(1, 7))
        self.cup = Cup(2, 6)
        self.yahtzee = Cup(5, 6)

    def test_die_roll(self):
        '''Testing die roll method'''
        self.assertEqual(self.die.roll(), 6)

    def test_die_get_value(self):
        '''Testing value getter'''
        self.assertEqual(self.die.value, 6)

    def test_die_set_value(self):
        '''Testing value setter'''
        with self.assertRaises(ValueError):
            self.die.value = 1

    def test_die_str(self):
        '''Testing die.__str__method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.die)
        self.assertEqual(output.getvalue().strip(), '6')

    def test_cup_shake(self):
        '''Testing shake method'''
        self.cup.shake()
        self.assertEqual(str(self.cup), '[6, 1]')

    def test_cup_add(self):
        '''Testing add method'''
        self.cup.add(Die(range(1, 7)))
        self.assertEqual(str(self.cup), '[1, 1, 6]')

    def test_cup_remove(self):
        '''Testing remove method'''
        self.cup.remove(0)
        self.assertEqual(str(self.cup), '[1]')

    def test_cup_roll(self):
        '''Testing cup roll method'''
        self.assertEqual(str(self.yahtzee), '[6, 3, 2, 2, 2]')
        self.yahtzee.shake()
        self.assertEqual(str(self.yahtzee), '[6, 1, 6, 6, 5]')
        self.yahtzee.roll(1, 3, 5)
        self.assertEqual(str(self.yahtzee), '[1, 1, 5, 6, 4]')

    def test_cup_str(self):
        '''Testing cup.__str__method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.cup)
        self.assertEqual(output.getvalue().strip(), '[1, 1]')

if __name__ == '__main__':
    unittest.main(verbosity=2)
