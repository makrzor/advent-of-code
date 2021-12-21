#!/usr/bin/env python3

from __init__ import *

SIMPLE_DIGIT_LENGTHS = [2, 3, 4, 7]

print(sum([len([digit for digit in line.split(" | ")[1].split() if len(digit) in SIMPLE_DIGIT_LENGTHS])
           for line in get_input_stream()]))
sys.exit(EXIT_SUCCESS)
