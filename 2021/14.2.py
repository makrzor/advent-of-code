#!/usr/bin/env python3

from __init__ import *


def count_mer(mer: str, count=1) -> None:
    if mer not in mer_counts:
        mer_counts[mer] = 0
    mer_counts[mer] += count


pairs = {}
polymer = ""
mer_counts = {}
pair_counts = {}

for line in get_input_stream():
    if " -> " in line:
        pair, insert = line.strip().split(" -> ")
        if pair not in pairs:
            pairs[pair] = [insert, 0, 0]
    elif line != "\n":
        polymer = line.strip()
for i in range(len(polymer)):
    if i:
        pairs[polymer[i - 1] + polymer[i]][1] += 1
    count_mer(polymer[i])

for step in range(40):
    for pair in pairs:
        predecessor = pair[0]
        successor = pair[1]
        pair_params = pairs[pair]
        insert = pair_params[0]
        pairs[predecessor + insert][2] += pair_params[1]
        pairs[insert + successor][2] += pair_params[1]
        pair_params[2] -= pair_params[1]
        count_mer(insert, pair_params[1])
    for pair in pairs:
        pairs[pair][1] += pairs[pair][2]
        pairs[pair][2] = 0

print(max(mer_counts.values()) - min(mer_counts.values()))
sys.exit(EXIT_SUCCESS)
