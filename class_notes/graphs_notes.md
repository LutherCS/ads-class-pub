

```python
import sys
class Vertex:
    """Graph vertex"""
    def __init__(self, key):
        """Graph constructor"""
        # Vertex name
        self.key = key
        # Adjucent vertices
        self.neighbors = {}
        # Distance to the source
        self.distance = sys.maxsize
        # Predecessor
        self.previous = None
        # Color (for BFS)
        self.color = "white"
        # Discovery time (for DFS)
        self.disc_time = 0
        # Closing time (for DFS)
        self.fin_time = 0

    def get_key(self):
        """Get node key"""
        return self.key

    def get_neighbor(self, other):
        """Get one adjacent node (neighbor)"""
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        """Add neighbor"""
        self.neighbors[other] = weight

    def get_neighbors(self):
        """Get all adjacent nodes (neighbors)"""
        return self.neighbors.keys()

    def get_distance(self):
        """Get distance"""
        return self.distance

    def set_distance(self, distance):
        """Set distance"""
        self.distance = distance

    def get_previous(self):
        """Get previous"""
        return self.previous

    def set_previous(self, previous):
        """Set previous"""
        self.previous = previous

    def get_color(self):
        """Get color"""
        return self.color


    def set_color(self, color):
        """Get color"""
        self.color = color

    def get_discovery(self):
        """Get discovery time"""
        return self.disc_time


    def set_discovery(self, t):
        """Set discovery time"""
        self.disc_time = t

    def get_finish(self):
        """Get finish time"""
        return self.fin_time

    def set_finish(self, t):
        """Set finish time"""
        self.fin_time = t

    def get_weight(self, other):
        """Get edge weight"""
        return self.neighbors[other]

    def __str__(self):
        """Print a vertex"""
        return 'Neighbors of ' + str(self.key) + ': ' + str([x.key for x in self.neighbors])

    def __lt__(self, other):
        return self.key < other.key
```


```python
class Graph:
    """Graph class"""
    def __init__(self):
        """Create a new, empty graph"""
        self.vertices = {}
        self.time = 0


    def add_vertex(self, key):
        """Add an instance of Vertex to the graph"""
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex


    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Add a new, weighted, directed edge to the graph that connects two vertices"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].set_neighbor(self.vertices[to_vertex], weight)


    def get_vertex(self, key):
        """Find the vertex in the graph named vert_key"""
        return self.vertices.get(key, None)


    def get_vertices(self):
        """Return the list of all vertices in the graph"""
        return self.vertices.keys()


    def reset_distances(self):
        """Reset distances to test Dijkstra's"""
        for v in self:
            v.set_distance(sys.maxsize)

    def __contains__(self, key):
        """Return True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise"""
        return key in self.vertices


    def __iter__(self):
        """Iterator"""
        return iter(self.vertices.values())


    def __len__(self):
        """Graph's size"""
        return len(self.vertices)
    
    def bfs(self, start):
        """Breadth First Search"""
        time_start = time.time()
        start.set_distance(0)
        start.set_previous(None)
        vert_queue = [start]
        while vert_queue:
            current_vert = vert_queue.pop(0)
            for neigh in current_vert.get_neighbors():
                if neigh.get_color() == "white":
                    neigh.set_color("gray")
                    neigh.set_distance(current_vert.get_distance() + 1)
                    neigh.set_previous(current_vert)
                    vert_queue.append(neigh)
            current_vert.set_color("black")
        time_end = time.time()
        print("Paths found in {:.2f} sec".format(time_end - time_start))
```


```python

```
