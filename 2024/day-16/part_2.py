import sys

filename = "./input.txt"
grid = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

sys.setrecursionlimit(len(grid) * len(grid[0]) * 4)
visited = [[[float("inf")] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
seen = [[[float("inf")] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]

# print(visited)
x, y = 0, 0
fx, fy = 0, 0
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "S":
            x, y = i, j
        if c == "E":
            fx, fy = i, j


# 0 >, 1 ^, 2 <, 3 v
def traverse(x, y, dir, score):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "#":
        return
    if seen[x][y][dir] <= score:
        return
    if grid[x][y] == "E":
        seen[x][y][dir] = score
        return
    # if visited[x][y][dir] != float("inf"):
    #     return visited[x][y][dir]

    seen[x][y][dir] = score
    # b, c = float("inf"), float("inf")
    inc_score = score + 1
    inc2_score = score + 1000
    if dir == 0:
        a = traverse(x, y + 1, 0, inc_score)
        b = traverse(x, y, 1, inc2_score)
        c = traverse(x, y, 3, inc2_score)
    elif dir == 1:
        a = traverse(x - 1, y, 1, inc_score)
        b = traverse(x, y, 2, inc2_score)
        c = traverse(x, y, 0, inc2_score)
    elif dir == 2:
        a = traverse(x, y - 1, 2, inc_score)
        b = traverse(x, y, 1, inc2_score)
        c = traverse(x, y, 3, inc2_score)
    else:
        a = traverse(x + 1, y, 3, inc_score)
        b = traverse(x, y, 0, inc2_score)
        c = traverse(x, y, 2, inc2_score)

    # res = min(a, b, c)
    # visited[x][y][dir] = res
    # seen[x][y][dir] = res
    # return res


counted = {}
counted[(x, y)] = True


def count_min_path(x, y):
    if (x, y) in counted:
        return 0

    counted[(x, y)] = True
    up_min = min(*seen[x - 1][y])
    down_min = min(*seen[x + 1][y])
    left_min = min(*seen[x][y - 1])
    right_min = min(*seen[x][y + 1])
    all_min = min(up_min, down_min, left_min, right_min)
    if x == 7 and y == 5:
        print(up_min, down_min, left_min, right_min, *seen[x][y])
    res = 1
    if all_min == up_min:
        res = res + count_min_path(x - 1, y)
    if all_min == down_min:
        res = res + count_min_path(x + 1, y)
    if all_min == left_min:
        res = res + count_min_path(x, y - 1)
    if all_min == right_min:
        res = res + count_min_path(x, y + 1)

    return res


res = traverse(x, y, 0, 0)
print(min(*seen[fx][fy]))
print(seen[fx][fy])
print(count_min_path(fx, fy))
print(counted.keys())

for i, j in counted.keys():
    grid[i][j] = "O"

print("\n".join(["".join(row) for row in grid]))
