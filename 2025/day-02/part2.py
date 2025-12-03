filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        ranges = line.strip().split(",")

        for r in ranges:
            n1 = int(r.split("-")[0])
            n2 = int(r.split("-")[1])
            data.append((n1, n2))

res = 0


def is_repeated(num: str, slice: int):
    l = len(num)
    if l % slice != 0:
        return False

    for start in range(slice):
        idx = start
        prev = num[idx]
        while idx < l and prev == num[idx]:
            idx += slice

        if idx < l:
            return False

    return True


def is_valid(num: str):
    h = len(num) // 2
    for i in range(1, h + 1):
        if is_repeated(num, i):
            return False

    return True


for a, b in data:
    for i in range(a, b + 1):
        if not is_valid(str(i)):
            res += i

print(res)
