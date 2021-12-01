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


def count_depths(sonar_measurements: list) -> int:
    return sum(
        [d2 > d1 for d1, d2 in zip(sonar_measurements, sonar_measurements[1:])]
    )


if __name__ == "__main__":

    depths = [int(x) for x in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################
    print(count_depths(depths))

    ##################
    # --- Part 2 --- #
    ##################

    window_size = 3
    depths_window = [
        sum(depths[i : i + window_size]) for i in range(len(depths) - window_size + 1)
    ]
    print(count_depths(depths_window))
