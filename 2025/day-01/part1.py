filename = "./input.txt"
data = []
locations2 = []

with open(filename) as file:
    for line in file:
        line = line.rstrip().strip()
        data.append(line)

i = 50
res = 0

for line in data:
    dir = line[0]
    n = int(line[1:]) % 100
    if dir == "R":
        n *= -1

    if n < 0:
        i += n
        if i < 0:
            i += 100
    else:
        i = (i + n) % 100

    if i == 0:
        res += 1

print(res)
