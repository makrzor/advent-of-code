#!/usr/bin/env python3

from __init__ import *

STEPS = 30000000

memory = {}
number = 0

starting_numbers = [int(x) for x in get_input_stream().read().split(",")]
for turn in range(len(starting_numbers)):
    memory[starting_numbers[turn]] = turn + 1
for turn in range(len(memory) + 1, STEPS):
    next_number = turn - memory[number] if number in memory else 0
    memory[number] = turn
    number = next_number
print(number)
