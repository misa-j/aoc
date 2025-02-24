import sys

filename = "./input.txt"
w = 70 + 1
grid = [[0 for _ in range(w)] for _ in range(w)]
cnt = 0

with open(filename) as file:
    for line in file:
        (x, y) = line.strip().split(",")
        grid[int(y)][int(x)] = 1
        cnt = cnt + 1
        if cnt > 1024:
            break


def bfs(x, y):
    steps = 1
    curr = [(x, y)]
    fx, fy = w - 1, w - 1
    while len(curr):

        for _ in range(len(curr)):
            x, y = curr.pop(0)
            if x == fx and y == fy:
                return grid[x][y]

            if x > 0 and grid[x - 1][y] == 0:
                grid[x - 1][y] = steps
                curr.append((x - 1, y))
            if x < len(grid) - 1 and grid[x + 1][y] == 0:
                grid[x + 1][y] = steps
                curr.append((x + 1, y))
            if y > 0 and grid[x][y - 1] == 0:
                grid[x][y - 1] = steps
                curr.append((x, y - 1))
            if y < len(grid) - 1 and grid[x][y + 1] == 0:
                grid[x][y + 1] = steps
                curr.append((x, y + 1))

        steps = steps + 1


grid[0][0] = 1
print(bfs(0, 0))

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
