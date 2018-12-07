#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

temp = 0
previous = ""

for line in input_file:
    temp += 1
    preceeding = line[5]
    succeeding = line[36]
    if preceeding != previous:
        print("", order)
    for i in range(len(order)):
        if order[i] == preceeding:
            for j in range(len(order)):
                if order[j] == succeeding and j < i:
                    order = order[:j] + order[j + 1:i + 1] + order[j:]
                    break
            print(temp, order)
            for i in range(26):
                letter = order[i]
                j = i + 1
                while j < len(order):
                    if order[j] == letter:
                        order = order[:j] + order[j + 1:]
                        j -= 1
                    j += 1
            break
    previous = preceeding
print(order)
