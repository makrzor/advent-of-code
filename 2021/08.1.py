#!/usr/bin/env python3

from __init__ import *

SIMPLE_DIGIT_LENGTHS = [2, 3, 4, 7]

digits_count = 0

for line in get_input_stream():
    digits_count += len([digit for digit in line.split(" | ")[1].split() if len(digit) in SIMPLE_DIGIT_LENGTHS])

print(digits_count)
sys.exit(EXIT_SUCCESS)
