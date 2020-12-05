#!/usr/bin/env python3

from __init__ import *

SLOPES = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

area = []

for line in get_input_stream():
    area.append([])
    for character in line:
        if character == ".":
            area[-1].append(0)
        elif character == "#":
            area[-1].append(1)

row_length = len(area[0])
product = 1

for step, skip_rows in SLOPES:
    distance = 0
    trees_encountered = 0
    for row in range(0, len(area), skip_rows):
        trees_encountered += area[row][distance]
        distance += step
        if distance >= row_length:
            distance -= row_length
    product *= trees_encountered

print(product)
