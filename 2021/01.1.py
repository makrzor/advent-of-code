#!/usr/bin/env python3

from __init__ import *

previous_depth = 10000
larger_depths_count = 0

for line in get_input_stream():
    if int(line) > previous_depth:
        larger_depths_count += 1
    previous_depth = int(line)

print(larger_depths_count)
sys.exit(EXIT_SUCCESS)

