from multiprocessing.resource_tracker import register

from utils import run_day


def main(input: str):


    class ChronospatialComputer:
        def __init__(self, input_string,  p2: bool=False):
            regs, prog = input_string.split("\n\n")
            _rg = []
            for reg in regs.split("\n"):
                _rg.append(int(reg.split(": ")[1]))

            self.program = tuple(map(int, prog.split(": ")[1].split(",")))
            self.reg = list(_rg)

            self.p2 = p2
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
            # print(f"Pre:")
            # self.print_state()
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



    p1_computer = ChronospatialComputer(input)
    p1_computer.operate_till_halt()
    print(print(",".join(map(str, p1_computer.output))))

    def run_for_i(i):
        c = ChronospatialComputer(input)
        c.operate_till_halt()
        return c.output





if __name__ == "__main__":
    run_day(main, run_dev=False)
