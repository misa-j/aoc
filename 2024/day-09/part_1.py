import sys

filename = "./input.txt"
data = ""

with open(filename) as file:
    for line in file:
        data = line.strip()

input_str = ""
file_id = 0
for i in range(0, len(data), 2):
    input_str = input_str + ("|" + str(file_id)) * int(data[i])
    if i < len(data) - 1:
        input_str = input_str + "|." * int(data[i + 1])
    file_id = file_id + 1

data_list = input_str.split("|")
data_list.pop(0)
i = 0
j = len(data_list) - 1
# print("".join(input_str))
while i < j:
    while i < len(data_list) and data_list[i] != ".":
        i = i + 1

    while j > 0 and data_list[j] == ".":
        j = j - 1

    if i < j:
        data_list[i] = data_list[j]
        data_list[j] = "."

res = 0
print(data_list)
for idx, char in enumerate(data_list):
    if idx == 0:
        continue
    if char == ".":
        break

    res = res + (idx * int(char))

print(res)
