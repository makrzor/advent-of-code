#!/usr/bin/env python3

from itertools import cycle

from __init__ import *


def rotated(beacon_data: list, beacon_rotation: int) -> list:
    enhanced_beacon_data = [beacon_data[d] for d in range(DIMENSIONS)] + [-beacon_data[d] for d in range(DIMENSIONS)]
    return [enhanced_beacon_data[r] for r in ROTATIONS[beacon_rotation]]


DIMENSIONS = 3
ROTATIONS = [
    [0, 1, 2], [0, 2, 4], [0, 4, 5], [0, 5, 1],
    [3, 1, 5], [3, 5, 4], [3, 4, 2], [3, 2, 1],
    [1, 2, 0], [1, 0, 5], [1, 5, 3], [1, 3, 2],
    [4, 2, 3], [4, 3, 5], [4, 5, 0], [4, 0, 2],
    [2, 0, 1], [2, 1, 3], [2, 3, 4], [2, 4, 0],
    [5, 0, 4], [5, 4, 3], [5, 3, 1], [5, 1, 0],
]
rotations = [n for n in range(len(ROTATIONS))]
MATCHING_BEACONS_NEEDED = 11
SPINNER = cycle("|/-\\")

scanners_data = []

for line in get_input_stream():
    if "---" in line:
        scanners_data.append([])
    elif line != "\n":
        beacon = [int(n) for n in line.split(",")]
        scanners_data[-1].append([rotated(beacon, rotation) for rotation in rotations])

for beacon_multi in scanners_data[0]:
    beacon_multi.append(beacon_multi[0])
scanner_positions = {0: [0, 0, 0]}
scanners_to_be_checked = [n for n in range(len(scanners_data))]

matching_beacons_count = 0
while len(scanners_to_be_checked) > 1:
    i = scanners_to_be_checked.pop(0)
    if i not in scanner_positions:
        scanners_to_be_checked.append(i)
        continue
    for j in scanners_to_be_checked:
        if j in scanner_positions:
            continue
        print("\r{}".format(next(SPINNER)), end="")
        for n in range(len(scanners_data[i]) - MATCHING_BEACONS_NEEDED):
            first_beacon_a = scanners_data[i][n][-1]
            for m in range(len(scanners_data[j])):
                first_beacon_b_multi = scanners_data[j][m]
                for rotation in rotations:
                    rotated_first_beacon_b = first_beacon_b_multi[rotation]
                    diff = [first_beacon_a[d] - rotated_first_beacon_b[d] for d in range(DIMENSIONS)]
                    matching_beacons_count = 0
                    for beacon_a_multi in scanners_data[i][n + 1:]:
                        beacon_a = beacon_a_multi[-1]
                        for beacon_b_multi in scanners_data[j]:
                            rotated_beacon_b = beacon_b_multi[rotation]
                            if beacon_a[0] == diff[0] + rotated_beacon_b[0] \
                                    and beacon_a[1] == diff[1] + rotated_beacon_b[1] \
                                    and beacon_a[2] == diff[2] + rotated_beacon_b[2]:
                                matching_beacons_count += 1
                                break
                    if matching_beacons_count == MATCHING_BEACONS_NEEDED:
                        scanner_positions[j] = diff
                        for beacon_b_multi in scanners_data[j]:
                            beacon_b_normalized = [beacon_b_multi[rotation][d] + scanner_positions[j][d]
                                                   for d in range(DIMENSIONS)]
                            beacon_b_multi.append(beacon_b_normalized)
                        break
                if matching_beacons_count == MATCHING_BEACONS_NEEDED:
                    break
            if matching_beacons_count == MATCHING_BEACONS_NEEDED:
                break

max_manhattan_distance = 0

for i in scanner_positions:
    for j in scanner_positions:
        manhattan_distance = sum([abs(scanner_positions[i][d] - scanner_positions[j][d]) for d in range(DIMENSIONS)])
        if manhattan_distance > max_manhattan_distance:
            max_manhattan_distance = manhattan_distance

print("\r{}".format(max_manhattan_distance))
sys.exit(EXIT_SUCCESS)
