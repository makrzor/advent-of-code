#!/usr/bin/env python3

from __init__ import *

height_map = {}
line_number = 0
height_map[line_number] = []

for line in get_input_stream():
    line_number += 1
    height_map[line_number] = []
    position = 1
    for height in line.strip():
        if height != "9":
            height_map[line_number].append(position)
        position += 1
height_map[line_number + 1] = []

top_three = [0, 0, 0]
top_three_min = 0
hot_points = []
for row in height_map:
    while height_map[row]:
        hot_points.append((row, height_map[row][0]))
        basin_area = 0
        while hot_points:
            y, x = hot_points.pop()
            height_map[y].remove(x)
            basin_area += 1
            for check_y, check_x in [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]:
                if check_x in height_map[check_y] and (check_y, check_x) not in hot_points:
                    hot_points.append((check_y, check_x))
        if basin_area > top_three_min:
            top_three.remove(top_three_min)
            top_three.append(basin_area)
            top_three_min = min(top_three)

print(top_three[0] * top_three[1] * top_three[2])
