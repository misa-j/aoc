filename = "./input.txt"
data = []

with open("input.txt", "r") as f:
    last_line = [x for x in f.readlines()[-1].split(" ") if x]

with open(filename) as file:
    for line in file:
        if "+" in line or "*" in line:
            continue
        nums = [int(n) for n in line.strip().split(" ") if n]
        if not data:
            data = nums
        else:
            for i, n in enumerate(nums):
                if last_line[i] == "+":
                    data[i] += n
                else:
                    data[i] *= n

print(sum(data))
