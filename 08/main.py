from collections import defaultdict
from itertools import permutations

from utils import run_day, get_grid_from_input, is_within_grid, grid_get

def main(input: str):
    map_arr = get_grid_from_input(input)

    antenna_positions = defaultdict(set)
    for i in range(len(map_arr)):
        for j in range(len(map_arr[0])):
            v = grid_get(map_arr, i, j)
            if v != ".":
                antenna_positions[v].add((i, j))

    def get_antinodes(map, antenna_positions):
        antinodes = set()
        for freq in antenna_positions.keys():
            for p1, p2 in permutations(antenna_positions[freq], 2):
                delta = (p1[0] - p2[0], p1[1] - p2[1])
                for point in [
                        (p1[0] + delta[0], p1[1] + delta[1]),
                        (p2[0] - delta[0], p2[1] - delta[1])
                    ]:
                    if is_within_grid(map, *point):
                        antinodes.add(point)
        return antinodes

    def get_p2_antinodes(map, antenna_positions):
        antinodes = set()
        for freq in antenna_positions.keys():
            for p1, p2 in permutations(antenna_positions[freq], 2):
                delta = (p1[0] -p2[0], p1[1] - p2[1])

                point = p1
                while is_within_grid(map, *point):
                    antinodes.add(point)
                    point = (point[0] + delta[0], point[1] + delta[1])

                point = p2
                while is_within_grid(map, *point):
                    antinodes.add(point)
                    point = (point[0] - delta[0], point[1] - delta[1])

        return antinodes

    print(f"Part 1: {len(get_antinodes(map_arr, antenna_positions))}")
    print(f"Part 2: {len(get_p2_antinodes(map_arr, antenna_positions))}")

if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)
