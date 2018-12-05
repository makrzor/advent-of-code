#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

line = input_file.read()[:-1]
line_length = len(line)
i = 0
while i < line_length - 1:
    if abs(ord(line[i]) - ord(line[i + 1])) == 32:
        line = line[:i] + line[i + 2:]
        line_length -=2
        if i > 0:
            i -= 2
        else:
            i = -1
    i += 1
print(line_length)
