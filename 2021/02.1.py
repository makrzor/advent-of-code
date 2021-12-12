#!/usr/bin/env python3

from __init__ import *

depth = 0
position = 0

for line in get_input_stream():
    direction, distance = line.split(" ")
    distance = int(distance)
    if direction == "forward":
        position += distance
    elif direction == "down":
        depth += distance
    elif direction == "up":
        depth -= distance

print(depth * position)
sys.exit(EXIT_SUCCESS)
