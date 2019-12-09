#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

COLS = 25
ROWS = 6
if "test" in filename:
    COLS = 2
    ROWS = 2

layers = [[[]]]

for line in input_file:
    digit = 0
    layer = 0
    x = 0
    y = 0
    while line[digit] != "\n":
        # print(layers, layer, x, y, line[digit])
        layers[layer][x].append(int(line[digit]))
        digit += 1
        y += 1
        if y == COLS:
            y = 0
            x += 1
            if x == ROWS:
                x = 0
                layer += 1
                layers.append([])
            layers[layer].append([])

for x in range(ROWS):
    for y in range(COLS):
        printed = False
        for layer in range(len(layers)):
            if printed:
                continue
            elif layers[layer][x][y] == 0:
                print("#", end="")
                printed = True
            elif layers[layer][x][y] == 1:
                print(".", end="")
                printed = True
    print()
