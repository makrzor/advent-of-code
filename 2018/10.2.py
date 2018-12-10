#!/usr/bin/env python
from __future__ import print_function
import sys
import curses
import time

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

position = []
velocity = []

for line in input_file:
    (p, v) = line[:-2].split("> ")
    position.append([int(x) for x in p[10:].split(", ")])
    velocity.append([int(x) for x in v[10:].split(", ")])
input_file.close()
size = len(position)
second = 0
dimensions = 499999
dimensions_prev = 500000

while dimensions < dimensions_prev:
    second += 1
    (first_column, top_line) = (last_column, bottom_line) = position[0]
    for i in range(size):
        for j in range(2):
            position[i][j] += velocity[i][j]
        (x, y) = position[i]
        if x < first_column:
            first_column = x
        if x > last_column:
            last_column = x
        if y < top_line:
            top_line = y
        if y > bottom_line:
            bottom_line = y
    dimensions_prev = dimensions
    dimensions = last_column - first_column + bottom_line - top_line
print(second - 1)
