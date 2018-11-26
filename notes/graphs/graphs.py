class Vertex:
    def __init__(self, key):
        self._key = key
        self._neighbors = {}
        self._distance = 100
        self._previous = None

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

class Graph:
    def __init__(self):
        self._vertices = {}
    
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self._vertices[key] = new_vertex
    
    def add_edge(self, src_vertex, dst_vertex, weight=0):
        if src_vertex not in self._vertices:
            self.add_vertex(src_vertex)
        if dst_vertex not in self._vertices:
            self.add_vertex(dst_vertex)
        self._vertices[src_vertex].set_neighbor(dst_vertex, weight)
    
    def get_vertex(self, key):
        return self._vertices.get(key, None)

    def get_vertices(self):
        return self._vertices.keys()
