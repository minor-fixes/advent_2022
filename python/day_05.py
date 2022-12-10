import collections
import dataclasses
import re
from typing import ClassVar, Optional


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


@dataclasses.dataclass
class Crate:
    name: str
    next: Optional["Crate"]


@dataclasses.dataclass
class Stack:
    top: Optional[Crate] = None

    def push(self, c: Crate) -> None:
        c.next = self.top
        self.top = c

    def pop(self) -> Crate:
        ret = self.top
        self.top = self.top.next
        return ret

    def peek(self) -> str:
        return self.top.name

    def restack_n_from(self, other: "Stack", n: int) -> None:
        for _ in range(n):
            self.push(other.pop())

    def move_n_from(self, other: "Stack", n: int) -> None:
        travel = other.top
        for _ in range(n - 1):
            travel = travel.next
        begin = other.top
        other.top = travel.next
        travel.next = self.top
        self.top = begin


class Stacks:
    def __init__(self, stacks_str):
        lines = stacks_str.splitlines()
        num_stacks = len(lines.pop().strip().split())
        self.stacks = [Stack() for _ in range(num_stacks)]
        for line in reversed(lines):
            for i in range(num_stacks):
                if (c := line[4 * i + 1]) != " ":
                    self.stacks[i].push(Crate(c, None))

    def restack_instruction(self, s: Step):
        self.stacks[s.end - 1].restack_n_from(self.stacks[s.start - 1], s.repeat)

    def move_instruction(self, s: Step):
        self.stacks[s.end - 1].move_n_from(self.stacks[s.start - 1], s.repeat)

    def message(self):
        return "".join([stack.peek() for stack in self.stacks])


def part_1(input: str) -> str:
    stack_str, instructions_str = input.split("\n\n")
    stacks = Stacks(stack_str)
    instructions = [
        Step.from_str(line) for line in instructions_str.strip().splitlines()
    ]
    _ = [stacks.restack_instruction(i) for i in instructions]
    return stacks.message()


def part_2(input: str) -> str:
    stack_str, instructions_str = input.split("\n\n")
    stacks = Stacks(stack_str)
    instructions = [
        Step.from_str(line) for line in instructions_str.strip().splitlines()
    ]
    _ = [stacks.move_instruction(i) for i in instructions]
    return stacks.message()
