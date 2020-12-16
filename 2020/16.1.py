#!/usr/bin/env python3

from __init__ import *

input_data = get_input_stream().read()
rules, _, nearby_tickets = input_data.split("\n\n")

valid_entries = {}

for rule in rules.split("\n"):
    for rule_part in rule.split(":")[1].split():
        if rule_part != "or":
            rule_min_value, rule_max_value = [int(x) for x in rule_part.split("-")]
            for i in range(rule_min_value, rule_max_value + 1):
                valid_entries[i] = 1

error_rate = 0

for field_entry in [int(x) for x in ",".join(nearby_tickets.split("\n")[1:-1]).split(",")]:
    if field_entry not in valid_entries:
        error_rate += field_entry
print(error_rate)
