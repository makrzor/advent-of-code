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
