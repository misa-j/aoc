filename = "./input2.txt"
locations1 = []
locations2_map = {}

with open(filename) as file:
    for line in file:
        line = line.rstrip().split(" ")
        locations1.append(line[0])
        l2 = line[-1]
        if l2 not in locations2_map:
            locations2_map[l2] = 0
        locations2_map[l2] = locations2_map[l2] + 1

score = 0

for n in locations1:
    score = score + int(n) * locations2_map.get(n, 0)

print(f"Similarity score: {score}")
