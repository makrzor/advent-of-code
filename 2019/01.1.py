#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

fuel_required = 0

for mass in input_file:
    fuel_required += int(mass) // 3 - 2

print(fuel_required)
