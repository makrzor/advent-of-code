#!/usr/bin/env python3

from __init__ import *


def decode(data):
    output = 0
    for character in data:
        output *= 2
        if character in "BR":
            output += 1
    return output


max_seat_id = 0

for line in get_input_stream():
    line = line.strip()
    seat_id = decode(line)
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
