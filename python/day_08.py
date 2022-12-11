from typing import List

import numpy


def num_visible(row: List[int]) -> int:
    max = row[0]
    for i, val in enumerate(row[1:]):
        if val > max:
            max = val
        else:
            return 1 + i


def apply_visible(arr: numpy.ndarray, row: int, num_visible: int) -> None:
    for i in range(num_visible):
        arr[row, i] = 1


def mark_visible(row: numpy.ndarray, visible: numpy.ndarray) -> None:
    visible[0] = 1
    max = row[0]
    for i, val in enumerate(row[1:]):
        if val > max:
            visible[i + 1] = 1
            max = val


def trees_visible(row):
    tallest = row[0]
    for i, val in enumerate(row[1:]):
        if val >= tallest:
            return i + 1
    return len(row) - 1


def part_1(input: str) -> int:
    data = numpy.asarray(
        [[int(c) for c in line] for line in input.strip().splitlines()]
    )
    visible = numpy.zeros_like(data)
    for _ in range(4):
        for i in range(len(data)):
            mark_visible(data[i, :], visible[i, :])
        data = numpy.rot90(data)
        visible = numpy.rot90(visible)
    return numpy.sum(visible)


def part_2(input: str) -> int:
    data = numpy.asarray(
        [[int(c) for c in line] for line in input.strip().splitlines()]
    )

    def scenic_score(i, j: int) -> int:
        l = trees_visible(numpy.flip(numpy.reshape(data[: i + 1, j : j + 1], (-1))))
        r = trees_visible(numpy.reshape(data[i:, j : j + 1], (-1)))
        u = trees_visible(numpy.flip(numpy.reshape(data[i : i + 1, : j + 1], (-1))))
        d = trees_visible(numpy.reshape(data[i : i + 1, j:], (-1)))
        score = l * r * u * d
        return score

    scenic_scores = numpy.array(
        [scenic_score(i, j) for (i, j) in numpy.ndindex(data.shape)], like=data
    )
    return scenic_scores.max()
