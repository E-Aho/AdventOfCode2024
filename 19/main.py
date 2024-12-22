import functools

from utils import run_day

def main(input: str):
    p, r = input.split("\n\n")
    towels = tuple(p.replace(" ", "").split(','))
    designs = r.splitlines()

    @functools.cache
    def get_options(design):
        if design:
            return sum([get_options(design[len(t):]) for t in towels if design.startswith(t)])
        else:
            return 1

    c = 0
    c2 = 0
    for design in designs:
        if poss := get_options(design):
            c += 1
            c2 += poss

    print(f"Part 1: {c}")
    print(f"Part 2: {c2}")


if __name__ == "__main__":
    run_day(main, run_dev=False)