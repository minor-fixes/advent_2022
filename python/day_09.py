import dataclasses
from typing import List, Tuple


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


@dataclasses.dataclass
class Vec:
    delta_x: int
    delta_y: int

    def pull_force(self) -> "Vec":
        clamped_x = clamp(self.delta_x, -1, 1)
        clamped_y = clamp(self.delta_y, -1, 1)
        if self.delta_x == clamped_x and self.delta_y == clamped_y:
            self.delta_x = 0
            self.delta_y = 0
            return self
        self.delta_x = clamped_x
        self.delta_y = clamped_y
        return self

    @classmethod
    def from_str(cls, s: str) -> "Vec":
        match s:
            case "R":
                return cls(1, 0)
            case "L":
                return cls(-1, 0)
            case "U":
                return cls(0, 1)
            case "D":
                return cls(0, -1)
            case _:
                raise ValueError(s)


@dataclasses.dataclass(eq=True, frozen=True)
class Pos:
    x: int
    y: int

    def add(self, vec: Vec) -> "Pos":
        return Pos(self.x + vec.delta_x, self.y + vec.delta_y)

    def diff(self, other: "Pos") -> Vec:
        return Vec(self.x - other.x, self.y - other.y)


class Rope:
    def __init__(self, num_knots: int):
        self.knots = [Pos(0, 0) for _ in range(num_knots)]
        self.tail_positions = set([self.knots[-1]])

    def pull_head(self, dir: Vec, repeat: int):
        for _ in range(repeat):
            self.knots[0] = self.knots[0].add(dir)
            for i, knot in enumerate(self.knots[1:], 1):
                self.knots[i] = knot.add(self.knots[i - 1].diff(knot).pull_force())
            self.tail_positions.add(self.knots[-1])

    def tail_trail_len(self):
        return len(self.tail_positions)


def parse(input: str) -> Tuple[List[Vec], int]:
    return [
        (Vec.from_str((fields := line.split())[0]), int(fields[1]))
        for line in input.strip().splitlines()
    ]


def part_1(input: str) -> int:
    rope = Rope(2)
    for (dir, repeat) in parse(input):
        rope.pull_head(dir, repeat)
    return rope.tail_trail_len()


def part_2(input: str) -> int:
    rope = Rope(10)
    for (dir, repeat) in parse(input):
        rope.pull_head(dir, repeat)
    return rope.tail_trail_len()
