import re

from utils import run_day


def main(input: str):

    def get_score_from_str(input_str):
        valid_mults = re.findall(r'mul\((\d+),(\d+)\)', input_str)
        return sum([int(a) * int(b) for a, b in valid_mults])

    print(f"Part 1: {get_score_from_str(input)}")

    # p2
    active_sections = []

    # get all sections broken up by a 'do()'
    do_sections = input.split("do()")

    for s in do_sections:
        # grab part of each section before first 'dont()'
        active_sections.append(s.split("don't()")[0])

    print(f"Part 2: {sum([get_score_from_str(x) for x in active_sections])}")



if __name__ == "__main__":
    run_day(main, run_dev=True, parse_input=False)
