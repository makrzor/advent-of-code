#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

input_data = {}
distance = {"COM": 0}


def calculate_distance(orbiting: str) -> int:
    if orbiting in distance.keys():
        orbiting_distance = distance[orbiting]
    else:
        orbiting_distance = calculate_distance(input_data[orbiting]) + 1
    return orbiting_distance


for line in input_file:
    (orbited, orbiting) = line.strip().split(")")
    input_data[orbiting] = orbited

distances_total = 0
for orbiting in input_data.keys():
    distances_total += calculate_distance(orbiting)

print(distances_total)
