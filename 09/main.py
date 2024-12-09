import math

from utils import run_day
from collections import deque, defaultdict


def main(input: str):
    res = [tuple(map(int, input[i: i+2]))for i in range(0, len(input), 2)]

    # forward_system = deque()
    # back_system = deque()

    # total_count = 0
    # for i, j in enumerate(res):
    #     total_count += (j[0])
    #     for _ in range(j[0]):
    #         forward_system.append(i)
    #         back_system.appendleft(i)
    #
    #     if len(j) == 2: # add empty space
    #         for _ in range(j[1]):
    #             forward_system.append(None)
    #
    # def construct_list(forward, backward, total_count):
    #     output = []
    #     while len(output) < total_count:
    #         val = forward_system.popleft()
    #         if val is not None:
    #             output.append(val)
    #             f = val
    #         else:
    #             backward_val = backward.popleft()
    #             output.append(backward_val)
    #
    #     return output

    def checksum(list):
        list = [k if k else 0 for k in list]
        return sum(
                i * k for i, k in enumerate(list)
                )

    # p2
    res = [tuple(map(int, input[i: i+2]))for i in range(0, len(input), 2)]

    filesystem = []
    file_map = {}
    free_space_map = defaultdict(set)
    idx = 0

    for i, j in enumerate(res):
        file_map[i] = (idx, j[0])
        for _ in range(j[0]):
            filesystem.append(i)
            idx += 1

        if len(j) == 2:
            free_space_map[j[1]].add(idx)

            for _ in range(j[1]):
                filesystem.append(None)
                idx += 1

    for file in sorted(list(file_map.keys()))[::-1]:
        i, length = file_map[file]

        # get viable free_spaces
        free_space_idx, space_width = math.inf, None
        max_free_space = max(free_space_map.keys())
        for k in range(length, max_free_space+1):
            if free_space_map[k] and (new_idx := min(free_space_map[k])) < free_space_idx:
                free_space_idx = new_idx
                space_width = k

        if space_width:
            # perform swap
            if free_space_idx < i:
                filesystem[free_space_idx:free_space_idx+length] = [file] * length
                filesystem[i:i+length] = [None] * length
                free_space_map[space_width].remove(free_space_idx)
                if space_width > length:
                    free_space_map[space_width - length].add(free_space_idx+length)

    print(filesystem)
    print(checksum(filesystem))




    # print(base_file_map, free_space_map)
    #
    # file_system = construct_list(forward_system, back_system, total_count)
    # print(f"Part 1: {checksum(file_system)}")

if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)

