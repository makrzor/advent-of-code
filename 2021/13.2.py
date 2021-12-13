#!/usr/bin/env python3

from __init__ import *

manual = {}

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
            for row in [row for row in manual if row > fold_y]:
                new_row = height - row
                if new_row not in manual:
                    manual[new_row] = manual[row]
                else:
                    for column in manual[row]:
                        if column not in manual[new_row]:
                            manual[new_row].append(column)
                del manual[row]
        elif "x=" in line:
            fold_x = int(line.strip().split("=")[1])
            width = 2 * fold_x
            for row in manual:
                for column in [col for col in manual[row] if col > fold_x]:
                    new_column = width - column
                    if new_column not in manual[row]:
                        manual[row].append(new_column)
                    else:
                        manual[row].remove(column)

for y in range(fold_y):
    for x in range(fold_x):
        if y in manual and x in manual[y]:
            print("#", end="")
        else:
            print(".", end="")
    print()
sys.exit(EXIT_SUCCESS)
