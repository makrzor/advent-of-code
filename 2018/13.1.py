#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

def move(cart):
    x = carts[cart]["x"]
    y = carts[cart]["y"]
    diagram[y][x][1] = -1
    x += DIRECTIONS[carts[cart]["direction"]][0]
    y += DIRECTIONS[carts[cart]["direction"]][1]
    carts[cart]["x"] = x
    carts[cart]["y"] = y
    carts[cart]["moved"] = 1
    if diagram[y][x][1] > -1:
        return cart
    else:
        diagram[y][x][1] = cart
        return -1

def rotate(cart):
    x = carts[cart]["x"]
    y = carts[cart]["y"]
    char = diagram[y][x][0]
    if char == "+":
        direction = carts[cart]["direction"]
        turn = carts[cart]["turn"]
        direction += TURNS[turn]
        if direction < 0:
            direction += 4
        carts[cart]["direction"] = direction
        turn += 1
        if turn >= choices:
            turn -= choices
        carts[cart]["turn"] = turn
    elif char == "/":
        direction = carts[cart]["direction"]
        if direction == 0 or direction == 2:
            direction += 1
        elif direction == 1 or direction == 3:
            direction -= 1
        carts[cart]["direction"] = direction
    elif char == "\\":
        direction = carts[cart]["direction"]
        if direction == 0:
            direction += 3
        elif direction == 1:
            direction += 1
        elif direction == 2:
            direction -= 1
        elif direction == 3:
            direction -= 3
        carts[cart]["direction"] = direction

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)] # ^>v<
TURNS = [-1, 0, -3] # lsr
choices = len(TURNS)

diagram = []
carts = []

y = 0
for line in input_file:
    diagram_row = []
    for x in range(len(line)):
        char = line[x]
        diagram_row.append([char, -1])
        if char in "^>v<":
            diagram_row[-1][1] = len(carts)
            carts.append({"y": y, "x": x, "direction": 0, "turn": 0, "moved": 0})
            if char in "^v":
                diagram_row[-1][0] = "|"
                if char == "v":
                    carts[-1]["direction"] = 2
            elif char in "><":
                diagram_row[-1][0] = "-"
                if char == ">":
                    carts[-1]["direction"] = 1
                elif char == "<":
                    carts[-1]["direction"] = 3
    diagram.append(diagram_row)
    y += 1

while True:
    for y in range(len(diagram)):
        for x in range(len(diagram[y])):
            cart = diagram[y][x][1]
            if cart > -1 and carts[cart]["moved"] == 0:
                if move(cart) >= 0:
                    print(carts[cart]["x"], carts[cart]["y"], sep=",")
                    exit(0)
                rotate(cart)
    for cart in carts:
        cart["moved"] = 0
