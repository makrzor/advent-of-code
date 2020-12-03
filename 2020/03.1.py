#!/usr/bin/env python
import os
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = os.path.basename(sys.argv[0]).split(".")[0] + ".txt"
input_file = open(filename, 'r')

area = []

for line in input_file:
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
