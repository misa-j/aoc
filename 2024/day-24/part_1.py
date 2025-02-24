import sys

filename = "./input.txt"
g = {}
ins = {}
start_nodes = set()
with open(filename) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            key, val = line.split(": ")
            ins[key] = int(val)
        else:
            parts = line.split(" ")
            n1 = parts[0]
            n2 = parts[2]
            n3 = parts[-1]

            if n1 not in g:
                g[n1] = []

            if n2 not in g:
                g[n2] = []

            g[n1].append({"node": n3, "gate": parts[1]})
            g[n2].append({"node": n3, "gate": parts[1]})


def bfs(nodes: list):

    while len(nodes):
        nlen = len(nodes)

        while nlen:
            node = nodes.pop(0)
            nbs = g.get(node["node"], [])

            for nb in nbs:
                nbame = nb["node"]
                if not nbame in ins:
                    ins[nbame] = []

                ins[nbame].append(ins[node["node"]])

                if len(ins[nbame]) == 2:
                    if nb["gate"] == "AND":
                        ins[nbame] = 1 if ins[nbame][0] and ins[nbame][1] else 0
                    elif nb["gate"] == "OR":
                        ins[nbame] = 1 if ins[nbame][0] or ins[nbame][1] else 0
                    else:
                        ins[nbame] = 1 if ins[nbame][0] != ins[nbame][1] else 0
                    nodes.append(nb)

            nlen = nlen - 1


snodes = []
for key, val in ins.items():
    snodes.append({"node": key, "out": int(val)})

# print(snodes)
bfs(snodes)

# print(ins)

zs = []
for key, val in ins.items():
    if key.startswith("z"):
        zs.append((key, val))
        # print(key, val)

zs.sort(key=lambda x: x[0], reverse=True)
# print(zs)
bin_val = "".join([str(z[1]) for z in zs])
print(bin_val)
print(int(bin_val, 2))
# print(g)
