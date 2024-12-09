from sys import argv
from itertools import repeat
from typing import TypeAlias

Filesystem: TypeAlias = list[int | None]


def parse_input(filename) -> Filesystem:
    fs: Filesystem = []

    with open(filename, "r") as f:
        content = "".join([line.strip() for line in f.readlines()])

    free = False
    id = 0

    for c in content:
        if free:
            fs.extend(repeat(None, int(c)))
        else:
            fs.extend(repeat(id, int(c)))
            id += 1
        free = not free

    return fs


def fragment_fs(fs: Filesystem) -> Filesystem:
    left = 0
    right = len(fs) - 1

    while True:
        # search for empty from left
        while fs[left] is not None:
            left += 1
        # search for filled from right
        while fs[right] is None:
            right -= 1

        if right <= left:
            break

        # swap their contents
        fs[left], fs[right] = fs[right], fs[left]

    return fs


def compress_fs(fs: Filesystem) -> Filesystem:

    file: int = max(fs, key=lambda a: a or 0) or 0

    for file in range(file, -1, -1):
        current_file = fs.index(file)
        current_filesize = fs.count(file)

        err = False
        left = 0
        while left < len(fs):
            freesize = 0

            while left < len(fs) and fs[left] is not None:
                left += 1
            if left >= len(fs) or left > current_file:
                err = True
                break

            while left + freesize < len(fs) and fs[left + freesize] is None:
                freesize += 1
            if left + freesize >= len(fs):
                err = True
                break

            # if freesize too small, skip
            if freesize >= current_filesize:
                break
            left += freesize

        if err:
            continue

        (
            fs[left : left + current_filesize],
            fs[current_file : current_file + current_filesize],
        ) = (
            fs[current_file : current_file + current_filesize],
            fs[left : left + current_filesize],
        )

    return fs


def get_checksum(fs: Filesystem) -> int:
    result = 0
    for idx, id in enumerate(fs):
        if id is None:
            continue
        result += idx * id

    return result


def part1(fs: Filesystem):
    compressed_fs = fragment_fs(fs[:])
    return get_checksum(compressed_fs)


def part2(fs: Filesystem):
    compressed_fs = compress_fs(fs)
    return get_checksum(compressed_fs)


def main():
    filename = "../test.txt"
    if len(argv) > 1:
        filename = argv[1]

    fs: Filesystem = parse_input(filename)

    print(part1(fs))
    print(part2(fs))


if __name__ == "__main__":
    main()
