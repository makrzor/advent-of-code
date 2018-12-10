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
    seen = set()
    collisions = set()
    for i in range(size):
        if tuple(position[i]) in seen:
            collisions.add(tuple(position[i]))
        seen.add(tuple(position[i]))
    for p in [list(x) for x in collisions]:
        while p in position:
            i = position.index(p)
            position.pop(i)
            velocity.pop(i)
            acceleration.pop(i)
    if size != len(position):
        print
    size = len(position)
    for i in range(size):
        for j in range(3):
            velocity[i][j] += acceleration[i][j]
            position[i][j] += velocity[i][j]
            distance[i] += abs(position[i][j])
    print '\r', size,
