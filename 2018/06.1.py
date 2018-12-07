#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

GRID_SIZE=400
grid = [[0 for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
points = []

point_id = 0
for line in input_file:
    coords = line.split(", ")
    points.append((point_id, int(coords[0]), int(coords[1])))
    point_id += 1
points_number = len(points)
locations_closest = [0] * points_number

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        min_distance = 2 * GRID_SIZE
        for point in points:
            distance = abs(point[1] - i) + abs(point[2] - j)
            if distance < min_distance:
#                print(i, j, distance, min_distance, point[0])
                grid[i][j] = point[0]
                min_distance = distance
            elif distance == min_distance:
                grid[i][j] = -1
#print(grid)
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] > 0:
            locations_closest[grid[i][j]] += 1
for i in range(GRID_SIZE):
    locations_closest[grid[i][0]] = 0
    locations_closest[grid[i][GRID_SIZE - 1]] = 0
    locations_closest[grid[0][i]] = 0
    locations_closest[grid[GRID_SIZE - 1][i]] = 0
print(max(locations_closest))
