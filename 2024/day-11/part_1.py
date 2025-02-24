import sys

filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        # data = [int(n) for n in line.strip().split(" ")]
        data = line.strip().split(" ")

for j in range(25):
    new_data = []
    for i, num in enumerate(data):
        if num == "0":
            new_data.append("1")
        elif len(num) % 2 == 0:
            half = len(num) // 2
            new_data.append(str(int(num[0:half])))
            new_data.append(str(int(num[half:])))
            # print(num[0:half], num[half:])
        else:
            new_data.append(str(int(num) * 2024))
    data = new_data
    # print(j, data)

print(len(data))
