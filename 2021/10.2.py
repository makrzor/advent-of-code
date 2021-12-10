#!/usr/bin/env python3

import re

from __init__ import *

VALUES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
CHUNKS = re.compile(r"\(\)|\[]|{}|<>")

line_points = []

for line in get_input_stream():
    while CHUNKS.search(line):
        line = CHUNKS.sub("", line)
    if re.search(r"[)\]}>]", line):
        continue
    line_points.append(0)
    for i in range(len(line) - 2, -1, -1):
        line_points[-1] *= 5
        line_points[-1] += VALUES[line[i]]

print(sorted(line_points)[(len(line_points) - 1) // 2])
