#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

marbles = [[0] * 3]
len_marbles = 1
marble_put = 1
current_player = 1
current_marble = 0

line = input_file.read()
number_of_players = int(line.split()[0])
stop_value = 100 * int(line.split()[6])
scores = [0] * (number_of_players + 1)

while True:
    for i in range(22):
        if len_marbles < 25:
            index = 0
        for i in range(2):
            current_marble = marbles[current_marble][1]
        marbles.append([0, 0, marble_put])
        marbles[marbles[current_marble][0]][1] = len_marbles
        marbles[len_marbles][0] = marbles[current_marble][0]
        marbles[current_marble][0] = len_marbles
        marbles[len_marbles][1] = current_marble
        current_marble = len_marbles
        len_marbles += 1
        marble_put += 1
        current_player += 1
        if current_player > number_of_players:
            current_player = 1
        if marble_put == stop_value:
            print(max(scores))
            exit(0)
    if len_marbles < 25:
        index = 0
    scores[current_player] += marble_put
    for i in range(7):
        current_marble = marbles[current_marble][0]
    scores[current_player] += marbles[current_marble][2]
    marbles[marbles[current_marble][0]][1] = marbles[current_marble][1]
    marbles[marbles[current_marble][1]][0] = marbles[current_marble][0]
    current_marble = marbles[current_marble][1]
    marble_put += 1
    current_player += 1
    if current_player > number_of_players:
        current_player = 1
    if marble_put == stop_value:
        print(max(scores))
        exit(0)
