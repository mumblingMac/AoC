#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/6
"""

import itertools
import pathlib


def sliding_window(datastream: str, n=4):
    iterables = itertools.tee(datastream, n)

    for iterable, num_skipped in zip(iterables, itertools.count()):
        for x in range(num_skipped):
            next(iterable, None)

    return zip(*iterables)


def unique_string(candidate: str):
    return len(set(candidate)) == len(candidate)


if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(input_file, "r") as data:
        puzzle_input = data.read()

    ##################
    # --- Part 1 --- #
    ##################
    packet_length = 4
    for index, packet in enumerate(sliding_window(puzzle_input, packet_length)):
        if unique_string(packet):
            print(index + packet_length)
            break

    ##################
    # --- Part 2 --- #
    ##################
    message_length = 14
    for index, message in enumerate(sliding_window(puzzle_input, message_length)):
        if unique_string(message):
            print(index + message_length)
            break
