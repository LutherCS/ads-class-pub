#!/usr/bin/env python3
"""
Exercise `recursion` import statement

@authors: Roman Yasinovskyy
@version: 2021.2
"""

from .recursion_functions import gcd
from .recursion_functions import hourglass_ite
from .recursion_functions import diamond_ite
from .recursion_functions import hourglass_rec
from .recursion_functions import diamond_rec


__all__ = [
    "gcd",
    "hourglass_ite",
    "diamond_ite",
    "hourglass_rec",
    "diamond_rec",
]
