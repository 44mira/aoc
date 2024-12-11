from collections import Counter
from sys import argv
from functools import cache
from timeit import timeit


def blink(stone) -> tuple[int] | tuple[int, int]:
    if stone == 0:
        return (1,)

    n = str(stone)

    if len(n) % 2 == 0:
        return int(n[: len(n) // 2]), int(n[len(n) // 2 :])

    return (stone * 2024,)


def solution(stones: list[int], iteration):
    stones_count = Counter(stones)

    for _ in range(iteration):
        next_count = Counter()
        for k, v in stones_count.items():
            if v == 0:
                continue

            for st in blink(k):
                next_count[st] += v
        stones_count = next_count

    return stones_count.total()


def main():
    global stones, iteration

    filename = "../test.txt"
    iteration = 25
    if len(argv) > 1:
        iteration = int(argv[1])
    if len(argv) > 2:
        filename = argv[2]

    with open(filename, "r") as f:
        stones = list(map(int, f.readline().strip().split()))

    # print(solution(stones, iteration))
    # print(solution(stones, iteration * 3))

    runs = 50

    print(f"\n\nINPUT: {stones}\n")
    print(f"Number of runs: {runs}\n")
    part1_time = timeit(
        stmt="solution(stones, iteration)",
        globals=globals(),
        number=runs,
    )
    print(f"Part 1 ({iteration} blinks): {part1_time:4f}s")

    part2_time = timeit(
        stmt="solution(stones, iteration * 3)",
        globals=globals(),
        number=runs,
    )
    print(f"Part 2 ({iteration * 3} blinks): {part2_time:4f}s")


if __name__ == "__main__":
    main()
