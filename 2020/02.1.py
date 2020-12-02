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
    limits, character, password = line.split(" ")
    character = character[0]
    lower_limit, upper_limit = limits.split("-")
    if int(lower_limit) <= password.count(character) <= int(upper_limit):
        valid_passwords_count += 1

print(valid_passwords_count)
