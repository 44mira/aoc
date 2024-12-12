from sys import argv
from itertools import product
import numpy as np
import numpy.typing as npt
from typing import Any, TypeAlias

point: TypeAlias = tuple[int, int]


def adjacent_squares():
    for y, x in product(range(-1, 2), repeat=2):
        if abs(x) == abs(y):
            continue
        yield y, x


def out_of_bound(grid: npt.NDArray, pt: point):
    y_bound, x_bound = np.shape(grid)
    y, x = pt

    return x < 0 or x >= x_bound or y < 0 or y >= y_bound


def find_dimension(
    grid: npt.NDArray,
    pt: point | Any,
    covered_points: set[point],
):
    if pt in covered_points:
        return 0, 0
    covered_points.add(pt)

    y, x = pt
    area = 1
    perimeter = 0

    for ydr, xdr in adjacent_squares():
        adj_pt = (y + ydr, x + xdr)
        if out_of_bound(grid, adj_pt):
            perimeter += 1
        elif grid[adj_pt] != grid[pt]:
            perimeter += 1
        elif adj_pt not in covered_points:
            a, p = find_dimension(grid, adj_pt, covered_points)
            area += a
            perimeter += p

    return area, perimeter


def part1(grid: npt.NDArray):
    covered_points: set[point] = set()

    result = 0
    for pt in np.ndindex(np.shape(grid)):
        if pt in covered_points:
            continue
        a, p = find_dimension(grid, pt, covered_points)
        print(grid[pt], a * p)
        result += a * p

    return result


def main():
    filename = "../test2.txt"

    if len(argv) > 1:
        filename = argv[1]

    grid = []
    with open(filename, "r") as f:
        for line in f:
            row = list(line.strip())
            grid.append(row)

    grid = np.array(grid)

    print(grid)
    print(part1(grid))


if __name__ == "__main__":
    main()
