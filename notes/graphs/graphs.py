import sys

class Vertex:
    def __init__(self, key):
        self._key = key
        self._neighbors = {}
        self._distance = sys.maxsize
        self._previous = None
        self._color = "white"

    def get_key(self):
        return self._key

    def get_all_neighbors(self):
        return self._neighbors

    def get_neighbor(self, n):
        return self._neighbors.get(n, None)

    def set_neighbor(self, n, weight=0):
        self._neighbors[n] = weight

    def get_previous(self):
        return self._previous

    def set_previous(self, p):
        self._previous = p

    def get_distance(self):
        return self._distance

    def set_distance(self, d):
        self._distance = d

    def get_color(self):
        return self._color

    def set_color(self, c):
        self._color = c


class Graph:
    def __init__(self):
        self._vertices = {}

    def __contains__(self, key):
        """Return True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise"""
        return key in self._vertices

    def __iter__(self):
        """Iterator"""
        return iter(self._vertices.values())

    def __len__(self):
        """Graph's size"""
        return len(self._vertices)

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self._vertices[key] = new_vertex

    def add_edge(self, src_vertex, dst_vertex, weight=0):
        if src_vertex not in self._vertices:
            self.add_vertex(src_vertex)
        if dst_vertex not in self._vertices:
            self.add_vertex(dst_vertex)
        self._vertices[src_vertex].set_neighbor(self._vertices[dst_vertex], weight)

    def get_vertex(self, key):
        return self._vertices.get(key, None)

    def get_vertices(self):
        return self._vertices.keys()

    def bfs(self, start):
        start.set_distance(0)
        start.set_previous(None)
        q = [start]
        while q:
            current_vert = q.pop(0)
            for neigh in current_vert.get_all_neighbors():
                if neigh.get_color() == "white":
                    neigh.set_color("gray")
                    neigh.set_distance(current_vert.get_distance() + 1)
                    neigh.set_previous(current_vert)
                    q.append(neigh)
            current_vert.set_color("black")

        print("Done")
