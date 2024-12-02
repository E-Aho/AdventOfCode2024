import os
from pathlib import Path

import numpy as np

from utils import parse_input

def main(input: list[list[str]]):
    input = [list(map(int, x)) for x in input]

    def check_safe(input):
        # check all inc or dec
        is_decending = (input[1] < input[0])
        for i in range(1, len(input)):
            if (input[i] < input[i-1]) != is_decending:
                return False
            if abs(input[i] - input[i-1]) not in {1,2,3}:
                return False
        return True

    print(f"part 1: {sum([check_safe(x) for x in input])}")

    def check_safe_p2(input):
        # small input (all less than 8 in length), brute force will work.
        # could do something smarter, but this is quick to implement and foolproof.
        if check_safe(input):
            return True
        else:
            # try popping each element
            for i in range(len(input)):
                inp = input.copy()
                inp.pop(i)
                if check_safe(inp):
                    return True
        return False

    print(f"part 2: {sum([check_safe_p2(x) for x in input])}")




if __name__ == "__main__":
    run_dev = True

    directory = Path(__file__).resolve().parent
    if run_dev:
        main(parse_input(directory / "dev_input.txt"))

    main(parse_input(directory / "input.txt"))

