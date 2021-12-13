#!/usr/bin/env python3

from __init__ import *

manual = {}
dots_count = 0

for line in get_input_stream():
    if "," in line:
        x, y = [int(n) for n in line.strip().split(",")]
        if y not in manual:
            manual[y] = []
        manual[y].append(x)
    elif "fold" in line:
        if "y=" in line:
            fold_y = int(line.strip().split("=")[1])
            height = 2 * fold_y
            for row in manual:
                if row > fold_y:
                    mirror_row = height - row
                    for column in manual[row]:
                        if mirror_row not in manual or column not in manual[mirror_row]:
                            dots_count += 1
                else:
                    dots_count += len(manual[row])
        elif "x=" in line:
            fold_x = int(line.strip().split("=")[1])
            width = 2 * fold_x
            for row in manual:
                for column in manual[row]:
                    if column < fold_x or column > fold_x and width - column not in manual[row]:
                        dots_count += 1
        break

print(dots_count)
sys.exit(EXIT_SUCCESS)
