#!/usr/bin/env python3
"""
Exercise `hashing` testing

@authors: Roman Yasinovskyy
@version: 2021.2
"""

import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.exercises.hashing import (
        hash_remainder,
        hash_mid_sqr,
        hash_folding,
        hash_str,
        hash_str_weighted,
    )


@pytest.mark.parametrize(
    "keys, size, expected",
    [
        ([10, 21, 32, 18, 17, 19, 42, 23, 99], 16, [10, 5, 0, 2, 1, 3, 10, 7, 3]),
        ([54, 26, 93, 17, 77, 31], 11, [10, 4, 5, 6, 0, 9]),
    ],
)
def test_hash_remainder(keys, size, expected):
    """Testing simple remainder hashing"""
    assert [hash_remainder(x, size) for x in keys] == expected


@pytest.mark.parametrize(
    "keys, size, expected",
    [
        ([10, 21, 32, 18, 17, 19, 42, 23, 99], 16, [10, 12, 2, 0, 12, 4, 12, 4, 0]),
        ([54, 26, 93, 17, 77, 31], 11, [3, 1, 9, 6, 4, 8]),
    ],
)
def test_hash_hash_mid_sqr(keys, size, expected):
    """Testing mid-square hashing"""
    assert [hash_mid_sqr(x, size) for x in keys] == expected


@pytest.mark.parametrize(
    "keys, size, expected",
    [
        (["563-555-1234", "800-555-8080", "888-555-0000"], 16, [0, 12, 4]),
        (["436-555-4601"], 11, [1]),
    ],
)
def test_hash_folding(keys, size, expected):
    """Testing folding hashing"""
    assert [hash_folding(x, size) for x in keys] == expected


@pytest.mark.parametrize(
    "keys, size, expected",
    [
        (
            [
                "pavel",
                "bruce",
                "talia",
                "harvey",
                "jim",
                "alfred",
                "lucius",
                "jonathan",
                "bane",
            ],
            16,
            [8, 1, 11, 15, 0, 14, 5, 3, 6],
        ),
        (["algorithm", "logarithm"], 11, [10, 10]),
    ],
)
def test_hash_str(keys, size, expected):
    """Testing string hashing"""
    assert [hash_str(x, size) for x in keys] == expected


@pytest.mark.parametrize(
    "keys, size, expected",
    [
        (
            [
                "pavel",
                "bruce",
                "talia",
                "harvey",
                "jim",
                "alfred",
                "lucius",
                "jonathan",
                "bane",
            ],
            16,
            [12, 9, 8, 8, 3, 6, 9, 14, 12],
        ),
        (["algorithm", "logarithm"], 11, [8, 2]),
    ],
)
def test_hash_str_weighted(keys, size, expected):
    """Testing weighted string hashing"""
    assert [hash_str_weighted(x, size) for x in keys] == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
