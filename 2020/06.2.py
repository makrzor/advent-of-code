#!/usr/bin/env python3

from __init__ import *

answers = [0]

for line in get_input_stream():
    line = line.rstrip()
    if not line:
        answers.append(0)
        continue
    if answers[-1] == 0:
        answers[-1] = line
    else:
        for character in answers[-1]:
            if character not in line:
                answers[-1] = answers[-1].replace(character, "")

answers_sum = 0

for answer in answers:
    answers_sum += len(answer)

print(answers_sum)
