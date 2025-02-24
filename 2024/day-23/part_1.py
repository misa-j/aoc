import sys

filename = "./input.txt"
g = {}
start_nodes = set()
with open(filename) as file:
    for line in file:
        x, y = line.strip().split("-")
        if x.startswith("t"):
            start_nodes.add(x)
        if y.startswith("t"):
            start_nodes.add(y)
        if x not in g:
            g[x] = set()
        if y not in g:
            g[y] = set()

        g[x].add(y)
        g[y].add(x)

# print(g)
uniq = set()


def traverse(node: str, g, seen: list):
    if len(seen) == 3:
        if seen[0] in g[seen[-1]]:
            # if seen[-1] == "aq" and seen[0] == "tb":
            #     print(g[node])
            uniq.add(tuple(sorted(seen)))
            # uniq.add(tuple(seen))
        return
    nbs = g[node]

    res = 0
    seen.append(node)
    for nb in nbs:
        if nb in seen:
            continue
        traverse(nb, g, seen)

    # uniq.add(tuple(sorted(seen)))
    seen.remove(node)


# traverse("ta", g, [])
for node in start_nodes:
    traverse(node, g, [])

print(len(uniq))
# print(uniq)
{
    ("ta", "co", "de"),
    ("tb", "wq", "aq"),
    ("tb", "vc", "ub"),
    ("tc", "wh", "yn"),
    ("tc", "co", "ta"),
    ("td", "tc", "wh"),
    ("td", "qp", "kh"),
    ("tb", "wq", "ub"),
    ("td", "yn", "wh"),
    ("tc", "kh", "ta"),
    ("ta", "ka", "co"),
    ("tc", "td", "qp"),
    ("tb", "ka", "de"),
    ("ta", "co", "ka"),
    ("tb", "cg", "de"),
    ("ta", "de", "ka"),
    ("td", "tc", "kh"),
    ("ta", "de", "co"),
    ("tc", "wh", "qp"),
    ("tb", "vc", "aq"),
    ("td", "qp", "wh"),
    ("ta", "kh", "tc"),
    ("ta", "ka", "de"),
    ("tc", "td", "yn"),
    ("tb", "cg", "aq"),
    ("ta", "co", "tc"),
    ("tc", "kh", "qp"),
}
