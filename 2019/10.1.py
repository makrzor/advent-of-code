#!/usr/bin/env python
import sys
import copy

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

asteroids = [[]]
x = 0
y = 0
asteroids_count = 0
for line in input_file:
    x = 0
    digit = 0
    while line[digit] != "\n":
        asteroids[y].append(1 if line[digit] == "#" else 0)
        asteroids_count += asteroids[y][x]
        digit += 1
        x += 1
    asteroids.append([])
    y += 1
cols = x
rows = y
dim_min = min(cols, rows)

common_divisors = [[copy.deepcopy([]) for x in range(cols)] for y in range(rows)]
for y in range(rows // 2 + 1):
    for x in range(cols // 2 + 1):
        if y == 0 and x == 0:
            continue
        for multiplier in range(2, dim_min // max(y, x) + 1):
            y_muled = multiplier * y
            x_muled = multiplier * x
            if y_muled < rows and x_muled < cols:
                common_divisors[y_muled][x_muled].append(multiplier)
common_divisors[0][0] = []

max_visible = 0
for y in range(rows):
    for x in range(cols):
        if asteroids[y][x] != 0:
            asteroids[y][x] = 0
            for dist_y in range(0 - y, rows - y):
                for dist_x in range(0 - x, cols - x):
                    if asteroids[y + dist_y][x + dist_x] != 0 and (dist_y != 0 or dist_x != 0):
                        eclipsed = False
                        for div in common_divisors[abs(dist_y)][abs(dist_x)]:
                            y_dived = dist_y // div
                            x_dived = dist_x // div
                            for i in range(1, div):
                                if asteroids[y + y_dived * i][x + x_dived * i] != 0:
                                    eclipsed = True
                        if not eclipsed:
                            asteroids[y][x] += 1
            if asteroids[y][x] > max_visible:
                max_visible = asteroids[y][x]

print(max_visible)
