#!/usr/bin/env python3

import re

from __init__ import *

REQUIRED_PASSPORT_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = [{}]

def is_passport_valid(passport):
    for field in REQUIRED_PASSPORT_FIELDS:
        if field not in passport:
            return False
    return True

for line in get_input_stream():
    line = line.rstrip()
    if not line:
        passports.append({})
        continue
    for field in line.split():
        field_id, field_value = field.split(":")
        passports[-1][field_id] = field_value

valid_passports_count = 0

for passport in passports:
    if is_passport_valid(passport):
        valid_passports_count += 1

print(valid_passports_count)
