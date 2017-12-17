#!/usr/bin/env python

STEP = 359

buffer = [0]
position = 0
for i in range(1, 2018):
    position += STEP
    position %= len(buffer)
    if position == len(buffer) - 1:
        buffer.append(i)
    else:
        buffer.insert(position + 1, i)
    position += 1
position += 1
position %= len(buffer)
print(buffer[position])
