#!/usr/bin/env python3

from __init__ import *

depths = []
previous_sum = 0
current_sum = 0
larger_sums_count = 0

for line in get_input_stream():
    depths.append(int(line))

for i in range(len(depths)):
    current_sum += depths[i]
    if i >= 3:
        current_sum -= depths[i - 3]
        if current_sum > previous_sum:
            larger_sums_count += 1
    previous_sum = current_sum

print(larger_sums_count)
sys.exit(EXIT_SUCCESS)

