"""Using Breadth first search to find Kevin Bacon's number of actors"""
#!/usr/bin/env python3
# encoding: UTF-8


from notes.graphs.graphs import Graph
import sys
import time


def read_file(filename):
    """Build a graph from the file"""
    raise NotImplementedError


def main():
    print("---Kevin Bacon number calculator---")
    print("\nReading the file")
    b_graph = read_file("data/projects/kevinbacon/movie_actors_full.txt")
    


if __name__ == "__main__":
    main()
