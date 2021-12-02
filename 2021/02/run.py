#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/2
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    @property
    def position(self):
        return self.horizontal * self.depth

    def down(self, count: int):
        self.depth += count

    def up(self, count: int):
        self.depth -= count

    def forward(self, count: int):
        self.horizontal += count


class Improved_Submarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def down(self, count: int):
        self.aim += count

    def up(self, count: int):
        self.aim -= count

    def forward(self, count: int):
        self.horizontal += count
        self.depth += self.aim * count


if __name__ == "__main__":

    commands = [i.split(" ") for i in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################
    submarine = Submarine()
    for command, count in commands:
        action = getattr(submarine, command)
        action(int(count))
    print(submarine.position)

    ##################
    # --- Part 2 --- #
    ##################
    submarine = Improved_Submarine()
    for command, count in commands:
        action = getattr(submarine, command)
        action(int(count))
    print(submarine.position)
