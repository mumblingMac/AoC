#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/9
"""

import pathlib
import pprint

import numpy

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


def out_of_bounds(x, y, grid):
    if y < 0 or y > len(grid) - 1:
        return True
    if x < 0 or x > len(grid[y]) - 1:
        return True
    return False


def up(x, y, grid):
    if out_of_bounds(x, y - 1, grid):
        return None
    else:
        return grid[y - 1][x]


def down(x, y, grid):
    if out_of_bounds(x, y + 1, grid):
        return None
    else:
        return grid[y + 1][x]


def left(x, y, grid):
    if out_of_bounds(x - 1, y, grid):
        return None
    else:
        return grid[y][x - 1]


def right(x, y, grid):
    if out_of_bounds(x + 1, y, grid):
        return None
    else:
        return grid[y][x + 1]


def neighbors(x, y, grid):
    return [direction(x, y, grid) for direction in (left, right, up, down)]


def is_lowpoint(left, right, up, down, center):
    neighbors = [x > center for x in [left, right, up, down] if x is not None]
    return sum(neighbors) == len(neighbors)


def in_basin(x, y, grid):
    if y < 0 or y > len(grid) - 1:
        return False
    if x < 0 or x > len(grid[y]) - 1:
        return False
    if grid[y][x] == "9":
        return False
    if grid[y][x] == "*":
        return False
    return True


def basin(x, y, grid):
    grid[y][x] = "*"

    if in_basin(x - 1, y, grid):
        basin(x - 1, y, grid)

    if in_basin(x + 1, y, grid):
        basin(x + 1, y, grid)

    if in_basin(x, y - 1, grid):
        basin(x, y - 1, grid)

    if in_basin(x, y + 1, grid):
        basin(x, y + 1, grid)

    return grid


if __name__ == "__main__":
    grid = [list(x) for x in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################
    risk_points = 0
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            center = grid[y][x]
            if is_lowpoint(*neighbors(x, y, grid), center):
                low_points.append((x, y))
                risk_points += int(center) + 1
    print(risk_points)

    ##################
    # --- Part 2 --- #
    ##################
    basin_size = sorted([
        sum([y.count("*") for y in basin(*point, [list(x) for x in puzzle_input])])
        for point in low_points
    ])
    print(numpy.prod(basin_size[-3:]))
