#!/usr/bin/env python3

from __init__ import *


def play_a_game(p1_deck, p2_deck):
    decks = set()
    while p1_deck and p2_deck:
        decks_combined = p1_deck + "." + p2_deck
        if decks_combined in decks:
            return [True, p1_deck]
        decks.add(decks_combined)
        p1_card, p1_deck = p1_deck[0], p1_deck[1:]
        p2_card, p2_deck = p2_deck[0], p2_deck[1:]
        p1_card_value = ord(p1_card)
        p2_card_value = ord(p2_card)
        if len(p1_deck) < p1_card_value or len(p2_deck) < p2_card_value:
            p1_won = p1_card > p2_card
        else:
            p1_won, _ = play_a_game(p1_deck[:p1_card_value], p2_deck[:p2_card_value])
        if p1_won:
            p1_deck += p1_card + p2_card
        else:
            p2_deck += p2_card + p1_card
    if p1_deck:
        return [True, p1_deck]
    else:
        return [False, p2_deck]


decks = get_input_stream().read()
p1_deck, p2_deck = decks[:-1].split("\n\n")
p1_deck = "".join([chr(int(x)) for x in p1_deck.split("\n")[1:]])
p2_deck = "".join([chr(int(x)) for x in p2_deck.split("\n")[1:]])
decks = p1_deck + p2_deck
_, decks = play_a_game(p1_deck, p2_deck)
score = 0
for i in range(len(decks) + 1):
    score += i * ord(decks[- i])
print(score)
