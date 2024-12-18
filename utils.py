import os
import sys
import time
from pathlib import Path
from typing import Callable, Union

import numpy as np


def get_parsed_input(filepath: os.PathLike):
    with open(filepath, 'r') as file:
        content = [x.strip().split() for x in file.readlines()]
        return content

def get_raw_input(filepath: os.PathLike):
    with open(filepath, 'r') as file:
        return file.read()


def run_day(
        main_func: Callable[[Union[list, str]], None],
        run_dev: bool = True,
        parse_input: bool = False
):
    """Simple wrapper function that calls main with the needed inputs and times the function"""
    directory = Path(os.path.abspath(sys.argv[0])).resolve().parent
    dev_path = directory / "dev_input.txt"
    main_math = directory / "input.txt"

    parse_func = get_parsed_input if parse_input else get_raw_input

    if run_dev:
        t0 = time.process_time_ns()
        print("Dev results: ")
        main_func(parse_func(dev_path))
        print("\n")
        dev_time = time.process_time_ns() - t0

    else:
        print("Main results: ")
        t1 = time.process_time_ns()
        main_func(parse_func(main_math))
        main_time = time.process_time_ns() - t1

    print ("\n")

    print("Timings:")
    if run_dev:
        print(f"Dev: {get_time_str(dev_time)}")
    else:
        print(f"Main: {get_time_str(main_time)}")

def get_time_str(timing):
    ms_time = timing / 1000000
    if ms_time > 1000:
        return f"{ms_time/1000:.4g} s"
    return f"{ms_time:.4g} ms"

def grid_get(
        grid: np.array,
        x: int,
        y: int,
        default = "."
):
    """Fault tolerant grid get function.

    Returns entry unless result is OOB, then returns default value."""
    if x < 0 or y < 0:
        return default
    try:
        return grid[x, y]
    except IndexError:
        return default

def is_within_grid(
        grid: np.array,
        x: int,
        y: int
    ):
    if x < 0 or y < 0:
        return False
    if x >= len(grid) or y >= len(grid[0]):
        return False
    return True

def get_grid_from_input(input):
    return np.rot90(
            np.array(
                    [list(x) for x in input.strip().split("\n")]), k=-1
            )

ADJACENT_DIRECTIONS = {(-1, 0), (1, 0), (0, -1), (0, 1)}

def get_adjacent_points(point, array=None):
    possible_points = [(point[0] + d[0], point[1] + d[1]) for d in ADJACENT_DIRECTIONS]
    adj_points = set()
    for p in possible_points:
        if array is None or is_within_grid(array, *p):
            adj_points.add(p)
    return adj_points

def print_grid(grid):
    s = ""
    for j in range(len(grid[0])-1, -1, -1):
        for i in range(len(grid)):
            s += str(grid[i, j])
        s+= "\n"
    print(s)
    print("\n")