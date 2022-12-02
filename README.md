# Advent of Code 2022

## Setup

1. **Install bazel** - Download
   [bazelisk](https://github.com/bazelbuild/bazelisk/releases/tag/v1.15.0) and
   place the binary in `$PATH` as `bazel`.

## Python

Run a specific day:

```
bazel run //python:aoc -- --day=1
```

Run a specific day using test data:

```
bazel run //python:aoc -- --day=1 --input=test
```