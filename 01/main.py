import os
from collections import Counter
from pathlib import Path

import numpy as np

from utils import run_day


def main(input: list[list[str]]):

    # get two sorted lists of integers from left/right of input
    left, right = tuple(map(
        lambda x: sorted(list(map(int, x))),
        zip(*input)
    ))

    # p1
    part_1 = sum([abs(left[i] - right[i]) for i in range(len(right))])
    print(f"part 1: {part_1}")

    # p2
    count_right = Counter(right)
    part_2 = 0
    for k in left:
        part_2 += (k * count_right.get(k, 0))
    print(f"part 2: {part_2}")


if __name__ == "__main__":
    run_day(main, run_dev=True)
