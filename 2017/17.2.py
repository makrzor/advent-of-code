#!/usr/bin/env python

STEP = 359

position = 1
for i in range(1, 50000001):
    if position == 1:
        print(i)
    position += STEP
    position %= i + 1
    position += 1
