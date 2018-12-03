#!/usr/bin/env python

FABRIC_SIZE = 1000
input_file = open("03.txt", 'r')

fabric = [[0 for col in range(FABRIC_SIZE)] for row in range(FABRIC_SIZE)]
overlaping = [0] * 1412

for line in input_file:
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
