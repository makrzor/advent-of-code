#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

fuel_required = 0

for mass in input_file:
    fuel_required_for_mass = int(mass) // 3 - 2
    while fuel_required_for_mass > 0:
        fuel_required += fuel_required_for_mass
        fuel_required_for_mass = fuel_required_for_mass // 3 - 2

print(fuel_required)
