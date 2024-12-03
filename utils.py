import os


def parse_input(filepath: os.PathLike):
    with open(filepath, 'r') as file:
        content = [x.split() for x in file.readlines()]
        return content

def raw_input(filepath: os.PathLike):
    with open(filepath, 'r') as file:
        return file.read()

if __name__ == "__main__":
    print(parse_input("/Users/eaho/Documents/AOC24/01/dev_input.txt"))