#!/usr/bin/env python3
"""
`kevinbacon` driver

@authors: Roman Yasinovskyy
@version: 2021.4
"""

import argparse
import time

from kevinbacon import read_file, find_max_kbn_actors


def main():
    """Main function"""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("actor", type=str, nargs="*")
    args = argparser.parse_args()

    print("Kevin Bacon number calculator")
    print("Reading the file")
    time_start = time.time()
    the_graph = read_file("data/projects/kevinbacon/movie_actors_full.txt")
    time_end = time.time()
    elapsed = time_end - time_start
    print(f"File read in {elapsed:.2f} sec")
    print()

    print("Analyzing the graph")
    connections = 0
    for vertex in the_graph:
        connections = connections + len(vertex.get_neighbors())
    print(f"There are {len(the_graph)} connected actors in the file")
    print(f"There are {connections} connections between actors in the file")
    print()

    print("Finding paths")
    kevin = the_graph.get_vertex("Kevin Bacon")
    time_start = time.time()
    the_graph.bfs(kevin)
    time_end = time.time()
    elapsed = time_end - time_start
    print(f"Paths found in {elapsed:.2f} sec")
    print()

    print("Looking for actors with the highest Kevin Bacon number")
    time_start = time.time()
    high_kbn_lst = find_max_kbn_actors(the_graph)
    time_end = time.time()
    elapsed = time_end - time_start
    print(f"{len(high_kbn_lst)} actor(s) found in {elapsed:.2f} sec")
    print(
        "The following actor(s) have the Kevin Bacon number of "
        + f"{the_graph.get_vertex(high_kbn_lst[0]).get_distance()}:"
    )
    for name in high_kbn_lst:
        print(name)
    print()

    actor = " ".join(args.actor) or high_kbn_lst[0]
    raise NotImplementedError


if __name__ == "__main__":
    main()
