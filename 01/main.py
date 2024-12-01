import os
from collections import Counter
from pathlib import Path

import numpy as np

from utils import parse_input

def main(input: list[str]):
    left, right = zip(*input)
    left = sorted(list(map(int, left)))
    right = sorted(list(map(int, right)))

    part_1 = sum([abs(left[x] - right[x]) for x in range(len(right))])
    print(f"part 1: {part_1}")

    count_right = Counter(right)
    part_2 = 0
    for k in left:
        part_2 += (k * count_right.get(k, 0))
    print(f"part 2: {part_2}")


if __name__ == "__main__":

    dir = Path(__file__).resolve().parent
    run_dev = False
    if run_dev:
        main(parse_input(dir/"dev_input.txt"))

    main(parse_input(dir / "input.txt"))

