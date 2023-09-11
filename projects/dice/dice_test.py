#!/usr/bin/env python3
"""
`dice` testing

@authors: Roman Yasinovskyy
@version: 2023.9
"""

import random

import pytest

from dice import Cup, Die, FrozenDie

random.seed(42)


@pytest.fixture(name="die")
def fixture_die():
    """A simple die with a random value"""
    return Die(range(1, 7))


@pytest.fixture(name="frozen_die")
def fixture_frozen_die():
    """A frozen die that cannot be rolled"""
    return FrozenDie(range(1, 7))


@pytest.fixture(name="cup")
def fixture_cup():
    """A cup with two standard dice"""
    return Cup(2, 6)


@pytest.fixture(name="yahtzee")
def fixture_yahtzee():
    """A cup with 5 standard dice"""
    return Cup(5, 6)


def test_die_get_value(die):
    """Testing value getter"""
    try:
        assert die.value == "1"
        print("exact match", end=" ")
    except AssertionError:
        assert die.value in range(1, 7)
        print("close enough", end=" ")


def test_die_set_value(die):
    """Testing value setter"""
    with pytest.raises(ValueError) as excinfo:
        die.value = 1
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "You must roll the die to change its value"


def test_die_str(capsys, die):
    """Testing die.__str__method"""
    print(die)
    out, _ = capsys.readouterr()
    try:
        assert int(out.strip()) == 1
        print("exact match", end=" ")
    except AssertionError:
        assert int(out.strip()) in range(1, 7)
        print("close enough", end=" ")


def test_die_roll(die):
    """Testing die roll method"""
    try:
        assert die.roll() == 1
        print("exact match", end=" ")
    except AssertionError:
        assert die.value in range(1, 7)
        print("close enough", end=" ")


def test_frozen_die_roll(frozen_die):
    """Testing frozen die roll method"""
    frozen_die.frozen = True
    check_value = frozen_die.value
    for _ in range(100):
        frozen_die.roll()
        assert frozen_die.value == check_value


def test_cup_shake(cup):
    """Testing shake method"""
    check_value = ", ".join([str(d) for d in cup])
    for i in range(100):
        cup.shake()
        if ", ".join([str(d) for d in cup]) != check_value:
            if 0 == i:
                assert True
                break
    else:
        assert False, "The cup did not change after vigorous shaking"


def test_cup_str(capsys, cup):
    """Testing cup.__str__method"""
    print(cup)
    out, _ = capsys.readouterr()
    try:
        assert out.strip() == "[3, 2]"
        print("exact match", end=" ")
    except AssertionError:
        for a_die in cup:
            assert int(a_die.value) in range(1, 7)
        print("close enough", end=" ")


def test_cup_add(cup):
    """Testing add method"""
    cup.add(Die(range(1, 7)))
    try:
        assert str(cup) == "[2, 2, 6]"
        print("exact match", end=" ")
    except AssertionError:
        for a_die in cup:
            assert int(a_die.value) in range(1, 7)
        print("close enough", end=" ")


def test_cup_remove(cup):
    """Testing remove method"""
    cup.remove(0)
    try:
        assert str(cup) == "[6]"
        print("exact match", end=" ")
    except AssertionError:
        for a_die in cup:
            assert int(a_die.value) in range(1, 7)
        print("close enough", end=" ")


def test_cup_roll(yahtzee):
    """Testing cup roll method"""
    check_value = [d.value for d in yahtzee]
    for _ in range(100):
        yahtzee.roll(1, 3, 5)
        new_value = [d.value for d in yahtzee]
        assert new_value[1::2] == check_value[1::2]


if __name__ == "__main__":
    pytest.main(["-v", __file__])
