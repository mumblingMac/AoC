#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/7
"""

import pathlib
from collections import defaultdict

if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(input_file, "r") as data:
        puzzle_input = data.read().splitlines()

    ##################
    # --- Part 1 --- #
    ##################

    cwd = pathlib.Path("/")
    stack = []
    folders = defaultdict(int)
    for line in puzzle_input:
        if line.startswith("$ cd"):
            name = line.replace("$ cd ", "")
            if name != "..":
                cwd = (cwd / name).resolve()
                stack.append(str(cwd))
            elif name == "..":
                cwd = cwd.parent.resolve()
                stack.pop()
        if not line.startswith("$"):
            size, item = line.split(" ")
            if size != "dir":
                for dir in stack:
                    folders[dir] += int(size)

    print(sum([folder for folder in folders.values() if folder <= 100000]))

    ##################
    # --- Part 2 --- #
    ##################

    required_space = 30000000 - (70000000 - folders["/"])
    for folder in sorted(folders.values()):
        if folder >= required_space:
            print(folder)
            break
