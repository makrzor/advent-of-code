#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

STEPS = 1000
if "test.01" in filename:
    steps = 10
elif "test.02" in filename:
    steps = 100
else:
    steps = STEPS

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
for step in range(steps):
    for body1 in range(len(positions)):
        for body2 in range(body1 + 1, len(positions)):
            for axis in range(dimensions):
                if positions[body1][axis] < positions[body2][axis]:
                    velocities[body1][axis] += 1
                    velocities[body2][axis] -= 1
                elif positions[body1][axis] > positions[body2][axis]:
                    velocities[body1][axis] -= 1
                    velocities[body2][axis] += 1
    for body in range(len(positions)):
        for axis in range(dimensions):
            positions[body][axis] += velocities[body][axis]

energy = 0
for body in range(len(positions)):
    pot = 0
    kin = 0
    for axis in range(dimensions):
        pot += abs(positions[body][axis])
        kin += abs(velocities[body][axis])
    energy += pot * kin

print(energy)
