#!/usr/bin/env python

input_file = open("19.txt", 'r')
diagram = []
steps = 1

for line in input_file:
    diagram.append(line)
(x, y) = (diagram[0].find('|'), 0)
direction = 'd'
while True:
    if direction == 'd':
        y += 1
    elif direction == 'u':
        y -= 1
    elif direction == 'r':
        x += 1
    else:
        x -= 1
    steps += 1
    if diagram[y][x] == 'Y':
        break
    elif diagram[y][x] == '+':
        if direction == 'd' or direction == 'u':
            if x > 0 and diagram[y][x - 1] != " ":
                direction = 'l'
            else:
                direction = 'r'
        else:
            if y > 0 and diagram[y - 1][x] != " ":
                direction = 'u'
            else:
                direction = 'd'
print steps
