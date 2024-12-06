from utils import run_day, grid_get

import numpy as np


def main(input: str):
    map_arr = np.array([
        list(x) for x in input.strip().split("\n")
    ])

    up = (-1, 0) # ive somehow rotated this in the above

    start_pos = np.where(map_arr == "^")
    start_pos = start_pos[0][0], start_pos[1][0]
    start_dir = up

    def take_guard_step(pos, dir, map):
        possible_next_step = pos[0] + dir[0], pos[1] + dir[1]
        if (res := grid_get(map, *possible_next_step, default='OOB')) == '#':
            dir = (dir[1], -dir[0])
        elif res == "OOB":
            return "OOB", None
        else:
            pos = possible_next_step

        return pos, dir

    seen = set()
    seen.add(start_pos)

    pos = start_pos
    dir = start_dir

    while pos != "OOB":
        pos, dir = take_guard_step(pos, dir, map_arr)
        if pos != "OOB":
            seen.add(pos)

    def check_if_loops(block, map):
        try:
            map[block] = "#"
        except Exception:
            return False
        seen_with_dir = set()
        pos, dir = start_pos, start_dir
        seen_with_dir.add((pos, dir))

        while pos != "OOB":
            pos, dir = take_guard_step(pos, dir, map)
            if (pos, dir) in seen_with_dir:
                return True
            seen_with_dir.add((pos, dir))
        return False

    count_loops = 0
    for potential_block in seen - {start_pos}:
        if check_if_loops(potential_block, map_arr.copy()):
            count_loops += 1

    print(f"Part 1: {len(seen)}")
    print(f"Part 2: {count_loops}")


if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)
