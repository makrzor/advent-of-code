#!/usr/bin/env python3

from __init__ import *

PREAMBLE_DEFAULT_LENGTH = 25


def is_preamble_valid(index):
    for j in range (index - preamble_length, index - 1):
        for k in range(j + 1, index):
            if data[j] != data[k] and data[j] + data[k] == data[index]:
                return True
    return False


def get_contiguous_extremes_sum(index, jndex):
    sum = 0
    min_value = max_number
    max_value = 0
    for k in range(index, jndex + 1):
        sum += data[k]
        if sum > invalid_number:
            return 0
        if data[k] < min_value:
            min_value = data[k]
        elif data[k] > max_value:
            max_value = data[k]
    if sum == invalid_number:
        return min_value + max_value
    else:
        return 0


data = []

for line in get_input_stream():
    line = line.strip()
    data.append(int(line))

max_number = max(data)

preamble_length = PREAMBLE_DEFAULT_LENGTH
if len(data) == 20:
    preamble_length = 5

for i in range(preamble_length, len(data)):
    if not is_preamble_valid(i):
        invalid_number = data[i]
        break
for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        sum = get_contiguous_extremes_sum(i, j)
        if sum:
            print(sum)
            sys.exit(0)
