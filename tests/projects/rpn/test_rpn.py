'''
Testing the module rpn
Karina Hoff, 2018
'''

#!/usr/bin/python3

import pytest
from projects.rpn.rpn import do_math
from projects.rpn.rpn import postfix_eval
from projects.rpn.rpn import StackError, TokenError


class TestRpnMethods:
    '''Testing module rpn'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''   
        self.rpn_expressions = ['2 3 + =', '2 1 - =', '1 2 - 3 * 3 + =']
        
    def test_postfix_eval(self):
        '''Test correct postfix expressions'''
        checksum = 0
        for expression in self.rpn_expressions:
            try:
                result = postfix_eval(expression)
                checksum = checksum + result
            except Exception:
                pass
        assert checksum == 6

    def test_postfix_eval_errors(self):
        '''Test incorrect postfix expressions'''
        # Empty Stack Error
        with pytest.raises(StackError) as excinfo:
            postfix_eval('=')
        exception_message = excinfo.value.args[0]
        assert exception_message == 'Stack is empty'

        # Non-empty Stack Error
        with pytest.raises(StackError) as excinfo:
            postfix_eval('1 2 3 + =')
        exception_message = excinfo.value.args[0]
        assert exception_message == 'Stack is not empty'

        # Unknown token Error
        with pytest.raises(TokenError) as excinfo:
            postfix_eval('a b + =')
        exception_message = excinfo.value.args[0]
        assert exception_message == "Unknown token: a"
        

    def test_do_math_simple(self):
        '''Test simple math expressions'''
        assert do_math('+', 2, 3) == 5
        assert do_math('-', 2, 3) == -1
        assert do_math('*', 2, 3) == 6
        assert do_math('/', 2, 3) == pytest.approx(0.6666, 0.001)
        with pytest.raises(Exception) as excinfo:
            do_math('/', 2, 0)
        exception_message = excinfo.value.args[0]
        assert exception_message == 'division by zero'

    def test_do_math_simple_error(self):
        '''Test incorrect simple math expressions'''
        for symbol in [1, 'a', ' ']:
            with pytest.raises(Exception) as excinfo:
                do_math(symbol, '+', 2)
            exception_message = excinfo.value.args[0]
            assert exception_message == 'Unknown operation: {}'.format(symbol)

    def test_do_math_advanced(self):
        '''Test simple math expressions'''
        assert do_math('//', 2, 3) == 0
        assert do_math('//', 3, 2) == 1
        assert do_math('**', 2, 3) == 8
        with pytest.raises(Exception) as excinfo:
            do_math('//', 2, 0)
        exception_message = excinfo.value.args[0]
        assert exception_message == 'integer division or modulo by zero'

if __name__ == '__main__':
    pytest.main(['test_rpn.py'])
