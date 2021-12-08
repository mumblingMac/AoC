#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/8
"""

import pathlib
import pprint
from collections import namedtuple

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


def populate_decoder_ring(signals):
    unique_digit_decoder = {
        2: "1",
        3: "7",
        4: "4",
        7: "8",
    }

    decoder_ring = {}
    for signal in signals:
        if len(signal) in [2, 4, 3, 7]:
            decoder_ring[unique_digit_decoder[len(signal)]] = set((sorted(signal)))

    digit_top_left_and_middle = decoder_ring["4"] - decoder_ring["1"]

    for signal in signals:
        current_set = set(sorted(signal))
        if len(current_set) in [2, 4, 3, 7]:
            continue
        if len(current_set) == 5:
            # either 2, 3, or 5
            if decoder_ring["1"].issubset(current_set):
                decoder_ring["3"] = current_set
            elif digit_top_left_and_middle.issubset(current_set):
                decoder_ring["5"] = current_set
            else:
                decoder_ring["2"] = current_set
        if len(current_set) == 6:
            # either 0, 6, or 9
            if digit_top_left_and_middle.issubset(current_set) \
                and decoder_ring["1"].issubset(current_set):
                decoder_ring["9"] = current_set
            elif digit_top_left_and_middle.issubset(current_set):
                decoder_ring["6"] = current_set
            else:
                decoder_ring["0"] = current_set
    return {"".join(sorted(list(v))): k for k, v in decoder_ring.items()}


if __name__ == "__main__":

    Note = namedtuple("Note", "signal_pattern output_values")
    notes = [Note(*x.split("|")) for x in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################

    count = 0
    for digits in [x.output_values for x in notes]:
        count += sum(
            [1 for digit in digits.split() if len(digit.strip()) in [2, 4, 3, 7]]
        )
    print(count)

    ##################
    # --- Part 2 --- #
    ##################

    count = 0
    for note in notes:
        decoder_ring = populate_decoder_ring(note.signal_pattern.split())
        count += int(
            "".join(
                [decoder_ring["".join(sorted(x))] for x in note.output_values.split()]
            )
        )
    print(count)
