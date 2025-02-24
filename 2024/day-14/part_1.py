import sys

filename = "./input.txt"
data = []
w = 101
h = 103

with open(filename) as file:
    positions = []
    for line in file:
        line = line.strip()

        for part in line.split(" "):
            (p1, p2) = part.split(",")
            idx = p1.index("=")
            positions.append(int(p1[idx + 1 :]))
            positions.append(int(p2))

        if len(positions) == 4:
            data.append(positions)
            positions = []


def calc_position(x, y, xp, yp):
    x1 = (x + (xp * 100)) % w
    y1 = (y + (yp * 100)) % h

    if x1 < 0:
        x1 = x1 + w
    if y1 < 0:
        y1 = y1 + h

    return y1, x1


q1, q2, q3, q4 = 0, 0, 0, 0
for position in data:
    (x, y, xp, yp) = position
    (x1, y1) = calc_position(x, y, xp, yp)
    if w // 2 == y1 or h // 2 == x1:
        continue
    if y1 < w // 2:
        if x1 < h // 2:
            q1 = q1 + 1
        else:
            q3 = q3 + 1
    else:
        if x1 < h // 2:
            q2 = q2 + 1
        else:
            q4 = q4 + 1

print(q1, q2, q3, q4)
print(q1 * q2 * q3 * q4)
