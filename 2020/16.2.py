#!/usr/bin/env python3

from __init__ import *

SEARCHED_NAMES_PREFIX = "departure"
input_data = get_input_stream().read()
rules, my_ticket, nearby_tickets = input_data.split("\n\n")

valid_entries = {}
ticket_fields = {}

for rule in rules.split("\n"):
    field_name, field_rules_set = rule.split(":")
    field_rules = [[int(x) for x in rule.split("-")] for rule in [field_rules_set.split()[i] for i in [0, 2]]]
    ticket_fields[field_name] = field_rules
    for rule_min_value, rule_max_value in field_rules:
        for i in range(rule_min_value, rule_max_value + 1):
            valid_entries[i] = 1

tickets = set(nearby_tickets.split("\n")[1:-1])
valid_tickets = []
for ticket in tickets:
    ticket_entries = [int(x) for x in ticket.split(",")]
    for entry in ticket_entries:
        if entry not in valid_entries:
            break
    else:
        valid_tickets.append(ticket_entries)

my_ticket_entries = [int(x) for x in my_ticket.split("\n")[1].split(",")]
field_names = ["" for name in range(len(my_ticket_entries))]
names_to_find = sum([1 for name in ticket_fields if name.startswith(SEARCHED_NAMES_PREFIX)])
product = 1
while names_to_find:
    for i in range(len(field_names)):
        if field_names[i]:
            continue
        names_matching = []
        for name in ticket_fields:
            if name in field_names:
                continue
            field_rules = ticket_fields[name]
            for j in range(len(valid_tickets)):
                entry = valid_tickets[j][i]
                if entry < field_rules[0][0] or field_rules[0][1] < entry < field_rules[1][0] or field_rules[1][1] < entry:
                    break
            else:
                names_matching.append(name)
        if len(names_matching) == 1:
            field_names[i] = names_matching[0]
            if names_matching[0].startswith(SEARCHED_NAMES_PREFIX):
                product *= my_ticket_entries[i]
                names_to_find -= 1
            break
print(product)
