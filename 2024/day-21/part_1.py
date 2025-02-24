import sys

filename = "./input.txt"
codes = []
# 10 - A
numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
keypad = [["", "^", "A"], ["<", "v", ">"]]

with open(filename) as file:
    for line in file:
        line = line.strip()
        codes.append(line)


def path(x, y, goal, grid):
    points = [(x, y, "")]
    seen = {(x, y)}
    r = len(grid)
    c = len(grid[0])
    while len(points):
        ln = len(points)
        while ln:
            ln = ln - 1
            cx, cy, pth = points.pop(0)
            seen.add((cx, cy))
            # print(cx, cy)
            if grid[cx][cy] == "":
                continue
            if grid[cx][cy] == goal:
                return cx, cy, pth
            if cx > 0 and (cx - 1, cy) not in seen:
                points.append((cx - 1, cy, pth + "^"))
            if cx < r - 1 and (cx + 1, cy) not in seen:
                points.append((cx + 1, cy, pth + "v"))
            if cy > 0 and (cx, cy - 1) not in seen:
                points.append((cx, cy - 1, pth + "<"))
            if cy < c - 1 and (cx, cy + 1) not in seen:
                points.append((cx, cy + 1, pth + ">"))


# x = 3
# y = 2
# x1 = 0
# y1 = 2
# moves = []
# for char in "029A":
#     x, y, pth = path(x, y, char, numpad)
#     pth = pth
#     print("pth", pth)
#     curr_pth = []
#     for char1 in pth:
#         x1, y1, pth1 = path(x1, y1, char1, keypad)
#         pth1 = pth1 if pth1 else "A"
#         curr_pth.append(pth1)
#     curr_pth.append("A")
#     curr_pth.append(path(x1, y1, "A", keypad)[2])
#     x1 = 0
#     y1 = 2
#     curr_pth.append("A")
#     moves.append("".join(curr_pth))
# print(pth)


def traverse(code, level):
    if level == 3:
        x, y = 3, 2
        res = []
        for char in code:
            x, y, pth = path(x, y, char, numpad)
            res.append(pth)
        return res
    if level != 0:
        x, y = 0, 2
        moves = traverse(code, level + 1)
        res = []
        for move in moves:
            curr_path = []
            for char in move:
                x, y, pth = path(x, y, char, keypad)
                curr_path.append(pth)
            res.extend(curr_path)

        return res

    x, y = 0, 2
    moves = traverse(code, level + 1)
    res = []
    for move in moves:
        curr_path = []
        for char in move:
            x, y, pth = path(x, y, char, keypad)
            curr_path.append(pth)
            # x, y, pth = path(x, y, "A", keypad)
        res.extend(curr_path)
        res.append("A")

    return res


res = "".join(traverse("379A", 0))
print(res)
print(len(res))
# print(traverse("029A", 0))
