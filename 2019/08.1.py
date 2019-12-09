#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

COLS = 25
ROWS = 6
if "test" in filename:
    COLS = 3
    ROWS = 2

zeroes = []
ones = []
twos = []

for line in input_file:
    digit = 0
    layer = 0
    x = 0
    y = 0
    count = [0] * 10
    while line[digit] != "\n":
        count[int(line[digit])] += 1
        digit += 1
        y += 1
        if y == COLS:
            y = 0
            x += 1
            if x == ROWS:
                x = 0
                layer += 1
                zeroes.append(count[0])
                ones.append(count[1])
                twos.append(count[2])
                count = [0] * 10

min_zeroes = 0
min_zeroes_count = COLS * ROWS
for i in range(len(zeroes)):
    if zeroes[i] < min_zeroes_count:
        min_zeroes_count = zeroes[i]
        min_zeroes = i

print(ones[min_zeroes] * twos[min_zeroes])
