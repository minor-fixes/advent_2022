import collections


class Window:
    def __init__(self, init: str):
        self.window = collections.deque(maxlen=len(init))
        for c in init:
            self.window.append(c)

    def slide(self, c: str) -> None:
        self.window.popleft()
        self.window.append(c[0])

    def is_marker(self) -> bool:
        return len(set(self.window)) == len(self.window)


def part_1(input: str) -> int:
    input = input.strip()
    i = 4
    window = Window(input[:i])
    while not window.is_marker():
        window.slide(input[i])
        i += 1
    return i


def part_2(input: str) -> int:
    input = input.strip()
    i = 14
    window = Window(input[:i])
    while not window.is_marker():
        window.slide(input[i])
        i += 1
    return i
