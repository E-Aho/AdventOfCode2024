from utils import run_day

def main(input: str):
    lines = input.strip().split("\n")
    equations = []
    for l in lines:
        test = int(l.split(":")[0])
        values = [int(x) for x in l.split(":")[1].strip().split()]
        equations.append((test, values))

    def eval_if_possible(test_val, input_vals, p2: bool = False):
        running_vals = {input_vals[0]}
        for i in range(1, len(input_vals)):
            new_vals = set()
            for v in running_vals:
                new_vals.add(input_vals[i] * v)
                new_vals.add(input_vals[i] + v)
                if p2:
                    new_vals.add(int(str(v)+str(input_vals[i])))
            running_vals = new_vals
        return test_val in running_vals

    print(sum([test if eval_if_possible(test, vals) else 0 for test, vals in equations]))
    print(sum([test if eval_if_possible(test, vals, p2=True) else 0 for test, vals in equations]))


if __name__ == "__main__":
    run_day(main, run_dev=False, parse_input=False)