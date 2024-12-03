import os
from pathlib import Path

import numpy as np

from utils import parse_input

def main(input: list[list[str]]):
    pass


if __name__ == "__main__":
    run_dev = True

    directory = Path(__file__).resolve().parent
    dev_path = directory / "dev_input.txt"
    main_math = directory / "input.txt"

    if run_dev:
        print("Dev results:")
        main(parse_input(dev_path))
        print("\n")

    print("Main results: ")
    main(parse_input(main_math))