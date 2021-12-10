#!/usr/bin/env python3

import re

from __init__ import *

VALUES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
CHUNKS = re.compile(r"\(\)|\[]|{}|<>")

points = 0

for line in get_input_stream():
    while CHUNKS.search(line):
        line = CHUNKS.sub("", line)
    for i in range(len(line) - 1):
        if line[i] in "([{<":
            continue
        else:
            points += VALUES[line[i]]
            break

print(points)
