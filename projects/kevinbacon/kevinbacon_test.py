#!/usr/bin/env python3
"""
`kevinbacon` testing

@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.11
"""

import pathlib

import pytest
from kevinbacon import find_max_kbn_actors, read_file


@pytest.fixture(scope="session")
def graph():
    """Setting up"""
    filename = "movie_actors_test.txt"
    if not pathlib.Path(filename).exists():
        filename = f"projects/kevinbacon/{filename}"
    g = read_file(filename)
    kevin = g.get_vertex("Kevin Bacon")
    g.bfs(kevin)
    return g


def test_read_file_vertices(graph):
    """Testing graph size (vertices)"""
    assert len(graph) == 7


def test_read_file_edges(graph):
    """Testing graph size (edges)"""
    assert sum([len(v.get_neighbors()) for v in graph]) == 18


def test_bfs(graph):
    """Testing graph BFS"""
    assert graph.get_vertex("Allen").distance == 1
    assert graph.get_vertex("Brad").distance == 2
    assert graph.get_vertex("Grace").distance == 3


def test_traversal(graph):
    """Testing graph traversal"""
    road_to_kb = []
    vertex = graph.get_vertex("David")
    while vertex:
        road_to_kb.append(vertex.key)
        vertex = vertex.previous
    assert " -> ".join(road_to_kb) == "David -> Tom -> Jennifer -> Kevin Bacon"


def test_max_kbn(graph):
    """Testing max_kbn"""
    max_kbn_list = find_max_kbn_actors(graph)
    assert len(max_kbn_list) == 2


if __name__ == "__main__":
    pytest.main(["-v", __file__])
