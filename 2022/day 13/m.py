# 

from collections.abc import Callable


filename = "input.txt"
filename = "sample.txt"

with open(filename, "r") as f:
    heightmap = [list(l.strip()) for l in f.readlines()]


def first() -> int:
    pass


def second() -> int:
    pass
    

if __name__ == '__main__':
    print(first())
    # print(second())
