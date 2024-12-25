import numpy as np

from utils import run_day, get_grid_from_input


def main(input: str):
    entries = input.split("\n\n")
    arrays = [np.rot90(get_grid_from_input(entry)) for entry in entries]
    keys, locks = [], []
    for obj in arrays:
        if np.all(obj[0] == "#"):
            keys.append(list(map(int, [sum(obj[1:, x] == "#") for x in range(len(obj[0]))])))
        else:
            locks.append(list(map(int, [sum(obj[:-1, x] == "#") for x in range(len(obj[0]))])))

    def do_fit(key, lock):
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                return False
        return True

    fits = set()
    for key in keys:
        for lock in locks:
            if do_fit(key, lock):
                fits.add((tuple(key), tuple(lock)))

    print(len(fits))

if __name__ == "__main__":
    run_day(main, run_dev=False)