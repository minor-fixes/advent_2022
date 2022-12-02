import importlib
import pathlib
import sys
import tempfile

from absl import app, flags
from rules_python.python.runfiles import runfiles

FLAGS = flags.FLAGS
flags.DEFINE_integer("day", None, "Day of code to run")
flags.DEFINE_string("input", "input", "Input to use")
flags.mark_flag_as_required("day")


def day_str(day_num: int) -> str:
    return f"day_{day_num:02}"


def main(argv):
    del argv

    input_file = (
        pathlib.Path("advent_2022")
        / "input"
        / f"{day_str(FLAGS.day)}_{FLAGS.input}.txt"
    )
    r = runfiles.Create()
    with open(r.Rlocation(str(input_file)), "r", encoding="utf-8") as f:
        contents = f.read()

    with tempfile.TemporaryDirectory() as pycache_dir:
        sys.pycache_prefix = pycache_dir
        mod = importlib.import_module(day_str(FLAGS.day), "python")
        if hasattr(mod, "part_1"):
            print(f"Part 1: {mod.part_1(contents)}")
        else:
            print("No part_1() function found")
        if hasattr(mod, "part_2"):
            print(f"Part 2: {mod.part_2(contents)}")
        else:
            print("No part_2() function found")


if __name__ == "__main__":
    app.run(main)
