filename = "./input1.txt"

ordering = []
data = []
ordering_map: dict[str, list[str]] = {}
curr_deps = set()

with open(filename) as file:
    for line in file:
        if "|" in line:
            a, b = line.strip().split("|")
            if b not in ordering_map:
                ordering_map[b] = []

            ordering_map[b].append(a)

with open(filename) as file:
    for line in file:
        if "," in line:
            line = line.strip()
            data.append(line)

data = "\n".join(data)

# for line in ordering.split("\n"):
#     a, b = line.strip().split("|")
#     if b not in ordering_map:
#         ordering_map[b] = []

#     ordering_map[b].append(a)

# print(ordering_map)

result = 0
for line in data.split("\n"):
    curr_deps = set()
    nums = line.strip().split(",")
    all_line_nums = set(nums)
    is_valid = True
    for num in nums:
        deps = ordering_map.get(num, [])
        for dep in deps:
            if dep in all_line_nums and dep not in curr_deps:
                # print("msssing", dep, curr_deps, line, num)
                # print("all deps", all_line_nums)
                is_valid = False
                break
        curr_deps.add(num)

    # print(is_valid, nums)
    if is_valid:
        middle_num = nums[len(nums) // 2]
        result = result + int(middle_num)
    else:
        print(nums, ",")

print(f"Result: {result}")
# {
#     "53": ["47", "75", "61", "97"],
#     "13": ["97", "61", "29", "47", "75", "53"],
#     "61": ["97", "47", "75"],
#     "47": ["97", "75"],
#     "29": ["75", "97", "53", "61", "47"],
#     "75": ["97"],
# }
