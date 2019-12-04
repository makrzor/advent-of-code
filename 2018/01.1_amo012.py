#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

frequency = 0

for frequency_change in input_file:
    frequency += int(frequency_change)

print(frequency)
