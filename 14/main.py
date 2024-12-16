import re
from collections import Counter, defaultdict

import numpy as np

from utils import run_day, get_adjacent_points


def print_bots(robots, w, h):
    bot_pos = Counter(r[0] for r in robots)
    s = ""
    for j in range(h):
        for i in range(w):
            if (i, j) in bot_pos.keys():
                s += str(bot_pos[(i, j)])
            else:
                s += "."
        s += "\n"
    return(s)


def main(input: str):
    w = 101
    h = 103

    re_string = r"^p=([\d,-]*) v=([\d,-]*)"
    robots = []
    for row in input.split("\n"):
        p, v = re.findall(re_string, row)[0]
        robots.append((
                tuple(map(int, p.split(','))),
                tuple(map(int, v.split(',')))
        ))

    def move_robot_for_n_seconds(p, v, t,  width, height):
        new_p = p[0] + (v[0] * t), p[1] + (v[1] * t)
        mod_p = [new_p[0] % width, new_p[1] % height]
        if mod_p[0] < 0:
            mod_p[0] = mod_p[0] + width
        if mod_p[1] < 0:
            mod_p[1] = mod_p[1] + height
        return (tuple(mod_p), v)

    new_bots = []
    for robot in robots:
        new_bots.append(move_robot_for_n_seconds(robot[0], robot[1], 100, w, h))

    # print_bots(new_bots, w, h) # looks good!

    def score_bots(bots, w, h):
        quadrants = defaultdict(int)
        mid_x, rem_x = divmod(w, 2)
        mid_y, rem_y = divmod(h, 2)

        for bot in bots:
            p = bot[0]
            if mid_x == p[0] or mid_y == p[1]:
                continue
            x_q = mid_x > p[0]
            y_q = mid_y > p[1]

            quadrants[(x_q, y_q)] += 1

        return np.prod(list(quadrants.values()))

    print(f"P1: {score_bots(new_bots, w, h)}")

    # p2
    def are_bots_clustered(bots):
        bot_positions = set([b[0] for b in bots])
        total = len(bot_positions)
        c = 0
        for p in bot_positions:
            if any(q in bot_positions for q in get_adjacent_points(p)):
                c += 1
        return c > total // 2

    running_bots = robots
    for _ in range (10000):
        running_bots = [move_robot_for_n_seconds(robot[0], robot[1], 1, w, h) for robot in running_bots]
        if are_bots_clustered(running_bots):
            print(f"T: {_}")
            s = print_bots(running_bots, w, h)
            print(s)
            print("\n\n")


if __name__ == "__main__":
    run_day(main, run_dev=False)
