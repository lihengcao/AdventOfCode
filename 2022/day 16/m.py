# 


filename = "input.txt"
filename = "sample.txt"


with open(filename, "r") as f:
    arr = []

    for line in f.readlines():
        l = line.strip().split(' ')
        arr.append([l[1], int(l[4].split('=')[-1][:-1]), l[9:]])

# print(arr)
[print(r) for r in arr]


def first() -> int:
    return 0


def second() -> int:
    return 0


if __name__ == '__main__':
    print(first())
    # print(second())
