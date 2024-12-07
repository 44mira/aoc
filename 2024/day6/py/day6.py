import sys
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def turn(state):
    next_state = {">": "v", "v": "<", "<": "^", "^": ">"}

    return next_state[state]


def find_guard(lines: list[list[str]]) -> Point:
    for idx, line in enumerate(lines):
        for state in "^>v<":
            if state in line:
                return Point(line.index(state), idx)
    return Point(-1, -1)


def scan_around(guard: Point, lines: list[list[str]]) -> Point | None:
    for dir, face in zip((1, -1), "v^"):
        if guard.y + dir >= len(lines) or guard.y + dir < 0:
            continue

        if (
            lines[guard.y + dir][guard.x] == "#"
            and lines[guard.y][guard.x] == face
        ):
            return Point(guard.x, guard.y + dir)

    for dir, face in zip((1, -1), "><"):
        if guard.x + dir >= len(lines[0]) or guard.x + dir < 0:
            continue
        if (
            lines[guard.y][guard.x + dir] == "#"
            and lines[guard.y][guard.x] == face
        ):
            return Point(guard.x + dir, guard.y)


def move(guard: Point, lines: list[list[str]]) -> Point | None:
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for (x, y), state in zip(directions, "^>v<"):
        if lines[guard.y][guard.x] != state:
            continue

        lines[guard.y][guard.x] = "."

        invalid_y = guard.y + y < 0 or guard.y + y >= len(lines)
        invalid_x = guard.x + x < 0 or guard.x + x >= len(lines[0])
        if invalid_x or invalid_y:
            return None

        lines[guard.y + y][guard.x + x] = state
        return Point(guard.x + x, guard.y + y)


def part1(lines):
    unique_pos = set()
    pos = 0
    guard = find_guard(lines)
    while True:
        if scan_around(guard, lines):
            lines[guard.y][guard.x] = turn(lines[guard.y][guard.x])
            continue

        guard = move(guard, lines)
        if guard is None:
            break

        if guard not in unique_pos:
            unique_pos.add(guard)
            pos += 1

    return pos


def main():
    filename = "../test.txt"

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename, "r") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    print(part1(lines))
    # print(part2(lines))


if __name__ == "__main__":
    main()
