#!/usr/bin/env python3
"""
`wordladder` testing

@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.4
"""

import importlib
import pathlib
import sys
from typing import List, Set

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.wordladder import Solver


@pytest.fixture
def solver():
    return Solver("data/projects/wordladder/words.txt")


def test_init(solver):
    """Test __init__ function"""
    assert len(solver.words3) == 1294
    assert len(solver.words4) == 4994
    assert len(solver.words5) == 5757


def test_init_error():
    """Test __init__ function error handling"""
    with pytest.raises(Exception) as excinfo:
        solver = Solver()  # pylint: disable=no-value-for-parameter, unused-variable
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "__init__() missing 1 required positional argument: 'filename'"
    )


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("hello", "hello", 0),
        ("hello", "Hello", 1),
        ("tenor", "tutor", 2),
        ("hello", "hippo", 3),
        ("hello", "olleh", 4),
        ("xenon", "jaded", 5),
    ],
)
def test_distance(solver, word1: str, word2: str, expected: int):
    """Test distance function"""
    assert solver.distance(word1, word2) == expected


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("hello", "hell"),
        ("hell", "elk"),
    ],
)
def test_distance_error(solver, word1, word2):
    """Test distance function error handling"""
    with pytest.raises(ValueError) as excinfo:
        solver.distance(word1, word2)
    exception_message = excinfo.value.args[0]
    assert exception_message == "Must use words of the same length"


@pytest.mark.parametrize(
    "word, all_words, used_words, expected",
    [
        (
            "elk",
            {"elf", "eld", "ilk", "elt", "eli", "els", "alk", "elm", "elb", "ell"},
            {"elf", "ilk", "eli", "elm", "elb"},
            ["alk", "eld", "ell", "els", "elt"],
        ),
        ("hello", {"jello", "happy"}, set(), ["jello"]),
        ("hello", {"jello", "happy"}, {"jello"}, []),
        (
            "terse",
            {"tense", "stone", "verse", "water", "terce"},
            {"tense", "merse"},
            ["terce", "verse"],
        ),
    ],
)
def test_diff_by_one_all(
    solver, word: str, all_words: Set[str], used_words: Set[str], expected: List[str]
):
    """Testing diff_by_one_all function"""
    assert sorted(solver.diff_by_one_all(word, all_words, used_words)) == expected


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("elk", "elf"),
        ("elf", "elk"),
        ("odd", "peg"),
        ("tar", "pit"),
        ("milk", "mint"),
        ("memo", "koko"),
        ("myxo", "zuza"),
        ("snob", "rynd"),
        ("tenor", "xenon"),
        ("start", "spark"),
        ("camel", "amigo"),
        ("water", "stone"),
    ],
)
def test_build_ladder(solver, word1: str, word2: str):
    """Testing build_ladder function"""
    assert solver.build_ladder(word1, word2)


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("abc", "xyz"),
        ("gizmo", "mulch"),
        ("tutor", "xenon"),
        ("peace", "piece"),
    ],
)
def test_no_ladder(solver, word1: str, word2: str):
    """Testing build_ladder function"""
    assert not solver.build_ladder(word1, word2)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
