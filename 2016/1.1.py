#!/usr/bin/env python

SEQUENCE = "R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3"
NEWS = "NESWN"

moves = SEQUENCE.split(", ")
facing = "N"
for i in range(len(moves)):
    news_index = NEWS.find(facing)
    if moves[i][0] == "R":
        facing = NEWS[news_index + 1]
    else:
        facing = NEWS[:-1][news_index - 1]
    moves[i] = facing + moves[i][1:]
east = 0
north = 0
for i in range(len(moves)):
    if moves[i][0] == "N":
        north += int(moves[i][1:])
    elif moves[i][0] == "S":
        north -= int(moves[i][1:])
    elif moves[i][0] == "E":
        east += int(moves[i][1:])
    else:
        east -= int(moves[i][1:])

print(abs(east) + abs(north))
