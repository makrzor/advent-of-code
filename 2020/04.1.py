#!/usr/bin/env python
import os
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = os.path.basename(sys.argv[0]).split(".")[0] + ".txt"
input_file = open(filename, 'r')

REQUIRED_PASSPORT_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = [{}]

def is_passport_valid(passport):
    for field in REQUIRED_PASSPORT_FIELDS:
        if field not in passport:
            return False
    return True

for line in input_file:
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
