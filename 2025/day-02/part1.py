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


def is_valid(num: str):
    l = len(num)
    if l % 2 != 0:
        return True

    l //= 2
    return not (num[0:l] == num[l:])


for a, b in data:
    for i in range(a, b + 1):
        if not is_valid(str(i)):
            res += i

print(res)
