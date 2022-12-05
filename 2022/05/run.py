#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code - https://adventofcode.com/
Problem : https://adventofcode.com/2022/day/5
"""

import pathlib
import re
from collections import defaultdict, namedtuple


class ContainerShip:
    def __init__(self, cargo: str):
        def emptyList():
            return []

        self.cargo = defaultdict(emptyList)

        for line in cargo.splitlines():
            column = 1
            for index in range(0, len(line), 4):
                element = line[index : index + 4]
                if "[" in element:
                    element = element.strip().replace("[", "").replace("]", "")
                    self.cargo[column].append(element)
                column += 1

        for value in self.cargo.values():
            value.reverse()

    def move_container(self, from_col: int, to_col: int, quantity: int = 1):
        crane = []
        for x in range(0, quantity):
            crane.append(self.cargo[from_col].pop())
        crane.reverse()
        self.cargo[to_col].extend(crane)

    def available_containers(self):
        containers = []
        for key in sorted(self.cargo.keys()):
            containers.append(self.cargo[key][-1])
        return "".join(containers)


Instruction = namedtuple("Instruction", ["quantity", "from_col", "to_col"])

if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(input_file, "r") as data:
        puzzle_input = data.read().split("\n\n")

    instructions = [
        Instruction(*([int(x) for x in re.findall(r"\d+", instruction)]))
        for instruction in puzzle_input[1].splitlines()
    ]

    ##################
    # --- Part 1 --- #
    ##################
    container_ship = ContainerShip(puzzle_input[0])

    for instruction in instructions:
        for x in range(0, instruction.quantity):
            container_ship.move_container(instruction.from_col, instruction.to_col)
    print(container_ship.available_containers())

    ##################
    # --- Part 2 --- #
    ##################
    container_ship = ContainerShip(puzzle_input[0])

    for instruction in instructions:
        container_ship.move_container(instruction.from_col, instruction.to_col, instruction.quantity)
    print(container_ship.available_containers())
