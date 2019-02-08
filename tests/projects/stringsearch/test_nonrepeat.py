#!/usr/bin/env python3
"""
Testing the module stringsearch
@authors: Roman Yasinovskyy, Karina Hoff
@updated: 2019
"""

from string import ascii_lowercase
from time import time
import pytest
from src.projects.stringsearch import find_non_repeat_count

TIME_LIMIT = 2


@pytest.mark.parametrize(
    "a_string, an_answer",
    [("abxaby", "x"), ("y", "y"), ("z" * 1_000_000 + "a", "a"), (ascii_lowercase, "a")],
)
def test_find_non_repeat_count(a_string, an_answer):
    """Test find_non_repeat_count function"""
    start = time()
    result = find_non_repeat_count(a_string)
    end = time()
    assert result == an_answer
    assert end - start < TIME_LIMIT


@pytest.mark.parametrize("str_len", [10, 100, 10000, 1_000_000])
def test_find_non_repeat_count_long(str_len):
    """Test find_non_repeat_count function on a long string"""
    a_string = "".join([chr(n) for n in range(1, str_len)])
    start = time()
    result = find_non_repeat_count(a_string)
    end = time()
    assert result == chr(1)
    assert end - start < TIME_LIMIT


@pytest.mark.parametrize("a_string", ["aa", "bbb", "", "z" * 1_000_000])
def test_find_non_repeat_count_error(a_string):
    """Test find_non_repeat_count function error handling"""
    with pytest.raises(ValueError) as excinfo:
        find_non_repeat_count(a_string)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "No non-repeating characters"


if __name__ == "__main__":
    pytest.main(["test_nonrepeat.py"])
