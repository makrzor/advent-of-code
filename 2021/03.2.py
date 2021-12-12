#!/usr/bin/env python3

from __init__ import *

report = []
gases = [[[]], [[]]]

number = 0
for line in get_input_stream():
    report.append([])
    for character in line.strip():
        report[-1].append(int(character))
    for i in range(len(gases)):
        gases[i][0].append(number)
    number += 1

for i in range(len(gases)):
    for position in range(len(report[0])):
        count = 0
        if len(gases[i][-1]) > 1:
            gases[i].append([])
            for number in gases[i][-2]:
                count += report[number][position]
            if count >= len(gases[i][-2]) / 2:
                selection = 1 - i
            else:
                selection = i
            for sample in gases[i][position]:
                if report[sample][position] == selection:
                    gases[i][position + 1].append(sample)

print(bin_digit_list_to_dec(report[gases[0][-1][0]]) * bin_digit_list_to_dec(report[gases[1][-1][0]]))
sys.exit(EXIT_SUCCESS)
