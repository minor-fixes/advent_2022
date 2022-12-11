import functools
import operator
from typing import Any, Iterable

from python import util


def split_ruck(rucksack: str) -> Iterable[str]:
    """Splits a rucksack into two halves at the midpoint."""
    return (rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :])


def common_item(rucks: Iterable[str]) -> str:
    """Finds a common item between any number of rucksacks."""
    common = functools.reduce(operator.and_, (set(r) for r in rucks))
    return common.pop()


def item_score(item: str) -> int:
    """Scores a single item."""
    assert len(item) == 1, "item should be single char"
    if item.islower():
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


def part_1(input: str) -> int:
    return sum(
        item_score(common_item(split_ruck(ruck))) for ruck in input.strip().splitlines()
    )


def part_2(input: str) -> int:
    groups = util.groups_of(input.strip().splitlines(), 3)
    return sum(item_score(common_item(group)) for group in groups)
