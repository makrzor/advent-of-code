#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

def str_to_bin(line):
    binary = []
    for i in range(len(line)):
        if line[i] == "#":
            binary.append(1)
        else:
            binary.append(0)
    return binary

def binary_count(binary_line, start):
    binary_number = 0
    for i in range(start, start + 5):
        binary_number <<= 1
        binary_number += binary_line[i]
    return binary_number

generation_change = [0] * 32
GENERATIONS = 20

line = input_file.readline()
pattern = str_to_bin(line[15:-1])
length = len(pattern)
pattern += [0] * GENERATIONS * 5
line = input_file.readline()

for line in input_file:
    (binary_line, arrow, child) = line.split()
    digit = binary_count(str_to_bin(binary_line), 0)
    if child == "#":
        generation_change[digit] = 1

for gen in range(1, GENERATIONS + 1):
    pattern_start = -2 * gen
    pattern_end = length + 2 * gen
    family = binary_count(pattern, pattern_start - 2)
    for i in range(pattern_start, pattern_end):
        pattern[i] = generation_change[family]
        family &= 15
        family <<= 1
        family += pattern[i + 3]
sum = 0
for i in range(pattern_start, pattern_end):
    sum += i * pattern[i]
print(sum)
