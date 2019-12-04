#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')


def check(x, y, current_line):
    value_spotted = grid[x][y]
    if value_spotted == -1 or value_spotted == current_line:
        return
    elif value_spotted != 0:
        global distance_min
        manhattan_distance = abs(x) + abs(y)
        if manhattan_distance < distance_min:
            distance_min = manhattan_distance
    grid[x][y] = current_line


GRID_SIZE = 50000
grid = [[0 for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]

distance_min = GRID_SIZE
line_number = 0
for line in input_file:
    line_number += 1
    x = 0
    y = 0
    grid[x][y] = -1
    for move in line.split(","):
        direction = move[0]
        distance = int(move[1:])
        if direction == "R" or direction == "L":
            horizontal = True
        else:
            horizontal = False
        if direction == "R" or direction == "U":
            step = 1
        else:
            step = -1
        while distance > 0:
            distance -= 1
            if horizontal:
                x += step
            else:
                y += step
            check(x, y, line_number)

print(distance_min)
