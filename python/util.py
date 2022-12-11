from typing import Any, Iterable


def groups_of(i: Iterable[Any], n: int) -> Iterable[Iterable[Any]]:
    # From: https://www.geeksforgeeks.org/python-split-tuple-into-groups-of-n/
    # iter(i) - makes an iterator over i
    # [...] * n - now there is a list of length n with copies of the iterator
    # zip(*...) - collect tuples by taking one element from each iter in list.
    # Because they are copies, taking from the first iter advances the others in
    # the list.
    return zip(*([iter(i)] * n))
