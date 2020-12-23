#!/usr/bin/env python3

from __init__ import *

DESTINATION_LIMIT = 10
DIMINISHED_CUPS_SIZE = 7
MOVES = 100

cups = [int(char) for char in get_input_stream().read().strip()]
extracted = []
for _ in range(MOVES):
    for _ in range(3):
        extracted.append(cups.pop(1))
    destination = cups[0] - 1
    while destination in extracted or not destination:
        if not destination:
            destination = DESTINATION_LIMIT
        destination -= 1
    for i in range(1, DIMINISHED_CUPS_SIZE):
        if cups[i] == destination:
            destination_place = i + 1
            break
    for _ in range(3):
        cups.insert(destination_place, extracted.pop())
    cups.append(cups.pop(0))
while cups[-1] != 1:
    cups.append(cups.pop(0))
print("".join(["{}".format(digit) for digit in cups[:-1]]))
