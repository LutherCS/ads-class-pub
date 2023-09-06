#!/usr/bin/env python3
"""
`collatz` testing

@authors: Roman Yasinovskyy
@version: 2023.9
"""

import pytest

from collatz import collatz


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "number, steps",
    [
        (1, 1),
        (2, 2),
        (3, 8),
        (25, 24),
        (26, 11),
        (27, 112),
        (42, 9),
        (1861, 38),
        (1862, 38),
        (9780657630, 1133),
        (942488749153153, 1863),
        (931386509544713451, 2284),
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
        (42, 64),
        (1861, 5584),
        (1862, 4192),
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
