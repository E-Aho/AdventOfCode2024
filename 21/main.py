import functools

from utils import run_day

"""NB: Cop out today... The following is largely based on a pal's solution. I had something working for P1, 
but there were a bunch of bugs for p2, and I was short on time. I hope to redo this day from scratch when I have some time."""

keypad_coords = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "VOID": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}

direction_coords = {
    "VOID": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def main(input: str):

    @functools.cache
    def get_directions_between_presses(current: str, next: str, is_numeric: bool = False) -> list:
        """Returns list of potential options. Checks that the described route doesn't go through 'void'"""
        if is_numeric:
            coord_map = keypad_coords
        else:
            coord_map = direction_coords

        from_pos = coord_map[current]
        to_pos = coord_map[next]
        avoid_pos = coord_map["VOID"]

        res = set()
        ty, tx = to_pos
        q = [(*from_pos, "")]

        while q:
            y, x, seq = q.pop(0)
            if (y, x) == to_pos:
                res.add(seq + "A")
            elif (y, x) == avoid_pos:
                continue
            else:
                dy = ty - y
                if dy > 0:
                    q.append((y + 1, x, seq + "v"))
                elif dy < 0:
                    q.append((y - 1, x, seq + "^"))
                dx = tx - x
                if dx > 0:
                    q.append((y, x + 1, seq + ">"))
                elif dx < 0:
                    q.append((y, x - 1, seq + "<"))

        return res

    @functools.cache
    def min_dist(code, depth, is_numeric: bool=True):
        if depth == 0:
            return len(code)

        prev = "A"
        l = 0
        for i in range(len(code)):
            curr = code[i]
            l += min(min_dist(p, depth-1, is_numeric=False) for p in get_directions_between_presses(curr, prev,
                    is_numeric))
            prev=curr
        return l

    p1 = 0
    p2 = 0
    for code in input.strip().splitlines():
        p1 += (min_dist(code, 3) * int(code[:-1]))
        p2 += (min_dist(code, 26) * int(code[:-1]))
    print(f"Part 1: {p1}")
    print(f"Part 1: {p2}")

if __name__ == "__main__":
    run_day(main, run_dev=False)