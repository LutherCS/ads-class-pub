#!/usr/bin/env python3
"""
Testing the module stringsearch
@authors: Roman Yasinovskyy, Karina Hoff
@updated: 2019
"""

from string import ascii_lowercase
import pytest
from src.projects.stringsearch import find_non_repeat

TIME_LIMIT = 4


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "a_string, an_answer",
    [("abxaby", "x"), ("y", "y"), ("abxxbac", "x"), (ascii_lowercase, "a")],
)
def test_find_non_repeat(a_string, an_answer):
    """Testing simple cases"""
    result = find_non_repeat(a_string)
    assert result == an_answer


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("str_len", [10, 100, 10000, 1_000_000])
def test_find_non_repeat_long_beginning(str_len):
    """Testing long string with a non-repeating symbol at the beginning"""
    a_string = "".join([chr(n) for n in range(1, str_len)])
    result = find_non_repeat(a_string)
    assert result == chr(1)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("str_len", [10, 100, 10000, 1_000_000])
def test_find_non_repeat_long_end(str_len):
    """Testing long string with a non-repeating symbol at the end"""
    assert find_non_repeat("z" * str_len + "a") == "a"


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("a_string", ["aa", ""])
def test_find_non_repeat_error(a_string):
    """Testing a string without a non-repeating symbol"""
    with pytest.raises(ValueError) as excinfo:
        find_non_repeat(a_string)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "No non-repeating characters"


@pytest.mark.timeout(TIME_LIMIT)
def test_find_non_repeat_error_long():
    """Testing a long string without a non-repeating symbol"""
    with pytest.raises(ValueError) as excinfo:
        find_non_repeat("z" * 1_000_000)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "No non-repeating characters"


if __name__ == "__main__":
    pytest.main(["-vv", "test_nonrepeat.py"])
