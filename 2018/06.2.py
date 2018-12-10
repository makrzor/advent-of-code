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
limit = 10000

point_id = 0
for line in input_file:
    coords = line.split(", ")
    points.append((point_id, int(coords[0]), int(coords[1])))
    point_id += 1
points_number = len(points)

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        for point in points:
            distance = abs(point[1] - i) + abs(point[2] - j)
            #print(i, j, point[0], distance)
            grid[i][j] += distance
        #break
locations_within_limit = 0
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] < limit:
            locations_within_limit += 1
        else:
            grid[i][j] = 0
#print(grid)
print(locations_within_limit)
