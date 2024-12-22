from collections import defaultdict

from utils import run_day


def main(input: str):

    def mix(a, b) -> int:
        return a ^ b

    def prune(a):
        return a % 16777216

    def apply(a) -> int:
        b = prune(mix(a, a* 64))
        c = prune(mix(int(b / 32),b))
        d = prune(mix(c * 2048, c))
        return d

    def apply_n(s, i: int = 2000):
        res = [s]
        for _ in range(i):
            s = apply(s)
            res.append(s)
        return s, res

    p1 = 0
    buyer_map = []
    for x in [int(x) for x in input.splitlines()]:
        buyer_final, buyer_hist = apply_n(x, 2000)
        p1 += buyer_final
        buyer_map.append(buyer_hist)

    print(f"Part 1: {p1}")

    delta_scores = defaultdict(int)

    for hist in buyer_map:
        scores = [x % 10 for x in hist]
        seen = set()
        deltas = tuple([scores[x + 1] - scores[x] for x in range(len(scores)-1)])
        for start in range(len(deltas)-4):
            d = deltas[start: start + 4]
            if d not in seen:
                seen.add(d)
                delta_scores[d] += scores[start+4]

    print(f"P2: {max(delta_scores.values())}")


if __name__ == "__main__":
    run_day(main, run_dev=False)