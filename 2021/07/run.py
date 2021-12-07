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
    fuel_spent = 0
    for crab in crab_alignment:
        fuel_spent += abs(crab - desired_aligment)
    print(fuel_spent)

    ##################
    # --- Part 2 --- #
    ##################
    desired_aligment = [ int(sum(crab_alignment) / len(crab_alignment)), int(round(sum(crab_alignment) / len(crab_alignment), 0)) ]

    cheapest_fuel = sum(range(max(crab_alignment)+1))*len(crab_alignment)
    for aligment in desired_aligment:
        fuel_spent = 0
        for crab in crab_alignment:
            fuel_spent += sum(range(abs(crab - aligment) + 1))
        if fuel_spent < cheapest_fuel:
            cheapest_fuel = fuel_spent
    print(f"{cheapest_fuel}")