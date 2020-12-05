#!/usr/bin/env python3

import re

from __init__ import *

REQUIRED_PASSPORT_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
REGEX_FIELD_CONSTRAINTS = {
    'byr': "^(19[2-9][0-9]|200[0-2])$",
    'iyr': "^20(1[0-9]|20)$",
    'eyr': "^20(2[0-9]|30)$",
    'hgt': "^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$",
    'hcl': "^#[0-9a-f]{6}$",
    'ecl': "^(amb|blu|brn|gry|grn|hzl|oth)$",
    'pid': "^[0-9]{9}$",
}

passports = [{}]


def is_field_valid(field_type, field_value):
    if field_type in REGEX_FIELD_CONSTRAINTS:
        if not re.match(REGEX_FIELD_CONSTRAINTS[field_type], field_value):
            return False
    return True


def is_passport_valid(passport_data):
    for required_field_id in REQUIRED_PASSPORT_FIELDS:
        if required_field_id not in passport_data:
            return False
    for field_id in passport_data:
        if not is_field_valid(field_id, passport_data[field_id]):
            return False
    return True


for line in get_input_stream():
    line = line.rstrip()
    if not line:
        passports.append({})
        continue
    for read_field in line.split():
        read_field_id, read_field_value = read_field.split(":")
        passports[-1][read_field_id] = read_field_value

valid_passports_count = 0

for passport in passports:
    if is_passport_valid(passport):
        valid_passports_count += 1

print(valid_passports_count)
