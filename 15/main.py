import os
from pathlib import Path

import numpy as np

from utils import parse_input

def main(input: list[list[str]]):
    pass


if __name__ == "__main__":
    run_dev = True

    directory = Path(__file__).resolve().parent
    if run_dev:
        main(parse_input(directory / "dev_input.txt"))

    main(parse_input(directory / "input.txt"))

