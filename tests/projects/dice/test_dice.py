'''
Testing the classes Die and Cup
Roman Yasinovskyy, 2017
'''
#!/usr/bin/env python3


import pytest
import random
from projects.dice.dice import Die, FrozenDie, Cup


class TestDiceMethods:
    '''Testing module Dice'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        random.seed(42)
        self.die = Die(range(1, 7))
        self.frozen_die = FrozenDie(range(1, 7))
        self.cup = Cup(2, 6)
        self.yahtzee = Cup(5, 6)

    def test_die_get_value(self):
        '''Testing value getter'''
        assert self.die.value == 6

    # Raises ValueError as a die's value cannot be set
    def test_die_set_value(self):
        '''Testing value setter'''
        with pytest.raises(ValueError) as excinfo:
            self.die.value = 1
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "You must roll the die to change its value"

    def test_die_str(self, capsys):
        '''Testing die.__str__method'''
        print(self.die)
        out, err = capsys.readouterr()
        assert out.strip() == '6'

    def test_die_roll(self):
        '''Testing die roll method'''
        assert self.die.roll() == 1

    def test_frozen_die_roll(self):
        '''Testing frozen die roll method'''
        self.frozen_die = FrozenDie(range(1, 7))
        assert self.frozen_die.value == 1
        self.frozen_die.frozen = True
        for _ in range(10):
            self.frozen_die.roll()
            assert self.frozen_die.value == 1

    def test_cup_shake(self):
        '''Testing shake method'''
        self.cup.shake()
        assert str(self.cup) == '[1, 6]'

    def test_cup_str(self, capsys):
        '''Testing cup.__str__method'''
        print(self.cup)
        out, err = capsys.readouterr()
        assert out.strip() == '[1, 6]'

    def test_cup_add(self):
        '''Testing add method'''
        self.cup.add(Die(range(1, 7)))
        assert str(self.cup) == '[1, 6, 1]'

    def test_cup_remove(self):
        '''Testing remove method'''
        self.cup.remove(0)
        assert str(self.cup) == '[6]'

    def test_cup_roll(self):
        '''Testing cup roll method'''
        assert str(self.yahtzee) == '[3, 2, 2, 2, 6]'
        self.yahtzee.shake()
        assert str(self.yahtzee) == '[1, 6, 6, 5, 1]'
        self.yahtzee.roll(1, 3, 5)
        assert str(self.yahtzee) == '[5, 6, 4, 5, 1]'


if __name__ == '__main__':
    pytest.main(['test_dice.py'])
