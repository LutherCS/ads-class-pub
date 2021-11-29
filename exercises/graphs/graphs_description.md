# Is it graph as in graphing calculator?

Complete the following tasks and submit your source code to KATIE as a single file (archive).

![Graph](network.png)

1. Assume the network graph in the picture above and use *Dijkstra's* algorithm to manually find the shortest path from vertex **t** to all other vertices in the network. Show each step of the algorithm.

2. Assume the network graph in the picture above and use *Dijkstra's* algorithm to manually find the shortest path from vertex **x** to all other vertices in the network. Show each step of the algorithm.

5. Add `__len____` method to the textbook implementation of the `Graph` class. It should print the number of vertices in a graph.

4. Add `size` method to the textbook implementation of the `Graph` class. It should print the number of edges in a graph. For the sake of simplicity, count edges from `a` to `b` and from `b` to `a` as a single edge.

5. Add `hub` property to the textbook implementation of the `Graph` class. It should return the vertex with the most **outgoing** connections (edges).

## What to do

`python3` should be `python3.9` or newer.

- Read _exercises/graphs/graphs_description.md_ (this file).
- Modify nd run _exercises/graphs/graphs.py_.

```bash
python3 exercises/graphs/graphs.py
```

- Test your implementation.

```bash
python3 -m pytest exercises/graphs/graphs_test.py
```
