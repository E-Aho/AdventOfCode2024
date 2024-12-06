from utils import run_day, grid_get

import numpy as np


def main(input: str):
    map_arr = np.rot90(np.array([
        list(x) for x in input.strip().split("\n")
    ]), k=-1) # rotate matrix, as it comes in rotated by default for some reason

    guard_start = np.where(map_arr == "^")
    start_pos = guard_start[0][0], guard_start[1][0]
    start_dir = (0, 1)

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

    print(f"Part 1: {len(seen)}")

    # p2
    def check_if_loops(block, map):
        map[block] = "#"
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

    print(f"Part 2: {count_loops}")

    # TODO: Rectangle based idea for p2:
    # track lines formed by pairs of blocks in set
    # track blocks in set
    # for each step in path:
        # if reflection of next point in any line by blocks in set:
            # check path of proposed loop does not contain block (set intersection)
                # forms valid loop


if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)
