#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

def insert_marble(current_marble, marble_put):
    if marble_put % 23:
        current_marble += 2
        if current_marble >= len(marbles):
            current_marble -= len(marbles)
        marbles.insert(current_marble, marble_put)
    else:
        print("Player:", current_player, "-", scores[current_player], end=" + ")
        scores[current_player] += marble_put
        print(marble_put, "=", scores[current_player])
        current_marble -= 7
        if current_marble < 0:
            current_marble += len(marbles)
        print("Player:", current_player, "-", scores[current_player], "+", marbles[current_marble], end=" = ")
        scores[current_player] += marbles.pop(current_marble)
        print(scores[current_player])
    return(current_marble)

marbles = [0]
marble_put = 1
current_player = 1
current_marble = 0

line = input_file.read()
number_of_players = int(line.split()[0])
stop_value = int(line.split()[6])
scores = [0] * (number_of_players + 1)

while marble_put <= stop_value:
    current_marble = insert_marble(current_marble, marble_put)
    marble_put += 1
    current_player += 1
    if current_player > number_of_players:
        current_player = 1
print(max(scores))
