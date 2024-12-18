from multiprocessing.resource_tracker import register

from utils import run_day


def main(input: str):

    regs, prog = input.split("\n\n")
    _rg = []
    for reg in regs.split("\n"):
        _rg.append(int(reg.split(": ")[1]))

    program = tuple(map(int, prog.split(": ")[1].split(",")))
    base_reg = list(_rg)

    class ChronospatialComputer:
        def __init__(self):
            self.program = program
            self.reg = base_reg.copy()

            self.pointer = 0
            self.output = []

        def combo(self, inp: int):
            match inp:
                case 0 | 1 | 2 | 3:
                    return inp
                case 4 | 5 | 6:
                    return self.reg[inp - 4]
                case 7:
                    print("oops")

        def print_state(self):
            print(f"Pointer: {self.pointer}\n Register: {self.reg}\n Output: {self.output}")

        def operate(self) -> bool:
            try:
                op, inp = self.program[self.pointer], self.program[self.pointer + 1]
            except IndexError:
                return False

            match op:
                case 0: #adv
                    self.reg[0] = self.reg[0] // (2 ** self.combo(inp))
                case 1: # bxl
                    self.reg[1] = self.reg[1] ^ inp
                case 2: # bst
                    self.reg[1] = self.combo(inp) % 8
                case 3: # jnz
                    if self.reg[0] != 0:
                        self.pointer = inp
                        return True
                case 4: # bxc
                    self.reg[1] = self.reg[1] ^ self.reg[2]
                case 5: #out
                    self.output.append(self.combo(inp) % 8)
                case 6: #bdv
                    self.reg[1] = int(self.reg[0] / (2 ** self.combo(inp)))
                case 7: #cdv
                    self.reg[2] = int(self.reg[0] / (2 ** self.combo(inp)))

            self.pointer += 2

            return True

        def operate_till_halt(self):
            while self.operate():
                pass

    p1_computer = ChronospatialComputer()
    p1_computer.operate_till_halt()

    output_str = ",".join(map(str, p1_computer.output))
    print(f'P1: {output_str}')

    def run_for_i(i):
        c = ChronospatialComputer()
        c.reg[0] = i
        c.operate_till_halt()
        return c.output

    def find_solutions(depth, a, results: list = None):
        # run backwards, finding next possible result
        if results is None:
            results = []

        v = program[-depth]
        for i in range(0, 8):
            output = run_for_i(a+i)
            if output[0] == v:
                if depth == len(program):
                    results.append(a+i)
                elif depth < len(program):
                    results += find_solutions(depth+1, (a+i) * 8)

        return results

    print(f"Part 2: {min(find_solutions(1, 0))}")

if __name__ == "__main__":
    run_day(main, run_dev=False)
