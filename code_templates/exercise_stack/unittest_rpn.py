'''
Testing the Reverse Polish Notation
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from rpn import *

# Change this value to match your IDE and/or system configuration
PATH = 'code_templates/exercise_stack/'

class TestRPNMethods(unittest.TestCase):
    '''Testing class RPN'''

    def test_rev_string(self):
        '''Testing rev_string method'''
        self.assertEqual(rev_string('Hello'), 'olleH')

    def test_rev_string_s(self):
        '''Testing rev_string_s method'''
        self.assertEqual(rev_string_s('Hello'), 'olleH')


    def test_pas_checker(self):
        '''Testing par_checker method'''
        self.assertTrue(par_checker('((()))'))
        self.assertFalse(par_checker('(()'))

    def test_par_checker_file(self):
        '''Testing par_checker_file method'''
        expected_output = '((())) is balanced\n' \
                            + '(())) is NOT balanced\n' \
                            + '((() is NOT balanced\n' \
                            + '(() is NOT balanced\n' \
                            + '() is balanced\n' \
                            + ') is NOT balanced'
        with patch('sys.stdout', new=StringIO()) as output:
            par_checker_file(PATH + 'input_parentheses.txt')
        self.assertEqual(output.getvalue().strip(), expected_output)

    def test_base_converter(self):
        '''Testing base_convrter method'''
        self.assertEqual(base_converter(10, 2), '1010')
        self.assertEqual(base_converter(127, 2), '1111111')
        self.assertEqual(base_converter(10, 8), '12')
        self.assertEqual(base_converter(127, 8), '177')
        self.assertEqual(base_converter(10, 16), 'A')
        self.assertEqual(base_converter(127, 16), '7F')

    def test_rpn_calc(self):
        '''Testing rpn_calc method'''
        self.assertEqual(rpn_calc('3 2 1 + *'), 9)
        self.assertEqual(rpn_calc('1 2 3 + -'), -4)
        self.assertEqual(rpn_calc('3 2 1 / *'), 6.0)
        self.assertAlmostEqual(rpn_calc('1 2 3 / -'), 1/3)
        with self.assertRaises(StackError):
            rpn_calc('3 2 1 +')
        with self.assertRaises(StackError):
            rpn_calc('3 2 1 + - *')
        with self.assertRaises(TokenError):
            rpn_calc('3 2 **')
        with self.assertRaises(TokenError):
            rpn_calc('a b +')

if __name__ == '__main__':
    unittest.main()
