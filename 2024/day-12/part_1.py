import sys

filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        data.append(line.strip())

visited = [[0 for i in data[0]] for j in data]


def traverse(i, j, curr, visited):
    if (
        i < 0
        or i >= len(visited)
        or j < 0
        or j >= len(visited[0])
        or data[i][j] != curr
    ):
        return 1, 0
    if visited[i][j]:
        return 0, 0
    visited[i][j] = 1

    a, a1 = traverse(i + 1, j, curr, visited)
    b, b1 = traverse(i - 1, j, curr, visited)
    c, c1 = traverse(i, j + 1, curr, visited)
    d, d1 = traverse(i, j - 1, curr, visited)

    return (a + b + c + d), (a1 + b1 + c1 + d1 + 1)


res = 0

for i, c1 in enumerate(data):
    for j, c2 in enumerate(data[i]):
        if not visited[i][j]:
            a, b = traverse(i, j, data[i][j], visited)
            res = res + a * b

print(res)
