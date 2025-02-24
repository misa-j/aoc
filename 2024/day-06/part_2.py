import sys
import copy

filename = "./input.txt"
grid = []


with open(filename) as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

should_visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
sys.setrecursionlimit(len(grid) * len(grid[0]))

si = 0
sj = 0
for i, x in enumerate(grid):
    for j, y in enumerate(grid[i]):
        if grid[i][j] == "^":
            si = i
            sj = j
            break


def traverse_helper(grid, i, j, dir) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 1

    if grid[i][j] == "#":
        if dir == 1:
            return traverse_helper(grid, i + 1, j + 1, 2)
        if dir == 2:
            return traverse_helper(grid, i + 1, j - 1, 3)
        if dir == 3:
            return traverse_helper(grid, i - 1, j - 1, 4)
        if dir == 4:
            return traverse_helper(grid, i - 1, j + 1, 1)
    else:
        should_visit[i][j] = 1
        if dir == 1:
            return traverse_helper(grid, i - 1, j, 1)
        if dir == 2:
            return traverse_helper(grid, i, j + 1, 2)
        if dir == 3:
            return traverse_helper(grid, i + 1, j, 3)
        if dir == 4:
            return traverse_helper(grid, i, j - 1, 4)


traverse_helper(grid, si, sj, 1)


# 1: up, 2: right: 3: down: 4: left
def traverse(grid, i, j, dir, visited: list[list[set]]) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False

    if grid[i][j] == "#":
        if dir == 1:
            return traverse(grid, i + 1, j + 1, 2, visited)
        if dir == 2:
            return traverse(grid, i + 1, j - 1, 3, visited)
        if dir == 3:
            return traverse(grid, i - 1, j - 1, 4, visited)
        if dir == 4:
            return traverse(grid, i - 1, j + 1, 1, visited)
    else:

        if not visited[i][j]:
            visited[i][j] = set()
        if dir in visited[i][j]:
            return True

        visited[i][j].add(dir)
        if dir == 1:
            res = traverse(grid, i - 1, j, 1, visited)
        if dir == 2:
            res = traverse(grid, i, j + 1, 2, visited)
        if dir == 3:
            res = traverse(grid, i + 1, j, 3, visited)
        if dir == 4:
            res = traverse(grid, i, j - 1, 4, visited)

        # print(visited[i][j])
        # if dir in visited[i][j]:
        #     visited[i][j].remove(dir)

        return res


result = 0

for i, x in enumerate(grid):
    for j, y in enumerate(grid[i]):
        if grid[i][j] == "." and should_visit[i][j]:
            visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            grid[i][j] = "#"
            if traverse(grid, si, sj, 1, visited):
                result = result + 1
            grid[i][j] = "."

# visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
# print(traverse(grid, si, sj, 1, visited))

# print(grid)
# print(result)
print(result)
# print("start", si, sj)
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

[
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, {1}, 0, 0, 0, 0, 0],
]
