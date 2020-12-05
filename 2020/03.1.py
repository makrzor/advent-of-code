#!/usr/bin/env python3

from __init__ import *

area = []

for line in get_input_stream():
    area.append([])
    for character in line:
        if character == ".":
            area[-1].append(0)
        elif character == "#":
            area[-1].append(1)

distance = 0
row_length = len(area[0])
trees_encountered = 0

for row in range(len(area)):
    trees_encountered += area[row][distance]
    distance += 3
    if distance >= row_length:
        distance -= row_length

print(trees_encountered)
