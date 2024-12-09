import math

from utils import run_day
from collections import deque, defaultdict


def main(input: str):
    file_free_space_pairs = [tuple(map(int, input[i: i+2]))for i in range(0, len(input), 2)]

    def checksum(list):
        zeroed_list = [k if k else 0 for k in list]
        return sum(i * k for i, k in enumerate(zeroed_list))

    def p1(file_space_pairs):
        forward_queue = deque()
        backward_queue = deque()

        total_count = 0
        for i, j in enumerate(file_space_pairs):
            total_count += (j[0])
            for _ in range(j[0]):
                forward_queue.append(i)
                backward_queue.appendleft(i)

            if len(j) == 2: # check here is an edge case for last entry, then add space to forward system
                for _ in range(j[1]):
                    forward_queue.append(None)

        output = []
        while len(output) < total_count:
            val = forward_queue.popleft()
            if val is not None:
                output.append(val)
            else:
                backward_val = backward_queue.popleft()
                output.append(backward_val)

        return checksum(output)


    # p2
    def p2(file_pairs):
        filesystem = []
        file_map = {}
        free_space_map = defaultdict(set)
        idx = 0

        for i, j in enumerate(file_pairs):
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

            # get left most viable free_space
            free_space_idx, space_width = math.inf, None
            for w in range(length, 10):  # widest possible free space is 9
                if free_space_map[w] and (new_idx := min(free_space_map[w])) < free_space_idx:
                    free_space_idx = new_idx
                    space_width = w

            if free_space_idx < i: # perform swap
                filesystem[free_space_idx:free_space_idx+length] = [file] * length
                filesystem[i:i+length] = [None] * length
                free_space_map[space_width].remove(free_space_idx)
                if space_width > length:
                    free_space_map[space_width - length].add(free_space_idx+length)

        return checksum(filesystem)

    print(f"Part 1: {p1(file_free_space_pairs)}")
    print(f"Part 2: {p2(file_free_space_pairs)}")


if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)
