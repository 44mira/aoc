test_input = (
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)

test_input2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)

import re


def mul(a, b):
    return a * b


def part1(inp):
    matches = re.findall(r"mul\(\d+,\d+\)", inp)
    return sum(map(eval, matches))


def part2(inp):
    matches = re.findall(r"mul\(\d+,\d+\)|do(?:n't)?\(\)", inp)

    ans = 0
    flag = True
    while matches:
        curr = matches.pop(0)

        if curr == "don't()":
            flag = False
        elif curr == "do()":
            flag = True
        elif flag:
            ans += eval(curr)

    return ans


with open("../input.txt", "r") as f:
    inp = "".join(f.readlines())

print(part1(inp))
print(part2(inp))
