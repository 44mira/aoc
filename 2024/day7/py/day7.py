from functools import reduce
import sys
from operator import mul, add
from itertools import product

choices = [mul, add]


def check(lhs: int, rhs: list[int]) -> bool:
    global choices
    n = len(rhs)
    perms = product(choices, repeat=n - 1)

    head, *rest = rhs

    for perm in perms:
        acc = head

        for op, term in zip(perm, rest):
            acc = op(acc, term)
        if acc == lhs:
            return True

    return False


def solution(equations: dict[int, list[int]]):
    result = 0
    for lhs, rhs in equations.items():
        if check(lhs, rhs):
            result += lhs

    return result


def main():
    filename = "../test.txt"

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    equations: dict[int, list[int]] = {}

    with open(filename, "r") as f:
        for line in f:
            target, rest = line.split(":")
            equations[int(target)] = [int(x) for x in rest.split()]

    # part 1
    print(solution(equations))

    # part 2
    choices.append(lambda a, b: int(str(a) + str(b)))
    print(solution(equations))


if __name__ == "__main__":
    main()
