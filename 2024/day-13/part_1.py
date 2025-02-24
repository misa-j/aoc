import sys

filename = "./input.txt"
data = []

with open(filename) as file:
    positions = []
    for line in file:
        line = line.strip()
        if line.startswith("Button"):
            for part in line.split(", "):
                idx = part.index("+")
                positions.append(int(part[idx + 1 :]))
        if line.startswith("Prize"):
            for part in line.split(", "):
                idx = part.index("=")
                positions.append(int(part[idx + 1 :]))

        if len(positions) == 6:
            data.append(positions)
            positions = []


# print(data)
def traverse(curr_x, curr_y, positions, map):
    (x, y, x1, y1, final_x, final_y) = positions
    if curr_x == final_x and curr_y == final_y:
        return 0
    if curr_x > final_x or curr_y > final_y:
        return float("inf")

    key = (curr_x, curr_y)
    if key in map:
        return map[key]
    a = traverse(curr_x + x, curr_y + y, positions, map) + 3
    b = traverse(curr_x + x1, curr_y + y1, positions, map) + 1
    res = min(a, b)
    map[key] = res
    return res


res = 0
for positions in data:
    cost = traverse(0, 0, positions, {})
    if cost != float("inf"):
        res = res + cost

print(res)
