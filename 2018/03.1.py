#!/usr/bin/env python

FABRIC_SIZE = 1000
input_file = open("03.txt", 'r')

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
