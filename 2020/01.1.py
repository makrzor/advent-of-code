#!/usr/bin/env python3

from __init__ import *

DESIRED_SUM = 2020

expenses = []

for line in get_input_stream():
    expenses.append(int(line))

for i in range(len(expenses)):
    for j in range(i + 1, len(expenses)):
        if expenses[i] + expenses[j] == DESIRED_SUM:
            print(expenses[i] * expenses[j])
            sys.exit(EXIT_SUCCESS)
