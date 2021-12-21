#!/usr/bin/env python3

from __init__ import *


def get_packet_version(adjust_pointer=True) -> int:
    global pointer
    # following check needed for test data
    if binary_code[pointer:].count("0") == code_length - pointer:
        pointer = code_length
        return 0
    local_versions_sum = int(binary_code[pointer:pointer + 3], 2)
    pointer += 3
    packet_type = int(binary_code[pointer:pointer + 3], 2)
    pointer += 3
    if packet_type == 4:
        continue_reading = True
        while continue_reading:
            if binary_code[pointer] == "0":
                continue_reading = False
            pointer += 5
    else:
        length_type = int(binary_code[pointer])
        pointer += 1
        if length_type == 0:
            length = int(binary_code[pointer:pointer + 15], 2)
            pointer += 15
            subpackets_stop = pointer + length
            while pointer < subpackets_stop:
                local_versions_sum += get_packet_version(adjust_pointer=False)
        else:
            subpackets_count = int(binary_code[pointer:pointer + 11], 2)
            pointer += 11
            while subpackets_count > 0:
                local_versions_sum += get_packet_version(adjust_pointer=False)
                subpackets_count -= 1
    if adjust_pointer:
        pointer += 3 - (pointer - 1) % 4
    return local_versions_sum


binary_code = ""
pointer = 0
versions_sum = 0

for hex_digit in get_input_stream().read().strip():
    binary_code += bin(int(hex_digit, 16))[2:].zfill(4)

code_length = len(binary_code)
while pointer < code_length:
    versions_sum += get_packet_version()

print(versions_sum)
sys.exit(EXIT_SUCCESS)
