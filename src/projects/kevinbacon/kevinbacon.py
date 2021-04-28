#!/usr/bin/env python3
"""
`kevinbacon` implementation

@authors: Roman Yasinovskyy
@version: 2021.4
"""

import sys
from typing import List

from pythonds3.graphs import Graph


def read_file(filename: str) -> Graph:
    """Build a graph from the file"""
    raise NotImplementedError


def find_max_kbn_actors(graph: Graph) -> List[str]:
    """Find actor(s) with the highest KBN value"""
    raise NotImplementedError
