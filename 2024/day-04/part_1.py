filename = "input1.txt"

# input = """....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX"""
grid = []

# for line in input.split("\n"):
#     grid.append(list(line))

with open(filename) as file:
    for line in file:
        grid.append(list(line))
    # lines = [line.rstrip() for line in file]

prev_char_map = {"X": "", "M": "X", "A": "M", "S": "A"}


def traverse(
    grid: list[list[str]], prev_char: str, i: int, j: int, prev_char_map, dir=-1
) -> int:
    if (
        i < 0
        or i >= len(grid)
        or j < 0
        or j >= len(grid[0])
        or grid[i][j] not in "XMAS"
    ):
        return 0
    curr_char = grid[i][j]
    if prev_char_map[curr_char] != prev_char:
        return 0
    if curr_char == "S":
        return 1

    a, b, c, d, e, f, g, h = [0, 0, 0, 0, 0, 0, 0, 0]

    if dir == 0 or dir == -1:
        a = traverse(grid, curr_char, i + 1, j, prev_char_map, 0)
    if dir == 1 or dir == -1:
        b = traverse(grid, curr_char, i - 1, j, prev_char_map, 1)
    if dir == 2 or dir == -1:
        c = traverse(grid, curr_char, i, j + 1, prev_char_map, 2)
    if dir == 3 or dir == -1:
        d = traverse(grid, curr_char, i, j - 1, prev_char_map, 3)

    if dir == 4 or dir == -1:
        e = traverse(grid, curr_char, i + 1, j + 1, prev_char_map, 4)
    if dir == 5 or dir == -1:
        f = traverse(grid, curr_char, i - 1, j - 1, prev_char_map, 5)
    if dir == 6 or dir == -1:
        g = traverse(grid, curr_char, i - 1, j + 1, prev_char_map, 6)
    if dir == 7 or dir == -1:
        h = traverse(grid, curr_char, i + 1, j - 1, prev_char_map, 7)

    return a + b + c + d + e + f + g + h


result = 0

for i, char1 in enumerate(grid):
    for j, char2 in enumerate(grid[i]):
        if grid[i][j] == "X":
            result = result + traverse(grid, "", i, j, prev_char_map)

print(f"XMAS count: {result}")
