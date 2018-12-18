#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

diagram = []
terrains = {".": 1, "|": 2, "#": 3}

def gather_neighbour_info():
    for y in range(1, y_max):
        for x in range(1, x_max):
            diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
            for k in range(-1, 2):
                for j in range(-1, 2):
                    if j == 0 and k == 0:
                        continue
                    type = diagram[y + k][x + j][0]
                    diagram[y][x][type] += 1
    for x in range(1, x_max):
        y = 0
        diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
        for k in range(0, 2):
            for j in range(-1, 2):
                if j == 0 and k == 0:
                    continue
                type = diagram[y + k][x + j][0]
                diagram[y][x][type] += 1
        y = y_max
        diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
        for k in range(-1, 1):
            for j in range(-1, 2):
                if j == 0 and k == 0:
                    continue
                type = diagram[y + k][x + j][0]
                diagram[y][x][type] += 1
    for y in range(1, x_max):
        x = 0
        diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
        for k in range(-1, 2):
            for j in range(0, 2):
                if j == 0 and k == 0:
                    continue
                type = diagram[y + k][x + j][0]
                diagram[y][x][type] += 1
        x = x_max
        diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
        for k in range(-1, 2):
            for j in range(-1, 1):
                if j == 0 and k == 0:
                    continue
                type = diagram[y + k][x + j][0]
                diagram[y][x][type] += 1
    y = 0
    x = 0
    diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
    for k in range(0, 2):
        for j in range(0, 2):
            if j == 0 and k == 0:
                continue
            type = diagram[y + k][x + j][0]
            diagram[y][x][type] += 1
    y = y_max
    x = 0
    diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
    for k in range(-1, 1):
        for j in range(0, 2):
            if j == 0 and k == 0:
                continue
            type = diagram[y + k][x + j][0]
            diagram[y][x][type] += 1
    y = 0
    x = x_max
    diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
    for k in range(0, 2):
        for j in range(-1, 1):
            if j == 0 and k == 0:
                continue
            type = diagram[y + k][x + j][0]
            diagram[y][x][type] += 1
    y = y_max
    x = x_max
    diagram[y][x] = [diagram[y][x][0], 0, 0, 0]
    for k in range(-1, 1):
        for j in range(-1, 1):
            if j == 0 and k == 0:
                continue
            type = diagram[y + k][x + j][0]
            diagram[y][x][type] += 1

def change_fields():
    for y in range(0, y_max + 1):
        for x in range(0, x_max + 1):
            if diagram[y][x][0] == 1 and diagram[y][x][2] >= 3:
                diagram[y][x][0] = 2
            elif diagram[y][x][0] == 2 and diagram[y][x][3] >= 3:
                diagram[y][x][0] = 3
            elif diagram[y][x][0] == 3 and (diagram[y][x][3] == 0 or diagram[y][x][2] == 0):
                diagram[y][x][0] = 1

def count(type):
    nummber_of_type = 0
    for y in range(0, y_max + 1):
        for x in range(0, x_max + 1):
            if diagram[y][x][0] == type:
                nummber_of_type += 1
    return nummber_of_type

for line in input_file:
    diagram_row = []
    for x in range(len(line) - 1):
        char = line[x]
        diagram_row.append([terrains[char], -1, -1, -1])
    diagram.append(diagram_row)
y_max = len(diagram) - 1
x_max = len(diagram[0]) - 1

for i in range(10):
    gather_neighbour_info()
    change_fields()
print(count(2) * count(3))
