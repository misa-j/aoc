filename = "./input.txt"
locations1 = []
locations2 = []

with open(filename) as file:
    for line in file:
        line = line.rstrip().split(" ")
        locations1.append(int(line[0]))
        locations2.append(int(line[-1]))

locations1.sort()
locations2.sort()
distance = 0

for l1, l2 in zip(locations1, locations2):
    distance = distance + abs(l1 - l2)

print(f"Total distance: {distance}")
