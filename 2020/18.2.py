#!/usr/bin/env python3

import re

from __init__ import *


def calculate(operation, first_operand, second_operand):
    if operation == "+":
        return first_operand + second_operand
    else:
        return first_operand * second_operand


def simplify(data_list):
    if len(data_list) < 3:
        return data_list[0]
    if data_list[1] == "+":
        return simplify([calculate(data_list[1], int(data_list[0]), int(data_list[2]))] + data_list[3:])
    else:
        return calculate(data_list[1], int(data_list[0]), int(simplify(data_list[2:])))


total_sum = 0
for line in get_input_stream():
    line = line.strip()
    while "(" in line:
        line = re.sub(r"\([^()]+\)", lambda x: str(simplify(x.group()[1:-1].split())), line)
    total_sum += int(simplify(line.split()))
print(total_sum)
