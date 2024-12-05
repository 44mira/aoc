import sys
from collections import defaultdict


def check_valid_update1(
    hashmap: dict[str, list[str]], update: list[str]
) -> int:
    order: set = set()

    for page in update:
        # check if any of the future pages are already passed
        if any(x in order for x in hashmap[page]):
            return -1
        order.add(page)

    return int(update[len(update) // 2])


def part1(hashmap: dict[str, list[str]], updates: list[list[str]]):
    sum_middle = 0

    for update in updates:
        result = check_valid_update1(hashmap, update)
        if result != -1:
            sum_middle += result

    return sum_middle


def check_valid_update2(
    hashmap: dict[str, list[str]], update: list[str]
) -> int:
    result: list[str] = []

    flag = False
    for page in update:
        max_index = 0
        for i in range(len(result)):
            # check if existing result should be BEFORE current page
            if result[i] in hashmap[page]:
                flag = True
                max_index = i + 1
        result.insert(max_index, page)

    if flag:
        return int(result[len(result) // 2])

    return -1


def part2(hashmap, updates):
    sum_middle = 0

    for update in updates:
        result = check_valid_update2(hashmap, update)
        if result != -1:
            sum_middle += result

    return sum_middle


def parse_input(lines):
    hashmap: dict[str, list[str]] = defaultdict(list)  # k must be in before v
    line = 0
    while True:
        if lines[line] == "":
            line += 1
            break
        k, v = lines[line].split("|")
        hashmap[k].append(v)
        line += 1

    updates: list[list[str]] = []
    while line < len(lines):
        updates.append(lines[line].split(","))
        line += 1

    return hashmap, updates


def main():
    filename = "../test.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    hashmap, updates = parse_input(lines)

    print(part1(hashmap, updates))
    print(part2(hashmap, updates))


if __name__ == "__main__":
    main()
