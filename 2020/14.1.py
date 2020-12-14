#!/usr/bin/env python3

from __init__ import *

memory = {}

for line in get_input_stream():
    line = line.strip()
    if line.startswith("mask"):
        mask_form = line.split()[2]
        antimask_0 = 0
        mask_1 = 0
        for char in mask_form:
            antimask_0 *= 2
            mask_1 *= 2
            if char in "X1":
                antimask_0 += 1
                if char == "1":
                    mask_1 += 1
    elif line.startswith("mem"):
        address = int(line.split("[")[1].split("]")[0])
        value = int(line.split()[2])
        value &= antimask_0
        value |= mask_1
        memory[address] = value
print(sum(memory.values()))
