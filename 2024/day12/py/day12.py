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


def get_perimeter(pt, ydr, xdr, bulk_x, bulk_y) -> int:
    if bulk_x is None or bulk_y is None:
        return 1

    y, x = pt

    # vertical side
    if ydr != 0:
        if y + ydr in bulk_y:
            return 0
        bulk_y.add(ydr + y)
        return 1
    # horizontal side
    if x + xdr in bulk_x:
        return 0
    bulk_x.add(x + xdr)
    return 1


def find_dimension(
    grid: npt.NDArray,
    pt: point | Any,
    covered_points: set[point],
    bulk_x=None,
    bulk_y=None,
):
    if pt in covered_points:
        return 0, 0
    covered_points.add(pt)

    y, x = pt
    area = 1
    perimeter = 0

    for ydr, xdr in adjacent_squares():
        adj_pt = (y + ydr, x + xdr)
        if out_of_bound(grid, adj_pt) or grid[adj_pt] != grid[pt]:
            perimeter += get_perimeter(pt, ydr, xdr, bulk_x, bulk_y)
        elif adj_pt not in covered_points:
            a, p = find_dimension(grid, adj_pt, covered_points, bulk_x, bulk_y)
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
        result += a * p

    return result


def part2(grid: npt.NDArray):
    covered_points: set[point] = set()

    result = 0
    for pt in np.ndindex(np.shape(grid)):
        if pt in covered_points:
            continue
        bulk_x, bulk_y = set(), set()
        a, p = find_dimension(grid, pt, covered_points, bulk_x, bulk_y)

        print(bulk_x, bulk_y)
        print(grid[pt], p, a * p)
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
    print(part2(grid))


if __name__ == "__main__":
    main()
