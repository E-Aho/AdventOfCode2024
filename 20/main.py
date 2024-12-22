import math
from collections import deque, defaultdict, Counter

import numpy as np

from utils import run_day, get_grid_from_input, get_adjacent_points, grid_get


def main(input: str):
    grid = get_grid_from_input(input)
    start = tuple(np.argwhere(grid=="S")[0].tolist())
    end = tuple(np.argwhere(grid=="E")[0].tolist())

    def flood_fill_to_dist_dict(grid, basis_point) -> dict[int]:
        queue = deque()
        distances_from_end = defaultdict(lambda: math.inf)
        distances_from_end[basis_point] = 0
        queue.append(basis_point)
        while queue:
            p = queue.popleft()
            for adj in [a for a in get_adjacent_points(p, grid)]:
                type = grid_get(grid, *adj, default="#")
                if type != "#":
                    d = distances_from_end[p] + 1
                    if d < distances_from_end[adj]:
                        distances_from_end[adj] = d
                        queue.append(adj)

        return dict(distances_from_end)

    def get_distance_map(points):
        distance_map = {}
        for p in points:
            for q in points:
                if p != q:
                    delta = abs(p[0] - q[0]) + abs(p[1] - q[1])
                    distance_map[tuple(sorted([p, q]))] = delta
        return distance_map

    start_distance = flood_fill_to_dist_dict(grid, start)
    end_distance = flood_fill_to_dist_dict(grid, end)

    abs_distances = get_distance_map(start_distance.keys())

    p1_savings = []
    p2_savings = []
    seen = set()
    for p, start in start_distance.items():
        for q, end in end_distance.items():
            if p != q and (key := tuple(sorted([p, q]))) not in seen:
                direct = abs_distances[key]
                seen.add(key)
                if direct >= 2:
                    full_path_distance = start + end_distance[p]
                    cheat_distance = start + end + direct
                    delta = full_path_distance - cheat_distance
                    if delta > 0:
                        if direct == 2 and delta >= 100:
                            p1_savings.append(delta)
                        if direct <= 20 and delta >= 100:
                            p2_savings.append(delta)

    print(f"Part 1: {len(p1_savings)}")
    print(f"Part 2: {len(p2_savings)}")


if __name__ == "__main__":
    run_day(main, run_dev=False)