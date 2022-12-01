#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/1
"""

import pathlib

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = [x.strip().split("\n") for x in data.read().split("\n\n")]

if __name__ == "__main__":

    calories_per_elf = [sum(int(x) for x in elf) for elf in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################
    print(max(calories_per_elf))

    ##################
    # --- Part 2 --- #
    ##################
    print(sum(sorted(calories_per_elf)[-3:]))
