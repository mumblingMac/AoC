#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/2
"""

import pathlib
import pprint

import numpy

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


class Submarine:
    def __init__(self, use_aim: bool = False):
        if use_aim:
            self.__aim = 0
        else:
            self.__aim = None

        self.__horizontal = 0
        self.__depth = 0

    @property
    def horizontal(self):
        return self.__horizontal

    @property
    def depth(self):
        return self.__depth

    @property
    def position(self):
        return self.horizontal, self.depth

    def down(self, moves: int):
        if self.__aim is not None:
            self.__aim += moves
        else:
            self.__depth += moves

    def up(self, moves: int):
        if self.__aim is not None:
            self.__aim -= moves
        else:
            self.__depth -= moves

    def forward(self, moves: int):
        if self.__aim is not None:
            self.__horizontal += moves
            self.__depth += self.__aim * moves
        else:
            self.__horizontal += moves


if __name__ == "__main__":

    commands = [i.split(" ") for i in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################
    submarine = Submarine()
    for command, count in commands:
        action = getattr(submarine, command)
        action(int(count))
    print(numpy.prod(submarine.position))

    ##################
    # --- Part 2 --- #
    ##################
    submarine = Submarine(use_aim=True)
    for command, count in commands:
        action = getattr(submarine, command)
        action(int(count))
    print(numpy.prod(submarine.position))
