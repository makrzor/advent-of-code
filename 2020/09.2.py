#!/usr/bin/env python3

from __init__ import *

PREAMBLE_DEFAULT_LENGTH = 25


def is_preamble_valid(index):
    for j in range (index - preamble_length, index - 1):
        for k in range(j + 1, index):
            if data[j] != data[k] and data[j] + data[k] == data[index]:
                return True
    return False


data = [int(line) for line in get_input_stream()]
preamble_length = PREAMBLE_DEFAULT_LENGTH
if len(data) <= PREAMBLE_DEFAULT_LENGTH:
    preamble_length = 5

for i in range(preamble_length, len(data)):
    if not is_preamble_valid(i):
        invalid_number = data[i]
        break
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        contiguous_candidate = data[i:j + 1]
        contiguous_candidate_sum = sum(contiguous_candidate)
        if contiguous_candidate_sum > invalid_number:
            break
        if contiguous_candidate_sum == invalid_number:
            print(min(contiguous_candidate) + max(contiguous_candidate))
            sys.exit(0)
