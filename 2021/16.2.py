#!/usr/bin/env python3

from __init__ import *


def get_packet_value() -> int:
    global pointer
    packet_value = 0
    pointer += 3
    packet_type = int(binary_code[pointer:pointer + 3], 2)
    pointer += 3
    if packet_type == 4:
        packet_value = 0
        continue_reading = True
        while continue_reading:
            if binary_code[pointer] == "0":
                continue_reading = False
            pointer += 1
            packet_value *= 16
            packet_value += int(binary_code[pointer:pointer + 4], 2)
            pointer += 4
    else:
        subpacket_values = []
        length_type = int(binary_code[pointer])
        pointer += 1
        if length_type == 0:
            length = int(binary_code[pointer:pointer + 15], 2)
            pointer += 15
            subpackets_stop = pointer + length
            while pointer < subpackets_stop:
                subpacket_values.append(get_packet_value())
        else:
            subpackets_count = int(binary_code[pointer:pointer + 11], 2)
            pointer += 11
            while subpackets_count > 0:
                subpacket_values.append(get_packet_value())
                subpackets_count -= 1
        if packet_type == 0:
            packet_value = sum(subpacket_values)
        elif packet_type == 1:
            packet_value = product(subpacket_values)
        elif packet_type == 2:
            packet_value = min(subpacket_values)
        elif packet_type == 3:
            packet_value = max(subpacket_values)
        elif packet_type == 5:
            if subpacket_values[0] > subpacket_values[1]:
                packet_value = 1
            else:
                packet_value = 0
        elif packet_type == 6:
            if subpacket_values[0] < subpacket_values[1]:
                packet_value = 1
            else:
                packet_value = 0
        elif packet_type == 7:
            if subpacket_values[0] == subpacket_values[1]:
                packet_value = 1
            else:
                packet_value = 0
    return packet_value


def product(factors: list) -> int:
    result = 1
    for n in factors:
        result *= n
    return result


binary_code = ""
pointer = 0

for hex_digit in get_input_stream().read().strip():
    binary_code += bin(int(hex_digit, 16))[2:].zfill(4)

print(get_packet_value())
sys.exit(EXIT_SUCCESS)
