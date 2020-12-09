#!/usr/bin/env python3

from __init__ import *

PREAMBLE_DEFAULT_LENGTH = 25


def is_preamble_valid(index):
    for j in range (index - preamble_length, index - 1):
        for k in range(j + 1, index):
            if data[j] != data[k] and data[j] + data[k] == data[index]:
                return True
    return False

data = []

for line in get_input_stream():
    line = line.strip()
    data.append(int(line))

preamble_length = PREAMBLE_DEFAULT_LENGTH
if len(data) == 20:
    preamble_length = 5

for i in range(preamble_length, len(data)):
    if not is_preamble_valid(i):
        print(data[i])
        break
