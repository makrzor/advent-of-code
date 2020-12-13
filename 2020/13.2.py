#!/usr/bin/env python3

from __init__ import *

stream = get_input_stream()
notes = stream.read().split()[-1].split(',')
bus_times = {}
for i in range(len(notes)):
    if notes[i] != "x":
        bus_times[int(notes[i])] = i

earliest = 0
product = 1

for bus_id, time in bus_times.items():
    while earliest % bus_id != (bus_id - (time % bus_id)) % bus_id:
        earliest += product
    product *= bus_id
print(earliest)
