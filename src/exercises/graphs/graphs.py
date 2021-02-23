#!/usr/bin/env python3
"""
Exercise `graphs` implementation

@author:
"""

import heapq
import sys


class Vertex:
    """Graph vertex"""

    def __init__(self, key):
        """Graph constructor"""
        self._key = key
        self._neighbors = {}
        self._distance = sys.maxsize
        self._previous = None
        self._color = "white"
        self._discovered = 0
        self._colored = 0

    def get_key(self):
        """Get node key"""
        return self._key

    key = property(get_key)

    def get_neighbor(self, other: str):
        """Get one adjacent node (neighbor)"""
        return self._neighbors.get(other, None)

    def set_neighbor(self, other: str, weight: int = 0):
        """Add neighbor"""
        self._neighbors[other] = weight

    neighbor = property(get_neighbor, set_neighbor)

    def get_all_neighbors(self):
        """Get all adjacent nodes (neighbors)"""
        return self._neighbors.keys()

    all_neighbors = property(get_all_neighbors)

    def get_distance(self):
        """Get distance"""
        return self._distance

    def set_distance(self, distance: int):
        """Set distance"""
        self._distance = distance

    distance = property(get_distance, set_distance)

    def get_previous(self):
        """Get previous"""
        return self._previous

    def set_previous(self, previous):
        """Set previous"""
        self._previous = previous

    previous = property(get_previous, set_previous)

    def get_color(self):
        """Get color"""
        return self._color

    def set_color(self, color: str):
        """Get color"""
        self._color = color

    color = property(get_color, set_color)

    def get_discovery(self):
        """Get discovery time"""
        return self._discovered

    def set_discovery(self, t):
        """Set discovery time"""
        self._discovered = t

    discovered = property(get_discovery, set_discovery)

    def get_finish(self):
        """Get finish time"""
        return self._colored

    def set_finish(self, t):
        """Set finish time"""
        self._colored = t

    finished = property(get_finish, set_finish)

    def get_weight(self, other):
        """Get edge weight"""
        return self._neighbors[other]

    def __str__(self):
        """Print a vertex"""
        return (
            "Neighbors of "
            + str(self._key)
            + ": "
            + str([x.key for x in self._neighbors])
        )

    def __lt__(self, other):
        return self._key < other.key


class Graph:
    """Graph class"""

    def __init__(self):
        """Create a new, empty graph"""
        self.vertices = {}
        self.time = 0

    def add_vertex(self, key: str):
        """Add an instance of Vertex to the graph"""
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def add_edge(self, from_vertex: str, to_vertex: str, weight=0):
        """Add a new, weighted, directed edge to the graph that connects two vertices"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].set_neighbor(self.vertices[to_vertex], weight)

    def get_vertex(self, key: str):
        """Find the vertex in the graph named vert_key"""
        return self.vertices.get(key, None)

    def get_vertices(self):
        """Return the list of all vertices in the graph"""
        return self.vertices.keys()

    def reset_distances(self):
        """Reset distances to test Dijkstra's"""
        for v in self:
            v.set_distance(sys.maxsize)

    def __contains__(self, key: str):
        """Return True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise"""
        return key in self.vertices

    def __iter__(self):
        """Iterator"""
        return iter(self.vertices.values())

    def __len__(self):
        """Graph's size"""
        raise NotImplementedError

    def hub(self):
        """Find a Vertex with the most outgoing edges"""
        raise NotImplementedError

    def size(self):
        """Find the number of edges in a Graph"""
        raise NotImplementedError

    def dijkstra(self, start: Vertex) -> None:
        """Dijkstra's shortest path algorithm"""
        start.distance = 0
        pq = [[start.distance, start]]
        heapq.heapify(pq)
        while len(pq) > 0:
            current_vertex = heapq.heappop(pq)[1]
            for next_vertex in current_vertex.all_neighbors:
                new_distance = current_vertex.distance + current_vertex.get_weight(
                    next_vertex
                )
                if new_distance < next_vertex.distance:
                    next_vertex.distance = new_distance
                    next_vertex.previous = current_vertex
                    found = False
                    for v in pq:
                        if v[1].key == next_vertex.key:
                            v[0] = next_vertex.distance
                            heapq.heapify(pq)
                            found = True
                    if not found:
                        heapq.heappush(pq, [next_vertex.distance, next_vertex])

