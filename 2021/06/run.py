#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/6
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()

if __name__ == "__main__":

    inital_count = {}
    for i in [int(x) for x in "\n".join(puzzle_input).split(",")]:
        inital_count[i] = inital_count.get(i, 0) + 1

    ##################
    # --- Part 1 --- #
    ##################
    
    school = [
        inital_count.get(0, 0),
        inital_count.get(1, 0),
        inital_count.get(2, 0),
        inital_count.get(3, 0),
        inital_count.get(4, 0),
        inital_count.get(5, 0),
        inital_count.get(6, 0),
        inital_count.get(7, 0),
        inital_count.get(8, 0),
    ]

    for i in range(80):
        today_births = school.pop(0)
        # Handle adult Lanternfish
        school[6] += today_births
        # Handle new born Lanternfish
        school.append(today_births)

    print(sum(school))

    ##################
    # --- Part 2 --- #
    ##################

    for i in range(80,256):
        today_births = school.pop(0)
        # Handle adult Lanternfish
        school[6] += today_births
        # Handle new born Lanternfish
        school.append(today_births)
    print(sum(school))
