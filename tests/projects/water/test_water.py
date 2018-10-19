'''
Testing the module water
Karina Hoff, 2018
'''

#!/usr/bin/python3
# pylint: disable=no-value-for-parameter, unused-variable

import pytest
from projects.water.water import State, search


class TestWaterMethods:
    '''Testing module water'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.s1 = State(1, 2)
        self.s2 = State(2, 0)
        self.s3 = State(1.0, 2.0)
        self.s4 = State(2.0, 0.0)
        
    def test_State_init(self):
        '''Testing State.__init__'''
        assert self.s1 is not None
        assert self.s2 is not None
        assert self.s3 is not None
        assert self.s4 is not None
        with pytest.raises(Exception) as excinfo:
            state = State()
        exception_message = excinfo.value.args[0]
        assert exception_message == "__init__() missing 2 required positional arguments: 'jug_1' and 'jug_2'"

    def test_State_eq(self):
        '''Testing State.__eq__'''
        assert self.s1 != self.s2
        assert not self.s3.__eq__(self.s4)

    def test_State_str(self):
        '''Testing State.__str__'''
        assert str(self.s1) == '(1, 2)'
        assert str(self.s2) == '(2, 0)'
        assert str(self.s3) == '(1.0, 2.0)'
        assert str(self.s4) == '(2.0, 0.0)'

    def test_State_clone(self):
        '''Testing State.__clone__'''        
        self.s5 = self.s1.clone()
        assert self.s1 == self.s5

    def test_State_fill_jug_1(self):
        '''Testing State.fill_jug_1'''
        self.s1.fill_jug_1()
        assert str(self.s1) == '(5, 2)'
        self.s1.fill_jug_1()
        assert str(self.s1) == '(5, 2)'

    def test_State_fill_jug_2(self):
        '''Testing State.__fill_jug_2__'''
        self.s1.fill_jug_2()
        assert str(self.s1) == '(1, 3)'
        self.s1.fill_jug_2()
        assert str(self.s1) == '(1, 3)'

    def test_State_empty_jug_1(self):
        '''Testing State.__empty_jug_1__'''
        self.s1.empty_jug_1()
        assert str(self.s1) == '(0, 2)'
        self.s1.empty_jug_1()
        assert str(self.s1) == '(0, 2)'

    def test_State_empty_jug_2(self):
        '''Testing State.__empty_jug_2__'''
        self.s1.empty_jug_2()
        assert str(self.s1) == '(1, 0)'
        self.s1.empty_jug_2()
        assert str(self.s1) == '(1, 0)'

    def test_State_pour_jug_1_to_jug_2(self):
        '''Testing State.pour_jug_1_to_jug_2'''
        self.s2.pour_jug_1_to_jug_2()
        assert str(self.s2) == '(0, 2)'
        self.s2.fill_jug_1()
        self.s2.pour_jug_1_to_jug_2()
        assert str(self.s2) == '(4, 3)'
    
    def test_State_pour_jug_2_to_jug_1(self):
        '''Testing State.pour_jug_2_to_jug_1'''
        self.s1.pour_jug_2_to_jug_1()
        assert str(self.s1) == '(3, 0)'
        self.s1.fill_jug_2()
        self.s1.pour_jug_2_to_jug_1()
        assert str(self.s1) == '(5, 1)'

    def test_search(self):
        '''Testing search'''
        result = []
        search(State(0, 0), State(4, 0), result)
        assert result[0] == State(0, 0)
        assert result[-1] == State(4, 0)
            

if __name__ == '__main__':
    pytest.main('test_water.py')
