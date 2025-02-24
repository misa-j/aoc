import sys

filename = "./input.txt"
grid = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

sys.setrecursionlimit(len(grid) * len(grid[0]))
print(sys.getrecursionlimit(), len(grid) * len(grid[0]))


# 1: up, 2: right: 3: down: 4: left
def traverse(grid, i, j, dir) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 1

    if grid[i][j] == "#":
        if dir == 1:
            return traverse(grid, i + 1, j + 1, 2)
        if dir == 2:
            return traverse(grid, i + 1, j - 1, 3)
        if dir == 3:
            return traverse(grid, i - 1, j - 1, 4)
        if dir == 4:
            return traverse(grid, i - 1, j + 1, 1)
    else:
        n = 1 if grid[i][j] == "." else 0
        grid[i][j] = "X"
        if dir == 1:
            return traverse(grid, i - 1, j, 1) + n
        if dir == 2:
            return traverse(grid, i, j + 1, 2) + n
        if dir == 3:
            return traverse(grid, i + 1, j, 3) + n
        if dir == 4:
            return traverse(grid, i, j - 1, 4) + n


result = 0
for i, x in enumerate(grid):
    for j, y in enumerate(grid[i]):
        if grid[i][j] == "^":
            result = traverse(grid, i, j, 1)

print(grid)
print(result)

[
    [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "X", ".", ".", ".", ".", "#"],
    [".", ".", ".", ".", "X", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", "X", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "X", ".", ".", "#", ".", "."],
    [".", ".", ".", ".", "X", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", "X", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
]
