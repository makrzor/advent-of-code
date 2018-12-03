#!/usr/bin/env python

input_file = open("01.txt", 'r')

frequency = 0

for frequency_change in input_file:
    frequency += int(frequency_change)

print(frequency)
