#!/usr/bin/env python3

from __init__ import *

decks = get_input_stream().read()
player_1_deck, player_2_deck = decks[:-1].split("\n\n")
player_1_deck = [int(x) for x in player_1_deck.split("\n")[1:]]
player_2_deck = [int(x) for x in player_2_deck.split("\n")[1:]]
while player_1_deck and player_2_deck:
    player_1_card = player_1_deck.pop(0)
    player_2_card = player_2_deck.pop(0)
    if player_1_card > player_2_card:
        player_1_deck += [player_1_card, player_2_card]
    else:
        player_2_deck += [player_2_card, player_1_card]
decks = player_1_deck + player_2_deck
score = 0
for i in range(len(decks) + 1):
    score += i * decks[- i]
print(score)
