import bisect
from typing import Iterable, Optional

from python import util


class Cpu:
    def __init__(self, program: Iterable[Optional[int]]):
        cycle = 1
        x = 1
        self.history = [(cycle, x)]
        for instruction in program:
            match instruction:
                case None:
                    cycle += 1
                case val:
                    x += val
                    cycle += 2
                    self.history.append((cycle, x))

    def register_value(self, cycle: int) -> int:
        i = bisect.bisect(self.history, cycle, key=lambda val: val[0])
        return self.history[i - 1][1]

    def signal_strength(self, cycle: int) -> int:
        return self.register_value(cycle) * cycle


def instruction_stream(input: str):
    for line in input.strip().splitlines():
        match line.split():
            case ["addx", num]:
                yield int(num)
            case ["noop"]:
                yield None
            case _:
                raise ValueError(line)


def part_1(input: str) -> int:
    cpu = Cpu(instruction_stream(input))
    return sum(cpu.signal_strength(n) for n in [20, 60, 100, 140, 180, 220])


def part_2(input: str) -> int:
    cpu = Cpu(instruction_stream(input))
    chars = [
        "#"
        if (sig := cpu.register_value(n + 1)) >= (n % 40) - 1 and sig <= (n % 40) + 1
        else "."
        for n in range(240)
    ]

    for g in util.groups_of(chars, 40):
        print("".join(g))
