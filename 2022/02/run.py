#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/2
"""

import pathlib
from enum import Enum


class MatchScore(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def choice(code: str):
    decoder = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS",
        "X": "ROCK",
        "Y": "PAPER",
        "Z": "SCISSORS",
    }
    return decoder[code]


def choose_shape(elf_code: str, outcome: str):
    decoder = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}
    shapes = ["A", "B", "C"]

    if decoder[outcome] == "LOSE":
        return choice(shapes[shapes.index(elf_code) - 1])

    if decoder[outcome] == "DRAW":
        return choice(elf_code)

    if decoder[outcome] == "WIN":
        return choice(shapes[(shapes.index(elf_code) + 1) % len(shapes)])


def score_match(elf_choice: str, human_choice: str):
    shapes = ["ROCK", "PAPER", "SCISSORS"]

    if elf_choice == human_choice:
        return MatchScore[human_choice].value + MatchScore.DRAW.value

    if elf_choice == shapes[shapes.index(human_choice) - 1]:
        return MatchScore[human_choice].value + MatchScore.WIN.value

    return MatchScore[human_choice].value + MatchScore.LOSE.value


if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(input_file, "r") as data:
        puzzle_input = data.read().splitlines()

    ##################
    # --- Part 1 --- #
    ##################
    matches = [shapes.split() for shapes in puzzle_input]
    print(sum(score_match(choice(elf_code), choice(human_code)) for (elf_code, human_code) in matches))

    ##################
    # --- Part 2 --- #
    ##################
    matches = [shapes.split() for shapes in puzzle_input]
    print(sum(score_match(choice(elf_code), choose_shape(elf_code, outcome)) for (elf_code, outcome) in matches))
