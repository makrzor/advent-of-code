#!/usr/bin/env python3

from __init__ import *

x = 0
y = 0
heading = 90

for line in get_input_stream():
    action = line[0]
    value = int(line[1:])
    if action == "F":
        if heading == 0: action = "N"
        elif heading == 90: action = "E"
        elif heading == 180: action = "S"
        elif heading == 270: action = "W"
    if action == "N": y += value
    elif action == "E": x += value
    elif action == "S": y -= value
    elif action == "W": x -= value
    else:
        if action == "R": heading += value
        elif action == "L": heading -= value
        heading %= 360
print(abs(x) + abs(y))
