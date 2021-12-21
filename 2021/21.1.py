#!/usr/bin/env python3

from itertools import cycle

from __init__ import *


def player_move(player: int) -> None:
    player_field[player] += next(throw)
    player_field[player] = (player_field[player] - 1) % 10 + 1
    player_score[player] += player_field[player]


SCORE_LIMIT = 1000
TURNS = [0, 1]
throw = cycle([n % 10 for n in range(16, 6, -1)])
turn = cycle(TURNS)

player_field = [int(line.split()[-1]) for line in get_input_stream()]

rolls = 0
player_score = [0, 0]
while player_score[0] < SCORE_LIMIT and player_score[1] < SCORE_LIMIT:
    player_move(next(turn))
    rolls += 3

print(player_score[next(turn)] * rolls)
sys.exit(EXIT_SUCCESS)
