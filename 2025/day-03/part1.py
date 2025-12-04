filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        data.append(line)

res = 0

for row in data:
    curr = 0
    l = len(row)
    mx = row[-1]
    idx = l - 2
    for n in range(l - 1):
        curr = max(curr, int(row[idx] + mx))
        mx = max(mx, row[idx])
        idx -= 1

    res += curr

print(res)
