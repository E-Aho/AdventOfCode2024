from functools import cmp_to_key

from utils import run_day


def main(input: str):
    first_section, second_section = input.split("\n\n")
    ordering_rules = [
        tuple(map(int, x.split("|")))
        for x in first_section.strip().split("\n")
    ]

    rules = set((a, b) for a, b in ordering_rules)
    updates = [list(map(int, x.split(','))) for x in second_section.strip().split("\n")]

    def compare(a, b):
        """compares two specific entries in list to check if they follow rules"""
        if (a, b) in rules:
            return -1
        elif (b, a) in rules:
            return 1
        return 0

    p1 = 0
    p2 = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(compare))
        if sorted_update == update:
            p1 += update[len(update)//2]
        else:
            p2 += sorted_update[len(update)//2]
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)
