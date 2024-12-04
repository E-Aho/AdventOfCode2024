from collections import Counter

from utils import run_day
import numpy as np

def main(input: str):
    m = np.array([list(x) for x in input.strip().split("\n")])

    diagonals = [(1, 1), (1, -1), (-1,1), (-1, -1)]
    linears = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    directions = diagonals + linears

    part1_count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i, j] == "X":
                for d in directions:
                    try:
                        # check M, A, S on same line
                        if (m[(i+d[0], j+d[1])] == "M" and
                           m[(i + 2*d[0], j + 2*d[1])] == "A" and
                           m[(i + 3*d[0], j + 3 * d[1])] == "S"):

                            # check end of line hasn't wrapped around matrix
                            if (0 <= i + 3*d[0] <= len(m) and
                               0 <= j + 3 * d[1] <= len(m[0])):

                                part1_count += 1
                    except IndexError:
                        pass

    print(f"Part 1: {part1_count}")

    # p2
    part2_count = 0
    for i in range(1, len(m)-1):
        for j in range(1, len(m[0])-1):
            if m[i, j] == "A":
                diagonal_count = Counter([m[i+a, j+b] for a, b in diagonals])
                if diagonal_count["M"] == 2 and diagonal_count["S"] == 2:

                    # checks the letters aren't on same diagonal
                    if m[i-1, j-1] != m[i+1, j+1]:
                        part2_count += 1

    print(f"Part 2: {part2_count}")


if __name__ == "__main__":
    run_day(main, run_dev=True, parse_input=False)
