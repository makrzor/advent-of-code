#!/usr/bin/env python

input_file = open("20.txt", 'r')
position = []
velocity = []
acceleration = []

for line in input_file:
    (p, v, a) = line[:-1].split(', ')
    position.append([int(x) for x in p[3:-1].split(',')])
    velocity.append([int(x) for x in v[3:-1].split(',')])
    acceleration.append([int(x) for x in a[3:-1].split(',')])
input_file.close()
size = len(position)
distance = [-1] * size

while True:
    for i in range(size):
        distance[i] = 0
        for j in range(3):
            velocity[i][j] += acceleration[i][j]
            position[i][j] += velocity[i][j]
            distance[i] += abs(position[i][j])
    min_distance = min(distance)
    print '\r', distance.index(min_distance), min_distance,
