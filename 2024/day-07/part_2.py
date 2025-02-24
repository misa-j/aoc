import sys

filename = "./input.txt"
data = []

with open(filename) as file:
    for line in file:
        line = line.strip().split(" ")
        line[0] = line[0][: len(line[0]) - 1]
        data.append([int(n) for n in line])


def traverse(res: int, curr_res: int, nums: list[int], idx: int):
    if idx >= len(nums):
        return res == curr_res

    num = nums[idx]
    return (
        traverse(res, curr_res + num, nums, idx + 1)
        or traverse(res, curr_res * num, nums, idx + 1)
        or traverse(res, int(str(curr_res) + str(num)), nums, idx + 1)
    )


res = 0
for input_data in data:
    if traverse(input_data[0], input_data[1], input_data[1:], 1):
        res = res + input_data[0]

print(f"Result: {res}")
