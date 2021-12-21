#!/usr/bin/env python3

from math import sqrt, floor
from __init__ import *

ranges = {}

for ranges_input in get_input_stream().read().strip().split(":")[1].split(","):
    axis, ranges_range = ranges_input.split("=")
    ranges[axis[1]] = [int(n) for n in ranges_range.split("..")]

min_speed_for_distance = floor(sqrt(2 * ranges["x"][0])) - 1
achievable_with_initial_speeds = []
for x_initial_speed in range(min_speed_for_distance, ranges["x"][1] + 1):
    achievable_in_steps = []
    x_distance = 0
    x_speed = x_initial_speed
    while x_distance <= ranges["x"][1] and x_speed > 0:
        x_distance += x_speed
        x_speed -= 1
        if ranges["x"][0] <= x_distance <= ranges["x"][1]:
            achievable_in_steps.append(x_initial_speed - x_speed)
    if not achievable_in_steps:
        continue
    if x_initial_speed in achievable_in_steps:
        for x_speed in range(x_initial_speed + 1, 2 * (-ranges["y"][0]) + 1):
            achievable_in_steps.append(x_speed)
    for steps in achievable_in_steps:
        for y_initial_speed in range(ranges["y"][0], steps // 2):
            step = 0
            y_distance = 0
            y_speed = y_initial_speed
            while step < steps:
                y_distance += y_speed
                y_speed -= 1
                step += 1
                if y_distance < ranges["y"][0]:
                    break
            if ranges["y"][0] <= y_distance <= ranges["y"][1]:
                if (x_initial_speed, y_initial_speed) not in achievable_with_initial_speeds:
                    achievable_with_initial_speeds.append((x_initial_speed, y_initial_speed))

print(len(achievable_with_initial_speeds))
sys.exit(EXIT_SUCCESS)
