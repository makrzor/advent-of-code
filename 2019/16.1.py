#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

PHASES_LIMIT = 100
OUTPUT_LENGTH = 8
BASE_PATTERN = [0, 1, 0, -1]
BASE_LEN = len(BASE_PATTERN)

signal = []
for digit in input_file.read()[:-1]:
    signal.append(int(digit))
signal_length = len(signal)

patterns_list = []
for pattern_number in range(signal_length):
    patterns_list.append([])
    i = 0
    while i <= signal_length:
        for pattern_digit in BASE_PATTERN:
            patterns_list[pattern_number] += (pattern_number + 1) * [pattern_digit]
            i += pattern_number + 1
    patterns_list[pattern_number] = patterns_list[pattern_number][1:signal_length + 1]

for phase in range(PHASES_LIMIT):
    results_list = [0] * signal_length
    for pattern_number in range(signal_length):
        for pattern_digit in range(signal_length):
            results_list[pattern_number] += patterns_list[pattern_number][pattern_digit] * signal[pattern_digit]
        results_list[pattern_number] = abs(results_list[pattern_number]) % 10
    for digit in range(signal_length):
        signal[digit] = results_list[digit]

for digit in range(OUTPUT_LENGTH):
    print(signal[digit], end="")
print()
