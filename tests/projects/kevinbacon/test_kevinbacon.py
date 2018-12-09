"""
Testing the module movies
Karina Hoff, 2018
"""

#!/usr/bin/python3


import pytest
from projects.kevinbacon import read_file


class TestMoviesMethods:
    """Testing module movies"""

    def setup_class(self):
        """Setting up"""
        self.graph = read_file("data/projects/kevinbacon/movie_actors_test.txt")
        kevin = self.graph.get_vertex("Kevin Bacon")
        self.graph.bfs(kevin)


    def test_read_file_vertices(self):
        assert len(self.graph) == 7
    
    def test_read_file_edges(self):
        connections = 0
        for v in self.graph:
            connections += len(v.get_all_neighbors())
            # connections += len(v.get_neighbors())
        assert connections == 18

    def test_bfs(self):
        assert self.graph.get_vertex("Allen").get_distance() == 1
        assert self.graph.get_vertex("Tom").get_distance() == 2
        assert self.graph.get_vertex("David").get_distance() == 3

    def test_traversal(self):
        road_to_kb = []
        v = self.graph.get_vertex("David")
        while v:
            road_to_kb.append(v.get_key())
            v = v.get_previous()
        assert " ".join(road_to_kb) == "David Tom Jennifer Kevin Bacon"

if __name__ == "__main__":
    pytest.main(["test_kevinbacon.py"])
