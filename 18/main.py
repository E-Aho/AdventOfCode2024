import math
from collections import deque, defaultdict
from utils import run_day, get_adjacent_points, grid_get
import numpy as np
import heapq

dev = False

if not dev:
    SHAPE = 70
    DIST_TO_DRAW = 1024
else:
    SHAPE = 6
    DIST_TO_DRAW = 12

def main(input: str):
    raw_falling_bytes = [tuple(map(int, x.split(","))) for x in input.split("\n")]

    initial_position = (0,0)
    target = (SHAPE, SHAPE)

    def get_grid_with_fallens(fallens):
        mem = np.zeros([SHAPE+1, SHAPE+1], object)
        for x, y in fallens:
            mem[x, y] = 1
        return mem

    def dijkstras_for_map(fallens):
        memory = get_grid_with_fallens(fallens)
        queue = [(0, initial_position)]
        fastest_to_position = defaultdict(lambda: math.inf)
        fastest_to_position[initial_position] = 0
        while queue:
            dist, pos = heapq.heappop(queue)

            if pos == target:
                return fastest_to_position[target]

            for adj in get_adjacent_points(pos):
                if grid_get(memory, *adj, default=1) != 1 and dist + 1 < fastest_to_position[adj]:
                    heapq.heappush(queue, (dist+1, adj))
                    fastest_to_position[adj] = dist + 1

    print(f"Part 1: {dijkstras_for_map(raw_falling_bytes[:DIST_TO_DRAW])}")

    # p2: just reuse dijkstras, it's fast enough, even if flood fill would be faster.
    # runs 2x slower than flood fill algorithm, but less code :))))
    for i in range(DIST_TO_DRAW, len(raw_falling_bytes)):
        fallens = raw_falling_bytes[:i+1]
        if not dijkstras_for_map(fallens):
            print(f"Part 2: {raw_falling_bytes[i]}")
            break

if __name__ == "__main__":
    run_day(main, run_dev=dev)