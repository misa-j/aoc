import numpy as np

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
                positions.append(int(part[idx + 1 :]) + 10000000000000)

        if len(positions) == 6:
            data.append(positions)
            positions = []


res = 0
for positions in data:
    (x, y, x1, y1, final_x, final_y) = positions

    # solve equation
    # (x * ac + x1 * bc) == final_x
    # (y * ac + y1 * bc) == final_y

    a = np.array([[x, x1], [y, y1]])
    b = np.array([final_x, final_y])
    (ac, bc) = np.linalg.solve(a, b)
    # print(ac, bc, ac.is_integer(), bc.is_integer(), int(ac))
    ac = round(ac)
    bc = round(bc)
    if (x * ac + x1 * bc) == final_x and (y * ac + y1 * bc) == final_y:
        # print(ac, bc, ac.is_integer(), bc.is_integer())
        res = res + (int(ac) * 3 + int(bc))

print(res)
