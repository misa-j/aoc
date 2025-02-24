import copy

filename = "./input.txt"
grid = []
moves = ""
with open(filename) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            row = []
            for char in line:
                if char == "#" or char == ".":
                    row.append(char)
                    row.append(char)
                elif char == "O":
                    row.append("[")
                    row.append("]")
                else:
                    row.append("@")
                    row.append(".")
            grid.append(row)
        else:
            moves = moves + line

print("\n".join(["".join(row) for row in grid]))
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
    while grid[x][y] in "[]":
        x = x + mx
        y = y + my

    if grid[x][y] == "#":
        return False

    return True


def move_lr(x, y, mx, my):
    while grid[x][y] in "[]":
        grid[x][y] = "[" if grid[x][y] == "]" else "]"
        y = y + my

    if grid[x][y] != "#":
        grid[x][y] = "[" if my < 0 else "]"


def place_bracket(next_x, next_y, cx, cy, grid):
    # print((cx, cy), "->", (next_x, next_y))
    grid[next_x][next_y] = grid[cx][cy]
    grid[cx][cy] = "."


def traverse(curr_x, curr_y, mx, my, grid):
    next_x = curr_x + mx
    next_y = curr_y + my
    # print((curr_x, curr_y))
    if grid[next_x][next_y] == "#":
        return False
    if grid[next_x][next_y] == ".":
        # print("end", next_x, next_y)
        return True
    if grid[curr_x][curr_y] == grid[next_x][next_y]:
        return traverse(next_x, next_y, mx, my, grid)

    if grid[curr_x][curr_y] == "[":
        a = traverse(next_x, next_y, mx, my, grid)
        b = traverse(next_x, next_y - 1, mx, my, grid)
    else:
        a = traverse(next_x, next_y, mx, my, grid)
        b = traverse(next_x, next_y + 1, mx, my, grid)

    return a and b


def move_grid(curr_x, curr_y, mx, my, grid):
    next_x = curr_x + mx
    next_y = curr_y + my

    if grid[next_x][next_y] == "#":
        return False
    if grid[next_x][next_y] == ".":
        place_bracket(next_x, next_y, curr_x, curr_y, grid)
        return True
    if grid[curr_x][curr_y] == grid[next_x][next_y]:
        move_grid(next_x, next_y, mx, my, grid)
        place_bracket(next_x, next_y, curr_x, curr_y, grid)
        return

    if grid[curr_x][curr_y] == "[":
        move_grid(next_x, next_y, mx, my, grid)
        move_grid(next_x, next_y - 1, mx, my, grid)
    else:
        move_grid(next_x, next_y, mx, my, grid)
        move_grid(next_x, next_y + 1, mx, my, grid)

    place_bracket(next_x, next_y, curr_x, curr_y, grid)


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
        if move in "<>":
            can_move = find_next_pos(next_x, next_y, mx, my)
            if can_move:
                move_lr(next_x, next_y, mx, my)
                grid[next_x][next_y] = "@"
                grid[x][y] = "."
                x, y = next_x, next_y
        else:
            grid_copy = copy.deepcopy(grid)
            if grid[next_x][next_y] == "[":
                a = traverse(next_x, next_y, mx, my, grid)
                b = traverse(next_x, next_y + 1, mx, my, grid)
                if a and b:
                    move_grid(next_x, next_y, mx, my, grid)
                    move_grid(next_x, next_y + 1, mx, my, grid)
            else:
                # print((next_x, next_y), (next_x, next_y - 1))
                a = traverse(next_x, next_y, mx, my, grid)
                b = traverse(next_x, next_y - 1, mx, my, grid)
                if a and b:
                    move_grid(next_x, next_y, mx, my, grid)
                    move_grid(next_x, next_y - 1, mx, my, grid)

            if a and b:
                # grid = grid_copy
                grid[next_x][next_y] = "@"
                grid[x][y] = "."
                x, y = next_x, next_y

print("\n".join(["".join(row) for row in grid]))
res = 0

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "[":
            res = res + (100 * i + j)


print(res)
