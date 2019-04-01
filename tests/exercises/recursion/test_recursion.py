#!/usr/bin/env python3
"""
Testing the Recursion
@authors: Roman Yasinovskyy
@updated: 2019
"""

import pytest
from src.exercises.recursion.recursion import gcd
from src.exercises.recursion.recursion import hourglass_ite
from src.exercises.recursion.recursion import diamond_ite
from src.exercises.recursion.recursion import hourglass_rec
from src.exercises.recursion.recursion import diamond_rec


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
    pytest.main(["-vv", "test_recursion.py"])
