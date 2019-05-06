#!/usr/bin/env python3
"""
Testing the module movies
@authors: Roman Yasinovskyy, Karina Hoff
@updated: 2019
"""

import pytest
from src.projects.kevinbacon import read_file


class TestMoviesMethods:
    """Testing module movies"""

    def setup_class(self):
        """Setting up"""
        self.graph = read_file("data/projects/kevinbacon/movie_actors_test.txt")
        kevin = self.graph.get_vertex("Kevin Bacon")
        self.graph.bfs(kevin)

    def test_read_file_vertices(self):
        """Testing graph size (verices)"""
        assert len(self.graph) == 7

    def test_read_file_edges(self):
        """Testing graph size (edges)"""
        connections = 0
        for input_file in self.graph:
            connections += len(input_file.get_neighbors())
        assert connections == 18

    def test_bfs(self):
        """Testing graph BFS"""
        assert self.graph.get_vertex("Allen").get_distance() == 1
        assert self.graph.get_vertex("Brad").get_distance() == 2
        assert self.graph.get_vertex("Grace").get_distance() == 3

    def test_traversal(self):
        """Testing graph traversal"""
        road_to_kb = []
        input_file = self.graph.get_vertex("David")
        while input_file:
            road_to_kb.append(input_file.get_key())
            input_file = input_file.get_previous()
        assert " ".join(road_to_kb) == "David Tom Jennifer Kevin Bacon"


if __name__ == "__main__":
    pytest.main(["-vv", "test_kevinbacon.py"])
