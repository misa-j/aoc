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


def calc_position(x, y, xp, yp, steps):
    x1 = (x + (xp * steps)) % w
    y1 = (y + (yp * steps)) % h

    if x1 < 0:
        x1 = x1 + w
    if y1 < 0:
        y1 = y1 + h

    return y1, x1


steps = 0
while True:
    seen = set()
    f = True
    for position in data:
        (x, y, xp, yp) = position
        pos = calc_position(x, y, xp, yp, steps)

        if pos in seen:
            f = False
            break
        seen.add(pos)

    if f:
        print(steps)
        break
    steps = steps + 1
