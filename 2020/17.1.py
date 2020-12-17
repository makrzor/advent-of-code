#!/usr/bin/env python3

from __init__ import *

GENERATIONS = 6

active_cubes = 0

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

    def add_neighbor(self, neighbor):
        if neighbor:
            neighbor.neighbors.append(self)
            self.neighbors.append(neighbor)

    def initialize_neighbors(self):
        for i in range (max(0, self.plane - 1), self.plane + 1):
            for j in range (max(0, self.row - 1), min(rows_number, self.row + 2)):
                for k in range(max(0, self.column - 1), min(columns_number, self.column + 2)):
                    if i == self.plane and j == self.row and k == self.column:
                        return
                    self.add_neighbor(grid[i][j][k])

    def notify_neighbors(self, value):
        for neighbor in self.neighbors:
            neighbor.active_neighbors += value

    def activate(self, change_state=0):
        if not change_state:
            change_state = self.change_state
        if change_state:
            self.active = change_state > 0
            self.notify_neighbors(change_state)
            global active_cubes
            active_cubes += change_state
            self.change_state = 0


def initialize_grid():
    for i in range(planes_number):
        for j in range(rows_number):
            for k in range(columns_number):
                cube = Cube(i, j, k)
                grid[i][j][k] = cube
                cubes_list.append(cube)


def generation_next():
    for cube in cubes_list:
        if not cube.active and cube.active_neighbors == 3:
            cube.change_state = 1
        elif cube.active and (cube.active_neighbors < 2 or cube.active_neighbors > 3):
            cube.change_state = -1
    for cube in cubes_list:
        cube.activate()


input_data = get_input_stream()
initial_size = len(input_data.read().split("\n")[0])
input_data.seek(0)
planes_number = 1 + 2 * GENERATIONS
rows_number = columns_number = initial_size + 2 * GENERATIONS
grid = [[[None] * columns_number for j in range(rows_number)] for i in range(planes_number)]
cubes_list = []
initialize_grid()
plane = row = GENERATIONS

for line in get_input_stream():
    line = line.strip()
    column = GENERATIONS
    for character in line:
        if character == "#":
            grid[plane][row][column].activate(1)
        column += 1
    row += 1

for i in range(GENERATIONS):
    generation_next()

print(active_cubes)
