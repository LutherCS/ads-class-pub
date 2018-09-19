'''
Testing the Stack
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3


import pytest
import sys
from exercises.stacks.stacks import base_converter
from exercises.stacks.stacks import rev_string_simple
from exercises.stacks.stacks import rev_string_stack
from exercises.stacks.stacks import par_checker
from exercises.stacks.stacks import par_checker_file
from exercises.stacks.stacks import rpn_calc
from exercises.stacks.stacks import StackError, TokenError

class TestStackMethods:
    '''Testing class Stack'''

    def test_rev_string(self):
        '''Testing rev_string method'''
        assert rev_string_simple('Hello') == 'olleH'

    def test_rev_string_stack(self):
        '''Testing rev_string_s method'''
        assert rev_string_stack('Hello') == 'olleH'

    def test_par_checker(self):
        '''Testing par_checker method'''
        assert par_checker('((()))')
        assert not par_checker('(()')

    def test_par_checker_file(self, capsys):
        '''Testing par_checker_file method'''
        expected_output = '(()()((()))))()()()()((())()((()))()()()))()(((((((()()))()))())))) is NOT balanced\n' \
                            + '((())) is balanced\n' \
                            + '(())) is NOT balanced\n' \
                            + '((() is NOT balanced\n' \
                            + '(() is NOT balanced\n' \
                            + '() is balanced\n' \
                            + ') is NOT balanced'
        par_checker_file('data/exercises/stacks/parentheses.txt')
        out, err = capsys.readouterr()
        assert out.strip() == expected_output

    def test_base_converter(self):
        '''Testing base_convrter method'''
        assert base_converter(10, 2) == '1010'
        assert base_converter(127, 2) == '1111111'
        assert base_converter(10, 8) == '12'
        assert base_converter(127, 8) == '177'
        assert base_converter(10, 16) == 'A'
        assert base_converter(127, 16) == '7F'

    def test_rpn_calc(self):
        '''Testing rpn_calc method'''
        assert rpn_calc('3 2 1 + *') == 9
        assert rpn_calc('1 2 3 + -') == -4
        assert rpn_calc('3 2 1 / *') == 6.0
        
        assert pytest.approx(rpn_calc('1 2 3 / -')) == 1/3
        
        with pytest.raises(StackError) as excinfo:
            rpn_calc('3 2 1 +')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Stack is not empty'
        
        with pytest.raises(StackError) as excinfo:
            rpn_calc('3 2 1 + - *')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Stack is empty'          
        token = '**'
        with pytest.raises(TokenError) as excinfo:
            rpn_calc('3 2 **')
        exception_msg = excinfo.value.args[0]          
        assert exception_msg == "Unknown token: {}".format(token)
        token = 'a'
        with pytest.raises(TokenError) as excinfo:
            rpn_calc('a b +')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Unknown token: {}".format(token)

if __name__ == '__main__':
    pytest.main(['test_stacks.py'])
