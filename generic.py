#!/usr/bin/env python3

import re

from __init__ import *

p1 = 0
p2 = 0
contents = {}

ints_1 = sorted([int(line) for line in get_input_stream()])

for line in get_input_stream():
    line = line.strip()
    words = line.split()
    ints = re.findall(r"-?\d+", line)
    print(line, words, ints)
print(p1)
print(p2)
