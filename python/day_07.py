import abc
import dataclasses
from typing import Dict, List, Optional, Tuple


class Dirent(abc.ABC):
    @abc.abstractmethod
    def name(self) -> int:
        pass

    @abc.abstractmethod
    def size(self) -> int:
        pass


@dataclasses.dataclass
class Dir(Dirent):
    _name: str
    parent: Optional["Dir"]
    entries: Dict[str, Dirent]

    def name(self) -> str:
        return self._name

    def size(self) -> int:
        return sum(e.size() for e in self.entries.values())


@dataclasses.dataclass
class File:
    _name: str
    _size: int

    def name(self) -> str:
        return self._name

    def size(self) -> int:
        return self._size


def dirent_from_str(cwd: Dir, line: str) -> Dirent:
    f1, f2 = line.split(" ")
    if f1 == "dir":
        return Dir(_name=f2, parent=cwd, entries=dict())
    return File(_name=f2, _size=int(f1))


def fs_tree(input: str) -> Tuple[Dir, List[Dir]]:
    cwd = root = Dir("/", None, dict())
    all_dirs = [root]

    input = input[2:]  # Remove leading `$ `
    commands_then_output = input.strip().split("\n$ ")
    for block in commands_then_output:
        lines = block.strip().splitlines()
        command, output = lines[0], lines[1:]
        match command.split():
            case ["cd", "/"]:
                cwd = root
            case ["cd", ".."]:
                cwd = cwd.parent
            case ["cd", dir]:
                cwd = cwd.entries[dir]
            case ["ls"]:
                entries = [dirent_from_str(cwd, line) for line in output]
                all_dirs.extend(e for e in entries if isinstance(e, Dir))
                cwd.entries = {entry.name(): entry for entry in entries}
            case _:
                raise Exception()
    return root, all_dirs


def part_1(input: str) -> int:
    _, dirs = fs_tree(input)
    return sum(d.size() for d in dirs if d.size() <= 100000)


def part_2(input: str) -> int:
    root, dirs = fs_tree(input)
    to_free = 30000000 - (70000000 - root.size())
    return next(s for s in sorted([dir.size() for dir in dirs]) if s >= to_free)
