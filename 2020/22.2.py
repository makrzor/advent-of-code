#!/usr/bin/env python3

from __init__ import *


def play_a_game(player_1_deck, player_2_deck):
    decks = []
    while player_1_deck and player_2_deck:
        decks_combined = player_1_deck + ["."] + player_2_deck
        if decks_combined in decks:
            return [0, player_1_deck]
        decks.append(decks_combined)
        player_1_card = player_1_deck.pop(0)
        player_2_card = player_2_deck.pop(0)
        if len(player_1_deck) < player_1_card or len(player_2_deck) < player_2_card:
            result = 0 if player_1_card > player_2_card else 1
        else:
            result, _ = play_a_game(player_1_deck[:player_1_card], player_2_deck[:player_2_card])
        if result:
            player_2_deck += [player_2_card, player_1_card]
        else:
            player_1_deck += [player_1_card, player_2_card]
    if player_1_deck:
        return [0, player_1_deck]
    else:
        return [1, player_2_deck]


decks = get_input_stream().read()
player_1_deck, player_2_deck = decks[:-1].split("\n\n")
player_1_deck = [int(x) for x in player_1_deck.split("\n")[1:]]
player_2_deck = [int(x) for x in player_2_deck.split("\n")[1:]]
decks = player_1_deck + player_2_deck
_, decks = play_a_game(player_1_deck, player_2_deck)
score = 0
for i in range(len(decks) + 1):
    score += i * decks[- i]
print(score)
