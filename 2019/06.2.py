#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

input_data = {}
path = {"COM": ["COM"]}
me = "YOU"
santa = "SAN"


def calculate_path(orbiting: str):
    if orbiting not in path.keys():
        calculate_path(input_data[orbiting])
        path[orbiting] = [orbiting] + path[input_data[orbiting]]


for line in input_file:
    (orbited, orbiting) = line.strip().split(")")
    input_data[orbiting] = orbited

calculate_path(me)
calculate_path(santa)

for i in range(len(path[me])):
    if path[me][-1] == path[santa][-1]:
        path[me] = path[me][:-1]
        path[santa] = path[santa][:-1]

print(len(path[me]) + len(path[santa]) - 2)
