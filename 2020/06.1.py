#!/usr/bin/env python3

from __init__ import *

answers = [[]]

for line in get_input_stream():
    line = line.rstrip()
    if not line:
        answers.append([])
        continue
    for character in line:
        if character not in answers[-1]:
            answers[-1].append(character)

answers_sum = 0

for answer in answers:
    answers_sum += len(answer)

print(answers_sum)
