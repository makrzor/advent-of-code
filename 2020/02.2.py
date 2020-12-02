#!/usr/bin/env python
import os
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = os.path.basename(sys.argv[0]).split(".")[0] + ".txt"
input_file = open(filename, 'r')

valid_passwords_count = 0

for line in input_file:
    positions, character, password = line.split(" ")
    character = character[0]
    matches_count = 0
    for position in positions.split("-"):
        if password[int(position) - 1] == character:
            matches_count += 1
    if matches_count == 1:
        valid_passwords_count += 1

print(valid_passwords_count)
