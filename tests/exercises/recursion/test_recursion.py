#!/usr/bin/env python3
"""
`recursion` testing

@authors: Roman Yasinovskyy
@version: 2021.3
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
    from src.exercises.recursion import gcd
    from src.exercises.recursion import diamond_ite
    from src.exercises.recursion import diamond_rec
    from src.exercises.recursion import hourglass_ite
    from src.exercises.recursion import hourglass_rec


@pytest.mark.parametrize(
    "number1, number2, result", [(1861, 2021, 1), (1860, 2020, 20)]
)
def test_gcd(number1, number2, result):
    """Testing gcd method"""
    assert gcd(number1, number2) == result


@pytest.mark.parametrize(
    "n, expected_output",
    [
        (
            2,
            " * " + 
            "***" + 
            " * ",
        ),
        (
            5,
            "    *    " + 
            "   ***   " + 
            "  *****  " + 
            " ******* " + 
            "*********" + 
            " ******* " + 
            "  *****  " + 
            "   ***   " + 
            "    *    ",
        ),
    ],
)
def test_diamond_ite(n, expected_output, capsys):
    """Testing diamond_ite method"""
    diamond_ite(n)
    out, _ = capsys.readouterr()
    assert "".join([line.strip("\n").strip("\r") for line in out]) == expected_output


@pytest.mark.parametrize(
    "n, expected_output",
    [
        (
            2,
            " * " + 
            "***" + 
            " * ",
        ),
        (
            5,
            "    *    " + 
            "   ***   " + 
            "  *****  " + 
            " ******* " + 
            "*********" + 
            " ******* " + 
            "  *****  " + 
            "   ***   " + 
            "    *    ",
        ),
    ],
)
def test_diamond_rec(n, expected_output, capsys):
    """Testing diamond_rec method"""
    diamond_rec(n)
    out, _ = capsys.readouterr()
    assert "".join([line.strip("\n").strip("\r") for line in out]) == expected_output


@pytest.mark.parametrize(
    "n, expected_output",
    [
        (
            2,
            "***" + 
            " * " + 
            "***",
        ),
        (
            5,
            "*********" + 
            " ******* " + 
            "  *****  " + 
            "   ***   " + 
            "    *    " + 
            "   ***   " + 
            "  *****  " + 
            " ******* " + 
            "*********",
        ),
    ],
)
def test_hourglass_ite(n, expected_output, capsys):
    """Testing hourglass_ite method"""
    hourglass_ite(n)
    out, _ = capsys.readouterr()
    assert "".join([line.strip("\n").strip("\r") for line in out]) == expected_output


@pytest.mark.parametrize(
    "n, expected_output",
    [
        (
            2,
            "***" + 
            " * " + 
            "***",
        ),
        (
            5,
            "*********" + 
            " ******* " + 
            "  *****  " + 
            "   ***   " + 
            "    *    " + 
            "   ***   " + 
            "  *****  " + 
            " ******* " + 
            "*********",
        ),
    ],
)
def test_hourglass_rec(n, expected_output, capsys):
    """Testing hourglass_rec method"""
    hourglass_rec(n)
    out, _ = capsys.readouterr()
    assert "".join([line.strip("\n").strip("\r") for line in out]) == expected_output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
