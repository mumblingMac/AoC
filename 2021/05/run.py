#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/5
"""

import pathlib
import pprint
from collections import namedtuple

import numpy

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()

if __name__ == "__main__":

    Point = namedtuple("Point", "x, y")

    hydrothermal_vents = []
    for line in puzzle_input:
        p1, p2 = line.split(" -> ")
        hydrothermal_vents.append(
            [
                Point(*[int(x) for x in p1.split(",")]),
                Point(*[int(x) for x in p2.split(",")]),
            ]
        )

    ##################
    # --- Part 1 --- #
    ##################

    grid = numpy.zeros((1000, 1000))
    for segments in hydrothermal_vents:
        p1 = segments[0]
        p2 = segments[1]

        if p1.x == p2.x:
            for i in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                grid[i][p1.x] += 1
        elif p1.y == p2.y:
            for i in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                grid[p1.y][i] += 1

    print(len([x for row in grid for x in row if x > 1]))

    ##################
    # --- Part 2 --- #
    ##################
    for segments in hydrothermal_vents:
        p1 = segments[0]
        p2 = segments[1]

        if p1.x == p2.x:
            # NOTE: Handled in part 1
            pass
        elif p1.y == p2.y:
            # NOTE: Handled in part 1
            pass
        else:
            if p1.x > p2.x:
                x_step = -1
            else:
                x_step = 1

            if p1.y > p2.y:
                y_step = -1
            else:
                y_step = 1

            x = p1.x
            y = p1.y
            while x != p2.x:
                grid[y][x] += 1
                x += x_step
                y += y_step
            grid[y][x] += 1

    print(len([x for row in grid for x in row if x > 1]))
