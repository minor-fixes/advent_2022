from typing import List


def elf_totals(input: str) -> List[int]:
    return [
        sum([int(line) for line in block.splitlines()])
        for block in input.strip().split("\n\n")
    ]


def part_1(input: str) -> int:
    return max(elf_totals(input))


def part_2(input: str) -> int:
    return sum(sorted(elf_totals(input), reverse=True)[:3])
