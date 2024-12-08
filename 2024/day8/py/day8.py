from sys import argv
from collections import namedtuple, defaultdict
from itertools import combinations

# point
P = namedtuple("P", ["x", "y"], defaults=[0, 0])
antennas = defaultdict[str, set[P]]

X_MAX = 0
Y_MAX = 0


def parse_input(filename: str) -> antennas:
    global X_MAX, Y_MAX

    points = defaultdict(set)

    with open(filename, "r") as f:
        dimensions = [line for line in f.readlines()]
        Y_MAX = len(dimensions)
        X_MAX = len(dimensions[0].strip())

        for y, line in enumerate(dimensions):
            for x, c in enumerate(line):
                if c.isalnum():
                    points[c].add(P(x, y))

    return points


def find_antinodes(p1: P, p2: P) -> set[P]:
    x_diff = p1.x - p2.x
    y_diff = p1.y - p2.y

    antinodes = set()

    antinodes.add(P(p1.x + x_diff, p1.y + y_diff))
    antinodes.add(P(p2.x - x_diff, p2.y - y_diff))

    return antinodes


def bounded(p):
    return p.x >= 0 and p.x < X_MAX and p.y >= 0 and p.y < Y_MAX


def part1(antennas: antennas) -> int:
    antinodes: set[P] = set()

    for antenna in antennas.values():
        for pair in combinations(antenna, 2):
            for node in find_antinodes(*pair):
                if bounded(node):
                    antinodes.add(node)

    return len(antinodes)


def find_antinodes_2(p1: P, p2: P) -> set[P]:
    x_diff = p1.x - p2.x
    y_diff = p1.y - p2.y

    antinodes = set()

    for i in range(-X_MAX, X_MAX):
        antinodes.add(P(p1.x + x_diff * i, p1.y + y_diff * i))

    return antinodes


def part2(antennas: antennas) -> int:
    antinodes: set[P] = set()

    for antenna in antennas.values():
        for pair in combinations(antenna, 2):
            for node in find_antinodes_2(*pair):
                if bounded(node):
                    antinodes.add(node)

    return len(antinodes)


def main():
    filename = "../test.txt"
    if len(argv) > 1:
        filename = argv[1]

    antennas = parse_input(filename)

    print(part1(antennas))
    print(part2(antennas))


if __name__ == "__main__":
    main()
