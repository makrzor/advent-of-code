#!/usr/bin/env python3

from statistics import mean

from __init__ import *


def cost_sum(meeting_point: int) -> int:
    calculated_sum = 0
    for crab in crab_positions:
        calculated_sum += abs(crab - meeting_point)
    return calculated_sum


crab_positions = [int(x) for x in get_input_stream().readline().split(",")]
point = round(mean(crab_positions))

while cost_sum(point + 1) < cost_sum(point):
    point += 1
while cost_sum(point - 1) < cost_sum(point):
    point -= 1

print(cost_sum(point))
sys.exit(EXIT_SUCCESS)
