#!/usr/bin/env python3

from functools import lru_cache

from __init__ import *

GENERATIONS = 80


@lru_cache(maxsize=None)
def check_number(local_counter: int, generations: int) -> int:
    if generations == 0:
        number = 1
    elif local_counter > 0:
        number = check_number(local_counter - 1, generations - 1)
    else:
        number = check_number(6, generations - 1) + check_number(8, generations - 1)
    return number


initial_numbers = {}

for counter in [int(x) for x in get_input_stream().readline().split(",")]:
    if counter not in initial_numbers:
        initial_numbers[counter] = 0
    initial_numbers[counter] += 1

total_count = 0

for counter in initial_numbers:
    total_count += check_number(counter, GENERATIONS) * initial_numbers[counter]

print(total_count)
sys.exit(EXIT_SUCCESS)
