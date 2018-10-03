'''
Testing customproblem
'''
#!/usr/bin/python3

import pytest


class TestCustomProblemMethods:
    '''Testing module customproblem'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        pass

    def test_a(self):
        '''Testing something'''
        pass

    def test_b(self):
        '''Testing something'''
        pass

    def test_c(self):
        '''Testing something'''
        pass

    def test_d(self):
        '''Testing something'''
        pass

    def test_e(self):
        '''Testing something'''
        pass

    def test_f(self):
        '''Testing something'''
        pass

    def test_g(self):
        '''Testing something'''
        pass

    def test_h(self):
        '''Testing something'''
        pass

    def test_i(self):
        '''Testing something'''
        pass

    def test_j(self):
        '''Testing something'''
        pass


if __name__ == '__main__':
    pytest.main(['test_customproblem.py'])
