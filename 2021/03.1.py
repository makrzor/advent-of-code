#!/usr/bin/env python3

from statistics import mode

from __init__ import *

report = []

for line in get_input_stream():
    report.append(line.strip())

report_t = transpose(report)
gamma = ""
epsilon = ""

for position in range(len(report[0])):
    gamma += mode(report_t[position])
    epsilon += str(1 - int(gamma[-1]))

print(int(gamma, 2) * int(epsilon, 2))
