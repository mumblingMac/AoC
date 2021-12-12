#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/12
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


def cave_map(puzzle_input):
    cave = {}
    for line in puzzle_input:
        key, value = line.split("-")
        if cave.get(key) is None:
            cave[key] = []
        if cave.get(value) is None:
            cave[value] = []
        cave[key].append(value)
        cave[value].append(key)
    return cave


def count_paths(cave, choice, visited):
    count = 0
    if choice == "end":
        return 1
    for value in cave[choice]:
        if value == value.upper():
            count += count_paths(cave, value, visited)
        elif value not in visited:
            visited.append(value)
            count += count_paths(cave, value, visited)
            visited.pop(visited.index(value))
    return count


def count_alternative_paths(cave, choice, visited, max_visits):
    count = 0
    if choice == "end":
        return 1
    for value in cave[choice]:
        if value == value.upper():
            count += count_alternative_paths(cave, value, visited, max_visits)
        elif visited.get(value, 0) == 0:
            visited[value] = visited.get(value, 0) + 1
            count += count_alternative_paths(cave, value, visited, max_visits)
            visited[value] = visited.get(value, 0) - 1
        elif (
            visited.get(value, 0) < max_visits
            and max_visits not in visited.values()
            and value != "start"
        ):
            visited[value] = visited.get(value, 0) + 1
            count += count_alternative_paths(cave, value, visited, max_visits)
            visited[value] = visited.get(value, 0) - 1
    return count


if __name__ == "__main__":

    ##################
    # --- Part 1 --- #
    ##################
    cave = cave_map(puzzle_input)
    print(count_paths(cave, "start", ["start"]))

    ##################
    # --- Part 2 --- #
    ##################
    print(count_alternative_paths(cave, "start", {"start": 1}, 2))
