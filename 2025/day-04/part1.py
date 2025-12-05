filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        data.append(line)

res = 0
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

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

        if n < 4:
            res += 1

print(res)
