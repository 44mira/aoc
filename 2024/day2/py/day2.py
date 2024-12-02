#!/usr/bin/env python3

from sys import argv
from typing import TypeAlias

matrix: TypeAlias = list[list[int]]


def check_safety(row: list[int]) -> bool:
    deltas = [b - a for a, b in zip(row, row[1:])]

    # rule 1: increasing or decreasing slope
    slope = all(d > 0 for d in deltas) or all(d < 0 for d in deltas)

    # rule 2: bounded distance
    rate = all(3 >= abs(d) >= 1 for d in deltas)

    return slope and rate


def part1(data: matrix) -> int:
    return sum(check_safety(row) for row in data)


def part2(data: matrix) -> int:
    safe = 0
    for row in data:
        if check_safety(row):
            safe += 1
            continue

        safe += any(
            check_safety(row[:i] + row[i + 1 :]) for i in range(len(row))
        )

    return safe


def parse_data(filename: str) -> matrix:
    data: matrix = []
    with open(filename, "r") as f:
        for line in f:
            row = [int(x) for x in line.strip().split()]
            data.append(row)
    return data


def main():
    filename = "../test.txt"
    if len(argv) > 1:
        filename = argv[1]

    data = parse_data(filename)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
