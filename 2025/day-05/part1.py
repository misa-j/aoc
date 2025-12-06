filename = "./input.txt"
ranges = []
ids = []
seen = False

with open(filename) as file:
    for line in file:
        line = line.strip()
        if not line:
            seen = True
            continue
        if not seen:
            id1, id2 = line.split("-")
            ranges.append((int(id1), int(id2)))
        else:
            ids.append(int(line))


res = 0

for id in ids:
    for min, max in ranges:
        if min <= id <= max:
            res += 1
            break

print(res)
