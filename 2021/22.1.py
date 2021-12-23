#!/usr/bin/env python3

from __init__ import *


def is_within_area(step_data: list) -> bool:
    for dim_range in step_data:
        if dim_range[0] < -50 or dim_range[1] > 51:
            return False
    return True


cube = {}
cubes_on = 0

for line in get_input_stream():
    turn, coords = line.strip().split()
    ranges = [[int(a), int(b) + 1] for a, b in [dim_range.split("=")[1].split("..") for dim_range in coords.split(",")]]
    if not is_within_area(ranges):
        continue
    for x in range(ranges[0][0], ranges[0][1]):
        if x not in cube:
            cube[x] = {}
        for y in range(ranges[1][0], ranges[1][1]):
            if y not in cube[x]:
                cube[x][y] = {}
            for z in range(ranges[2][0], ranges[2][1]):
                if z not in cube[x][y]:
                    cube[x][y][z] = False
                if turn == "on":
                    if not cube[x][y][z]:
                        cube[x][y][z] = True
                        cubes_on += 1
                elif cube[x][y][z]:
                    cube[x][y][z] = False
                    cubes_on -= 1

print(cubes_on)
sys.exit(EXIT_SUCCESS)
