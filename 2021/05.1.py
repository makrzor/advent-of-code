#!/usr/bin/env python3

from __init__ import *


def mark_vent(x: int, y: int):
    if x not in vents_map:
        vents_map[x] = {}
    if y not in vents_map[x]:
        vents_map[x][y] = 0
    vents_map[x][y] += 1


vents_map = {}

for line in get_input_stream():
    line_split = line.split()
    coords = "{},{}".format(line_split[0], line_split[2])
    (x1, y1, x2, y2) = [int(x) for x in coords.split(",")]
    if x1 == x2:
        y_step = 1 if y2 > y1 else -1
        for y in range(y1, y2 + y_step, y_step):
            mark_vent(x1, y)
    elif y1 == y2:
        x_step = 1 if x2 > x1 else -1
        for x in range(x1, x2 + x_step, x_step):
            mark_vent(x, y1)

overlapping_lines_count = 0

for row in vents_map.values():
    for vent in row.values():
        if vent > 1:
            overlapping_lines_count += 1

print(overlapping_lines_count)
sys.exit(EXIT_SUCCESS)
