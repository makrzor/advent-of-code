#!/usr/bin/env python3

from __init__ import *


def count_mer(new_mer: str) -> None:
    if new_mer not in mer_counts:
        mer_counts[new_mer] = 0
    mer_counts[new_mer] += 1


rules = {}
polymer = []
mer_counts = {}

for line in get_input_stream():
    if " -> " in line:
        pair, insert = line.strip().split(" -> ")
        if pair not in rules:
            rules[pair] = insert
    elif line != "\n":
        for mer in line.strip():
            polymer.append(mer)
            count_mer(mer)

for step in range(10):
    for i in range(0, 2 * len(polymer) - 2, 2):
        pair = "".join(polymer[i:i + 2])
        mer = rules[pair]
        polymer.insert(i + 1, mer)
        count_mer(mer)

print(max(mer_counts.values()) - min(mer_counts.values()))
sys.exit(EXIT_SUCCESS)
