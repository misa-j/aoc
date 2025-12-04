filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        data.append(line)

res = 0


for row in data:
    curr = []
    remaining = len(row) - 1
    idx = 0
    for n in range(len(row)):
        if not curr:
            curr.append(row[idx])
            idx += 1
            continue

        while curr and curr[-1] < row[idx] and (len(curr) + remaining) > 12:
            curr.pop()

        if len(curr) < 12:
            curr.append(row[idx])

        idx += 1
        remaining -= 1

    res += int("".join(curr))

print(res)
