import re

from utils import run_day


def main(input: str):
    regex_str = r'[XY][+=](\d*)'
    machines = []
    sections = input.split("\n\n")
    for s in sections:
        s = s.split("\n")
        x_a, y_a = tuple(map(int, re.findall(regex_str, s[0])))
        x_b, y_b = tuple(map(int, re.findall(regex_str, s[1])))
        x_p, y_p = tuple(map(int, re.findall(regex_str, s[2])))
        machines.append({"a": (x_a, y_a), "b": (x_b, y_b), "p": (x_p, y_p)})

    costs = [get_cost(m) for m in machines]
    p2_costs = [get_cost(m, p2=True) for m in machines]
    print(f"Part 1: {sum(costs)}")
    print(f"Part 2: {sum(p2_costs)}")

def get_cost(machine, p2=False):
    target = machine["p"]
    if p2:
        target = [int("10000000000000" + str(target[x])) for x in [0, 1]]
    a, b = machine["a"], machine["b"]

    # lil bit of linalg
    b_count, b_rem = divmod(a[1]*target[0] - a[0]*target[1], a[1]*b[0] - a[0]*b[1])
    a_count, a_rem = divmod(target[0] - b_count * b[0], a[0])

    if a_rem or b_rem:
        return 0
    return 3 * a_count + b_count

if __name__ == "__main__":
    run_day(main, run_dev=False)
