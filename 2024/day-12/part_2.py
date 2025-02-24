import sys

filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        data.append(line.strip())

visited = [[0 for i in data[0]] for j in data]


def get_edge_count(i, j, curr, grid):
    if (
        i - 1 >= 0
        and i + 1 <= len(grid)
        and grid[i - 1][j] == curr
        and grid[i + 1][j] == curr
    ):
        return 0
    if (
        j - 1 >= 0
        and j + 1 <= len(grid[0])
        and grid[i][j - 1] == curr
        and grid[i][j + 1] == curr
    ):
        return 0
    edges = 0
    if i - 1 < 0 or grid[i - 1][j] != curr:
        edges = edges + 1
    if i - 1 < 0 or grid[i - 1][j] != curr:
        edges = edges + 1
    return edges


def traverse(i, j, curr, visited, visited_row, visited_col):
    if (
        i < 0
        or i >= len(visited)
        or j < 0
        or j >= len(visited[0])
        or data[i][j] != curr
    ):
        n = 1 if i not in visited_row else 0
        n1 = 1 if j not in visited_row else 0
        visited_row[i] = True
        visited_row[j] = True
        return 1, n + n1
    if visited[i][j]:
        return 0, 0
    visited[i][j] = 1

    a, a1 = traverse(i + 1, j, curr, visited, visited_row, visited_col)
    b, b1 = traverse(i - 1, j, curr, visited, visited_row, visited_col)
    c, c1 = traverse(i, j + 1, curr, visited, visited_row, visited_col)
    d, d1 = traverse(i, j - 1, curr, visited, visited_row, visited_col)

    return (a + b + c + d), (a1 + b1 + c1 + d1)


res = 0

for i, c1 in enumerate(data):
    for j, c2 in enumerate(data[i]):
        if not visited[i][j]:
            a, b = traverse(i, j, data[i][j], visited, {}, {})
            print(a, b)
            res = res + a * b

print(res)
