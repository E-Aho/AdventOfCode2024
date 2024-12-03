import os
import sys
import time
from pathlib import Path
from typing import Callable, Union


def get_parsed_input(filepath: os.PathLike):
    with open(filepath, 'r') as file:
        content = [x.split() for x in file.readlines()]
        return content

def get_raw_input(filepath: os.PathLike):
    with open(filepath, 'r') as file:
        return file.read()


def run_day(
        main_func: Callable[[Union[list, str]], None],
        run_dev: bool = True,
        parse_input: bool = True
):
    directory = Path(os.path.abspath(sys.argv[0])).resolve().parent
    dev_path = directory / "dev_input.txt"
    main_math = directory / "input.txt"

    parse_func = get_parsed_input if parse_input else get_raw_input

    if run_dev:
        t0 = time.process_time_ns()
        print("Dev results:")
        main_func(parse_func(dev_path))
        print("\n")
        dev_time = time.process_time_ns() - t0


    print("Main results: ")
    t1 = time.process_time_ns()
    main_func(parse_func(main_math))
    main_time = time.process_time_ns() - t1

    print ("\n")

    print("Timings:")
    if run_dev:
        print(f"Dev: {dev_time / 1000000:.4g}ms")
    print(f"Main: {main_time / 1000000:.4g}ms")