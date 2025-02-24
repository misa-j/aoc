import sys

filename = "./input.txt"
grid = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

cnt = [[[-1, -1] for _ in range(len(grid[0]))] for _ in range(len(grid))]


# f = 0 from start, f = 1 from end
def bfs(x1, y1, grid, f):
    nodes = [(x1, y1)]
    cnt[x1][y1][f] = 0
    steps = 1
    while nodes:
        clen = len(nodes)

        while clen:
            clen = clen - 1
            x, y = nodes.pop(0)
            if x > 0 and grid[x - 1][y] != "#" and cnt[x - 1][y][f] == -1:
                cnt[x - 1][y][f] = steps
                nodes.append((x - 1, y))
            if x < len(grid) - 1 and grid[x + 1][y] != "#" and cnt[x + 1][y][f] == -1:
                cnt[x + 1][y][f] = steps
                nodes.append((x + 1, y))
            if y > 0 and grid[x][y - 1] != "#" and cnt[x][y - 1][f] == -1:
                cnt[x][y - 1][f] = steps
                nodes.append((x, y - 1))
            if y < len(grid) - 1 and grid[x][y + 1] != "#" and cnt[x][y + 1][f] == -1:
                cnt[x][y + 1][f] = steps
                nodes.append((x, y + 1))

        steps = steps + 1


seen = {}
path_len = 0


def traverse(x, y, grid, points):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in points:
        return
    if len(points) == 2:
        (x, y) = points[1]
        if grid[x][y] != "#":
            return

    if len(points) == 4:
        spoints = sorted(points, key=lambda x: (x[0] - x[1]))
        walls = [[r, c] for r, c in spoints if grid[r][c] == "#"]
        key = []
        for w in walls:
            key.append(w[0])
            key.append(w[1])

        (x0, y0) = points[0]
        (x1, y1) = points[-1]
        if cnt[x0][y0][0] > cnt[x1][y1][0]:
            return

        saving = path_len - (cnt[x0][y0][0] + cnt[x1][y1][1] + 2)
        key = tuple(key)
        if saving >= 100:
            seen[key] = saving

        return

    points.append((x, y))
    traverse(x + 1, y, grid, points)
    traverse(x - 1, y, grid, points)
    traverse(x, y + 1, grid, points)
    traverse(x, y - 1, grid, points)
    points.pop()


sx, sy = 0, 0
ex, ey = 0, 0
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "S":
            sx = i
            sy = j
        if c == "E":
            ex = i
            ey = j

bfs(sx, sy, grid, 0)
bfs(ex, ey, grid, 1)
path_len = cnt[sx][sy][1]

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if not (cnt[i][j][0] == -1 or cnt[i][j][1] == -1):
            traverse(i, j, grid, [])

print(len(seen))
