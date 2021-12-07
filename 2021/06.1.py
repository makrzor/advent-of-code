#!/usr/bin/env python3

from __init__ import *

GENERATIONS = 80


def check_number(counter: int, generations: int) -> int:
    if generations not in cached_number:
        cached_number[generations] = {}
    if counter not in cached_number[generations]:
        if generations == 0:
            number = 1
        elif counter > 0:
            number = check_number(counter - 1, generations - 1)
        else:
            number = check_number(6, generations - 1) + check_number(8, generations - 1)
        cached_number[generations][counter] = number
    return cached_number[generations][counter]


cached_number = {}
initial_numbers = {}

for counter in [int(x) for x in get_input_stream().readline().split(",")]:
    if counter not in initial_numbers:
        initial_numbers[counter] = 0
    initial_numbers[counter] += 1

total_count = 0

for counter in initial_numbers:
    total_count += check_number(counter, GENERATIONS) * initial_numbers[counter]

print(total_count)
