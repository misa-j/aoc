filename = "./input.txt"
grid = []
moves = ""
with open(filename) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            grid.append(list(line))
        else:
            moves = moves + line


moves_map = {
    ">": [0, 1],
    "<": [0, -1],
    "^": [-1, 0],
    "v": [1, 0],
}

x, y = 0, 0

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "@":
            x, y = i, j
            break


def find_next_pos(x, y, mx, my):
    while grid[x][y] == "O":
        x = x + mx
        y = y + my

    if grid[x][y] == "#":
        return -1, -1

    return x, y


print(x, y)
for move in moves:
    (mx, my) = moves_map[move]
    next_x = x + mx
    next_y = y + my

    if grid[next_x][next_y] == "#":
        continue
    if grid[next_x][next_y] == ".":
        grid[next_x][next_y] = "@"
        grid[x][y] = "."
        x, y = next_x, next_y
    else:
        dest_x, dest_y = find_next_pos(next_x, next_y, mx, my)
        if dest_x == -1:
            continue

        grid[dest_x][dest_y] = "O"
        grid[next_x][next_y] = "@"
        grid[x][y] = "."
        x = next_x
        y = next_y

res = 0

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "O":
            res = res + (100 * i + j)

print("\n".join(["".join(row) for row in grid]))

print(res)
