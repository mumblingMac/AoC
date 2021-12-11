#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/11
"""

import pathlib
import pprint

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


def synchronized(grid):
    synchronize_value = grid[0][0]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != synchronize_value:
                return False
    return True


def increase_octopus_energy(x: int, y: int, grid):
    for point in [
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1),
    ]:
        if not out_of_bounds(point[0], point[1], grid):
            if type(grid[point[1]][point[0]]) is int:
                grid[point[1]][point[0]] += 1
    return grid


def increase_all_energy(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1
    return grid


def process_flashes(grid):
    flash = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if type(grid[y][x]) is int and grid[y][x] > 9:
                grid[y][x] = "*"
                return process_flashes(increase_octopus_energy(x, y, grid)) + 1
    return flash


def reset_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if type(grid[y][x]) is not int:
                grid[y][x] = 0
    return grid


if __name__ == "__main__":

    ##################
    # --- Part 1 --- #
    ##################
    grid = []
    for line in puzzle_input:
        grid.append([int(octopus) for octopus in list(line)])

    flashes = 0
    for i in range(100):
        increase_all_energy(grid)
        flashes += process_flashes(grid)
        reset_grid(grid)
    print(flashes)

    ##################
    # --- Part 2 --- #
    ##################
    grid = []
    for line in puzzle_input:
        grid.append([int(octopus) for octopus in list(line)])

    steps = 0
    while not synchronized(grid):
        increase_all_energy(grid)
        process_flashes(grid)
        reset_grid(grid)
        steps += 1
    print(steps)
