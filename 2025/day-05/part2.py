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
ranges.sort()
non_overlapping = []

for min, mx in ranges:
    if not non_overlapping:
        non_overlapping.append((min, mx))
        continue

    if non_overlapping[-1][1] >= min:
        min1, max1 = non_overlapping.pop()
        non_overlapping.append((min1, max(mx, max1)))
    else:
        non_overlapping.append((min, mx))

for min, max in non_overlapping:
    res += (max - min) + 1

print(res)
