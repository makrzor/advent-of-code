#!/usr/bin/env python3

from __init__ import *

ARRANGEMETS_MAP = [0, 1, 1, 2, 4, 7]
last_3_diff = 0
arrangements = 1
adapters = sorted([int(line) for line in get_input_stream()])

adapters = [0] + adapters + [adapters[-1] + 3]
for i in range(1, len(adapters)):
    joltage_diff = adapters[i] - adapters[i - 1]
    if joltage_diff == 3:
        arrangements *= ARRANGEMETS_MAP[i - last_3_diff]
        last_3_diff = i

print(arrangements)
