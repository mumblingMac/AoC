#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/1
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


def count_increases(sonar_measurements: list) -> int:
    increases = 0
    for index, depth in enumerate(sonar_measurements):
        if index == 0:
            continue
        if sonar_measurements[index - 1] < depth:
            increases += 1
    return increases


if __name__ == "__main__":
    puzzle_input = [int(x) for x in puzzle_input]
    ##################
    # --- Part 1 --- #
    ##################

    print(count_increases(puzzle_input))

    ##################
    # --- Part 2 --- #
    ##################

    puzzle_input_window = []
    for index in range(len(puzzle_input)):
        # Guard clause to prevent cyclically wrapping of the list
        if index + 3 > len(puzzle_input):
            break
        puzzle_input_window.append(sum(puzzle_input[index : index + 3]))
    print(count_increases(puzzle_input_window))
