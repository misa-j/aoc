filename = "./input.txt"
grid = []
cnt = []

with open("input.txt", "r") as f:
    first_line = f.readlines()[0]

with open(filename) as file:
    for line in file:
        grid.append([c for c in line.strip()])
        cnt.append([0] * len(grid[0]))

idx = first_line.index("S")
q = [(0, idx)]
seen = set()
res = 0
cnt[0][idx] = 1

while q:
    l = len(q)
    for i in range(l):
        x, y = q.pop(0)
        if x + 1 >= len(grid):
            continue

        if grid[x + 1][y] == ".":
            key1 = (x + 1, y)
            if not key1 in seen:
                q.append(key1)
            cnt[x + 1][y] += cnt[x][y]
            seen.add(key1)
        else:
            key1 = (x + 1, y - 1)
            key2 = (x + 1, y + 1)
            if not key1 in seen:
                q.append(key1)

            if not key2 in seen:
                q.append(key2)

            cnt[x + 1][y + 1] += cnt[x][y]
            cnt[x + 1][y - 1] += cnt[x][y]
            res += 1
            seen.add(key1)
            seen.add(key2)

print(sum(cnt[-1]))
