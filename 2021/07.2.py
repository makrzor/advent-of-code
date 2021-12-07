#!/usr/bin/env python3

from statistics import mean

from __init__ import *


def cost_sum(meeting_point: int) -> int:
    calculated_sum = 0
    for crab in crab_positions:
        calculated_sum += cost_db[abs(crab - meeting_point)]
    return calculated_sum


crab_positions = [int(x) for x in get_input_stream().readline().split(",")]
point = round(mean(crab_positions))

cost_db = {0: 0}
for i in range(1, max(crab_positions)):
    cost_db[i] = cost_db[i - 1] + i

while cost_sum(point + 1) < cost_sum(point):
    point += 1
while cost_sum(point - 1) < cost_sum(point):
    point -= 1

print(cost_sum(point))
