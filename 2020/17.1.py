#!/usr/bin/env python3

from __init__ import *

GENERATIONS = 6

class Cube:

    def __init__(self, plane, row, column):
        self.plane = plane
        self.row = row
        self.column = column
        self.active = False
        self.change_state = 0
        self.active_neighbors = 0
        self.neighbors = []
        self.initialize_neighbors()

    def initialize_neighbors(self):
        for i in range (max(- GENERATIONS, self.plane - 1), self.plane + 1):
            for j in range (max(- GENERATIONS, self.row - 1), min(rows_number - GENERATIONS, self.row + 2)):
                for k in range(max(- GENERATIONS, self.column - 1), min(columns_number - GENERATIONS, self.column + 2)):
                    if i == self.plane and j == self.row and k == self.column:
                        return
                    self.add_neighbor(i, j, k)

    def add_neighbor(self, plane, row, column):
        cube = grid[plane][row][column]
        cube.neighbors.append(self)
        self.neighbors.append(cube)

    def notify_neighbors(self, value):
        for neighbor in self.neighbors:
            neighbor.active_neighbors += value


def initialize_grid():
    for i in range(- GENERATIONS, planes_number - GENERATIONS):
        for j in range(- GENERATIONS, rows_number - GENERATIONS):
            for k in range(- GENERATIONS, columns_number - GENERATIONS):
                grid[i][j][k] = Cube(i, j, k)


def generation_next(active):
    for i in range(planes_number):
        for j in range(rows_number):
            for k in range(columns_number):
                cube = grid[i][j][k]
                if not cube.active and cube.active_neighbors == 3:
                    cube.change_state = 1
                elif cube.active and (cube.active_neighbors < 2 or cube.active_neighbors > 3):
                    cube.change_state = -1
    for i in range(planes_number):
        for j in range(rows_number):
            for k in range(columns_number):
                cube = grid[i][j][k]
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
planes_number = 1 + 2 * GENERATIONS
rows_number = initial_size + 2 * GENERATIONS
columns_number = initial_size + 2 * GENERATIONS
grid = [[[None] * columns_number for j in range(rows_number)] for i in range(planes_number)]
initialize_grid()
plane = 0
row = 0

active = 0
for line in get_input_stream():
    line = line.strip()
    column = 0
    for character in line:
        if character == "#":
            cube = grid[plane][row][column]
            cube.active = True
            cube.notify_neighbors(1)
            active += 1
        column += 1
    row += 1

for i in range(GENERATIONS):
    active = generation_next(active)

print(active)
