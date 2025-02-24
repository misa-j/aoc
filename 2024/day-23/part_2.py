import sys

filename = "./input.txt"
g = {}
edges_count = {}
start_nodes = set()
with open(filename) as file:
    for line in file:
        x, y = line.strip().split("-")
        # if x.startswith("t"):
        #     start_nodes.add(x)
        # if y.startswith("t"):
        #     start_nodes.add(y)
        if x not in g:
            g[x] = {x}
        if y not in g:
            g[y] = {y}

        g[x].add(y)
        g[y].add(x)

# print(g)

# for key, value in g.items():
#     g[key] = tuple(sorted(list([key, *value])))

common = set()
for node, nbs in g.items():
    for node1 in nbs:
        intnbs = nbs.intersection(g[node1])
        nbs_list = list(intnbs)
        for nb1 in nbs_list:
            intnbs = intnbs.intersection(g[nb1])

        if len(common) < len(intnbs):
            common = intnbs

print(",".join(sorted(list(common))))
# print(len(uniq))
# print(edges_count)
