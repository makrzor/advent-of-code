#!/usr/bin/env python3

from __init__ import *


def is_local_low() -> bool:
    height = height_map[i][j]
    if height_map[i - 1][j] > height \
            and height_map[i][j - 1] > height \
            and height_map[i][j + 1] > height \
            and height_map[i + 1][j] > height:
        return True
    else:
        return False


height_map = [[]]

for line in get_input_stream():
    height_map.append([9])
    for x in line.strip():
        height_map[-1].append(int(x))
    height_map[-1].append(9)
height_map.append([])
for i in range(len(height_map[1])):
    height_map[0].append(9)
    height_map[-1].append(9)

total_risk_level = 0

for i in range(1, len(height_map) - 1):
    for j in range(1, len(height_map[1]) - 1):
        if is_local_low():
            total_risk_level += height_map[i][j] + 1

print(total_risk_level)
