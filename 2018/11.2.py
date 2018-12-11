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

def max_power_of_squares(x, y):
    square_power = grid[x][y]
    max_power = square_power
    power_size = 1
    for size in range(2, SIZE - max(x, y) + 1):
        for i in range(size):
            square_power += grid[x + size - 1][y + i] + grid[x + i][y + size - 1]
        square_power -= grid[x + size - 1][y + size - 1]
        if square_power > max_power:
            max_power = square_power
            power_size = size
    return (max_power, power_size)

SIZE = 301
grid = [[0 for row in range(SIZE)] for col in range(SIZE)]

grid_serial_number = int(input_file.read())

for x in range(1, SIZE):
    for y in range(1, SIZE):
        fill(x, y)
max_power = 0
max_x = 0
max_y = 0
max_power_size = 0
for x in range(1, SIZE):
    for y in range(1, SIZE):
        (square_power, power_size) = max_power_of_squares(x, y)
        if square_power > max_power:
            max_power = square_power
            max_x = x
            max_y = y
            max_power_size = power_size
print(max_x, max_y, max_power_size, sep=",")
