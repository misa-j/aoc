import sys

filename = "./input.txt"
w = 70 + 1
towels = set()
combs = []
cnt = 0

with open(filename) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if "," in line:
            line = line.split(",")
            towels = set([p.strip() for p in line])
        else:
            combs.append(line)


def traverse(word, towels, seen):
    if not word:
        return True
    if word in seen:
        return seen[word]

    for i, char in enumerate(word):
        curr = word[: i + 1]
        # print(curr, "rest", word[i + 1 :])
        if curr in towels:
            if traverse(word[i + 1 :], towels, seen):
                seen[word] = True
                return True

    seen[word] = False
    return False


res = 0
for comb in combs:
    if traverse(comb, towels, {}):
        res = res + 1

print(res)
