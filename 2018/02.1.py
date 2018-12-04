#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

containing_twos = 0
containing_threes = 0

for box in input_file:
    letters = [0] * 123
    twos = []
    threes = []

    for i in range(len(box)):
        letter = box[i]
        appearances = letters[ord(letter)] + 1
        letters[ord(letter)] = appearances
        if appearances == 2:
            twos.append(letter)
        elif appearances == 3:
            twos.remove(letter)
            threes.append(letter)
        elif appearances == 4:
            threes.remove(letter)
    if len(twos) > 0:
        containing_twos += 1
    if len(threes) > 0:
        containing_threes += 1
print(containing_twos * containing_threes)
