from pathlib import Path

input = Path("./input1.txt").read_text()
# input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
idx = 0

print(input)


def parse_int() -> int | None:
    global idx
    result = ""
    while idx < len(input) and input[idx] >= "0" and input[idx] <= "9":
        result = result + input[idx]
        idx = idx + 1

    return int(result) if result else None


def get_result(input: str) -> int:
    global idx
    result = 0
    enabled = True

    while idx < len(input):
        if (
            input[idx] == "d"
            and input[idx + 1] == "o"
            and input[idx + 2] == "("
            and input[idx + 3] == ")"
        ):
            enabled = True
        elif (
            input[idx] == "d"
            and input[idx + 1] == "o"
            and input[idx + 2] == "n"
            and input[idx + 3] == "'"
            and input[idx + 4] == "t"
            and input[idx + 5] == "("
            and input[idx + 6] == ")"
        ):
            enabled = False

        elif (
            input[idx] == "m"
            and input[idx + 1] == "u"
            and input[idx + 2] == "l"
            and input[idx + 3] == "("
        ):
            idx = idx + 4
            a = parse_int()
            b = None
            if idx < len(input) and input[idx] == ",":
                idx = idx + 1
                b = parse_int()
                if a and b and input[idx] == ")" and enabled:
                    result = result + a * b
        idx = idx + 1

    return result


print(f"Result is: {get_result(input)}")
