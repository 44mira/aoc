from sys import argv
from constants import *


def in_board(point: P) -> bool:
    return (
        point.x >= 0 and point.x < X_MAX and point.y >= 0 and point.y < Y_MAX
    )


def check_front(guard: G, obstacles: set[P]) -> bool:
    return (guard.coordinates + guard.direction) in obstacles


def part1(guard: G, obstacles: set[P]) -> set[P]:
    unique_points: set[P] = set()

    while in_board(guard.coordinates):
        unique_points.add(guard.coordinates)

        if check_front(guard, obstacles):
            guard.turn()
            continue

        guard.move()

    return unique_points


def check_loop(guard: G, obstacles: set[P]) -> bool:
    # we use tuples to lower overhead
    guard_path: set[tuple[D, P]] = set()

    while in_board(guard.coordinates):
        if check_front(guard, obstacles):
            # check if guard has been at the same turn, same direction
            # if yes, we found a loop
            if (guard.direction, guard.coordinates) in guard_path:
                return True
            guard_path.add((guard.direction, guard.coordinates))

            guard.turn()
            continue

        guard.move()

    return False


def part2(guard: G, obstacles: set[P], guard_path: set[P]):
    loop_count = 0

    # consider the path traced by part 1 as candidates for new obstacles
    new_obstacles = guard_path - {guard.coordinates}

    # check if a loop occurs on adding a candidate to the set of obstacles
    for obstacle in new_obstacles:
        loop_count += check_loop(guard.clone(), obstacles | {obstacle})

    return loop_count


# [[ MAIN ]] {{{


def main():
    global X_MAX, Y_MAX

    filename = "../test.txt"
    if len(argv) > 1:
        filename = argv[1]

    obstacles: set[P] = set()
    guard: G = G(D(-1, -1), P(-1, -1))
    with open(filename, "r") as f:
        dimensions = [line.strip() for line in f.readlines()]
        Y_MAX = len(dimensions)
        X_MAX = len(dimensions[0])

        for y, line in enumerate(dimensions):
            for x, c in enumerate(line):
                if c == "#":
                    obstacles.add(P(x, y))
                elif c == "^":
                    guard = G(D(0, -1), P(x, y))

    part1_ans = part1(guard.clone(), obstacles)  # guard path
    print(len(part1_ans))

    part2_ans = part2(guard.clone(), obstacles, part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()


# }}}
