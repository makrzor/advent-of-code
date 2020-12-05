#!/usr/bin/env python3

import re

from __init__ import *

REQUIRED_PASSPORT_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
NUMBER_FIELDS_CONSTRAINTS = {
    'byr': [4, 1920, 2002],
    'iyr': [4, 2010, 2020],
    'eyr': [4, 2020, 2030],
}
MIXED_FIELDS_CONSTRAINTS = {
    'hgt': {
        'cm': [150, 193],
        'in': [59, 76],
    },
}
REGEX_FIELD_CONSTRAINTS = {
    'hcl': "^#[0-9a-f]{6}$",
    'ecl': "^(amb|blu|brn|gry|grn|hzl|oth)$",
    'pid': "^[0-9]{9}$",
}

passports = [{}]


def is_field_valid(field_type, field_value):
    if field_type in NUMBER_FIELDS_CONSTRAINTS:
        constraint_list = NUMBER_FIELDS_CONSTRAINTS[field_type]
        if not re.match("^\\d{{{}}}$".format(constraint_list[0]), field_value):
            return False
        if not constraint_list[1] <= int(field_value) <= constraint_list[2]:
            return False
    elif field_type in MIXED_FIELDS_CONSTRAINTS:
        constraint_dict = MIXED_FIELDS_CONSTRAINTS[field_type]
        measure = field_value[-2:]
        value = field_value[:-2]
        if measure not in constraint_dict:
            return False
        constraint_list = constraint_dict[measure]
        if not constraint_list[0] <= int(value) <= constraint_list[1]:
            return False
    elif field_type in REGEX_FIELD_CONSTRAINTS:
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
