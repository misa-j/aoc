import sys

filename = "./input.txt"
nums = []

with open(filename) as file:
    for line in file:
        line = line.strip()
        nums.append(int(line))

print(nums)


def calc_val(snum):
    res = snum * 64
    res1 = res ^ snum
    res1 = res1 % 16777216

    res2 = res1 // 32
    res2 = res2 ^ res1
    res2 = res2 % 16777216

    re3 = res2 * 2048
    re3 = re3 ^ res2
    re3 = re3 % 16777216

    return re3


for idx, n in enumerate(nums):
    for i in range(2000):
        nums[idx] = calc_val(nums[idx])

# for i in range(2000):
#     val = calc_val(val)

# print(val)
# print(calc_val(15887950))

print(nums)
print(sum(nums))
