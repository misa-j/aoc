import sys

filename = "./input.txt"
w = 70 + 1
points = []
grid = [[0 for _ in range(w)] for _ in range(w)]
cnt = 0

with open(filename) as file:
    for line in file:
        (x, y) = line.strip().split(",")
        points.append((int(x), int(y)))
        # grid[int(y)][int(x)] = 1
        # cnt = cnt + 1
        # if cnt > 1024:
        #     break


def bfs(x, y, seen):
    steps = 1
    curr = [(x, y)]
    fx, fy = w - 1, w - 1
    while len(curr):

        for _ in range(len(curr)):
            x, y = curr.pop(0)
            if x == fx and y == fy:
                return seen[x][y]

            if x > 0 and seen[x - 1][y] == 0 and grid[x - 1][y] == 0:
                seen[x - 1][y] = steps
                curr.append((x - 1, y))
            if x < len(grid) - 1 and seen[x + 1][y] == 0 and grid[x + 1][y] == 0:
                seen[x + 1][y] = steps
                curr.append((x + 1, y))
            if y > 0 and seen[x][y - 1] == 0 and grid[x][y - 1] == 0:
                seen[x][y - 1] = steps
                curr.append((x, y - 1))
            if y < len(seen) - 1 and seen[x][y + 1] == 0 and grid[x][y + 1] == 0:
                seen[x][y + 1] = steps
                curr.append((x, y + 1))

        steps = steps + 1


grid[0][0] = 1

for x, y in points:
    seen = [[0 for _ in range(w)] for _ in range(w)]
    grid[y][x] = 1
    if bfs(0, 0, seen) is None:
        print(x, y)
        break

# print(bfs(0, 0))

# print(grid)
[
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
]
