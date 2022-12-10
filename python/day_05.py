import collections
import dataclasses
import re
from typing import ClassVar


@dataclasses.dataclass
class Step:
    start: int
    end: int
    repeat: int

    parse_expr: ClassVar[re.Pattern] = re.compile(r"^move (\d+) from (\d+) to (\d+)$")

    @classmethod
    def from_str(cls, s: str) -> "Step":
        m = cls.parse_expr.match(s)
        return cls(start=int(m[2]), end=int(m[3]), repeat=int(m[1]))


class Stacks:
    def __init__(self, stacks_str):
        lines = stacks_str.splitlines()
        num_stacks = len(lines.pop().strip().split())
        self.stacks = [collections.deque() for _ in range(num_stacks)]
        for line in reversed(lines):
            for i in range(num_stacks):
                if (c := line[4 * i + 1]) != " ":
                    self.stacks[i].append(c)

    def step(self, s: Step):
        for i in range(s.repeat):
            self.stacks[s.end - 1].append(self.stacks[s.start - 1].pop())

    def message(self):
        return "".join([stack[-1] for stack in self.stacks])


def part_1(input: str) -> str:
    stack_str, instructions_str = input.split("\n\n")
    stacks = Stacks(stack_str)
    instructions = [
        Step.from_str(line) for line in instructions_str.strip().splitlines()
    ]
    _ = [stacks.step(i) for i in instructions]
    return stacks.message()


def part_2(input: str) -> str:
    pass
