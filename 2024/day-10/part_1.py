import sys

filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        data.append(line.strip())

seen = set()


def traverse(i, j, prev, grid, path_len):
    if (
        i < 0
        or i >= len(grid)
        or j < 0
        or j >= len(grid[0])
        or (path_len != 0 and int(grid[i][j]) - prev != 1)
        or f"{i},{j}" in seen
    ):
        return 0

    curr_val = int(grid[i][j])
    if curr_val == 9 and path_len == 9:
        seen.add(f"{i},{j}")
        return 1

    a = traverse(i + 1, j, curr_val, grid, path_len + 1)
    b = traverse(i - 1, j, curr_val, grid, path_len + 1)
    c = traverse(i, j + 1, curr_val, grid, path_len + 1)
    d = traverse(i, j - 1, curr_val, grid, path_len + 1)

    return a + b + c + d


res = 0
for i, c1 in enumerate(data):
    for j, c2 in enumerate(data[i]):
        seen = set()
        if data[i][j] == "0":
            res = res + traverse(i, j, 0, data, 0)

# res = traverse(0, 2, 0, data, 0, "")
print(res)

# for path in seen:
#     curr_vals = []
#     for pair in path.split("|"):
#         if pair == "":
#             continue
#         (a, b) = pair.split(",")
#         curr_vals.append(data[int(a)][int(b)])

#     print(curr_vals)

# print(len(seen))
