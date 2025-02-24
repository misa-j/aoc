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


def can_fit(j, data_list):
    # print("canfit", j)
    i = 0
    char = data_list[j]
    empty = 0
    char_len = 0
    # print("start: ", j)
    start = j
    while j >= 0 and data_list[j] == char:
        j = j - 1
        char_len = char_len + 1

    # if j != 0:
    #     print(data_list[j + 1 : start + 1])
    # else:
    #     print(data_list[j : start + 1])

    # print(char_len)

    while i <= j and empty < char_len:
        if data_list[i] != ".":
            empty = 0
        else:
            empty = empty + 1
        i = i + 1

    # print(char_len, "".join(data_list[j + 1 : start + 1]), empty)
    # if empty == char_len:
    #     print("".join(data_list[j + 1 : start + 1]), "->", i - empty)
    return i - empty if empty == char_len else -1


idx_list = []


data_list = input_str.split("|")
data_list.pop(0)
data_list_copy = [*data_list]

j = len(data_list) - 1
while 0 < j:
    while j > 0 and data_list_copy[j] == ".":
        j = j - 1
    end = j
    char = data_list[j]
    while j > 0 and data_list_copy[j] == char:
        j = j - 1

    idx_list.append([j, end])

# print(idx_list)

# for [s, e] in idx_list:
#     print(data_list[s + 1])
#     print("-------------------")
#     # print("data_list[s + 1 : e + 1]")


def place_data(i, j):
    char = data_list[j]
    while j < len(data_list) and data_list[j] == char:
        data_list[i] = data_list[j]
        data_list[j] = "."
        j = j + 1
        i = i + 1


# print("".join(data_list))
i = 0
j = len(data_list) - 1
# print("".join(input_str))
for [s, e] in idx_list:
    idx = can_fit(e, data_list)

    if idx != -1:
        # print("placeing", data_list[s])
        place_data(idx, s + 1)


res = 0
# data_list.reverse()
# print("".join(data_list))
for idx, char in enumerate(data_list):
    if char == ".":
        continue

    res = res + (idx * int(char))

print(res)
