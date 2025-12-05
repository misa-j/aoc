filename = "./input.txt"
data = []
cnt = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        data.append(line)
        cnt.append([0] * len(line))

res = 0
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
seen = set()
stack = []

for i, row in enumerate(data):
    for j, char in enumerate(row):
        n = 0
        if char == ".":
            continue
        for x, y in dirs:
            if i + x < 0 or i + x >= len(data) or j + y < 0 or j + y >= len(row):
                continue

            if data[i + x][j + y] == "@":
                n += 1

        cnt[i][j] = n
        if n < 4:
            seen.add((i, j))
            stack.append((i, j))

while stack:
    i, j = stack.pop()
    res += 1

    for x, y in dirs:
        x1 = x + i
        y1 = y + j
        if x1 < 0 or x1 >= len(data) or y1 < 0 or y1 >= len(row):
            continue
        if data[x1][y1] != "@":
            continue

        cnt[x1][y1] -= 1

        if cnt[x1][y1] < 4 and not (x1, y1) in seen:
            seen.add((x1, y1))
            stack.append((x1, y1))

print(res)
