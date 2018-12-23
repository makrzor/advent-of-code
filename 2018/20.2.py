#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

map = input_file.readline()[:-1]
#print(map)

MIN_DOORS = 1000
char = map[0]
parentheses_open = []
i = 1
x = 0
y = 0
distance = 0
distances = {(x, y): 0}

while char != "$":
    char = map[i]
    if char == "(":
        parentheses_open.append([i + 1, x, y])
    elif char == ")":
        chains = []
        (chain_start, x, y) = parentheses_open[-1]
	distance = distances[(x, y)]
        zero_detected = False
        for j in range(chain_start, i + 1):
            if map[j] == "|" or map[j] == ")":
                chains.append(map[chain_start:j])
                if chain_start == j:
                    zero_detected = True
                chain_start = j + 1
        chain_to_be_appended = ""
        max_chain_length = 0
        if not zero_detected:
            for chain in range(len(chains)):
                if len(chains[chain]) > max_chain_length:
                    max_chain_length = len(chains[chain])
                    max_chain = chain
            chain_to_be_appended = chains[max_chain]
        map = map[:parentheses_open[-1][0]] + chain_to_be_appended + map[i + 1:]
        i = parentheses_open.pop()[0] - 1 + max_chain_length
    elif char == "|":
        (chain_start, x, y) = parentheses_open[-1]
	distance = distances[(x, y)]
    elif char in "NESW":
        if char == "N":
	    y -= 1
        elif char == "E":
	    x += 1
        elif char == "S":
            y += 1
        elif char == "W":
            x -= 1
        if (x, y) in distances.keys():
            distance = min(distances[(x, y)], distance + 1)
	else:
	    distance += 1
        distances[(x, y)] = distance
#        print(map)
    i += 1
far_rooms = 0
for distance in distances.values():
    if distance >= MIN_DOORS:
        far_rooms += 1
print(far_rooms)
