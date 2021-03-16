#!/usr/bin/env python3
"""
`recursion` package

@authors: Roman Yasinovskyy
@version: 2021.3
"""

from .recursion_functions import gcd
from .recursion_functions import diamond_ite
from .recursion_functions import diamond_rec
from .recursion_functions import hourglass_ite
from .recursion_functions import hourglass_rec


__all__ = [
    "gcd",
    "diamond_ite",
    "diamond_rec",
    "hourglass_ite",
    "hourglass_rec",
]
