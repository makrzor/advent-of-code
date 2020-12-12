#!/usr/bin/env python3

from __init__ import *

ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1

for line in get_input_stream():
    action = line[0]
    value = int(line[1:])
    if action == "N": waypoint_y += value
    elif action == "E": waypoint_x += value
    elif action == "S": waypoint_y -= value
    elif action == "W": waypoint_x -= value
    elif action == "F":
        ship_x += value * waypoint_x
        ship_y += value * waypoint_y
    else:
        old_waypoint_x = waypoint_x
        old_waypoint_y = waypoint_y
        if action == "L": value = 0 - value
        value %= 360
        if value in [90, 180]: old_waypoint_x = 0 - old_waypoint_x
        if value in [180, 270]: old_waypoint_y = 0 - old_waypoint_y
        if value % 180 == 0:
            waypoint_x = old_waypoint_x
            waypoint_y = old_waypoint_y
        elif value % 180 == 90:
            waypoint_x = old_waypoint_y
            waypoint_y = old_waypoint_x
print(abs(ship_x) + abs(ship_y))
