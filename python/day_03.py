import functools
import itertools
import operator
from typing import Any, Iterable


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


def groups_of(i: Iterable[Any], n: int) -> Iterable[Iterable[Any]]:
    # From: https://www.geeksforgeeks.org/python-split-tuple-into-groups-of-n/
    # iter(i) - makes an iterator over i
    # [...] * n - now there is a list of length n with copies of the iterator
    # zip(*...) - collect tuples by taking one element from each iter in list.
    # Because they are copies, taking from the first iter advances the others in
    # the list.
    return zip(*([iter(i)] * n))


def part_1(input: str) -> int:
    return sum(
        item_score(common_item(split_ruck(ruck))) for ruck in input.strip().splitlines()
    )


def part_2(input: str) -> int:
    groups = groups_of(input.strip().splitlines(), 3)
    return sum(item_score(common_item(group)) for group in groups)
