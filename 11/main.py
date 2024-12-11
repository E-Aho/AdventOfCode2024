import functools

from utils import run_day


def main(input: str):
    input = [int(x) for x in input.split(" ")]

    @functools.cache
    def recursive_final_num(stone, i):
        if i == 0:
            return 1
        if stone == 0:
            return recursive_final_num(1, i - 1)

        s, l = str(stone), len(str(stone))
        if l % 2 == 0:
            return (recursive_final_num(int(s[:l // 2]), i - 1) +
                    recursive_final_num(int(s[l // 2:]), i - 1))

        return recursive_final_num(stone * 2024, i - 1)

    print(f"P1: {sum([recursive_final_num(stone, 25) for stone in input])}")
    print(f"P2: {sum([recursive_final_num(stone, 75) for stone in input])}")


if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)