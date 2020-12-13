#!/usr/bin/env python3

from __init__ import *

stream = get_input_stream()
eta = int(stream.readline())
notes = set(stream.readline().split(','))
notes.remove("x")
bus_ids = sorted([int(x) for x in notes])

nearest_times = {}
min_i = bus_ids[0]
min_time = eta + min_i

for i in bus_ids:
    for j in range(0, eta + i, i):
        nearest_times[i] = j
    if nearest_times[i] < min_time:
        min_time = nearest_times[i]
        min_i = i
print(min_i * (min_time - eta))
