#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

DESIRED_SUM = 2020

expenses = []

for line in input_file:
    expenses.append(int(line))

for i in range(len(expenses)):
    for j in range(i + 1, len(expenses)):
        for k in range(j + 1, len(expenses)):
            if expenses[i] + expenses[j] + expenses[k] == DESIRED_SUM:
                print(expenses[i] * expenses[j] * expenses[k])
                sys.exit(0)

