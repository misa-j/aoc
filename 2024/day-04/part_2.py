filename = "input2.txt"

# input = """.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# .........."""
grid = []

# for line in input.split("\n"):
#     grid.append(list(line))

with open(filename) as file:
    for line in file:
        grid.append(list(line))


result = 0
# print(grid)
for i, char1 in enumerate(grid):
    if i == 0 or i == len(grid) - 1:
        continue
    for j, char2 in enumerate(grid[i]):
        if j == 0 or j == len(grid[i]) - 1:
            continue
        if grid[i][j] == "A":
            a = False
            b = False
            # up and right -1, 1 -- down left 1, -1
            if (grid[i - 1][j + 1] == "S" and grid[i + 1][j - 1] == "M") or (
                grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S"
            ):
                a = True
            # up and left -1, -1 -- down right 1, 1
            if (grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M") or (
                grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S"
            ):
                b = True

            if a and b:
                result = result + 1

print(f"X-MAS count: {result}")
# [
#     [".", "M", ".", "S", ".", ".", ".", ".", ".", "."],
#     [".", ".", "A", ".", ".", "M", "S", "M", "S", "."],
#     [".", "M", ".", "S", ".", "M", "A", "A", ".", "."],
#     [".", ".", "A", ".", "A", "S", "M", "S", "M", "."],
#     [".", "M", ".", "S", ".", "M", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["S", ".", "S", ".", "S", ".", "S", ".", "S", "."],
#     [".", "A", ".", "A", ".", "A", ".", "A", ".", "."],
#     ["M", ".", "M", ".", "M", ".", "M", ".", "M", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
# ]
