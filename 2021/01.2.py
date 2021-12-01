#!/usr/bin/env python3

from __init__ import *

depths = []
larger_sums_count = 0

for line in get_input_stream():
    depths.append(int(line))

for i in range(3, len(depths)):
    if depths[i] > depths[i - 3]:
        larger_sums_count += 1

print(larger_sums_count)
sys.exit(EXIT_SUCCESS)

