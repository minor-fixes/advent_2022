import dataclasses
import re
from typing import ClassVar, List, Optional, Tuple


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

    def push(self, begin: Crate, end: Crate) -> None:
        end.next = self.top
        self.top = begin

    def pop(self, n: int) -> Tuple[Crate, Crate]:
        begin = travel = self.top
        for _ in range(n - 1):
            travel = travel.next
        self.top = travel.next
        return (begin, travel)

    def peek(self) -> str:
        return self.top.name


class Stacks:
    def __init__(self, stacks_str):
        lines = stacks_str.splitlines()
        num_stacks = len(lines.pop().strip().split())
        self.stacks = [Stack() for _ in range(num_stacks)]
        for line in reversed(lines):
            for i in range(num_stacks):
                if (c := line[4 * i + 1]) != " ":
                    self.stacks[i].push(crate := Crate(c, None), crate)

    def restack(self, s: Step):
        for _ in range(s.repeat):
            self.stacks[s.end - 1].push(*self.stacks[s.start - 1].pop(1))

    def move(self, s: Step):
        self.stacks[s.end - 1].push(*self.stacks[s.start - 1].pop(s.repeat))

    def message(self):
        return "".join([stack.peek() for stack in self.stacks])


def parse(input: str) -> Tuple[Stacks, List[Step]]:
    stack_str, instructions_str = input.split("\n\n")
    stacks = Stacks(stack_str)
    instructions = [
        Step.from_str(line) for line in instructions_str.strip().splitlines()
    ]
    return (stacks, instructions)


def part_1(input: str) -> str:
    stacks, instructions = parse(input)
    _ = [stacks.restack(i) for i in instructions]
    return stacks.message()


def part_2(input: str) -> str:
    stacks, instructions = parse(input)
    _ = [stacks.move(i) for i in instructions]
    return stacks.message()
