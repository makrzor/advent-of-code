#!/usr/bin/env python3

from __init__ import *


def point_append(risk: int) -> None:
    point = {"risk": risk}
    for d in DIRECTIONS:
        point[d] = MAX
    cavern_map[-1].append(point)


MAX = 65535
DIRECTIONS = ["e", "s"]
cavern_map = [[]]

for line in get_input_stream():
    cavern_map.append([{}])
    for n in line.strip():
        point_append(int(n))
    cavern_map[-1].append({})
cavern_map.append([])
height = len(cavern_map) - 2
width = len(cavern_map[1]) - 2
cavern_map[height][width]["e"] = 0
cavern_map[height][width]["s"] = 0
for i in range(width + 1):
    cavern_map[0].append({})
    cavern_map[-1].append({})

for row in range(height, 0, -1):
    for column in range(width, 0, -1):
        me = cavern_map[row][column]
        e_neighbour = cavern_map[row][column + 1]
        s_neighbour = cavern_map[row + 1][column]
        if e_neighbour:
            me["e"] = e_neighbour["risk"] + min(e_neighbour[direction] for direction in DIRECTIONS)
        if s_neighbour:
            me["s"] = s_neighbour["risk"] + min(s_neighbour[direction] for direction in DIRECTIONS)

print(min(cavern_map[1][1][direction] for direction in DIRECTIONS))
sys.exit(EXIT_SUCCESS)
