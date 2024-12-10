import math
from collections import deque, defaultdict
import numpy as np
from utils import run_day, grid_get, get_grid_from_input

def main(input: str):
    grid = get_grid_from_input(input).astype(int)

    def get_adj(idx):
        return [(idx[0]+x, idx[1]+y) for x, y in [
                (1, 0), (-1, 0), (0, 1), (0, -1)
                ]]

    def get_trailhead_data(grid, idx):
        starting_h = grid_get(grid, *idx)
        completed_routes = defaultdict(set)
        route_queue = deque([[(starting_h, idx)]])

        while len(route_queue) > 0:
            route = route_queue.pop()
            h, coord = route[-1]
            for adj_point in get_adj(coord):
                if (new_h := grid_get(grid, *adj_point, default=math.inf)) == 1 + h:
                    new_step = (new_h, adj_point)
                    new_route = route + [new_step]
                    if new_h == 9: # keep all routes to each peak in a set
                        completed_routes[adj_point].add(str(new_route))  # lazy way to hash this frankenstein-typed route
                    else:
                        route_queue.append(new_route)

        return completed_routes

    trailheads = np.argwhere(grid == 0)
    all_trailhead_data = [get_trailhead_data(grid, x) for x in trailheads]

    print(f"P1: {sum([len(x.keys()) for x in all_trailhead_data])}")
    print(f"P2: {sum([len(trailhead[peak]) for trailhead in all_trailhead_data for peak in trailhead.keys()])}")

if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)