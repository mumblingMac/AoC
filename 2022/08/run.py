#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/8
"""

import pathlib
import pprint

import numpy

pp = pprint.PrettyPrinter(indent=4)


def up(x, y, grid):
    return grid[y - 1][x]


def down(x, y, grid):
    return grid[y + 1][x]


def left(x, y, grid):
    return grid[y][x - 1]


def right(x, y, grid):
    return grid[y][x + 1]


def edge(x, y, grid):
    if y == 0 or y == len(grid) - 1:
        return True
    if x == 0 or x == len(grid[y]) - 1:
        return True
    return False


def visible_from_north(x, y, grid):
    tree_x = x
    tree_y = y
    while edge(x, y, grid) is False:
        if grid[tree_y][tree_x] <= up(x, y, grid):
            return False
        y -= 1
    return True


def visible_from_south(x, y, grid):
    tree_x = x
    tree_y = y
    while edge(x, y, grid) is False:
        if grid[tree_y][tree_x] <= down(x, y, grid):
            return False
        y += 1
    return True


def visible_from_west(x, y, grid):
    tree_x = x
    tree_y = y
    while edge(x, y, grid) is False:
        if grid[tree_y][tree_x] <= left(x, y, grid):
            return False
        x -= 1
    return True


def visible_from_east(x, y, grid):
    tree_x = x
    tree_y = y
    while edge(x, y, grid) is False:
        if grid[tree_y][tree_x] <= right(x, y, grid):
            return False
        x += 1
    return True


def look_up(x, y, grid):
    return [grid[new_y][x] for new_y in range(y, -1, -1)]


def look_left(x, y, grid):
    return [grid[y][new_x] for new_x in range(x, -1, -1)]


def look_right(x, y, grid):
    return [grid[y][new_x] for new_x in range(x, len(grid[y]))]


def look_down(x, y, grid):
    return [grid[new_y][x] for new_y in range(y, len(grid))]


def viewable_distance(view: list):
    view.reverse()
    count = 0
    current_height = view.pop()
    while len(view) > 0:
        next_height = view.pop()
        if current_height > next_height:
            count += 1
        elif current_height <= next_height:
            count += 1
            break
        else:
            break
    return count


if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(input_file, "r") as data:
        puzzle_input = data.read().splitlines()

    grid = [list(x.strip()) for x in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################

    visible = numpy.full((len(grid), len(grid[-1])), ".")
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for direction in [visible_from_north, visible_from_south, visible_from_west, visible_from_east]:
                if direction(x, y, grid):
                    visible[y][x] = grid[y][x]
                    break
    print((visible != ".").sum())

    ##################
    # --- Part 2 --- #
    ##################

    scores = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            scores.append(
                viewable_distance(look_up(x, y, grid))
                * viewable_distance(look_down(x, y, grid))
                * viewable_distance(look_left(x, y, grid))
                * viewable_distance(look_right(x, y, grid))
            )
    scores.sort()
    print(scores[-1])
