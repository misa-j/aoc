filename = "./input.txt"
data = []

with open("input.txt", "r") as f:
    last_line = [x for x in f.readlines()[-1].split(" ") if x]

with open(filename) as file:
    for line in file:
        if "+" in line or "*" in line:
            continue
        data.append(" " + line[:-1])

idx = len(data[0]) - 1
curr_nums = []
res = 0

while idx >= 0:
    curr = ""
    for line in data:
        if line[idx]:
            curr += line[idx]
    curr = curr.strip()
    if curr:
        curr_nums.append(int(curr))
    else:
        curr_res = None
        for n in curr_nums:
            if curr_res is None:
                curr_res = n
                continue

            if last_line[-1] == "+":
                curr_res += n
            else:
                curr_res *= n

        last_line.pop()
        res += curr_res
        curr_nums = []

    idx -= 1

print(res)
