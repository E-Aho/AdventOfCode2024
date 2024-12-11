import functools

from utils import run_day


def main(input: str):
    input = [int(x) for x in input.split(" ")]

    @functools.cache
    def recursive_count(stone, t):
        if t == 0:
            return 1
        if stone == 0:
            return recursive_count(1, t - 1)

        s, l = str(stone), len(str(stone))
        if l % 2 == 0:
            return (recursive_count(int(s[:l // 2]), t - 1) +
                    recursive_count(int(s[l // 2:]), t - 1))

        return recursive_count(stone * 2024, t - 1)

    print(f"P1: {sum([recursive_count(stone, 25) for stone in input])}")
    print(f"P2: {sum([recursive_count(stone, 75) for stone in input])}")


if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)