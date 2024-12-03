import os
from pathlib import Path

import numpy as np
import re

from utils import parse_input, raw_input


def main(input: str):

    def get_score_from_str(input_str):
        # regex to get all valid mults
        regex_str = r'mul\(\d+,\d+\)'
        valid_mults = re.findall(regex_str, input_str)
        tot = 0
        for s in valid_mults:
            # messy way to get prod of ints from the found strings
            tot += np.prod(tuple(map(int, s.split("(")[1].split(")")[0].split(","))))
        return tot

    print(f"Part 1: {get_score_from_str(input)}")

    #p2
    active_sections = []

    # get all sections broken up by a 'do()'
    do_sections = input.split("do()")

    for s in do_sections:
        # grab part of each section before first 'dont()'
        active_sections.append(s.split("don't()")[0])

    tot = sum([get_score_from_str(x) for x in active_sections])
    print(f"Part 2: {tot}")



if __name__ == "__main__":
    run_dev = True

    directory = Path(__file__).resolve().parent
    dev_path = directory / "dev_input.txt"
    main_math = directory/"input.txt"

    if run_dev:
        print("Dev results:")
        main(raw_input(dev_path))
        print("\n")

    print("Main results: ")
    main(raw_input(main_math))

