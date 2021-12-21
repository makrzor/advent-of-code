#!/usr/bin/env python3

from __init__ import *

STEPS = 50

enhancement_algorithm = []
image = [[] for _ in range(STEPS)]

for line in get_input_stream():
    if len(line) == 513:
        for bit in line.strip():
            if bit == ".":
                enhancement_algorithm.append(0)
            elif bit == "#":
                enhancement_algorithm.append(1)
    elif line != "\n":
        image.append([])
        line = "." * STEPS + line.strip() + "." * STEPS
        for pixel in line:
            if pixel == ".":
                image[-1].append([0, 0])
            elif pixel == "#":
                image[-1].append([1, 0])
width = len(image[-1])
image += [[] for _ in range(STEPS)]
for i in range(STEPS):
    image[i] = [[0, 0] for _ in range(width)]
    image[-1 - i] = [[0, 0] for _ in range(width)]
height = len(image)

for _ in range(STEPS):
    for y in range(height):
        for x in range(width):
            number = 0
            for scan_y in range(y - 1, y + 2):
                for scan_x in range(x - 1, x + 2):
                    number *= 2
                    if scan_x < 0:
                        shifted_x = 0
                    elif scan_x >= width:
                        shifted_x = width - 1
                    else:
                        shifted_x = scan_x
                    if scan_y < 0:
                        shifted_y = 0
                    elif scan_y >= height:
                        shifted_y = height - 1
                    else:
                        shifted_y = scan_y
                    number += image[shifted_y][shifted_x][0]
            image[y][x][1] = enhancement_algorithm[number]
    for y in range(height):
        for x in range(width):
            image[y][x][0] = image[y][x][1]

lit_count = 0
for y in range(height):
    for x in range(width):
        lit_count += image[y][x][0]
print(lit_count)
sys.exit(EXIT_SUCCESS)
