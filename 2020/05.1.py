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
    row = decode(line[:7])
    column = decode(line[7:-1])
    seat_id = row * 8 + column
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
