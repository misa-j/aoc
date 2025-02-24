import sys

filename = "./input.txt"
grid = []
points = []

with open(filename) as file:
    for i, line in enumerate(file):
        grid.append(line.strip())
        for j, char in enumerate(line.strip()):
            if char != ".":
                points.append([i, j])

visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
res = 0

for i, (p1x, p1y) in enumerate(points):
    for j, (p2x, p2y) in enumerate(points):
        if i == j or grid[p1x][p1y] != grid[p2x][p2y]:
            continue

        x = (p1x - p2x) * 2
        y = (p1y - p2y) * 2

        x1 = p2x + x
        y1 = p2y + y

        if x1 < 0 or x1 >= len(grid) or y1 < 0 or y1 >= len(grid[0]) or visited[x1][y1]:
            continue

        visited[x1][y1] = 1

        res = res + 1

print(f"Result: {res}")
