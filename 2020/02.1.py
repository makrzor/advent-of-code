#!/usr/bin/env python3

from __init__ import *

valid_passwords_count = 0

for line in get_input_stream():
    limits, character, password = line.split(" ")
    character = character[0]
    lower_limit, upper_limit = limits.split("-")
    if int(lower_limit) <= password.count(character) <= int(upper_limit):
        valid_passwords_count += 1

print(valid_passwords_count)
