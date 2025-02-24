import sys

filename = "./input.txt"
instructions = []
ra, rb, rc = 0, 0, 0

with open(filename) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Register A:"):
            ra = int(line.split(": ")[1])
        elif line.startswith("Register B:"):
            rb = int(line.split(": ")[1])
        elif line.startswith("Register C:"):
            rc = int(line.split(": ")[1])
        else:
            instructions.extend([int(n) for n in line.split(" ")[1].split(",")])


def get_op_val(op):
    if op <= 3:
        return op
    if op == 4:
        return ra
    if op == 5:
        return rb
    if op == 6:
        return rc


i = 0
output = []
while i < len(instructions):
    instruction = instructions[i]
    opl = instructions[i + 1]
    opc = get_op_val(instructions[i + 1])
    match instruction:
        case 0:
            res = ra // 2**opc
            ra = res
        case 1:
            res = rb ^ opl
            rb = res
        case 2:
            res = opc % 8
            rb = res
        case 3:
            if ra != 0:
                i = opl
                continue
        case 4:
            res = rb ^ rc
            rb = res
        case 5:
            res = opc % 8
            output.append(str(res))
        case 6:
            res = ra // 2**opc
            rb = res
        case 7:
            res = ra // 2**opc
            rc = res

    i = i + 2

print(",".join(output))
