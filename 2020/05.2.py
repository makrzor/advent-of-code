#!/usr/bin/env python3

from __init__ import *


def decode(data):
    output = 0
    for character in data:
        output *= 2
        if character in "BR":
            output += 1
    return output


used_seat_ids = []

for line in get_input_stream():
    line = line.strip()
    seat_id = decode(line)
    used_seat_ids.append(seat_id)

for seat_id in range(max(used_seat_ids), 0, -1):
    if seat_id not in used_seat_ids:
        print(seat_id)
        sys.exit(EXIT_SUCCESS)
