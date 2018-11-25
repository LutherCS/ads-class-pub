"""
Testing the Graphs module
Roman Yasinovskyy, 2018
"""

import pytest
from exercises.graphs import Vertex
from exercises.graphs import Graph


class TestGraphMethods:
    """Testing the Graph module"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.g = Graph()
        self.g.add_edge('t', 'u', 2)
        self.g.add_edge('t', 'v', 4)
        self.g.add_edge('t', 'y', 7)
        self.g.add_edge('u', 't', 2)
        self.g.add_edge('u', 'v', 3)
        self.g.add_edge('u', 'w', 3)
        self.g.add_edge('v', 't', 4)
        self.g.add_edge('v', 'u', 3)
        self.g.add_edge('v', 'w', 4)
        self.g.add_edge('v', 'x', 3)
        self.g.add_edge('v', 'y', 8)
        self.g.add_edge('w', 'u', 3)
        self.g.add_edge('w', 'v', 4)
        self.g.add_edge('w', 'x', 6)
        self.g.add_edge('x', 'v', 3)
        self.g.add_edge('x', 'w', 6)
        self.g.add_edge('x', 'y', 6)
        self.g.add_edge('x', 'z', 8)
        self.g.add_edge('y', 't', 7)
        self.g.add_edge('y', 'v', 8)
        self.g.add_edge('y', 'x', 6)
        self.g.add_edge('y', 'z', 12)
        self.g.add_edge('z', 'x', 8)
        self.g.add_edge('z', 'y', 12)


    def test_dijkstra_t(self):
        """Testing Dijkstra's Shortest Path algorithm"""
        self.g.dijkstra(self.g.get_vertex('t'))
        expected = {'t': 0, 'u': 2, 'v': 4, 'w': 5, 'x': 7, 'y': 7, 'z': 15}
        for v in self.g.vertices:
            assert self.g.vertices[v].distance == expected[v]

    def test_dijkstra_x(self):
        """Testing Dijkstra's Shortest Path algorithm"""
        self.g.dijkstra(self.g.get_vertex('x'))
        expected = {'t': 7, 'u': 6, 'v': 3, 'w': 6, 'x': 0, 'y': 6, 'z': 8}
        for v in self.g.vertices:
            assert self.g.vertices[v].distance == expected[v]

    def test_len(self):
        """Testing __len__() method"""
        assert len(self.g) == 7

    def test_size(self, capsys):
        """Testing size() method"""
        assert self.g.size() == 12

    def test_hub(self):
        """Testing hub() method"""
        assert self.g.hub() == "v"

if __name__ == "__main__":
    pytest.main(["test_graphs.py"])
