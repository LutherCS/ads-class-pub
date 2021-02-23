#!/usr/bin/env python3
"""
Exercise `recursion` testing

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
    from src.exercises.recursion import gcd
    from src.exercises.recursion import hourglass_ite
    from src.exercises.recursion import diamond_ite
    from src.exercises.recursion import hourglass_rec
    from src.exercises.recursion import diamond_rec


class TestRecursionMethods:
    """Testing exercise recursion"""

    def test_gcd(self):
        """Testing gcd method"""
        assert gcd(1860, 2020) == 20
        assert gcd(1861, 2019) == 1

    def test_hourglass_ite(self, capsys):
        """Testing hourglass_ite method"""
        expected_output = (
            "*********\n"
            + " ******* \n"
            + "  *****  \n"
            + "   ***   \n"
            + "    *    \n"
            + "   ***   \n"
            + "  *****  \n"
            + " ******* \n"
            + "*********"
        )
        hourglass_ite(5)
        out, _ = capsys.readouterr()
        assert out.strip() == expected_output

    def test_diamond_ite(self, capsys):
        """Testing diamond_ite method"""
        expected_output = (
            "*    \n"
            + "   ***   \n"
            + "  *****  \n"
            + " ******* \n"
            + "*********\n"
            + " ******* \n"
            + "  *****  \n"
            + "   ***   \n"
            + "    *"
        )
        diamond_ite(5)
        out, _ = capsys.readouterr()
        assert out.strip() == expected_output

    def test_hourglass_rec(self, capsys):
        """Testing hourglass_rec method"""
        expected_output = (
            "*********\n"
            + " ******* \n"
            + "  *****  \n"
            + "   ***   \n"
            + "    *    \n"
            + "   ***   \n"
            + "  *****  \n"
            + " ******* \n"
            + "*********"
        )
        hourglass_rec(5)
        out, _ = capsys.readouterr()
        assert out.strip() == expected_output

    def test_diamond_rec(self, capsys):
        """Testing diamond_rec method"""
        expected_output = (
            "*    \n"
            + "   ***   \n"
            + "  *****  \n"
            + " ******* \n"
            + "*********\n"
            + " ******* \n"
            + "  *****  \n"
            + "   ***   \n"
            + "    *"
        )
        diamond_rec(5)
        out, _ = capsys.readouterr()
        assert out.strip() == expected_output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
