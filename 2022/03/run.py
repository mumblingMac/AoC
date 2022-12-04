#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/3
"""

import pathlib


def priority(letter: str):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(input_file, "r") as data:
        puzzle_input = data.read().splitlines()

    ##################
    # --- Part 1 --- #
    ##################

    print(
        sum(
            [
                priority((set(rucksack[: int(len(rucksack) / 2)]) & set(rucksack[int(len(rucksack) / 2) :])).pop())
                for rucksack in puzzle_input
            ]
        )
    )

    ##################
    # --- Part 2 --- #
    ##################

    print(
        sum(
            [
                priority((set(puzzle_input[i]) & set(puzzle_input[i + 1]) & set(puzzle_input[i + 2])).pop())
                for i in range(0, len(puzzle_input) - 3 + 1, 3)
            ]
        )
    )
