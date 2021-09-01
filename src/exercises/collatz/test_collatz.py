#!/usr/bin/env python3
"""
`collatz` testing

@authors: Roman Yasinovskyy
@version: 2021.8
"""

import pytest

from collatz import collatz


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "number, steps",
    [
        (1, 0),
        (2, 1),
        (3, 7),
        (25, 23),
        (26, 10),
        (27, 111),
        (2021, 63),
        (9780657630, 1132),
        (942488749153153, 1862),
        (931386509544713451, 2283),
    ],
)
def test_collatz_steps(number, steps):
    """Test stopping distance"""
    assert collatz(number)[0] == steps


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "number, max_point",
    [
        (1, 1),
        (2, 2),
        (3, 16),
        (25, 88),
        (26, 40),
        (27, 9232),
        (2021, 6064),
        (77671, 1570824736),
        (704511, 56991483520),
        (931386509544713451, 428671993798064720840020),
    ],
)
def test_collatz_max(number, max_point):
    """Test highest point"""
    assert collatz(number)[1] == max_point


if __name__ == "__main__":
    pytest.main(["-v", __file__])
