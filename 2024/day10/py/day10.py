from sys import argv
from itertools import product
import numpy as np


def floodfill(grid, scores, current_idx, current_val=0):
    y_bounds, x_bounds = np.shape(grid)

    def out_of_bounds(x, y):
        return (
            y + ydr >= y_bounds
            or y + ydr < 0
            or x + xdr >= x_bounds
            or x + xdr < 0
        )

    if current_val == 9:
        return 1

    y, x = current_idx

    score = 0
    for xdr, ydr in product([-1, 0, 1], repeat=2):
        if abs(xdr) == abs(ydr):  # skip diagonals and 0, 0
            continue

        if out_of_bounds(x, y) or grid[y + ydr, x + xdr] != current_val + 1:
            continue

        if scores[y + ydr, x + xdr] != -1:
            score += scores[y + ydr, x + xdr]
            continue

        score += floodfill(grid, scores, (y + ydr, x + xdr), current_val + 1)

    scores[y, x] = score

    return score


def part1(grid):
    zeroes = zip(*np.where(grid == 0))
    scores = np.zeros(np.shape(grid), dtype=np.int64) - 1

    score = 0
    for zero in zeroes:
        score += floodfill(grid, scores, zero)

    return score


def main():
    filename = "../test.txt"

    if len(argv) > 1:
        filename = argv[1]

    grid = []
    with open(filename, "r") as f:
        for line in f:
            row = list(map(int, line.strip()))
            grid.append(row)

    parsed_grid = np.array(grid)

    print(part1(parsed_grid))


if __name__ == "__main__":
    main()
