from collections import deque
from copy import deepcopy

import numpy as np

from utils import run_day, get_grid_from_input, grid_get


def main(input: str):
    grid_str, commands = input.split("\n\n")
    initial_grid = get_grid_from_input(grid_str)
    commands = list(commands.replace("\n", ""))


    initial_position = tuple(np.argwhere(initial_grid == "@")[0])

    def perform_move(position, direction, grid):
        move_map = {
                "<": (-1, 0),
                ">": (1, 0),
                "^": (0, 1),
                "v": (0, -1)
                }

        v = move_map[direction]
        p = position
        p1 = p[0] + v[0], p[1] + v[1]
        p2 = p1[0] + v[0], p1[1] + v[1]

        obj_1 = grid_get(grid, *p1, default="#")
        if obj_1 == "#":
            return p, grid

        if obj_1 == ".":
            grid[p] = "."
            grid[p1] = "@"
            return p1, grid

        if obj_1 == "O":
            obj_2 = grid_get(grid, *p2, default="#")
            while obj_2 == "O":
                p2 = p2[0] + v[0], p2[1] + v[1]
                obj_2 = grid_get(grid, *p2, default="#")

            if obj_2 == "#":
                return p, grid

            # else, can move
            if obj_2 == ".":
                grid[p] = "."
                grid[p1] = "@"
                grid[p2] = "O"
                return p1, grid

        def get_box_from_one_position(p, grid):
            obj = grid_get(grid, *p, default="#")
            if obj == "[":
                l, r = p, (p[0] + 1, p[1])
            else:
                l, r = (p[0] - 1, p[1]), p
            return (l, r)

        box_parts = ["[", "]"]

        if obj_1 in box_parts:
            rights = set()
            lefts = set()
            box_queue = deque()

            l, r = get_box_from_one_position(p1, grid)
            lefts.add(l), rights.add(r)
            box_queue.append(l), box_queue.append(r)

            seen = {l, r}

            while box_queue:
                base = box_queue.popleft()
                n = base[0] + v[0], base[1] + v[1]
                obj = grid_get(grid, *n, default="#")
                if obj == "#":
                    return p, grid

                if obj == ".":
                    continue

                elif obj in box_parts:
                    l, r = get_box_from_one_position(n, grid)
                    lefts.add(l), rights.add(r)
                    if l not in seen:
                        box_queue.append(l)
                        seen.add(l)
                    if r not in seen:
                        box_queue.append(r)
                        seen.add(r)

            new_lefts = {(l[0] + v[0], l[1] + v[1]) for l in lefts}
            new_rights = {(r[0] + v[0], r[1] + v[1]) for r in rights}
            new_dots = lefts.union(rights) - (new_lefts.union(new_rights))

            for l in new_lefts:
                grid[l] = "["
            for r in new_rights:
                grid[r] = "]"
            for d in new_dots:
                grid[d] = "."

            grid[p] = "."
            grid[p1] = "@"
            return p1, grid


        # else:
        return p, grid


    def get_score(grid, p2=False):
        if not p2:
            boxes = np.argwhere(grid=="O")
        else:
            boxes = np.argwhere(grid=="[")
        h = len(grid[0])
        score = 0
        for b in boxes:
            score += (b[0]) + 100*(h - b[1]-1)
        print(score)

    def print_grid(grid):
        s = ""
        for j in range(len(grid[0])-1, -1, -1):
            for i in range(len(grid)):
                s += grid[i, j]
            s+= "\n"
        print(s)

        print("\n")

    # grid, position = deepcopy(initial_grid), deepcopy(initial_position)
    # for command in commands:
    #     position, grid = perform_move(position, command, grid)
    # print_grid(grid)
    # get_score(grid)


    def part_2ify(input: str) -> np.ndarray:

        s = input.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
        print(s)
        return get_grid_from_input(s.split("\n\n")[0])

    p2_grid = part_2ify(input)
    p2_initial =  tuple(np.argwhere(p2_grid == "@")[0])

    grid, position = deepcopy(p2_grid), deepcopy(p2_initial)
    for command in commands:
        position, grid = perform_move(position, command, grid)
        # print_grid(grid)

    get_score(grid, True)




if __name__ == "__main__":
    run_day(main, run_dev=False)