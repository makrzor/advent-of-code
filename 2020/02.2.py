#!/usr/bin/env python3

from __init__ import *

valid_passwords_count = 0

for line in get_input_stream():
    positions, character, password = line.split(" ")
    character = character[0]
    matches_count = 0
    for position in positions.split("-"):
        if password[int(position) - 1] == character:
            matches_count += 1
    if matches_count == 1:
        valid_passwords_count += 1

print(valid_passwords_count)
