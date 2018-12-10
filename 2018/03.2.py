#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

FABRIC_SIZE = 1000

fabric = [[0 for col in range(FABRIC_SIZE)] for row in range(FABRIC_SIZE)]
overlaping = [0]

for line in input_file:
    overlaping.append(0)
    (number, rectangle) = line.split(" @ ")
    number = int(number[1:])
    (coords, dimensions) = rectangle.split(": ")
    (coord_x, coord_y) = coords.split(",")
    (dimension_x, dimension_y) = dimensions.split("x")
    for row in range(int(coord_y), int(coord_y) + int(dimension_y)):
        for col in range(int(coord_x), int(coord_x) + int(dimension_x)):
            if fabric[col][row] != 0:
                overlaping[fabric[col][row]] = 1
                overlaping[number] = 1
            fabric[col][row] = number
for i in range(1, len(overlaping)):
    if overlaping[i] == 0:
        print(i)
