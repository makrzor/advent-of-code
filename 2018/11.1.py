#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

def fill(x, y):
    rack_ID = x + 10
    power_level = rack_ID * y
    power_level += grid_serial_number
    power_level *= rack_ID
    power_level /= 100
    power_level %= 10
    power_level -= 5
    grid[x][y] = power_level

def power_of_3x3(x, y):
    square_power = 0
    for i in range(3):
        for j in range(3):
            square_power += grid[x + i][y + j]
    return square_power

SIZE = 301
grid = [[0 for row in range(SIZE)] for col in range(SIZE)]

grid_serial_number = int(input_file.read())

for x in range(1, SIZE):
    for y in range(1, SIZE):
        fill(x, y)
max_power = 0
for x in range(1, SIZE - 2):
    for y in range(1, SIZE - 2):
        square_power = power_of_3x3(x, y)
        if square_power > max_power:
            max_power = square_power
            max_x = x
            max_y = y
print(max_x, max_y, sep=",")
