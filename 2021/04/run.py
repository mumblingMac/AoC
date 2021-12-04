#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/4
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


class YellBingo(Exception):
    pass


class BingoCard():
    def __init__(self, card):
        self.card = card

        self.rows = [row.split() for row in card.split("\n")]
        self.cols = []
        for col in range(len(self.rows[0])):
            self.cols.append([number for number in list(list(zip(*self.rows))[col])])

    def mark(self, number: int):
        for index, row in enumerate(self.rows):
            self.rows[index] = ["*" if x == str(number) else x for x in row]
        for index, col in enumerate(self.cols):
            self.cols[index] = ["*" if x == str(number) else x for x in col]

    def has_bingo(self):
        for row in self.rows:
            if "".join(row).replace("*", "") == "":
                return True
        for col in self.cols:
            if "".join(col).replace("*", "") == "":
                return True
        return False

    def unmark_numbers(self):
        return [int(item) for row in self.rows for item in row if item != "*"]


if __name__ == "__main__":

    bingo_caller = [int(x) for x in puzzle_input.pop(0).split(",")]

    ##################
    # --- Part 1 --- #
    ##################
    bingo_cards = [BingoCard(x.strip()) for x in "\n".join(puzzle_input).split("\n\n")]
    try:
        for number in bingo_caller:
            for card in bingo_cards:
                card.mark(number)
                if card.has_bingo():
                    raise YellBingo(sum(card.unmark_numbers() * number))
    except YellBingo as e:
        print(e)

    ##################
    # --- Part 2 --- #
    ##################
    try:
        for number in bingo_caller:
            bingo_cards = [card for card in bingo_cards if not card.has_bingo()]
            for index, card in enumerate(bingo_cards):
                card.mark(number)
                if card.has_bingo():
                    if len(bingo_cards) == 1:
                        raise YellBingo(sum(card.unmark_numbers() * number))
    except YellBingo as e:
        print(e)
