import sys

filename = "./input.txt"
keys = []
locks = []


def sum_rows(arr):
    res = [0] * len(arr[0])
    for row in arr:
        for i, char in enumerate(row):
            if char == "#":
                res[i] = res[i] + 1

    return res


with open(filename) as file:
    arr = []
    for line in file:
        line = line.strip()
        if line:
            arr.append(line)
        if len(arr) == 7:
            if "." in arr[0]:
                keys.append(sum_rows(arr))
            else:
                locks.append([*sum_rows(arr), len(arr)])
            arr = []


def fits(key, lock):
    for i, val in enumerate(key):
        if key[i] + lock[i] > 7:
            return False
    return True


count = 0
for key in keys:
    for lock in locks:
        if fits(key, lock):
            count = count + 1

print(count)
