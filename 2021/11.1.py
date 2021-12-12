#!/usr/bin/env python3

from __init__ import *


def flash(flash_y: int, flash_x: int) -> None:
    global flashes
    flashes += 1
    for y in range(flash_y - 1, flash_y + 2):
        for x in range(flash_x - 1, flash_x + 2):
            if octopi_map[y][x] != -1:
                octopus_increase(y, x)


def octopus_increase(y: int, x: int) -> None:
    octopi_map[y][x] += 1
    if octopi_map[y][x] == 10:
        flash(y, x)


octopi_map = [[]]

for line in get_input_stream():
    octopi_map.append([-1])
    for n in line.strip():
        octopi_map[-1].append(int(n))
    octopi_map[-1].append(-1)
octopi_map.append([])
height = len(octopi_map) - 1
width = len(octopi_map[1]) - 1
for i in range(width + 1):
    octopi_map[0].append(-1)
    octopi_map[-1].append(-1)

flashes = 0

for step in range(100):
    for row in range(1, height):
        for column in range(1, width):
            octopus_increase(row, column)

    for row in range(1, height):
        for column in range(1, width):
            if octopi_map[row][column] > 9:
                octopi_map[row][column] = 0

print(flashes)
sys.exit(EXIT_SUCCESS)
