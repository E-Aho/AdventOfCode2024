from collections import defaultdict

from utils import run_day


def main(input: str):
    raw_gates, raw_commands = input.split("\n\n")

    gates = {x[0]: int(x[1]) for x in list(map(lambda y: y.split(": "), raw_gates.splitlines()))}
    commands = {tuple(y.split()) for y in raw_commands.replace("->", " ").splitlines()}

    logic_map = {}
    result_map = {}
    for command in commands:
        g1, op, g2, out = command
        s = tuple(sorted([g1, g2]) + [op])
        logic_map[s] = out
        result_map[out] = s


    get_op = {
            "AND": lambda a, b: a & b,
            "OR": lambda a, b: a | b,
            "XOR": lambda a, b: a ^ b
            }

    def parse_state(gate, state: dict) -> dict:
        if gate in state:
            return state

        g1, g2, op = result_map[gate]
        for g in (g1, g2):
            if not g in state:
                state.update(parse_state(g, state))

        state[gate] = get_op[op](state[g1], state[g2])
        return state


    def get_z_state():
        z_keys = sorted([x for x in result_map if x[0] == "z"])
        state = gates.copy()

        for g in z_keys:
            state = parse_state(g, state)

        out_str = "".join([str(state[g]) for g in z_keys])
        return out_str[::-1]

    print(f"P1: {int(get_z_state(), 2)}")


    def find_incorrect_gates():
        swapped_gates = set()
        xs = sorted([x for x in gates.keys() if x[0] == "x"])
        ys = sorted([x for x in gates.keys() if x[0] == "y"])
        zs = sorted([x for x in result_map.keys() if x[0] == "z"])

        def find_gate(a, b, op):
            return logic_map.get(tuple(sorted([a, b]) + [op]), None)

        def swap_gate(a, b):
            inp_a = result_map[a]
            inp_b = result_map[b]

            result_map[a] = inp_b
            result_map[b] = inp_a
            logic_map[inp_a] = b
            logic_map[inp_b] = a

            swapped_gates.update({a,b})


        carry = None

        bit = 0
        while bit < len(xs):
            if bit == 0:
                carry = find_gate(xs[0], ys[0], "AND")
            else:
                xor_gate = find_gate(xs[bit], ys[bit], "XOR")
                and_gate = find_gate(xs[bit], ys[bit], "AND")

                carry_xor = find_gate(xor_gate, carry, "XOR")
                if not carry_xor:
                    # xy xor and the last carry should exist as xor
                    swap_gate(xor_gate, and_gate)
                    bit = 0
                    print("carry")
                    continue

                if carry_xor != zs[bit]:
                    # carry_xor should be the output
                    swap_gate(carry_xor, zs[bit])
                    bit = 0
                    print("zs")
                    continue

                carry_and = find_gate(xor_gate, carry, "AND")
                carry = find_gate(and_gate, carry_and, "OR")

            bit += 1
            print(bit)
        return swapped_gates

    print(f"Part 2: {",".join(sorted(find_incorrect_gates()))}")





if __name__ == "__main__":
    run_day(main, run_dev=False)