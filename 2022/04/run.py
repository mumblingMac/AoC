#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/4
"""

import pathlib


def expand_range(values: str):
    left, right = values.split("-")
    return list(range(int(left), int(right) + 1))


if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(input_file, "r") as data:
        puzzle_input = data.read().splitlines()

    ##################
    # --- Part 1 --- #
    ##################
    left_elf = [set(expand_range(input.split(",")[0])) for input in puzzle_input]
    right_elf = [set(expand_range(input.split(",")[-1])) for input in puzzle_input]
    print(sum([1 if set1.issubset(set2) or set2.issubset(set1) else 0 for set1, set2 in zip(left_elf, right_elf)]))

    ##################
    # --- Part 2 --- #
    ##################
    print(sum([1 if len(set1 & set2) != 0 else 0 for set1, set2 in zip(left_elf, right_elf)]))
