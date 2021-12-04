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


def get_oxygen_generator_rating(diagnostic_codes: list, cribit_position: int = 0):
    if len(diagnostic_codes) == 1:
        return int("".join(diagnostic_codes.pop()), 2)
    if bit_position > len(diagnostic_codes[0]):
        raise IndexError("Bit position is out of range.")
    on_bits, off_bits = count_bits(bit_position, diagnostic_codes)
    if on_bits >= off_bits:
        bit_criteria = "1"
    else:
        bit_criteria = "0"
    return get_oxygen_generator_rating(
        [code for code in diagnostic_codes if code[bit_position] == bit_criteria],
        bit_position + 1,
    )


def get_co2_srubber_rating(diagnostic_codes: list, bit_position: int = 0):
    if len(diagnostic_codes) == 1:
        return int("".join(diagnostic_codes.pop()), 2)
    if bit_position > len(diagnostic_codes[0]):
        raise IndexError("Bit position is out of range.")
    on_bits, off_bits = count_bits(bit_position, diagnostic_codes)
    if on_bits >= off_bits:
        bit_criteria = "0"
    else:
        bit_criteria = "1"
    return get_co2_srubber_rating(
        [code for code in diagnostic_codes if code[bit_position] == bit_criteria],
        bit_position + 1,
    )


if __name__ == "__main__":

    diagnostic_report = [list(x) for x in puzzle_input]

    ##################
    # --- Part 1 --- #
    ##################
    gamma_rate = []
    for bit_position in range(len(diagnostic_report[0])):
        on_bits, off_bits = count_bits(bit_position, diagnostic_report)
        if on_bits > off_bits:
            gamma_rate.append("1")
        else:
            gamma_rate.append("0")
    epsilon_rate = ["1" if bit == "0" else "0" for bit in gamma_rate]
    print(int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2))

    ##################
    # --- Part 2 --- #
    ##################
    oxygen_generator_rating = get_oxygen_generator_rating(diagnostic_report.copy())
    co2_srubber_rating = get_co2_srubber_rating(diagnostic_report.copy())
    print(oxygen_generator_rating * co2_srubber_rating)
