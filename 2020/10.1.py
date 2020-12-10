#!/usr/bin/env python3

from __init__ import *

ones = 0
threes = 0
adapters = sorted([int(line) for line in get_input_stream()])

adapters = [0] + adapters + [adapters[-1] + 3]
for i in range(1, len(adapters)):
    joltage_diff = adapters[i] - adapters[i - 1]
    if joltage_diff == 1:
        ones += 1
    elif joltage_diff == 3:
        threes += 1

print(ones * threes)
