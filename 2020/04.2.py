#!/usr/bin/env python
import os
import re
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = os.path.basename(sys.argv[0]).split(".")[0] + ".txt"
input_file = open(filename, 'r')

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


def is_passport_valid(passport):
    for required_field in REQUIRED_PASSPORT_FIELDS:
        if required_field not in passport:
            return False
    for field in passport:
        if not is_field_valid(field, passport[field]):
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
