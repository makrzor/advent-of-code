#!/usr/bin/env python
import sys

INITIAL_BLOCK_COUNTS = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"

def find_highest(block_counts):
    value_max = 0
    position = -1
    for i in range(len(block_counts)):
        if block_counts[i] > value_max:
            value_max = block_counts[i]
            position = i
    return position

def redistribute(block_counts, position):
    size = len(block_counts)
    value = block_counts[position]
    block_counts[position] = 0
    for i in range(value):
        position += 1
        if position >= size:
            position = 0
        block_counts[position] += 1

cycles_count = 0
block_counts = [int(i) for i in INITIAL_BLOCK_COUNTS.split()]
while True:
    if cycles_count > 14029:
        print(block_counts)
    redistribute(block_counts, find_highest(block_counts))
    cycles_count += 1
    if cycles_count > 30000:
        sys.exit(0)
# now do | sort -u | wc -l to get the answer
