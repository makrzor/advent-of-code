#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

LETTER_CODES = range(65, 91)
min_length = 50000

line_original = input_file.read()[:-1]
for letter_code in LETTER_CODES:
    line = line_original
    line_length = len(line)
    i = 0
    while i < line_length - 1:
        if ord(line[i]) == letter_code or ord(line[i]) == letter_code + 32:
            line = line[:i] + line[i + 1:]
            line_length -=1
            i -= 1
        if abs(ord(line[i]) - ord(line[i + 1])) == 32:
            line = line[:i] + line[i + 2:]
            line_length -=2
            if i > 0:
                i -= 2
            else:
                i = -1
        i += 1
    if ord(line[i]) == letter_code or ord(line[i]) == letter_code + 32:
        line_length -=1
    if line_length < min_length:
        min_length = line_length
print(min_length)
