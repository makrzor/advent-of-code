#!/usr/bin/env python3

from copy import deepcopy

from __init__ import *


def put_in(turn_on: bool, new_set: list) -> int:
    global sets
    sets_checked = []
    new_cubes_x, new_start_x, new_stop_x, \
        _, new_start_y, new_stop_y, \
        _, new_start_z, new_stop_z = new_set
    cubes_turned = 0
    while sets:
        checked_set = sets.pop()
        checked_cubes_x, checked_start_x, checked_stop_x, \
            checked_cubes_y, checked_start_y, checked_stop_y, \
            checked_cubes_z, checked_start_z, checked_stop_z = checked_set
        if checked_start_x >= new_stop_x or checked_stop_x <= new_start_x \
                or checked_start_y >= new_stop_y or checked_stop_y <= new_start_y \
                or checked_start_z >= new_stop_z or checked_stop_z <= new_start_z:
            sets_checked.append(checked_set)
            continue
        if checked_start_x < new_start_x:
            diff_cubes_x = (new_start_x - checked_start_x) * checked_cubes_y
            sets_checked.append([diff_cubes_x, checked_start_x, new_start_x] + checked_set[3:])
            checked_cubes_x -= diff_cubes_x
            checked_start_x = new_start_x
        if checked_stop_x > new_stop_x:
            diff_cubes_x = (checked_stop_x - new_stop_x) * checked_cubes_y
            sets_checked.append([diff_cubes_x, new_stop_x, checked_stop_x] + checked_set[3:])
            checked_cubes_x -= diff_cubes_x
            checked_stop_x = new_stop_x
        if checked_start_y < new_start_y:
            diff_cubes_y = (new_start_y - checked_start_y) * checked_cubes_z
            diff_cubes_x = (checked_stop_x - checked_start_x) * diff_cubes_y
            sets_checked.append([diff_cubes_x, checked_start_x, checked_stop_x,
                                 diff_cubes_y, checked_start_y, new_start_y] + checked_set[6:])
            checked_cubes_x -= diff_cubes_x
            checked_start_y = new_start_y
        if checked_stop_y > new_stop_y:
            diff_cubes_y = (checked_stop_y - new_stop_y) * checked_cubes_z
            diff_cubes_x = (checked_stop_x - checked_start_x) * diff_cubes_y
            sets_checked.append([diff_cubes_x, checked_start_x, checked_stop_x,
                                 diff_cubes_y, new_stop_y, checked_stop_y] + checked_set[6:])
            checked_cubes_x -= diff_cubes_x
            checked_stop_y = new_stop_y
        if checked_start_z < new_start_z:
            diff_cubes_z = new_start_z - checked_start_z
            diff_cubes_y = (checked_stop_y - checked_start_y) * diff_cubes_z
            diff_cubes_x = (checked_stop_x - checked_start_x) * diff_cubes_y
            sets_checked.append([diff_cubes_x, checked_start_x, checked_stop_x,
                                 diff_cubes_y, checked_start_y, checked_stop_y,
                                 diff_cubes_z, checked_start_z, new_start_z])
            checked_cubes_x -= diff_cubes_x
        if checked_stop_z > new_stop_z:
            diff_cubes_z = checked_stop_z - new_stop_z
            diff_cubes_y = (checked_stop_y - checked_start_y) * diff_cubes_z
            diff_cubes_x = (checked_stop_x - checked_start_x) * diff_cubes_y
            sets_checked.append([diff_cubes_x, checked_start_x, checked_stop_x,
                                 diff_cubes_y, checked_start_y, checked_stop_y,
                                 diff_cubes_z, new_stop_z, checked_stop_z])
            checked_cubes_x -= diff_cubes_x
        cubes_turned -= checked_cubes_x
    if turn_on:
        sets_checked.append(new_set)
        cubes_turned += new_cubes_x
    sets = deepcopy(sets_checked)
    return cubes_turned


sets = []
cubes_on = 0

for line in get_input_stream():
    switch, ranges = line.strip().split()
    switch_on = True if switch == "on" else False
    (start_x, stop_x), (start_y, stop_y), (start_z, stop_z) = \
        [[int(a), int(b) + 1] for a, b in [dim_range.split("=")[1].split("..") for dim_range in ranges.split(",")]]
    cubes_z = stop_z - start_z
    cubes_y = (stop_y - start_y) * cubes_z
    cubes_x = (stop_x - start_x) * cubes_y
    cubes_on += put_in(switch_on, [cubes_x, start_x, stop_x,
                                   cubes_y, start_y, stop_y,
                                   cubes_z, start_z, stop_z])

print(cubes_on)
sys.exit(EXIT_SUCCESS)
