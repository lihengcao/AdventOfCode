# sorting packets

from my_functions import *


filename = "input.txt"
filename = "sample.txt"


with open(filename, "r") as f:
    # ast.literal_eval() is cheating... but I did use it to verify correctness
    # packets = [deserialize_nested_list(l.strip()) == literal_eval(l.strip()) for l in f.readlines() if l != '\n']
    # print(all(packets))

    packets = [line.strip() for line in f.readlines()]


def first() -> int:
    pass


def second() -> int:
    pass


if __name__ == '__main__':
    print(first())
    # print(second())
