#!/usr/bin/env python3

from __init__ import *

class Chair:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.occupied = False
        self.change_state = 0
        self.occupied_neighbours = 0
        self.neighbours = []

    def add_neighbour(self, row, column):
        place = ferry_places[row][column]
        if place:
            place.neighbours.append(self)
            self.neighbours.append(place)

    def notify_neighbours(self, value):
        for neighbour in self.neighbours:
            neighbour.occupied_neighbours += value


def round_run(occupied):
    changes = 0
    for i in range(rows_number):
        for j in range(columns_number):
            place = ferry_places[i][j]
            if place:
                if not place.occupied and not place.occupied_neighbours:
                    place.change_state = 1
                    changes += 1
                elif place.occupied and place.occupied_neighbours >= 4:
                    place.change_state = -1
                    changes += 1
    for i in range(rows_number):
        for j in range(columns_number):
            place = ferry_places[i][j]
            if place:
                if place.change_state == 1:
                    place.occupied = True
                    place.notify_neighbours(1)
                    occupied += 1
                elif place.change_state == -1:
                    place.occupied = False
                    place.notify_neighbours(-1)
                    occupied -= 1
                place.change_state = 0
    return occupied, changes


ferry_places = []

for line in get_input_stream():
    line = line.strip()
    row = len(ferry_places)
    ferry_places.append([])
    for character in line:
        column = len(ferry_places[row])
        if character == "L":
            chair = Chair(row, column)
            ferry_places[row].append(chair)
            if row > 0:
                if column > 0:
                    chair.add_neighbour(row - 1, column - 1)
                chair.add_neighbour(row - 1, column)
                if column < len(ferry_places[row - 1]) - 1:
                    chair.add_neighbour(row - 1, column + 1)
            if column > 0:
                chair.add_neighbour(row, column - 1)
        else:
            ferry_places[-1].append(None)

rows_number = len(ferry_places)
columns_number = len(ferry_places[0])

occupied = 0
changed = -1
while changed:
    occupied, changed = round_run(occupied)

print(occupied)
