from collections import defaultdict

from utils import run_day

import networkx as nx


def main(input: str):

    connections = set()
    node_connections = defaultdict(set)
    for line in input.splitlines():
        nodes = tuple(sorted(line.split("-")))
        connections.add(nodes)
        node_connections[nodes[0]].add(nodes[1])
        node_connections[nodes[1]].add(nodes[0])


    t_triads = set()
    for c in connections:
        for n in node_connections[c[0]]:
            if n in node_connections[c[1]]:
                if len([x for x in [c[0], c[1], n] if x[0] == "t"]) > 0:
                    t_triads.add(tuple(sorted([c[0], c[1], n])))

    print(f"Part 1: {len(t_triads)}")


    # P2: Use NetworkX cliques.
    # Could do with raw python using Bron-Kerbosh, but this is cleaner
    graph = nx.Graph()
    graph.add_edges_from(connections)
    clusters = list(nx.find_cliques(graph))
    clusters.sort(key=len, reverse=True)

    print(f"Part 2: {",".join(sorted(list(clusters[0])))}")

if __name__ == "__main__":
    run_day(main, run_dev=False)