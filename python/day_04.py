from typing import Tuple


def split_nums(s: str, delim: str) -> Tuple[str, str]:
    (x, y) = s.split(delim)
    return (int(x), int(y))


def parse_pair(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    first, second = line.split(",")
    return split_nums(first, "-"), split_nums(second, "-")


def fully_contains(a, b: Tuple[int, int]) -> bool:
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    return b[0] >= a[0] and b[1] <= a[1]


def overlaps(a, b: Tuple[int, int]) -> bool:
    if a[0] > b[1]:
        return False
    return b[0] <= a[1]


def part_1(input: str) -> int:
    elf_pairs = [parse_pair(line) for line in input.strip().splitlines()]
    fully_containing = sum(1 if fully_contains(*p) else 0 for p in elf_pairs)
    return fully_containing


def part_2(input: str) -> int:
    elf_pairs = [parse_pair(line) for line in input.strip().splitlines()]
    overlapping = sum(1 if overlaps(*p) else 0 for p in elf_pairs)
    return overlapping
