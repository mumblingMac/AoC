#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/13
"""

import pathlib
import pprint

import numpy

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


def count_dots(grid):
    return (grid == "#").sum()


def merge_rows(grid_one, grid_two):
    grid = []
    for r1, r2 in zip(grid_one, grid_two):
        row = ["#" if c1 == "#" or c2 == "#" else "." for c1, c2, in zip(r1, r2)]
        grid.append(row)
    return numpy.array(grid)


def fold_on_y(y, grid):
    top_grid = grid[:y]
    bottom_grid = grid[y + 1 :]
    return merge_rows(top_grid, bottom_grid[::-1])


def fold_on_x(x, grid):
    left_grid = [row[:x] for row in grid]
    right_grid = [row[x + 1 :] for row in grid]
    return merge_rows(left_grid, [row[::-1] for row in right_grid])


if __name__ == "__main__":

    dots, folds = "\n".join(puzzle_input).split("\n\n")

    x_values = [int(dot.split(",")[0]) for dot in dots.splitlines()]
    y_values = [int(dot.split(",")[1]) for dot in dots.splitlines()]

    ##################
    # --- Part 1 --- #
    ##################
    grid = numpy.full((max(y_values) + 1, max(x_values) + 1), ".")
    for x, y in zip(x_values, y_values):
        grid[y][x] = "#"

    for fold in folds.splitlines():
        instruction, location = fold.split("=")
        if "y" in instruction:
            grid = fold_on_y(int(location), grid)
        if "x" in instruction:
            grid = fold_on_x(int(location), grid)
        break
    print(count_dots(grid))

    ##################
    # --- Part 2 --- #
    ##################
    grid = numpy.full((max(y_values) + 1, max(x_values) + 1), ".")
    for x, y in zip(x_values, y_values):
        grid[y][x] = "#"

    for fold in folds.splitlines():
        instruction, location = fold.split("=")
        if "y" in instruction:
            grid = fold_on_y(int(location), grid)
        if "x" in instruction:
            grid = fold_on_x(int(location), grid)
    for row in grid:
        print("".join([x if x != "." else " " for x in row]))
