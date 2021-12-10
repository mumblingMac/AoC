#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/10
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


def autocomplete_scorer(completion_stack: list):
    character_points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    score = 0
    for element in completion_stack:
        score = (score * 5) + character_points[element]

    return score


def illegal_character_scorer(character: str):
    character_points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    return character_points[character]


def matching_character(character: str):
    character_matches = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    return character_matches[character]


if __name__ == "__main__":

    ##################
    # --- Part 1 --- #
    ##################

    illegal_characters = []
    for array in [list(x) for x in puzzle_input]:
        opening_stack = []
        for character in array:
            if character in ["(", "[", "{", "<"]:
                opening_stack.append(character)
            elif (
                character in [")", "]", "}", ">"]
                and matching_character(character) == opening_stack[-1]
            ):
                opening_stack.pop()
            else:
                illegal_characters.append(character)
                break
    print(sum([illegal_character_scorer(x) for x in illegal_characters]))

    ##################
    # --- Part 2 --- #
    ##################

    scores = []
    for array in [list(x) for x in puzzle_input]:
        opening_stack = []
        for character in array:
            if character in ["(", "[", "{", "<"]:
                opening_stack.append(character)
            elif (
                character in [")", "]", "}", ">"]
                and matching_character(character) == opening_stack[-1]
            ):
                opening_stack.pop()
            else:
                opening_stack = []
                break
        completion_stack = []
        while opening_stack:
            element = opening_stack.pop()
            completion_stack.append(matching_character(element))
        if completion_stack:
            scores.append(autocomplete_scorer(completion_stack))
    print(sorted(scores)[int(len(scores) / 2)])
