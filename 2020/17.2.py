#!/usr/bin/env python3

from __init__ import *

GENERATIONS = 6

class Cube:

    def __init__(self, hyperplane, plane, row, column):
        self.hyperplane = hyperplane
        self.plane = plane
        self.row = row
        self.column = column
        self.active = False
        self.change_state = 0
        self.active_neighbors = 0
        self.neighbors = []
        self.initialize_neighbors()

    def initialize_neighbors(self):
        for i in range (max(- GENERATIONS, self.hyperplane - 1), self.hyperplane + 1):
            for j in range (max(- GENERATIONS, self.plane - 1), min(planes_number - GENERATIONS, self.plane + 2)):
                for k in range (max(- GENERATIONS, self.row - 1), min(rows_number - GENERATIONS, self.row + 2)):
                    for l in range(max(- GENERATIONS, self.column - 1), min(columns_number - GENERATIONS, self.column + 2)):
                        if i == self.hyperplane and j == self.plane and k == self.row and l == self.column:
                            return
                        self.add_neighbor(i, j, k, l)

    def add_neighbor(self, hyperplane, plane, row, column):
        cube = grid[hyperplane][plane][row][column]
        cube.neighbors.append(self)
        self.neighbors.append(cube)

    def notify_neighbors(self, value):
        for neighbor in self.neighbors:
            neighbor.active_neighbors += value


def initialize_grid():
    for i in range(- GENERATIONS, hyperplanes_number - GENERATIONS):
        for j in range(- GENERATIONS, planes_number - GENERATIONS):
            for k in range(- GENERATIONS, rows_number - GENERATIONS):
                for l in range(- GENERATIONS, columns_number - GENERATIONS):
                    grid[i][j][k][l] = Cube(i, j, k, l)


def generation_next(active):
    for i in range(hyperplanes_number):
        for j in range(planes_number):
            for k in range(rows_number):
                for l in range(columns_number):
                    cube = grid[i][j][k][l]
                    if not cube.active and cube.active_neighbors == 3:
                        cube.change_state = 1
                    elif cube.active and (cube.active_neighbors < 2 or cube.active_neighbors > 3):
                        cube.change_state = -1
    for i in range(hyperplanes_number):
        for j in range(planes_number):
            for k in range(rows_number):
                for l in range(columns_number):
                    cube = grid[i][j][k][l]
                    if cube.change_state == 1:
                        cube.active = True
                        cube.notify_neighbors(1)
                        active += 1
                    elif cube.change_state == -1:
                        cube.active = False
                        cube.notify_neighbors(-1)
                        active -= 1
                    cube.change_state = 0
    return active


input_data = get_input_stream()
initial_size = len(input_data.read().split("\n")[0])
input_data.seek(0)
hyperplanes_number = 1 + 2 * GENERATIONS
planes_number = 1 + 2 * GENERATIONS
rows_number = initial_size + 2 * GENERATIONS
columns_number = initial_size + 2 * GENERATIONS
grid = [[[[None] * columns_number for k in range(rows_number)] for j in range(planes_number)] for i in range(hyperplanes_number)]
initialize_grid()
hyperplane = 0
plane = 0
row = 0

active = 0
for line in get_input_stream():
    line = line.strip()
    column = 0
    for character in line:
        if character == "#":
            cube = grid[hyperplane][plane][row][column]
            cube.active = True
            cube.notify_neighbors(1)
            active += 1
        column += 1
    row += 1

for i in range(GENERATIONS):
    active = generation_next(active)

print(active)
