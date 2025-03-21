from heapq import heappush, heappop

filename = "./input1.txt"

all_pages = set()
data = []
g = {}
deps = {}
curr_deps = set()

with open(filename) as file:
    for line in file:
        if "|" in line:
            a, b = line.strip().split("|")
            if a not in g:
                g[a] = []

            if b not in deps:
                deps[b] = 0
            if a not in deps:
                deps[a] = 0

            deps[b] = deps[b] + 1
            g[a].append(b)
            all_pages.add(a)
            all_pages.add(b)

with open(filename) as file:
    for line in file:
        if "," in line:
            line = line.strip()
            data.append(line.split(","))


def get_min_node(deps):
    res = float("inf")
    min_node = ""
    for key, val in deps.items():
        if val < res:
            res = val
            min_node = key
        elif val == res and min_node > key:
            res = val
            min_node = key

    return min_node


order = {}
i = 0
while True:
    i = i + 1
    node = get_min_node(deps)
    if not node:
        break
    order[node] = i
    nbs = g.get(node, [])

    for nb in nbs:
        if nb in deps:
            deps[nb] = deps[nb] - 1

    del deps[node]

data = [
    ["78", "45", "48", "38", "52", "62", "29"],
    [
        "74",
        "66",
        "65",
        "34",
        "93",
        "32",
        "21",
        "26",
        "89",
        "31",
        "78",
        "44",
        "18",
        "13",
        "37",
        "85",
        "33",
        "68",
        "79",
        "64",
        "55",
    ],
    ["68", "36", "64", "33", "48", "32", "93", "31", "13", "26", "74"],
    [
        "33",
        "16",
        "44",
        "34",
        "85",
        "79",
        "65",
        "22",
        "42",
        "25",
        "64",
        "87",
        "18",
        "55",
        "52",
        "89",
        "13",
    ],
    [
        "14",
        "78",
        "45",
        "23",
        "16",
        "36",
        "57",
        "74",
        "76",
        "87",
        "75",
        "59",
        "62",
        "73",
        "54",
        "27",
        "17",
        "91",
        "48",
        "29",
        "84",
        "69",
        "38",
    ],
    [
        "11",
        "84",
        "59",
        "45",
        "54",
        "38",
        "36",
        "14",
        "29",
        "52",
        "16",
        "27",
        "62",
        "76",
        "87",
        "78",
        "75",
    ],
    ["34", "18", "26", "74", "29", "31", "85", "17", "64"],
    ["91", "31", "78", "66", "27", "84", "74", "36", "32", "39", "68", "73", "44"],
    [
        "69",
        "62",
        "36",
        "74",
        "45",
        "66",
        "54",
        "91",
        "14",
        "11",
        "27",
        "32",
        "75",
        "39",
        "84",
        "48",
        "73",
        "76",
        "31",
        "29",
        "17",
        "78",
        "97",
    ],
    [
        "59",
        "73",
        "22",
        "21",
        "76",
        "62",
        "14",
        "23",
        "16",
        "79",
        "27",
        "36",
        "55",
        "75",
        "38",
        "54",
        "48",
        "11",
        "52",
        "45",
        "25",
        "84",
        "69",
    ],
    [
        "64",
        "68",
        "39",
        "44",
        "93",
        "13",
        "31",
        "26",
        "74",
        "33",
        "22",
        "66",
        "79",
        "42",
        "55",
        "34",
        "18",
        "65",
        "89",
        "85",
        "37",
    ],
    [
        "87",
        "38",
        "78",
        "57",
        "36",
        "62",
        "45",
        "17",
        "91",
        "59",
        "23",
        "84",
        "76",
        "75",
        "54",
        "14",
        "29",
        "27",
        "48",
        "16",
        "11",
    ],
    [
        "68",
        "17",
        "57",
        "31",
        "11",
        "48",
        "54",
        "73",
        "14",
        "76",
        "91",
        "75",
        "69",
        "74",
        "78",
        "32",
        "84",
        "45",
        "97",
        "66",
        "29",
        "36",
        "39",
    ],
    [
        "38",
        "55",
        "65",
        "52",
        "13",
        "87",
        "18",
        "44",
        "22",
        "16",
        "64",
        "26",
        "23",
        "34",
        "37",
        "42",
        "59",
        "85",
        "21",
    ],
    ["59", "93", "33", "79", "62", "16", "55"],
    [
        "89",
        "21",
        "37",
        "79",
        "93",
        "25",
        "22",
        "52",
        "34",
        "42",
        "64",
        "55",
        "23",
        "68",
        "44",
        "65",
        "32",
        "66",
        "31",
        "26",
        "85",
        "18",
        "13",
    ],
    [
        "16",
        "65",
        "25",
        "33",
        "55",
        "79",
        "21",
        "34",
        "87",
        "18",
        "64",
        "93",
        "52",
        "38",
        "37",
        "23",
        "59",
        "42",
        "62",
    ],
    ["68", "13", "32", "93", "85", "18", "25", "97", "39", "42", "34"],
    ["16", "37", "89", "73", "87", "13", "14", "52", "23"],
    [
        "78",
        "27",
        "73",
        "14",
        "38",
        "45",
        "84",
        "69",
        "23",
        "48",
        "11",
        "87",
        "54",
        "16",
        "62",
        "57",
        "29",
        "74",
        "36",
        "17",
        "59",
        "91",
        "75",
    ],
    ["33", "68", "17", "21", "39"],
    ["93", "13", "68", "34", "32", "37", "55"],
    ["57", "38", "84", "75", "14", "59", "23"],
    [
        "48",
        "91",
        "65",
        "33",
        "97",
        "68",
        "31",
        "57",
        "39",
        "44",
        "27",
        "29",
        "78",
        "64",
        "17",
        "75",
        "93",
        "36",
        "74",
        "66",
        "54",
        "45",
        "32",
    ],
    [
        "25",
        "52",
        "26",
        "65",
        "18",
        "13",
        "23",
        "22",
        "37",
        "59",
        "32",
        "42",
        "33",
        "85",
        "44",
    ],
    ["57", "29", "75", "59", "73", "17", "36"],
    [
        "16",
        "13",
        "89",
        "33",
        "21",
        "42",
        "65",
        "38",
        "55",
        "37",
        "59",
        "34",
        "44",
        "25",
        "85",
        "23",
        "22",
        "64",
        "87",
    ],
    ["32", "97", "42", "39", "78", "21", "33", "26", "13", "85", "55"],
    ["31", "84", "74", "91", "32", "78", "76", "36", "62"],
    [
        "85",
        "23",
        "13",
        "55",
        "42",
        "89",
        "22",
        "68",
        "93",
        "21",
        "26",
        "79",
        "52",
        "59",
        "65",
        "18",
        "87",
        "25",
        "37",
        "34",
        "38",
    ],
    ["34", "75", "84", "23", "62", "54", "48"],
    [
        "76",
        "55",
        "59",
        "62",
        "29",
        "36",
        "38",
        "73",
        "84",
        "16",
        "75",
        "48",
        "87",
        "22",
        "14",
        "79",
        "11",
    ],
    [
        "93",
        "26",
        "21",
        "89",
        "64",
        "31",
        "78",
        "79",
        "17",
        "66",
        "13",
        "65",
        "33",
        "32",
        "44",
        "37",
        "68",
        "74",
        "34",
    ],
    ["42", "37", "21", "44", "85", "16", "64"],
    [
        "65",
        "31",
        "57",
        "13",
        "78",
        "64",
        "45",
        "66",
        "17",
        "48",
        "68",
        "93",
        "54",
        "27",
        "29",
        "36",
        "32",
        "97",
        "44",
        "84",
        "39",
    ],
    ["73", "45", "55", "11", "23", "59", "76", "75", "25", "87", "34", "52", "22"],
    ["18", "37", "79", "26", "11"],
    [
        "16",
        "59",
        "48",
        "11",
        "14",
        "55",
        "36",
        "87",
        "73",
        "21",
        "76",
        "23",
        "69",
        "27",
        "52",
        "75",
        "54",
        "45",
        "62",
        "84",
        "22",
    ],
    [
        "31",
        "44",
        "65",
        "37",
        "78",
        "33",
        "68",
        "36",
        "32",
        "66",
        "17",
        "18",
        "91",
        "93",
        "64",
        "74",
        "26",
        "89",
        "85",
    ],
    [
        "89",
        "65",
        "79",
        "85",
        "22",
        "18",
        "64",
        "42",
        "55",
        "31",
        "34",
        "33",
        "97",
        "26",
        "13",
        "25",
        "68",
    ],
    [
        "17",
        "39",
        "16",
        "59",
        "54",
        "36",
        "78",
        "69",
        "57",
        "48",
        "76",
        "27",
        "84",
        "97",
        "91",
        "75",
        "45",
        "73",
        "62",
        "11",
        "14",
    ],
    [
        "93",
        "21",
        "32",
        "66",
        "55",
        "89",
        "42",
        "74",
        "85",
        "68",
        "22",
        "44",
        "13",
        "64",
        "26",
    ],
    ["65", "26", "44", "74", "36", "78", "89", "31", "66", "32", "29", "13", "57"],
    ["59", "91", "75", "11", "84"],
    [
        "91",
        "97",
        "39",
        "29",
        "57",
        "32",
        "73",
        "78",
        "48",
        "11",
        "84",
        "75",
        "45",
        "76",
        "27",
        "36",
        "69",
        "31",
        "68",
        "66",
        "74",
        "14",
        "17",
    ],
    [
        "33",
        "93",
        "44",
        "85",
        "22",
        "26",
        "64",
        "31",
        "32",
        "65",
        "52",
        "66",
        "34",
        "55",
        "68",
        "39",
        "37",
        "42",
        "18",
    ],
    [
        "23",
        "37",
        "26",
        "42",
        "34",
        "65",
        "18",
        "21",
        "68",
        "79",
        "33",
        "31",
        "66",
        "89",
        "52",
        "22",
        "25",
        "93",
        "32",
    ],
    [
        "37",
        "33",
        "18",
        "66",
        "34",
        "64",
        "32",
        "89",
        "26",
        "79",
        "85",
        "25",
        "68",
        "39",
        "52",
        "44",
        "21",
    ],
    [
        "65",
        "22",
        "33",
        "79",
        "13",
        "68",
        "32",
        "42",
        "37",
        "44",
        "26",
        "25",
        "64",
        "85",
        "18",
        "93",
        "66",
        "89",
        "39",
    ],
    ["14", "59", "69", "87", "26", "13", "34"],
    [
        "42",
        "34",
        "23",
        "11",
        "79",
        "45",
        "75",
        "52",
        "55",
        "73",
        "38",
        "54",
        "22",
        "25",
        "87",
    ],
    [
        "85",
        "34",
        "68",
        "65",
        "33",
        "21",
        "37",
        "26",
        "93",
        "89",
        "22",
        "79",
        "38",
        "52",
        "55",
        "44",
        "87",
        "42",
        "23",
        "13",
        "18",
    ],
    ["75", "48", "22", "73", "27", "45", "57"],
    ["26", "32", "48", "36", "91", "33", "65", "93", "66"],
    [
        "36",
        "39",
        "84",
        "13",
        "17",
        "57",
        "26",
        "32",
        "65",
        "54",
        "93",
        "37",
        "97",
        "78",
        "31",
    ],
    ["42", "87", "34", "73", "13", "14", "85"],
    [
        "66",
        "13",
        "37",
        "17",
        "91",
        "31",
        "57",
        "65",
        "27",
        "78",
        "84",
        "97",
        "68",
        "54",
        "39",
    ],
    [
        "42",
        "39",
        "97",
        "68",
        "25",
        "26",
        "79",
        "18",
        "21",
        "85",
        "44",
        "34",
        "65",
        "89",
        "93",
        "37",
        "55",
        "31",
        "22",
    ],
    ["18", "34", "55", "37", "64", "44", "21"],
    ["23", "52", "84", "87", "57", "38", "76", "27", "69", "22", "48", "62", "16"],
    [
        "26",
        "93",
        "29",
        "44",
        "54",
        "33",
        "31",
        "13",
        "66",
        "65",
        "84",
        "78",
        "64",
        "27",
        "74",
        "39",
        "37",
    ],
    ["37", "18", "57", "13", "17", "29", "31", "32", "36", "93", "26"],
    ["27", "87", "76", "29", "78", "48", "17"],
    ["27", "54", "17", "64", "45", "39", "97", "84", "36", "65", "44", "32", "74"],
    [
        "66",
        "31",
        "22",
        "32",
        "55",
        "13",
        "42",
        "37",
        "18",
        "68",
        "21",
        "79",
        "89",
        "23",
        "85",
        "44",
        "33",
        "34",
        "25",
    ],
    [
        "93",
        "74",
        "39",
        "78",
        "17",
        "18",
        "64",
        "57",
        "13",
        "31",
        "33",
        "29",
        "36",
        "37",
        "84",
        "26",
        "32",
        "65",
        "27",
        "66",
        "97",
        "91",
        "44",
    ],
    ["97", "18", "33", "31", "13", "93", "84", "44", "26"],
    [
        "62",
        "73",
        "48",
        "27",
        "45",
        "54",
        "36",
        "97",
        "16",
        "84",
        "57",
        "76",
        "11",
        "69",
        "78",
        "91",
        "87",
        "59",
        "39",
        "29",
        "17",
        "74",
        "14",
    ],
    ["29", "31", "14", "39", "45", "11", "84", "16", "57", "27", "73"],
    [
        "69",
        "74",
        "59",
        "84",
        "48",
        "73",
        "16",
        "87",
        "62",
        "97",
        "75",
        "76",
        "54",
        "38",
        "45",
        "29",
        "17",
        "36",
        "14",
        "91",
        "27",
    ],
    [
        "93",
        "22",
        "26",
        "64",
        "33",
        "23",
        "52",
        "65",
        "87",
        "18",
        "25",
        "44",
        "55",
        "38",
        "37",
        "21",
        "42",
        "68",
        "85",
        "13",
        "79",
        "89",
        "59",
    ],
    [
        "22",
        "37",
        "13",
        "38",
        "69",
        "18",
        "55",
        "21",
        "52",
        "14",
        "62",
        "34",
        "25",
        "23",
        "16",
        "73",
        "59",
        "85",
        "89",
    ],
    [
        "79",
        "55",
        "62",
        "73",
        "85",
        "87",
        "26",
        "13",
        "69",
        "42",
        "76",
        "37",
        "64",
        "38",
        "16",
        "21",
        "23",
        "52",
        "25",
        "18",
        "59",
        "34",
        "22",
    ],
    ["14", "57", "11", "17", "74", "29", "87"],
    ["85", "66", "68", "23", "21", "32", "93"],
    ["85", "89", "93", "74", "65", "26", "64", "78", "79", "33", "66", "39", "55"],
    [
        "69",
        "91",
        "76",
        "75",
        "14",
        "36",
        "97",
        "54",
        "11",
        "74",
        "62",
        "17",
        "29",
        "45",
        "27",
    ],
    [
        "33",
        "65",
        "89",
        "37",
        "69",
        "38",
        "18",
        "79",
        "87",
        "52",
        "16",
        "23",
        "34",
        "59",
        "21",
        "62",
        "26",
        "42",
        "55",
    ],
    ["85", "25", "13", "55", "21", "64", "93", "38", "62", "79", "65", "23", "37"],
    ["44", "36", "33", "68", "29", "32", "13", "65", "97", "39", "27"],
    ["16", "22", "38", "14", "62", "11", "52"],
    ["45", "36", "93", "68", "14", "33", "44", "32", "48"],
    ["93", "57", "45", "97", "75", "78", "27", "76", "14"],
    ["62", "23", "65", "33", "22", "34", "13", "21", "69", "79", "87"],
    ["22", "69", "14", "16", "52", "79", "73", "11", "37"],
    ["66", "68", "26", "13", "39", "34", "52", "85", "32", "64", "33"],
    ["37", "21", "73", "25", "38", "55", "62", "59", "34", "87", "79", "89", "64"],
    ["84", "59", "73", "74", "75", "17", "91", "78", "23"],
    ["78", "45", "74", "17", "84", "27", "91", "29", "14"],
    ["54", "45", "44", "27", "17", "39", "75", "31", "57", "64", "48"],
    [
        "25",
        "84",
        "23",
        "45",
        "57",
        "69",
        "91",
        "76",
        "87",
        "17",
        "27",
        "73",
        "62",
        "29",
        "54",
        "52",
        "11",
    ],
    ["34", "21", "93", "23", "65", "52", "37", "32", "26", "25", "22"],
    [
        "21",
        "89",
        "87",
        "59",
        "16",
        "62",
        "26",
        "76",
        "55",
        "23",
        "11",
        "14",
        "25",
        "69",
        "42",
        "85",
        "79",
        "34",
        "38",
        "22",
        "37",
    ],
    [
        "68",
        "13",
        "38",
        "32",
        "18",
        "26",
        "93",
        "89",
        "52",
        "85",
        "22",
        "42",
        "44",
        "65",
        "25",
        "34",
        "21",
        "59",
        "33",
    ],
    [
        "97",
        "26",
        "13",
        "79",
        "66",
        "37",
        "64",
        "42",
        "31",
        "55",
        "65",
        "85",
        "39",
        "44",
        "22",
        "18",
        "68",
        "34",
        "93",
        "33",
        "32",
    ],
    [
        "87",
        "11",
        "17",
        "27",
        "36",
        "14",
        "29",
        "76",
        "75",
        "69",
        "78",
        "74",
        "59",
        "91",
        "38",
        "48",
        "62",
        "73",
        "16",
        "57",
        "23",
    ],
    ["29", "18", "34", "13", "89", "17", "39", "37", "26"],
    [
        "68",
        "89",
        "32",
        "17",
        "85",
        "42",
        "74",
        "33",
        "65",
        "18",
        "34",
        "37",
        "31",
        "79",
        "44",
    ],
    [
        "23",
        "21",
        "73",
        "18",
        "42",
        "22",
        "34",
        "14",
        "79",
        "59",
        "69",
        "45",
        "25",
        "52",
        "87",
        "55",
        "75",
    ],
    ["31", "26", "17", "39", "97", "36", "13", "65", "89", "29", "64"],
    [
        "21",
        "62",
        "18",
        "25",
        "69",
        "55",
        "26",
        "65",
        "85",
        "79",
        "33",
        "34",
        "89",
        "42",
        "13",
        "59",
        "22",
        "87",
        "38",
    ],
    ["34", "32", "37", "55", "44", "52", "22", "42", "23", "26", "66", "85", "25"],
]

print(deps)
res = 0
for row in data:
    curr_list = []
    last_idx = -1
    is_valid = True
    for n in row:
        if last_idx > order[n]:
            is_valid = False

        curr_list.append((order[n], n))
        last_idx = order[n]

    if not is_valid:
        curr_list.sort(key=lambda tup: tup[0])
        middle = int(curr_list[len(curr_list) // 2][1])
        res = res + middle

print(res)
