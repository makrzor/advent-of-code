#!/usr/bin/env python3

from __init__ import *

input_stream = get_input_stream()
queue = [int(x) for x in input_stream.readline().strip().split(",")]
boards = []

for line in input_stream:
    if not line.strip():
        boards.append([])
        continue
    boards[-1].append([])
    for number in line.strip().split():
        boards[-1][-1].append(int(number))

for board in boards:
    board_t = transpose(board)
    for row in board_t:
        board.append(row)

number = -1
winners = []
for number in queue:
    for board in boards:
        for row in board:
            if number in row:
                row.remove(number)
            if not row and board not in winners:
                winners.append(board)
    if winners and len(boards) > len(winners):
        for winner in winners:
            boards.remove(winner)
        winners = []
    if winners:
        break

if len(winners) > 1:
    print("More than one winner: {}".format(winners))
board_sum = 0
for row in winners[0]:
    for addend in row:
        board_sum += addend
board_sum //= 2
print(board_sum * number)
