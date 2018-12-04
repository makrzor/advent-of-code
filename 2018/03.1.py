#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

FABRIC_SIZE = 1000

fabric = [[0 for col in range(FABRIC_SIZE)] for row in range(FABRIC_SIZE)]
overlaping = 0

for line in input_file:
    rectangle = line.split(" @ ")[1]
    (coords, dimensions) = rectangle.split(": ")
    (coord_x, coord_y) = coords.split(",")
    (dimension_x, dimension_y) = dimensions.split("x")
    for row in range(int(coord_y), int(coord_y) + int(dimension_y)):
        for col in range(int(coord_x), int(coord_x) + int(dimension_x)):
            fabric[col][row] += 1
            if fabric[col][row] == 2:
                overlaping += 1
print(overlaping)
