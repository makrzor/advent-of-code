#!/usr/bin/env python
import sys
import copy
import math

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

positions = []
velocities = []
for line in input_file:
    line = line[line.index("<") + 1:line.index(">")]
    positions.append([])
    velocities.append([])
    for coord in line.split(","):
        positions[-1].append(int(coord.split("=")[1]))
        velocities[-1].append(0)

dimensions = len(positions[0])
bodies_count = len(positions)
pos = []
vel = []
for axis in range(dimensions):
    pos.append([])
    vel.append([])
    for body in range(bodies_count):
        pos[axis].append(positions[body][axis])
        vel[axis].append(velocities[body][axis])

pos_zero = copy.deepcopy(pos)
vel_zero = copy.deepcopy(vel)
steps = [0] * dimensions
for axis in range(dimensions):
    step = 0
    while True:
        for body1 in range(bodies_count):
            for body2 in range(body1 + 1, bodies_count):
                if pos[axis][body1] < pos[axis][body2]:
                    vel[axis][body1] += 1
                    vel[axis][body2] -= 1
                elif pos[axis][body1] > pos[axis][body2]:
                    vel[axis][body1] -= 1
                    vel[axis][body2] += 1
        for body in range(bodies_count):
            pos[axis][body] += vel[axis][body]
        step += 1
        if pos[axis] == pos_zero[axis] and vel[axis] == vel_zero[axis]:
            break
    steps[axis] = step

lcm = steps[0]
for i in range(1, dimensions):
    lcm = lcm * steps[i] // math.gcd(lcm, steps[i])
print(lcm)
