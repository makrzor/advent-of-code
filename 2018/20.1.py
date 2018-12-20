#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

map = input_file.readline()[:-1]
#print(map)

char = map[0]
parentheses_open = []
i = 1

while char != "$":
    char = map[i]
    if map[i] == "(":
        parentheses_open.append(i)
    elif map[i] == ")":
        chains = []
        chain_start = parentheses_open[-1] + 1
        zero_detected = False
        for j in range(chain_start, i + 1):
            if map[j] == "|" or map[j] == ")":
                chains.append(map[chain_start:j])
                if chain_start == j:
                    zero_detected = True
                chain_start = j + 1
        chain_to_be_appended = ""
        max_chain_length = 0
        if not zero_detected:
            for chain in range(len(chains)):
                if len(chains[chain]) > max_chain_length:
                    max_chain_length = len(chains[chain])
                    max_chain = chain
            chain_to_be_appended = chains[max_chain]
        map = map[:parentheses_open[-1]] + chain_to_be_appended + map[i + 1:]
        i = parentheses_open.pop() - 1 + max_chain_length
#        print(map)
    i += 1
print(i - 2)
