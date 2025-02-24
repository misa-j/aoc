import sys

filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        # data = [int(n) for n in line.strip().split(" ")]
        data = line.strip().split(" ")

# for j in range(75):
#     new_data = []
#     for i, num in enumerate(data):
#         if num == "0":
#             new_data.append("1")
#         elif len(num) % 2 == 0:
#             half = len(num) // 2
#             new_data.append(str(int(num[0:half])))
#             new_data.append(str(int(num[half:])))
#             # print(num[0:half], num[half:])
#         else:
#             new_data.append(str(int(num) * 2024))
#     data = new_data
#     # print(j, data)

seen = {}


def traverse(num, level):
    if level >= 75:
        return 1
    key = f"{num}-{level}"
    if key in seen:
        return seen[key]

    if num == "0":
        n = traverse("1", level + 1)
    elif len(num) % 2 == 0:
        half = len(num) // 2
        n = traverse(str(int(num[0:half])), level + 1)
        n = n + traverse(str(int(num[half:])), level + 1)
    else:
        n = traverse(str(int(num) * 2024), level + 1)

    seen[key] = n
    return n


res = 0
for num in data:
    res = res + traverse(num, 0)

# print(len(data))
print(res)
