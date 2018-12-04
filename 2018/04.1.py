#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = sorted(open(filename, 'r').readlines())

GUARDS_MAX = 10000
MINS_PER_HOUR = 60

guards_dozes = [[0 for col in range(MINS_PER_HOUR)] for row in range(GUARDS_MAX)]
guards_sleep_length = [0] * GUARDS_MAX
biggest_sleeper = 0
biggest_sleepers_total = 0
most_slept_minute = 0
most_slept_minutes_number = 0

for line in input_file:
    event = line.split(" ")[2]
    minute = int(line.split(":")[1][:2])
    if event == "Guard":
        guard = int(line.split()[3][1:])
    elif event == "falls":
        doze_start = minute
    elif event == "wakes":
        for i in range(doze_start, minute):
            guards_dozes[guard][i] += 1
            guards_sleep_length[guard] += 1
for i in range(GUARDS_MAX):
    if guards_sleep_length[i] > biggest_sleepers_total:
        biggest_sleeper = i
        biggest_sleepers_total = guards_sleep_length[i]
for i in range(MINS_PER_HOUR):
    if guards_dozes[biggest_sleeper][i] > most_slept_minutes_number:
        most_slept_minute = i
        most_slept_minutes_number = guards_dozes[biggest_sleeper][i]
print(biggest_sleeper * most_slept_minute)