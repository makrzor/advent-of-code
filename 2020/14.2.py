#!/usr/bin/env python3

from __init__ import *

memory = {}

for line in get_input_stream():
    line = line.strip()
    if line.startswith("mask"):
        mask_form = line.split()[2]
        mask_length = len(mask_form)
        mask_1 = 0
        mask_float_bits = []
        for i in range(mask_length):
            mask_1 *= 2
            if mask_form[i] == "1":
                mask_1 += 1
            elif mask_form[i] == "X":
                mask_float_bits.append(mask_length - i - 1)
    elif line.startswith("mem"):
        base_address = int(line.split("[")[1].split("]")[0])
        value = int(line.split()[2])
        addresses = set([base_address | mask_1])
        for float_bit in mask_float_bits:
            mask = 1 << float_bit
            addresses_to_add = set()
            for address in addresses:
                address |= mask
                if address not in addresses:
                    addresses_to_add.add(address)
                else:
                    address &= ~mask
                    addresses_to_add.add(address)
            addresses.update(addresses_to_add)
        for address in addresses:
            memory[address] = value
print(sum(memory.values()))
