import heapq
import math
from collections import deque, defaultdict

import numpy as np

from utils import run_day, get_grid_from_input, get_adjacent_points, grid_get

E = (1, 0)
W = (-1, 0)
N = (0, 1)
S = (0, -1)

def get_number_of_turns(v0, v1):
    if v0 == v1:
        return 0
    elif v0[1] == -v1[1]:
        return 2
    elif v0[1] == -v1[0] or v0[0] == -v1[1]:
        return 1
    return 3

def main(input: str):
    grid = get_grid_from_input(input)
    start = tuple(np.argwhere(grid=="S")[0])
    end = tuple(np.argwhere(grid=="E")[0])

    fastest_journies = defaultdict(lambda: math.inf)
    pq = []
    heapq.heappush(pq, (0, (start, E)))
    fastest_journies[(start, E)] = 0

    paths_to_point = defaultdict(lambda: defaultdict(set))
    paths_to_point[(start, E)][0] = {start}

    while pq:
        score, (pos, vec) = heapq.heappop(pq)

        for adj in get_adjacent_points(pos, grid):
            if grid_get(grid, *adj, default="#") in [".", "E"]:
                delta = adj[0] - pos[0], adj[1] - pos[1]
                turn_score = 1000 * get_number_of_turns(vec, delta)
                new_score = score + 1 + turn_score

                if new_score <= fastest_journies[(adj, delta)] and new_score <= 66404:
                    fastest_journies[(adj, delta)] = new_score
                    heapq.heappush(pq, (new_score, (adj, delta)))

                    paths_to_point[(adj, delta)][new_score].update(
                            paths_to_point[(pos, vec)][score].union({adj})
                            )

    fastest_end = min(
            [fastest_journies[(end, X)] for X in [N, E, S, W]])
    print(f"Part 1: {fastest_end}")

    all_paths = [paths_to_point[(end, X)][fastest_end] for X in [N, E, S, W]]
    all_points_on_paths = set()
    for path in all_paths:
        all_points_on_paths.update(path)
    print(f"Part 2: {len(all_points_on_paths)}")


if __name__ == "__main__":
    run_day(main, run_dev=False)