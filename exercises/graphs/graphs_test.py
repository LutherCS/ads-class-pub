#!/usr/bin/env python3
"""
`graphs` testing

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import pytest

from graphs import Graph


@pytest.fixture(name="network_graph")
def graph_fixture():
    """Setting up"""
    g = Graph()
    g.add_edge("t", "u", 2)
    g.add_edge("t", "v", 4)
    g.add_edge("t", "y", 7)
    g.add_edge("u", "t", 2)
    g.add_edge("u", "v", 3)
    g.add_edge("u", "w", 3)
    g.add_edge("v", "t", 4)
    g.add_edge("v", "u", 3)
    g.add_edge("v", "w", 4)
    g.add_edge("v", "x", 3)
    g.add_edge("v", "y", 8)
    g.add_edge("w", "u", 3)
    g.add_edge("w", "v", 4)
    g.add_edge("w", "x", 6)
    g.add_edge("x", "v", 3)
    g.add_edge("x", "w", 6)
    g.add_edge("x", "y", 6)
    g.add_edge("x", "z", 8)
    g.add_edge("y", "t", 7)
    g.add_edge("y", "v", 8)
    g.add_edge("y", "x", 6)
    g.add_edge("y", "z", 12)
    g.add_edge("z", "x", 8)
    g.add_edge("z", "y", 12)

    return g


@pytest.mark.skip("Paper-based task")
@pytest.mark.parametrize(
    "start, expected",
    [
        ("t", {"t": 0, "u": 2, "v": 4, "w": 5, "x": 7, "y": 7, "z": 15}),
        ("x", {"t": 7, "u": 6, "v": 3, "w": 6, "x": 0, "y": 6, "z": 8}),
    ],
)
def test_dijkstra_t(network_graph, start, expected):
    """Testing Dijkstra's Shortest Path algorithm"""
    network_graph.dijkstra(network_graph.get_vertex(start))
    for v in network_graph.vertices:
        assert network_graph.vertices[v].distance == expected[v]


def test_len(network_graph):
    """Testing __len__() method"""
    assert len(network_graph) == 7


def test_size(network_graph):
    """Testing size() method"""
    assert network_graph.size() == 12


def test_hub(network_graph):
    """Testing hub() method"""
    assert network_graph.hub() == "v"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
