#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2021/day/3
"""

import pathlib
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
with open(input_file, "r") as data:
    puzzle_input = data.read().splitlines()


def count_bits(bit_position: int, diagnostic_codes: list):
    elements = [int(bit) for bit in list(list(zip(*diagnostic_codes))[bit_position])]
    on_bits = sum(elements)
    off_bits = abs(on_bits - len(elements))
    return on_bits, off_bits


if __name__ == "__main__":

    diagnostic_report = [list(x) for x in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################
    gamma_rate = []
    epsilon_rate = []

    for bit_position in range(len(diagnostic_report[0])):
        on_bits, off_bits = count_bits(bit_position, diagnostic_report)
        if on_bits > off_bits:
            gamma_rate.append("1")
            epsilon_rate.append("0")
        else:
            gamma_rate.append("0")
            epsilon_rate.append("1")

    print(int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2))

    ##################
    # --- Part 2 --- #
    ##################

    oxygen_generator_rating = diagnostic_report.copy()
    for bit_position in range(len(diagnostic_report[0])):
        if len(oxygen_generator_rating) == 1:
            break
        on_bits, off_bits = count_bits(bit_position, oxygen_generator_rating)
        if on_bits >= off_bits:
            bit_criteria = "1"
        else:
            bit_criteria = "0"
        oxygen_generator_rating = [
            x for x in oxygen_generator_rating if x[bit_position] == bit_criteria
        ]
    oxygen_generator_rating = oxygen_generator_rating.pop()

    co2_srubber_rating = diagnostic_report.copy()
    for bit_position in range(len(diagnostic_report[0])):
        if len(co2_srubber_rating) == 1:
            break
        on_bits, off_bits = count_bits(bit_position, co2_srubber_rating)
        if on_bits >= off_bits:
            bit_criteria = "0"
        else:
            bit_criteria = "1"
        co2_srubber_rating = [
            x for x in co2_srubber_rating if x[bit_position] == bit_criteria
        ]
    co2_srubber_rating = co2_srubber_rating.pop()

    print(
        int("".join(oxygen_generator_rating), 2)
        * int("".join(co2_srubber_rating), 2)
    )
