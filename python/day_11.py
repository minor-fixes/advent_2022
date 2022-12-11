import collections
import functools
import operator
import itertools
import math
from typing import List

from absl import logging as log


class Monkey:
    def __init__(self):
        pass

    def init(self, pool: List["Monkey"], input: str) -> None:
        lines = input.strip().splitlines()
        self._inspect_count = 0
        self.pool = pool
        self.items = collections.deque(
            int(s)
            for s in lines[1].strip().removeprefix("Starting items: ").split(", ")
        )
        self.operation = lines[2].strip().removeprefix("Operation: new = ")
        self.modulus = int(lines[3].strip().removeprefix("Test: divisible by "))
        self.divisible_idx = int(
            lines[4].strip().removeprefix("If true: throw to monkey ")
        )
        self.not_divisible_idx = int(
            lines[5].strip().removeprefix("If false: throw to monkey ")
        )

    def take_turn(self, lcm, worry_factor=1):
        while self.items:
            self.process_item(lcm, worry_factor)

    def catch(self, item: int) -> None:
        if item is None:
            raise ValueError(item)
        self.items.append(item)

    def inspect_count(self):
        return self._inspect_count

    def process_item(self, lcm, worry_factor):
        old = self.items.popleft()
        log.debug("  Monkey inspects an item with a worry level of %d.", old)
        new = eval(self.operation, {}, {"old": old})
        log.debug("    Worry level is now %d", new)

        if worry_factor != 1:
            new = new // worry_factor
            log.debug(
                "    Monkey gets bored with item. Worry level is divided by %d to %d.",
                worry_factor,
                new,
            )
        else:
            new = new % lcm

        self._inspect_count += 1

        if new % self.modulus:
            log.debug("    Current worry level not is divisible by %d.", self.modulus)
            log.debug(
                "    Item with worry level %d is thrown to monkey %d.",
                new,
                self.not_divisible_idx,
            )
            self.pool[self.not_divisible_idx].catch(new)
        else:
            log.debug("    Current worry level is divisible by %d.", self.modulus)
            log.debug(
                "    Item with worry level %d is thrown to monkey %d.",
                new,
                self.divisible_idx,
            )
            self.pool[self.divisible_idx].catch(new)


def monkey_pool(input: str) -> List[Monkey]:
    blocks = [i for i in input.strip().split("\n\n")]
    pool = [Monkey() for _ in range(len(blocks))]
    [m.init(pool, blocks[i]) for (i, m) in enumerate(pool)]
    return pool


def monkey_business(pool: List[Monkey]) -> int:
    return functools.reduce(
        operator.mul,
        itertools.islice(sorted((m.inspect_count() for m in pool), reverse=True), 2),
    )


def part_1(input: str) -> int:
    pool = monkey_pool(input)
    lcm = math.lcm(*[m.modulus for m in pool])
    for _ in range(20):
        for (i, monkey) in enumerate(pool):
            log.debug("Monkey %d", i)
            monkey.take_turn(lcm=lcm, worry_factor=3)
    return monkey_business(pool)


def part_2(input: str) -> int:
    pool = monkey_pool(input)
    lcm = math.lcm(*[m.modulus for m in pool])
    for turn in range(10000):
        log.info("Turn %d", turn)
        for (i, monkey) in enumerate(pool):
            monkey.take_turn(lcm=lcm)
    return monkey_business(pool)
