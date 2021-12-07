#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/7
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()

if __name__ == "__main__":

    crab_alignment = [int(x) for x in "\n".join(puzzle_input).split(",")]

    ##################
    # --- Part 1 --- #
    ##################
    desired_aligment = sorted(crab_alignment)[int(len(crab_alignment) / 2)]
    fuel_spent = sum([abs(crab - desired_aligment) for crab in crab_alignment])
    print(fuel_spent)

    ##################
    # --- Part 2 --- #
    ##################
    average = int(sum(crab_alignment) / len(crab_alignment))
    desired_aligment = list(range(average - 1, average + 2))
    fuel_spent = [
        sum([sum(range(abs(crab - aligment) + 1)) for crab in crab_alignment])
        for aligment in desired_aligment
    ]
    print(min(fuel_spent))
