#!/usr/bin/env python3

from functools import lru_cache
from itertools import product

from __init__ import *


@lru_cache(maxsize=None)
def roll(player_0_score: int, player_1_score: int, player_0_field: int, player_1_field: int) -> list:
    player_0_wins = 0
    player_1_wins = 0
    for roll_result, factor in DIE.items():
        next_player_0_score = player_0_score
        next_player_0_field = player_0_field
        next_player_0_field += roll_result
        next_player_0_field = (next_player_0_field - 1) % 10 + 1
        next_player_0_score += next_player_0_field
        if next_player_0_score >= SCORE_LIMIT:
            player_0_wins += factor
            continue
        next_result = roll(player_1_score, next_player_0_score, player_1_field, next_player_0_field)
        player_1_wins += next_result[0] * factor
        player_0_wins += next_result[1] * factor
    return [player_0_wins, player_1_wins]


SCORE_LIMIT = 21
DIE_SIDES = 3
ROLLS_NUMBER = 3
ROLL_RESULTS = [sum(rolls) for rolls in product(range(1, DIE_SIDES + 1), repeat=ROLLS_NUMBER)]
DIE = {result: ROLL_RESULTS.count(result) for result in range(min(ROLL_RESULTS), max(ROLL_RESULTS) + 1)}

player_scores = [0, 0]
print(max(roll(*player_scores, *[int(line.split()[-1]) for line in get_input_stream()])))
sys.exit(EXIT_SUCCESS)
